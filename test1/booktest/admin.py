from django.contrib import admin

# Register your models here.

from .models import *
#為了讓網頁顯示出models.py裡面有定義的欄位 (attribute)
class BookInfoAdmin(admin.ModelAdmin):
    list_display = ['id', 'btitle', 'bpub_date'] #id是django會自己產生的
    list_filter = ['btitle']

admin.site.register(BookInfo, BookInfoAdmin)
admin.site.register(HeroInfo)