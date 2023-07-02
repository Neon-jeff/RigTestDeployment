from django.db import models
from django.contrib.auth.models import User
import uuid
from datetime import date,timedelta
from cloudinary.models import CloudinaryField
# Create your models here.


class Partner(models.Model):

    Type=(
        ('VIP','VIP'),
        ('EXECUTIVE','EXECUTIVE'),
        ('AMBASSADOR','AMBASSADOR')

    )
    id=models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    user=models.OneToOneField(User,on_delete=models.CASCADE,related_name='user_ref')
    account_type=models.CharField(choices=Type,blank=True,max_length=300,null=True)
    donation_amount=models.IntegerField(blank=True)
    registered_at=models.DateField(auto_now_add=True)
    profile_image=CloudinaryField('image',blank=True,null=True)

    def save(self,*args,**kwargs):
        if self.account_type=='VIP':
            self.donation_amount=10000
        elif self.account_type =='EXECUTIVE':
            self.donation_amount=30000
        elif self.account_type =='AMBASSADOR':
            self.donation_amount=150000
        super(Partner, self).save(*args, **kwargs)

    def __str__(self):
        return self.user.username + " " + self.account_type

class Donation(models.Model):
        pay_date=models.DateField(auto_now_add=True)
        partner=models.ForeignKey(User, on_delete=models.CASCADE,related_name='payment_ref')
        verified=models.BooleanField(default=False)
        next_due=models.DateField(null=True,blank=True)
        contact_email=models.EmailField(blank=True)

        class Meta:
            ordering=('-pay_date',)
        def save(self,*args,**kwargs):
            if self.verified==True:
                self.next_due=self.pay_date + timedelta(days=30)
            else:
                self.next_due=None
            super(Donation, self).save(*args, **kwargs)
        def __str__(self):
            return f'{self.partner.username} donation at {self.pay_date}'


