# -*- coding: utf-8 -*-
# @Time    : 18-12-19 下午2:39
# @Author  : SamSa
# @Email   : sajinde@qq.com
# @File    : middleware.py
# @statement:中间件  登录状态获取
from django.shortcuts import redirect
from django.urls import reverse
from django.utils.deprecation import MiddlewareMixin

from App.models import User

LOGIN = [
    '/app/cart/',
    '/app/add_cart/',

]


class LoginMiddleware(MiddlewareMixin):

    def process_request(self, request):
        # print('-----------123-----------')
        print(request.path)
        if request.path in LOGIN:
            print('-----------123-----------')
            username = request.session.get('username')
            if username:
                try:
                    user = User.objects.get(username=username)
                    request.user = user
                except Exception as e:
                    print(e)
                    return redirect(reverse('app:login'))
            else:
                print('-----------456-----------')
                return redirect(reverse('app:login'))
