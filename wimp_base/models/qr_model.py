import uuid
import io
from django.db import models
from django.conf import settings
import qrcode


class QrPet(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    pet = models.ForeignKey(
        'Pet', 
        on_delete=models.CASCADE, 
        related_name='qr_codes',
        null=True,
        blank=True,
        help_text="Pet to generate QR code for"
    )
    redirect_to = models.CharField(
        "Redirects to", 
        max_length=255, 
        blank=True,
        help_text="Auto-generated URL based on pet ID"
    )
    qr_image = models.ImageField(
        "QR Code Image", 
        upload_to='qr_codes/', 
        blank=True,
        help_text="Generated QR code image"
    )

    def __str__(self) -> str:
        return f"QR for {self.pet.name}"

    def save(self, *args, **kwargs):
        if self.pk:
            try:
                old_instance = QrPet.objects.get(pk=self.pk)
                old_pet_id = old_instance.pet.id if old_instance.pet else None
            except QrPet.DoesNotExist:
                old_pet_id = None
        else:
            old_pet_id = None
        
        new_pet_id = self.pet.id if self.pet else None
        pet_changed = old_pet_id != new_pet_id
        
        if self.pet:
            self.redirect_to = f"/pets/{self.pet.id}/"
        
        super().save(*args, **kwargs)
        
        if self.pet and (pet_changed or not self.qr_image):
            self.generate_qr_code()

    def generate_qr_code(self):
        if not self.pet or not self.redirect_to:
            return
            
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        
        full_url = self.redirect_to
        if not full_url.startswith('http'):
            full_url = settings.ALLOWED_HOSTS[0] + self.redirect_to if settings.ALLOWED_HOSTS else 'localhost' + self.redirect_to
        
        qr.add_data(full_url)
        qr.make(fit=True)

        img = qr.make_image(fill_color="black", back_color="white")
        
        buffer = io.BytesIO()
        img.save(buffer, format='PNG')
        buffer.seek(0)
        
        filename = f"qr_{self.pet.id}_{self.id}.png"
        self.qr_image.save(filename, buffer)
        buffer.close()
        
        super().save(update_fields=['qr_image'])
