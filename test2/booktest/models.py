from django.db import models

# Create your models here.

class BookInfoManager(models.Manager): #繼承models.Manager類別
    def get_queryset(self): #重寫models.Manager的get_queryset方法 (比原本多出一個.filter(isDelete=False))
        return super(BookInfoManager, self).get_queryset().filter(isDelete=False)

    #使用method來創建物件
    def create(self, btitle, bpub_date):
        b = BookInfo()
        b.btitle = btitle
        b.bpub_date = bpub_date
        b.bread = 0
        b.bcommet = 0
        b.isDelete = False
        return b

class BookInfo(models.Model):
    btitle = models.CharField(max_length=20)
    bpub_date = models.DateTimeField(db_column='pub_date') #刻意修改table裡面的欄位名稱(把b拿掉),要注意之後調用還是認attribute name (bpub_date)
    bread = models.IntegerField(default=0)
    bcommet = models.IntegerField(default=0)
    isDelete = models.BooleanField(default=False)
    class Meta(): #預設的table name會是<app_name>_<model_name>, 所以應該會是booktest_BookInfo
        db_table = 'bookinfo' #這邊自訂修改表的名子 所以會變成bookinfo

    #使用自訂的manager類別
    books1 = models.Manager()
    books2 = BookInfoManager()

    #用class method來創建物件 (但是比較建議在manager類裡面做)
    @classmethod
    def create(cls, btitle, bpub_date):
        b = BookInfo()
        b.btitle = btitle
        b.bpub_date = bpub_date
        b.bread = 0
        b.bcommet = 0
        b.isDelete = False
        return b

class HeroInfo(models.Model):
    hname = models.CharField(max_length=20)
    hgender = models.BooleanField(default=True)
    isDelete = models.BooleanField(default=False)
    hcontent = models.CharField(max_length=100)
    hbook = models.ForeignKey('BookInfo')