from django.db import models
from django.urls import reverse
from datetime import date
# Create your models here.

from django.contrib.auth.models import User

# Create your models here.
class Child(models.Model):
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField(max_length=250)
    address = models.CharField(max_length=250)
    pcp = models.CharField(max_length=100)
    bio= models.CharField(max_length=250)

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name

# michelle = Child(image='', name='Michelle', age=5, gender ='Female', address='Houston, TX', pcp='Dr. Joy', bio ='She likes to dance')

# tuples (value1, value2, value3) immutable pop() no changing of the values
ACTIVITIES  = (
    ('B', 'Breakfast'),
    ('L', 'Lunch'),
    ('D', 'Dinner')
)

class Daily_Activity(models.Model):
    date = models.DateField("select today's date")
    # time = models.TimeField(auto_now=False, auto_now_add=False, **options)
    activity= models.CharField(
        max_length=1,
        # possible choices are the MEALS
        choices = ACTIVITIES,
        default = ACTIVITIES [0][0]
    )
    # make association to Cat Model, when child is deleted, delete assoc. daily-activitie
    child = models.ForeignKey(Child, on_delete=models.CASCADE)

    def __str__(self):
        # return f"{self.get_activity_display()} on {self.date} on {self.time}"
        return f"{self.get_activity_display()} on {self.date}"