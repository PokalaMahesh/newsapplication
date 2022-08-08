from django.shortcuts import render

from .utils import get_news_from_api
from .models import Articles

# Create your views here.
def home(request):
    # url = 'https://newsapi.org/v2/everything?q=tesla&from=2022-07-07&sortBy=publishedAt&apiKey=9a25036484a34d8dab9433e010159929'
    # get_news_from_api(url)
    return render(request, 'home.html' , context={'Articles' : Articles.objects.all()})
