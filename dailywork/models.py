from django.db import models

# Create your models here.

class user_infor(models.Model):
    username = models.CharField(max_length=50,primary_key=True)
    email_id = models.CharField(max_length=50,blank=True,default="")
    password = models.CharField(max_length=10,blank=False)
    first_name = models.CharField(max_length=50,blank=True,default="")
    middle_name = models.CharField(max_length=50,blank=True,default="")
    last_name = models.CharField(max_length=50,blank=True,default="")
    pin_code = models.CharField(max_length=10,blank=True,default="")
    nation = models.CharField(max_length=50,blank=True,default="")
    address = models.CharField(max_length=50,blank=True,default="")

    def __str__(self):
        return self.username

class user_events_info(models.Model):
    class Meta:
        unique_together = (('event_title','event_date','username'),)
    
    event_title = models.CharField(max_length=50)
    event_description = models.TextField(blank=True)
    event_comments = models.TextField(blank=True)
    event_date = models.DateField()
    event_completed = models.BooleanField()
    username = models.CharField(max_length=50,blank=False)

    def __str__(self):
        return self.username

class admin_info(models.Model):
    admin_name = models.CharField(max_length=50,primary_key=True)
    email_id = models.CharField(max_length=50,blank=True,default="")
    password = models.CharField(max_length=10,blank=False)
    first_name = models.CharField(max_length=50,blank=True,default="")
    middle_name = models.CharField(max_length=50,blank=True,default="")
    last_name = models.CharField(max_length=50,blank=True,default="")
    pin_code = models.CharField(max_length=10,blank=True,default="")
    nation = models.CharField(max_length=50,blank=True,default="")
    address = models.CharField(max_length=50,blank=True,default="")
    admin_auth_pass = models.CharField(max_length=10,blank=False)

    def __str__(self):
        return self.admin_name


class tickets_info(models.Model):
    class Meta:
        unique_together=(('username','ticket_title','ticket_status'),)
    STATUS_CHOICES = (
        ("Active","Active"),
        ("Open","Open"),
        ("Closed","Closed"),
    )
    username = models.CharField(max_length=50,blank=False)
    ticket_title = models.CharField(max_length=100,blank=False)
    ticket_description = models.TextField(blank=False)
    ticket_status = models.CharField(max_length=20,choices=STATUS_CHOICES,default="Open")

    def __str__(self):
        return self.username




