from django.db import models

# Create your models here.
class Child(models.Model):
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField(max_length=250)
    address = models.CharField(max_length=250)
    pcp = models.CharField(max_length=100)
    bio= models.CharField(max_length=250)

    def __str__(self):
        return self.name

# michelle = Child(image='', name='Michelle', age=5, gender ='Female', address='Houston, TX', pcp='Dr. Joy', bio ='She likes to dance')