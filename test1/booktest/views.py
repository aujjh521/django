from django.shortcuts import render
from django.http import * # 這是django的 request, response等等package, 以request來講django會幫忙先處理好相關的request資料

from django.template import RequestContext, loader #為了使用template
from .models import * #為了從SQL table取資料

# Create your views here.
def index(request): #意思是server等待外面來的request, 再return response
    #temp = loader.get_template('booktest/index.html')
    #return HttpResponse(temp.render())
    booklist = BookInfo.objects.all()
    context = {'booklist': booklist}
    return render(request, 'booktest/index.html',context) # 透過django本身的render一次執行完讀取template & 渲染並返回http response