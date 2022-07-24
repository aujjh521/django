from django.db import models

# Create your models here.
class BookInfo(models.Model):
    btitle = models.CharField(max_length=20)
    bpub_date = models.DateTimeField(db_column='pub_date') #刻意修改table裡面的欄位名稱(把b拿掉),要注意之後調用還是認attribute name (bpub_date)
    bread = models.IntegerField(default=0)
    bcommet = models.IntegerField(default=0)
    isDelete = models.BooleanField(default=False)
    class Meta(): #預設的table name會是<app_name>_<model_name>, 所以應該會是booktest_BookInfo
        db_table = 'bookinfo' #這邊自訂修改表的名子 所以會變成bookinfo

class HeroInfo(models.Model):
    hname = models.CharField(max_length=20)
    hgender = models.BooleanField(default=True)
    isDelete = models.BooleanField(default=False)
    hcontent = models.CharField(max_length=100)
    hbook = models.ForeignKey('BookInfo')