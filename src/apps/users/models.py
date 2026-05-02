import uuid
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models


class TechnicianManager(BaseUserManager):
    use_in_migrations = True

    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("Email is required")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        return self.create_user(email, password, **extra_fields)


class Technician(AbstractUser):
    class Specialty(models.TextChoices):
        ELECTRICAL = "ELECTRICAL", "Eléctrico"
        PLUMBING = "PLUMBING", "Plomería"
        HVAC = "HVAC", "Climatización"
        TELECOM = "TELECOM", "Telecomunicaciones"
        GENERAL = "GENERAL", "General"

    username = None

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(unique=True)
    employee_id = models.CharField(max_length=50, unique=True)
    specialty = models.CharField(
        max_length=20, choices=Specialty.choices, default=Specialty.GENERAL
    )
    phone = models.CharField(max_length=20, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["employee_id"]

    objects = TechnicianManager()

    class Meta:
        verbose_name = "technician"
        verbose_name_plural = "technicians"

    def __str__(self):
        return self.email
