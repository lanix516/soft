from django.db import models

# Create your models here.
PROVINCE = ((0, '北京'),(1, '上海'),(2,),(3,),(4,),(5,),(6,),(7,),(8,),(9,),(10,),)

class SiteClass(models.Model):
    class_name = models.CharField(max_length=32)
    class_info = models.CharField(max_length=128)
    
    def __str__(self):
        return self.class_name


class CommonSite(models.Model):
    WEB_STATUS = ((0,"OK"),(1,"STOP"),(2,"FAILED"))
    name = models.CharField(max_length=32)
    star = models.PositiveIntegerField()
    example = models.CharField(max_length=128)
    price = models.IntegerField(default=0)
    status = models.IntegerField(choices=WEB_STATUS, default=0)
    remark = models.CharField(max_length=512)
    
    class Meta:
        abstract = True
        ordering = ["star","id"]
    
    def __str__(self):
        return self.name


class WebSite(CommonSite):
    site_class = models.ForeignKey(SiteClass)
    success_rate = models.PositiveIntegerField(default=100)
