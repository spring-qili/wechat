from django.db import models

# Create your models here.


# class Grades(models.Model):
#     gname = models.CharField(max_length=20)
#     gdate = models.DateTimeField()
#     ggirlnum = models.IntegerField()
#     gboynum = models.IntegerField()
#     isDelete = models.BooleanField(default=False)

class Userinfo(models.Model):
    uname = models.CharField(max_length=20)
    ic_number = models.CharField(max_length=50)
    tel_number = models.CharField(max_length=30)
    room = models.CharField(max_length=20)
    seat = models.CharField(max_length=20)
    temperature = models.FloatField()
    date = models.DateTimeField()
    isnormal = models.BooleanField(default=False)
    openid = models.CharField(max_length=100)

    # def __str__(self):
    #     """定义每个数据对象的显示信息"""
    #     return str({"uname": self.uname, "ic_number": self.ic_number, "tel_number": self.tel_number, "room": self.room, "seat": self.seat})
