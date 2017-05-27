# coding:utf-8
from __future__ import unicode_literals
from datetime import datetime

from django.db import models

# Create your models here.


class MicroService(models.Model):
    micro_service = models.CharField(max_length=64, verbose_name=u"微服务")
    service_name = models.CharField(max_length=64, verbose_name=u"服务名")

    class Meta:
        verbose_name = u"微服务"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.micro_service


class StatusCode(models.Model):
    status_code = models.CharField(max_length=10, verbose_name=u"状态码")

    class Meta:
        verbose_name = u"状态码"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.status_code


class CreateTestApi(models.Model):
    micro_service = models.ForeignKey(MicroService)
    host = models.CharField(max_length=20, choices=(("ytk.yuantiku.ws", u"测试环境"), ("www.yuantiku.com", u"线上环境")))
    base_url = models.CharField(max_length=60, verbose_name=u"URL")
    method = models.CharField(max_length=10, choices=(("POST", u"POST"), ("GET", u"GET")), default="GET")
    header = models.TextField(verbose_name=u"header")
    body = models.TextField(verbose_name=u"body")
    description = models.TextField(verbose_name=u"Case描述")
    status_code = models.ForeignKey(StatusCode)
    assertion = models.CharField(max_length=6, choices=(("等于", u"等于"), ("不等于", u"不等于"), ("包含", u"包含")))
    value_assertion = models.TextField(verbose_name=u"断言值")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"新建接口"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.description