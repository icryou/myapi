# coding:utf-8

from django.contrib import admin
from index.models import MicroService, StatusCode, CreateTestApi
# Register your models here.


class MicroServiceAdmin(admin.ModelAdmin):
    list_display = ['micro_service', 'service_name']
    search_fields = ['micro_service']
    list_filter = ['micro_service']


class StatusCodeAdmin(admin.ModelAdmin):
    list_display = ['status_code']
    search_fields = ['status_code']
    list_filter = ['status_code']


class CreateTestApiAdmin(admin.ModelAdmin):
    list_display = ['micro_service', 'host', 'base_url', 'method', 'description', 'status_code', 'assertion', 'value_assertion', 'add_time']
    # search_fields = ['micro_service']
    list_filter = ['micro_service']


admin.site.register(MicroService, MicroServiceAdmin)
admin.site.register(StatusCode, StatusCodeAdmin)
admin.site.register(CreateTestApi, CreateTestApiAdmin)