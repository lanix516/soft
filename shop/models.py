from django.db import models
from django.contrib.auth.models import User 
# Create your models here.
PROVINCE = ((0, '北京'), (1, '上海'), (2, '天津'), (3, '重庆'), (4, '山东'), (5, '广东'), (6,'浙江'), (7,'福建'), (8,'江苏'), (9,'湖南'), (10,'湖北'), (11,'广西'))


class UserProfile(models.Model):
    GRADE = ((1, '注册会员'), (2, '铜牌VIP'), (3, '银牌VIP'), (4, '金牌VIP'), (5, '钻石VIP'))
    user = models.OneToOneField(User)
    account = models.PositiveIntegerField()
    grade = models.SmallIntegerField()
    
    def __str__(self):
        return self.user.username


class SiteClass(models.Model):
    class_name = models.CharField(max_length=32)
    class_info = models.CharField(max_length=128)
    
    def __str__(self):
        return self.class_name


class PortalSite(models.Model):
    name = models.CharField(max_length=16)
    
    def __str__(self):
        return self.name


class CommonSite(models.Model):
    WEB_STATUS = ((0, "OK"), (1, "STOP"), (2, "FAILED"))
    name = models.CharField(max_length=32)
    star = models.PositiveIntegerField()
    example = models.CharField(max_length=128)
    price = models.IntegerField(default=0)
    status = models.IntegerField(choices=WEB_STATUS, default=0)
    remark = models.CharField(max_length=512)
    has_phone = models.BooleanField(default=False)
    has_IM = models.BooleanField(default=False)
    has_link = models.BooleanField(default=False)
    
    class Meta:
        abstract = True
        ordering = ["star", "id"]
    def __str__(self):
        return self.name


class WebSite(CommonSite):
    portal_site = models.ForeignKey(PortalSite)
    site_class = models.ForeignKey(SiteClass)
    success_rate = models.PositiveIntegerField(default=100)
    area = models.CharField(max_length=16, default='')


class BbsSite(CommonSite):
    board = models.CharField(max_length=32)
    survival = models.IntegerField(default=100)


class SitePlan(models.Model):
    name = models.CharField(max_length=32)
    remark = models.CharField(max_length=512)
    banner = models.ImageField(upload_to='upload')
    price = models.PositiveIntegerField()
    sites = models.ManyToManyField(WebSite)
    star = models.PositiveIntegerField()

    def __str__(self):
        return self.name


class WebOrder(models.Model):
    ORDER_STATUS = ((0, '提交'), (1, '已受理'), (2, '发布中'), (3, '已发布'), (4, '部分完成'), (5, '废弃'))
    order_serial = models.CharField(max_length=16) 
    user = models.ForeignKey(User)
    create_time = models.DateTimeField(auto_now_add=True)
    order_file  = models.FileField(upload_to='files')
    status = models.SmallIntegerField(default=0, choices=ORDER_STATUS)
    sites = models.ManyToManyField(WebSite, through='WebOrderSite')

    def __str__(self):
        return self.pk


class WebOrderSite(models.Model):
    web_order = models.ForeignKey(WebOrder)
    web_site = models.ForeignKey(WebSite)
    result = models.URLField(blank=True, null=True)
    success = models.BooleanField(default=True)
    refund = models.IntegerField()
    create_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.pk


class RechargeRecord(models.Model):
    user = models.ForeignKey(User)
    money = models.PositiveIntegerField()
    successed = models.BooleanField(default=False)
    create_time = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.user.username

     
class ConsumingRecord(models.Model):
    consuming = models.CharField(default='', max_length=256)
    money = models.IntegerField(default=0)
    create_time = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.order.user.username + "-" + self.order.pk


class CollectSite(models.Model):
    user = models.ForeignKey(User)
    site = models.ForeignKey(WebSite)
    
    def __str__(self):
        return self.site.name


class Comment(models.Model):
    user = models.ForeignKey(User)
    context = models.CharField(max_length=512)
    create_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.context
