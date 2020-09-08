from django.db import models
from django.core.exceptions import ValidationError

# Create your models here.
class Blog(models.Model):
    name = models.CharField(max_length=50)
    img = models.ImageField(upload_to='pics')
    desc = models.TextField()

    def __str__(self):
        return self.name


# Creating a validator function
def validate_gmail(value):
    if "@gmail.com" in value:
        return value
    else:
        raise ValidationError("This fields accept only Google Mail ID")


# Specifying choices
GENDER_CHOICE = (
    ("Male", "Male"),
    ("Female", "Female"),
    ("Others", "Others")
)


class Blogger(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField()
    profession = models.TextField()
    gmail = models.CharField(max_length=50, validators=[validate_gmail])
    gender = models.CharField(max_length=20, choices=GENDER_CHOICE, default='None')

    def __str__(self):
        return self.name