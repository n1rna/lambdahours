from django.db import models
from django.contrib.auth.models import User, UserManager

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    avatar = models.ImageField(upload_to = 'static/avatars/')
    salary = models.FloatField()
    timezone = models.CharField(max_length=50, default='Asia/Tehran')
    id_number = models.IntegerField(unique=True)
    is_admin = models.BooleanField(default=False)

    def add_activity(self, comment, date, time):
        a = activity(activity_date=date, activity_time=time, activity_comment=comment, user=self)
        a.save()

    def filter_activities(start_date, end_date):
        return self.activity_set.filter(activity_date__range=[start_date, end_date])

class activity(models.Model):
    #activity_id = models.IntegerField(unique=True)
    activity_date = models.DateField()
    activity_time = models.CharField(max_length=200)
    activity_comment = models.CharField(max_length=2000)
    payed = models.BooleanField(default=False)
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
