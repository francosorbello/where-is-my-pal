# Step 1: set work directory and get dependencies
FROM python:3.14-slim AS builder

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# UPDATE AND INSTALL PYTHON PACKAGES
COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt


# Stage 2
FROM python:3.14-slim

# create non root user and give it access to app folder
RUN useradd -m -r appuser && mkdir /app && chown -R appuser /app

# Copy the Python dependencies from the builder stage
COPY --from=builder /usr/local/lib/python3.14/site-packages/ /usr/local/lib/python3.14/site-packages/
COPY --from=builder /usr/local/bin/ /usr/local/bin/

# copy project to folder and give access to non root user
WORKDIR /app
COPY --chown=appuser:appuser . . 

ENV PROD_VOLUME="prod"
RUN mkdir -p prod

COPY --chown=appuser:appuser entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

EXPOSE 8000

ENTRYPOINT ["/entrypoint.sh"]

