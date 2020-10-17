from django.db import models
from PIL import Image
from io import BytesIO
import sys
from django.core.files.uploadedfile import InMemoryUploadedFile
from djrichtextfield.models import RichTextField
# from django.contrib.postgres.fields import JSONField

# Create your models here.

class State(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name


# class Itinerary(models.Model):



class Package(models.Model):
    name = models.CharField(max_length=150)
    itinerary = models.TextField()
    listPrice = models.FloatField()
    mrp = models.FloatField()
    duration = models.IntegerField()
    sightseeing = models.CharField(max_length=250)
    destination = models.CharField(max_length=250)
    best_time = models.CharField(max_length=100)
    # overview = models.TextField()
    overview = RichTextField()
    inclusion = models.TextField()
    exclusion = models.TextField()
    cancellation_policy = models.TextField()
    tnc = models.TextField()
    state = models.CharField(max_length=100)
    tags = models.CharField(max_length=200)
    # itnery =:

    def __str__(self):
        return self.name



class Banner(models.Model):
    package = models.OneToOneField(Package,on_delete=models.CASCADE)
    original = models.ImageField(upload_to='photos/banner/original',null=True,blank=True)
    normal = models.ImageField(upload_to='photos/banner/thumbs',null=True,blank=True)
    thumbnail = models.ImageField(upload_to='photos/banner/thumbs',null=True,blank=True)
    alt = models.CharField(max_length=200,null=True,blank=True)
    def __str__(self):
        return "{} : {}".format(self.package.name,self.alt)
    def save(self,force_insert=False,force_update=False,using=None):
        im = Image.open(self.original)
        output = BytesIO()
        basewidth = 600
        wpercent = (basewidth/float(im.size[0]))
        hsize = int((float(im.size[1])*float(wpercent)))
        im = im.resize((basewidth,hsize), Image.ANTIALIAS)
        im = im.convert("RGB")
        im.save(output, format='JPEG', quality=40)
        self.normal = InMemoryUploadedFile(output,'ImageField', "%s.jpg" %self.original.name.split('.')[0], 'image/jpeg', sys.getsizeof(output), None)


        weight,height=im.size
        if weight > height:
            r=(weight-height)/2
            imc=im.crop((r,0,height+r,height))
        else:
            r=(height-weight)/2
            imc=im.crop((0,r,weight,height-r))
        imc = imc.convert("RGB") 
        imc=imc.resize((300,300),Image.ANTIALIAS)
        output = BytesIO()
        imc.save(output, format='JPEG', quality=70)
        output.seek(0)
        self.thumbnail = InMemoryUploadedFile(output,'ImageField', "%s.jpg" %self.original.name.split('.')[0], 'image/jpeg', sys.getsizeof(output), None)
        super(Banner,self).save()



class ProductImages(models.Model):
    package = models.ForeignKey(Package,on_delete=models.CASCADE)
    original = models.ImageField(upload_to='photos/packages/original',null=True,blank=True)
    normal = models.ImageField(upload_to='photos/packages/thumbs',null=True,blank=True)
    thumbnail = models.ImageField(upload_to='photos/packages/thumbs',null=True,blank=True)
    alt = models.CharField(max_length=200,null=True,blank=True)
    def __str__(self):
        return "{} : {}".format(self.package.name,self.alt)
    def save(self,force_insert=False,force_update=False,using=None):
        im = Image.open(self.original)
        output = BytesIO()
        basewidth = 600
        wpercent = (basewidth/float(im.size[0]))
        hsize = int((float(im.size[1])*float(wpercent)))
        im = im.resize((basewidth,hsize), Image.ANTIALIAS)
        im = im.convert("RGB")
        im.save(output, format='JPEG', quality=40)
        self.normal = InMemoryUploadedFile(output,'ImageField', "%s.jpg" %self.original.name.split('.')[0], 'image/jpeg', sys.getsizeof(output), None)


        weight,height=im.size
        if weight > height:
            r=(weight-height)/2
            imc=im.crop((r,0,height+r,height))
        else:
            r=(height-weight)/2
            imc=im.crop((0,r,weight,height-r))
        imc = imc.convert("RGB") 
        imc=imc.resize((300,300),Image.ANTIALIAS)
        output = BytesIO()
        imc.save(output, format='JPEG', quality=70)
        output.seek(0)
        self.thumbnail = InMemoryUploadedFile(output,'ImageField', "%s.jpg" %self.original.name.split('.')[0], 'image/jpeg', sys.getsizeof(output), None)
        super(ProductImages,self).save()


    

