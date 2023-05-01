from django.db import models

# Create your models here.
class Event(models.Model):
    STATUS=(
        ('Completed','Completed'),
        ('Upcoming','Upcoming')
    )
    event_name=models.CharField(max_length=300)
    event_start_date=models.DateTimeField(null=True)
    event_end_date=models.DateTimeField(null=True)
    event_status=models.CharField(choices=STATUS,max_length=100)
    event_flyer=models.ImageField(upload_to='flyers')
    completed=models.BooleanField(default=False)
    description=models.TextField(max_length=2000,null=True,blank=True)
    def __str__(self):
        return self.event_name


class EventDay(models.Model):
    day_flyer=models.ImageField(null=True,blank=True,upload_to='dayflyer')
    day_name=models.CharField(max_length=200)
    event=models.ForeignKey(Event,on_delete=models.CASCADE,related_name='event_ref')
    recording=models.FileField(upload_to='recordings')

    def __str__(self):
        return f'{self.event.event_name} {self.day_name}'

