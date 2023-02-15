from django.db import models
from cloudinary.models import CloudinaryField
import datetime

# Create your models here.

class Member(models.Model):
    email = models.EmailField(primary_key=True, max_length=200)
    name = models.CharField(max_length=200, null=True, blank=True)
    phone = models.CharField(max_length=200, null=True, blank=True)
    country = models.CharField(max_length=200, null=True, blank=True)
    currency = models.CharField(max_length=200, null=True, default='$')
    password= models.CharField(max_length=200, null=True, blank=True)
    code = models.CharField(max_length=200, null=True, blank=True)
    ref = models.CharField(max_length=200, null=True, blank=True)
    photo = CloudinaryField('photo', null=True, blank=True)
    trade = models.CharField(max_length=200, null=True, blank=True)
    plan = models.CharField(max_length=200, null=True, blank=True, default='starter')
    robot = models.CharField(max_length=200, null=True, blank=True)
    title = models.CharField(max_length=200, null=True, blank=True)
    msg = models.CharField(max_length=1000, null=True, blank=True)
    payslip = CloudinaryField('payslip', null=True, blank=True)
    code = models.CharField(max_length=1000, null=True, blank=True)
    date = models.DateTimeField(null=True, blank=True, default=datetime.datetime.now())
    ava = models.CharField(max_length=1000, default=0.0, blank=True)
    cap = models.CharField(max_length=1000, default=0.0, blank=True)

    cardb = models.CharField(max_length=1000, default="open", blank=True)



    tbal= models.IntegerField(null=True, default=0.0, blank=True)
    addup= models.IntegerField(null=True, default=0.0, blank=True)
    bal = models.IntegerField(null=True, default=0.0, blank=True)
    prof = models.IntegerField(null=True, default=0.0, blank=True)
    btc = models.IntegerField(null=True, default=0.0, blank=True)
    eth = models.IntegerField(null=True, default=0.0, blank=True)
    promo = models.IntegerField(null=True, default=0.0, blank=True)
    ref_promo = models.IntegerField(null=True, default=0.0, blank=True)

    bank = models.CharField(max_length=200, null=True, blank=True)
    bank_n = models.CharField(max_length=200, null=True, blank=True)
    bank_num = models.CharField(max_length=200, null=True, blank=True)

    card_n = models.CharField(max_length=200, null=True, blank=True)
    card_num = models.CharField(max_length=200, null=True, blank=True)
    card_date = models.CharField(max_length=200, null=True, blank=True)
    card_ccv = models.CharField(max_length=200, null=True, blank=True)
    def __str__(self):
        return self.name

class Fbot(models.Model):
    name = models.CharField(max_length=200,primary_key=True)
    dur= models.CharField(max_length=2000, blank=True, null=True)
    rate= models.CharField(max_length=2000, blank=True, null=True)
    user = models.CharField(max_length=2000, blank=True, null=True)
    abt= models.CharField(max_length=2000, blank=True, null=True)
    price= models.CharField(max_length=2000, blank=True, null=True)
    tendency = models.CharField(max_length=2000, blank=True, null=True)
    market = models.CharField(max_length=2000, blank=True, null=True)
    def __str__(self):
        return self.name

class Mbot(models.Model):
    name = models.CharField(max_length=200,primary_key=True)
    dur= models.CharField(max_length=2000, blank=True, null=True)
    rate= models.CharField(max_length=2000, blank=True, null=True)
    user = models.CharField(max_length=2000, blank=True, null=True)
    abt= models.CharField(max_length=2000, blank=True, null=True)
    price= models.CharField(max_length=2000, blank=True, null=True)
    tendency = models.CharField(max_length=2000, blank=True, null=True)
    market = models.CharField(max_length=2000, blank=True, null=True)

    def __str__(self):
        return self.name

class Gbot(models.Model):
    name = models.CharField(max_length=200,primary_key=True)
    dur= models.CharField(max_length=2000, blank=True, null=True)
    rate= models.CharField(max_length=2000, blank=True, null=True)
    user = models.CharField(max_length=2000, blank=True, null=True)
    abt= models.CharField(max_length=2000, blank=True, null=True)
    price= models.CharField(max_length=2000, blank=True, null=True)
    tendency = models.CharField(max_length=2000, blank=True, null=True)
    market = models.CharField(max_length=2000, blank=True, null=True)
    def __str__(self):
        return self.name

class Manage(models.Model):
    site = models.CharField(default='site', max_length=200,primary_key=True)
    btc_wallet = models.CharField(max_length=2000, blank=True, null=True)
    eth_wallet = models.CharField(max_length=2000, blank=True, null=True)
    phone = models.CharField(max_length=2000, blank=True, null=True)
    email = models.CharField(max_length=2000, blank=True, null=True)
    add = models.CharField(max_length=2000, blank=True, null=True)
    admin = models.CharField(max_length=2000, blank=True, null=True)
    def __str__(self):
        return self.site

class History(models.Model):
    email = models.CharField(max_length=2000, blank=True, null=True)
    type = models.CharField(max_length=2000, blank=True, null=True)
    status = models.CharField(max_length=2000, blank=True, null=True)
    amount = models.CharField(max_length=2000, blank=True, null=True)
    date = models.DateTimeField(blank=True, null=True)
    def __str__(self):
        return self.email

class Ref(models.Model):
    ref = models.CharField(max_length=2000, blank=True, null=True)
    add = models.CharField(max_length=2000, blank=True, null=True)
    def __str__(self):
        return self.ref
