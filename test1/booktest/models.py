from django.db import models

# Create your models here.
#定義這邊的類別是為了創建出SQL的table
#之後django會直接把這邊類別的物件導向操作映射成SQL語句去操作SQL
class BookInfo(models.Model):
    btitle = models.CharField(max_length=20)
    bpub_date = models.DateTimeField()

    #這個是為了讓之後如果透過BookInfo.objects.all()拿到東西會print出內容
    #不然就只有 [<BookInfo: BookInfo object>]
    def __str__(self):
        return self.btitle

class HeroInfo(models.Model):
    hname = models.CharField(max_length=10)
    hgender = models.BooleanField()
    hcontent = models.CharField(max_length=1000)
    hbook = models.ForeignKey(BookInfo) #這邊是希望讓hbook指向一個BookInfo的類別

    def __str__(self):
        return self.hname
