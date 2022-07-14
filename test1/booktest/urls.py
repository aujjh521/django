from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index), #django會利用政則表達匹配網址路径部分，即除去域名、参数后的字符串, 只要符合就會執行views指定的function
]