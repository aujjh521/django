from django.db import models

# Create your models here.
#定義這邊的類別是為了創建出SQL的table
#之後django會直接把這邊類別的物件導向操作映射成SQL語句去操作SQL
class BookInfo(models.Model):
    btitle = models.CharField(max_length=20)
    bpub_date = models.DateTimeField()

class HeroInfo(models.Model):
    hname = models.CharField(max_length=10)
    hgender = models.BooleanField()
    hcontent = models.CharField(max_length=1000)
    hbook = models.ForeignKey(BookInfo) #這邊是希望讓hbook指向一個BookInfo的類別
