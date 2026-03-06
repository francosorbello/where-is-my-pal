# Where is my pal?

"Where is my pal?" is a web app created with Django and Python. Admins can create owners and attach pets to them. Then, they can create a QR code that redirects to a website with the owner and the pet information. The intended use is to 
1. spin up your own server, 
2. setup your and your pets information,
3. Create a QR code and print it
4. Put the QR code on a collar, so if your pet gets lost, they can contact you.

## Project structure

`static/` - Contains static files like css and images
`where_is_my_pal/` - projects folder, created by Django. Contains url redirects in `urls.py` file
`wimp_base/` - app folder, created by DJango. Contains views, models and templates for webapp.
