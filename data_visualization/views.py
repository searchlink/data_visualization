# -*- coding: utf-8 -*-
# @Time    : 2020/7/21 16:56
# @Author  : skydm
# @Email   : wzwei1636@163.com
# @File    : views.py
# @Software: PyCharm

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from dashboard.models import City
from django.db.models import Sum
import json


def index(request):
    return render(request, 'index.html', {})


def pie_chart(request):
    labels = []
    data = []

    queryset = City.objects.order_by('-population')[:5]
    for city in queryset:
        labels.append(city.name)
        data.append(city.population)

    data = dict(zip(labels, data))

    return render(request, 'pie_chart.html', {'data': json.dumps(data)})


def home(request):
    return render(request, 'home.html')


def population_chart(request):
    labels = []
    data = []

    # 跨models进行查询，注意要使用 "__" + 字段名来调用，另外annotate类似groupby操作, 可以对进行聚合操作的数据赋予新的名称
    queryset = City.objects.values('country__name').annotate(country_population=Sum('population')).order_by('-country_population')
    for entry in queryset:
        labels.append(entry['country__name'])
        data.append(entry['country_population'])

    return JsonResponse(data={'labels': labels, 'data': data})



