from django.shortcuts import render ,redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.http import JsonResponse
# Create your views here.
import random
from random import sample
import datetime
from mysite.models import Post ,Country, City,Note
from plotly.offline import plot
import plotly.graph_objs as go
import numpy as np
from django.contrib.auth import logout


def index(request):
    name = "陳志清"
    lotto = [random.randint(1,42) for i in range(6)]
    alla = []
    for i in range(1,49):
        alla.append(i)
    a = sample(alla, k=6)
    special = a[0]
    lotto = a[1:6]
    x = np.linspace(0, 2 * np.pi, 360)
    y1 = np.sin(x)
    y2 = np.cos(x)
    plot_div = plot([go.Scatter(x=x, y=y1,
                    mode='lines', name='SIN',
                    opacity=0.8, marker_color='green'),

                     go.Scatter(x=x, y=y2,
                    mode='lines', name='COS',
                    opacity=0.8, marker_color='blue')
                     ],
                    output_type='div')
    return render(request, "index.html",locals())       #locals在func設變數,立即丟變數

def news(request):
    posts = Post.objects.all()                  #加資料庫的方法
    return render(request,"news.html",locals())
@login_required(login_url="/admin/login/")
def show(request,id):
    try:
        post = Post.objects.get(id=id)      #找出符合條件第一個紀錄
        #post = Post.objects.filter(id=id)   #找出符合條件所有紀錄
    except:
        return redirect("/news/")           #返回到首頁
    return render(request,"show.html",locals())

@login_required(login_url="/admin/login/")
def rank(request):
    #POST 需id
    if request.method =='POST':
        id = request.POST["id"]
        if id.strip() =="999":
            return redirect("/rank/")
        try:
            country = Country.objects.get(id=id)
        except:
            return redirect("/rank/")
        cities = City.objects.filter(country=country).order_by('population')    #-population由後往前
    else:
        cities = City.objects.all().order_by('population')        #無找到指定國家
    countries = Country.objects.all()
    return render(request,"rank.html",locals())

@login_required(login_url="/admin/login/")
def chart(request):

    # POST 需id
    if request.method == 'POST':
        id = request.POST["id"]
        if id.strip() =="999":
            return redirect("/chart/")
        try:
            country = Country.objects.get(id=id)
        except:
            return redirect("/chart/")
        cities = City.objects.filter(country=country).order_by('-population')  # -population由後往前
    else:
        cities = City.objects.all().order_by('-population')  # 無找到指定國家
    countries = Country.objects.all()

    names = [city.name for city in cities]
    population = [city.population for city in cities]
    return render(request, "chart.html", locals())      #locals變數全丟

def mylogout(request):
    logout(request)
    return redirect("/")


def delete(request, id):
    try:
        post = Post.objects.get(id=id)
        post.delete()
    except:
        return redirect("/news/")

    return redirect("/news/")

def note(request):
    notes = Note.objects.all()
    return render(request, "note.html", locals())

def addnote(request):
    if request.method =="POST":
        title = request.POST["title"]
        if len(title) >10:
            note = Note(title=title)
            note.save()
    return redirect("/note/")