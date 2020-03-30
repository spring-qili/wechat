from django.contrib import admin

# Register your models here.
from .models import Userinfo
# 对admin界面进行美化修改


class UserinfoAdmin(admin.ModelAdmin):
    # 列表页属性
    # 显示的字段
    list_display = ['pk', 'uname', 'openid', 'ic_number', 'tel_number',
                    'room', 'seat', 'temperature', 'date', 'isnormal']
    # 以某个字段，对数据进行过滤
    list_filter = []
    # 按某个字段来搜索
    search_fields = []
    # 每页多少条数据
    list_per_page = 10

    # 添加、修改页属性，两个属性不能同时使用
    # 添加时的字段先后顺序
    # fields = []
    # 添加时，给字段分组
    # fieldset = []


# 注册
admin.site.register(Userinfo, UserinfoAdmin)
