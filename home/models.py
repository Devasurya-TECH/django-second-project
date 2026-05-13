import os

from django.db import models
from PIL import Image, ImageOps


class Doctor(models.Model):

    name = models.CharField(max_length=120)

    specialty = models.CharField(max_length=120)

    image = models.ImageField(
        upload_to="doctors/",
        blank=True,
        null=True
    )

    image_url = models.URLField(
        default="https://images.unsplash.com/photo-1612349317150-e413f6a5b16d?q=80&w=800&auto=format&fit=crop",
        blank=True
    )

    bio = models.TextField(blank=True)

    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:

        ordering = ["name"]

    def __str__(self):

        return f"{self.name} - {self.specialty}"

    def save(self, *args, **kwargs):

        super().save(*args, **kwargs)

        if self.image and self.image.path and os.path.exists(self.image.path):
            image_path = self.image.path

            with Image.open(image_path) as img:
                img = ImageOps.exif_transpose(img)

                if img.mode in ("RGBA", "P"):
                    img = img.convert("RGB")

                # Keep doctor photos web-friendly instead of serving large camera originals.
                img.thumbnail((900, 900))
                img.save(image_path, format="JPEG", quality=82, optimize=True)

class Appointment(models.Model):

    patient_name = models.CharField(max_length=100)

    email = models.EmailField()

    phone = models.CharField(max_length=15)

    department = models.CharField(max_length=100)

    appointment_date = models.DateField()

    appointment_time = models.TimeField()

    message = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):

        return self.patient_name
