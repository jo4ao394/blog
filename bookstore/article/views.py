import datetime
from lib2to3.fixes.fix_input import context

from django.shortcuts import render
from django.template.defaulttags import now


def article(request):
    '''
    Render the article page
    '''
    now = datetime.datetime.now()
    print(now.hour)
    context={'hello':'歡迎光臨本書店', 'now':now}
    return render(request, 'article/article.html',context)
# Create your views here.
