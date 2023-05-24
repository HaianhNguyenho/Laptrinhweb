from django.db import models

TITLE_CHOICES = (
('PM01', 'Pm01.'),
('PM02', 'Pm02.'),
('IOT', 'IoT.'),
)

# Create your models here.
class svModel(models.Model):
    name = models.CharField(max_length=255)
    mssv = models.CharField(max_length=10)
    birth_day = models.DateField(blank=True, null=True)
    lop = models.CharField(max_length=5, choices=TITLE_CHOICES)
    image = models.ImageField()
    
    def __str__(self):
        return self.lop
