'''
 -*- coding: utf-8 -*-
 @Time : 18-12-13 下午3:44
 @Author : SamSa
 @File : urls.py
 @Software: PyCharm
 @Statement:
'''
from django.conf.urls import url

from App import views

urlpatterns = [
    url(r'^index/', views.index, name='index'),

    url(r'^home', views.home, name='home'),
    url(r'^market/', views.market, name='market'),
    url(r'^cart/', views.cart, name='cart'),
    url(r'^mine/',views.mine, name='mine'),
    url(r'^market_detailed/(?P<typeid>\d+)/(?P<childcid>\d+)/(?P<rule>\d+)/', views.market_detailed, name='detailed'),

    url(r'^register/', views.register, name='register'),
    url(r'^active/', views.active, name='active'),

    url(r'^login/', views.login, name='login'),
    url(r'^logout', views.logout, name='logout'),
    url(r'^checkuser/', views.checkuser, name='checkuser'),

    url(r'^person/', views.person, name='person'),

    # 购物车删减
    url(r'^add_cart/', views.add_cart, name='add_cart'),
    # 单选
    url(r'^select/', views.select, name='select'),
    # 全选
    url(r'^select_all/', views.select_all, name='select_all'),

    url(r'^make_order/', views.make_order, name='make_order'),
    url(r'^pay/', views.pay, name='pay'),
    url(r'^alipay/', views.alipay, name='alipay'),

]