from django.db import models
from django.core.validators import RegexValidator

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=70)
    email = models.EmailField()
    phone = models.CharField(
        max_length=15, 
        validators=[RegexValidator(regex=r'^\d{10,15}$', message='Phone number must be 10-15 digits')]
    )
    desc = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['-date']
        verbose_name_plural = "Contacts"