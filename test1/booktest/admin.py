from django.contrib import admin

# Register your models here.

from .models import *
#這個類是為了把HeroInfo鑲嵌到BookInfo裡面去,效果是在admin網頁產生BookInfo的時候可以連帶產生HeroInfo
class HeroInfoInline(admin.StackedInline):
    model = HeroInfo
    extra = 3 #選單裡面起始要出現幾個HeroInfo新增

#為了讓網頁顯示出models.py裡面有定義的欄位 (attribute)
class BookInfoAdmin(admin.ModelAdmin):
    list_display = ['id', 'btitle', 'bpub_date'] #id是django會自己產生的
    list_filter = ['btitle'] #在admin網頁出現filter要篩選的欄位
    search_fields = ['btitle'] #在admin網頁出現search要篩選的欄位
    list_per_page = 5 #每頁出現幾條

    inlines = [HeroInfoInline]


class HeroInfoAdmin(admin.ModelAdmin):
    list_display = ['id', 'hname', 'hgender','hcontent','hbook'] #id是django會自己產生的
    list_filter = ['hname']



admin.site.register(BookInfo, BookInfoAdmin)
admin.site.register(HeroInfo, HeroInfoAdmin)