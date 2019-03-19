from django.contrib.auth import get_user_model
from django.shortcuts import render
from django.shortcuts import render, redirect
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
import requests
import bs4
from textblob import TextBlob
# import matplotlib.pyplot as plt
User = get_user_model()
def index(request):
    return render(request,'index.html',{"customer":10})


def get_data(request ,*arg,**kwargs):
    res = requests.get("https://www.football365.com/")
    soup = bs4.BeautifulSoup(res.text,'html')
    select_text = soup.find_all("figcaption" , {"class":"articleList__figcaption"})
    for x in select_text:
        con = x.contents[1].text
        con += x.contents[3].text
        positive , negative , neutral = 0,0,0
    for con in select_text:
        text = con.get_text()
        sentiment = TextBlob(text).sentiment.polarity
        if (sentiment >=0 and sentiment< 0.4):
            positive+=1
        elif (sentiment>=0.4 and sentiment<=0.6):
            neutral+=1
        else:
            negative+=1
    labels = [  'Positive', 'Neutral', 'Negative']
    default_items = [positive,neutral,negative]
    data = {

    "labels":labels,
    "default":default_items,

    }
    return JsonResponse(data)
class ChartData(APIView):
    """
    View to list all users in the system.

    * Requires token authentication.
    * Only admin users are able to access this view.
    """
    authentication_classes = []
    permission_classes =[]

    def get(self, request, format=None):
        # qs_count = User.objects.all().count()

        labels = [  'Positive', 'Neutral', 'Negative']
        default_items = [12,36,13]
        data = {
        "labels":labels,
        "default":default_items,


        }
        return Response(data)
    def scarpdate(self):
        res = requests.get("https://www.football365.com/")
        soup = bs4.BeautifulSoup(res.text,'html')
        select_text = soup.find_all("figcaption" , {"class":"articleList__figcaption"})
        for x in select_text:
            con = x.contents[1].text
            con += x.contents[3].text
            positive , negative , neutral = 0,0,0
        for con in select_text:
            text = con.get_text()
            sentiment = TextBlob(text).sentiment.polarity
            if (sentiment >=0 and sentiment< 0.4):
                positive+=1
            elif (sentiment>=0.4 and sentiment<=0.6):
                neutral+=1
            else:
                negative+=1
        return positive,negative,neutral
