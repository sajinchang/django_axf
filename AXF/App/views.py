from uuid import uuid4

from alipay import AliPay
from django.contrib.auth.hashers import make_password, check_password
from django.core.cache import cache
from django.core.mail import send_mail
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect

from django.template import loader
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt

from AXF import settings
from AXF.settings import ALIPAY_APPID, APP_PRIVATE_KEY, ALIPAY_PUBLIC_KEY
from App.models import Wheel, Nav, MustBuy, Shop, MainShow, User, FoodType, Goods, Cart, Order, OrderGoods
from App.views_contstant import ORDER_PRICE_DOWN, ORDER_PRICE_UP, ORDER_SALE_UP, ORDER_SALE_DOWN, ALLTYPE, \
    DEFAULT, sum_price


# Create your views here.

def index(request):

    return HttpResponse('<h1 style="color:green;font-size:100px;">我是SamSa派来的测试小网页!</h1>')

'主页'
def home(request):
    # 轮播
    wheels = Wheel.objects.all()
    # 导航
    navs = Nav.objects.all()
    # 每日必买
    mustbuys = MustBuy.objects.all()
    # 热销
    shops = Shop.objects.all()

    main_info = MainShow.objects.all()

    context = {
        'title': '首页',
        'main_wheels': wheels,
        'main_navs': navs,
        'main_mustbuys': mustbuys,
        'shops_conv': shops[0],
        'shops_top': shops[1:3],
        'shops_more': shops[3:7],
        'shops_reco': shops[7:],
        'main_shops': main_info,

    }
    return render(request, 'main/home.html', context=context)

'闪购'
def market(request):

    data = {
        'typeid': '104749',
        'childcid': '0',
        'rule': '0',
    }
    return redirect(reverse('app:detailed',kwargs=data ))

'购物车'
def cart(request):
    user = request.user

    carts = Cart.objects.filter(user_id_id=user.id)
    total_price = sum_price(carts)

    data = {
        'title':'购物车',
        'user': user,
        'carts': carts,
        'total_price': total_price
    }


    return render(request, 'main/cart.html', context=data)

'我的'
def mine(request):
    username = request.session.get('username')
    # print('===============')
    # print(username)
    data = {
        'flag': False,
        'title': '我的',

    }
    if username:
        # print('----------------')
        user = User.objects.get(username=username)
        data['flag'] = True
        data['nickname'] = user.nickname
        data['level'] = user.level
        data['img']= settings.MEDIA_KEY_PREFIX + user.img.url
        data['username'] = username
    # print(data)

    return render(request, 'main/mine.html', context=data)

# 注册
def register(request):
    if request.method == 'GET':
        return render(request, 'user/register.html')

    username = request.POST.get('username')
    password = request.POST.get('password')
    email = request.POST.get('email')
    nickname= request.POST.get('nickname')
    address = request.POST.get('address')
    img = request.FILES.get('img')

    user = User()
    user.username = username
    user.password = make_password(password)
    user.email = email
    user.nickname = nickname
    user.img = img
    user.address = address

    token = str(uuid4())
    user.token = token
    cache.set(token, token, timeout=60)
    user.save()

    # 发送邮件
    title = '激活'
    msg = ' '

    data = {
        'username': username,
        'url': 'http://127.0.0.1:8000/app/active/?token=' + token
    }
    temp = loader.get_template('user/active.html')
    html = temp.render(data)

    receiver = [
        email,
    ]

    send_mail(title,
              msg,
              from_email=settings.DEFAULT_FROM_EMAIL,
              recipient_list=receiver,
              html_message=html,
              )
    return redirect(reverse('app:login'))
    # return render(request,'main/mine.html')

@csrf_exempt
def login(request):
    if request.method == 'GET':
        return render(request, 'user/login.html')

    username = request.POST.get('username')
    password = request.POST.get('password')

    user = User.objects.filter(username=username).last()
    error = {
        'msg':'登录',
    }
    if not user:
        error['msg'] = '用户名错误'
        return render(request, 'user/login.html', error)

    if not check_password(password,user.password):
        error['msg'] = '密码不正确'
        return render(request=request, template_name='user/login.html', context=error)

    if not user.active:
        error['msg'] = '未激活'
        return render(request=request, template_name='user/login.html', context=error)

    if not user.is_delete:
        error['msg'] = '用户已删除'
        return render(request=request, template_name='user/login.html', context=error)

    data ={
        'title':'登陆',
        'flag': True,
        'nickname': user.nickname,
        'level': user.level,
        'img': settings.MEDIA_KEY_PREFIX + user.img.url,
        'username': username,
    }

    # print('-' * 50)
    # print(data['img'])
    # print('-' * 50)
    # 设置session
    request.session['username'] = username
    request.session['userid'] = user.id
    return render(request, 'main/mine.html', context=data)

# logout
def logout(request):
    # print('*****2222*********')
    request.session.flush()
    return render(request, 'main/mine.html', {'flag': False})

# 激活
def active(request):
    token = request.GET.get('token')

    if cache.get(token):
        user = User.objects.filter(token=token).last()
        user.active = True
        user.save()
        return render(request, 'user/success.html')

    return render(request, 'user/fail.html')

def checkuser(request):
    username = request.GET.get('username')
    user = User.objects.filter(username=username).first()
    data = {
        'status': 200,
    }
    if user:
        data['status'] = 201
        return JsonResponse(data=data)
    print('*' * 50)
    print(123)
    print('*' * 50)
    return JsonResponse(data=data)

# 闪购页面展示
def market_detailed(request, typeid, childcid, rule):
    foodtypes = FoodType.objects.all()
    goods = Goods.objects.filter(categoryid=typeid)

    order_rule_list = [

        ['综合排序', DEFAULT],
        ['价格升序', ORDER_PRICE_UP],
        ['价格降序', ORDER_PRICE_DOWN],
        ['销量升序', ORDER_SALE_UP],
        ['销量降序', ORDER_SALE_DOWN],
    ]
    if childcid == ALLTYPE:
        pass
    else:
        goods = goods.filter(childcid=childcid)

    if rule == DEFAULT:
        pass

    elif rule == ORDER_PRICE_UP:
        goods = goods.order_by('price')

    elif rule == ORDER_SALE_DOWN:
        goods = goods.order_by('-price')

    elif rule == ORDER_SALE_UP:
        goods = goods.order_by('productnum')

    elif rule == ORDER_SALE_DOWN:
        goods = goods.order_by('-productnum')

    # 获取详细分类类型
    foodtype = foodtypes.get(typeid=typeid)
    # 切取分类名称
    type_list = foodtype.childtypenames.split('#')
    types = []
    for type in type_list:
        types.append(type.split(':'))

    data = {
        'title': '闪购',
        'foodtypes': foodtypes,
        'order_rule_list': order_rule_list,
        'goods':goods,
        'childcid': childcid,
        'rule': rule,
        'typeid': typeid,
        'types': types,

    }

    # print(typeid, childcid, rule)
    # print(123)
    return render(request, 'main/market.html', context=data)


# 个人详细信息
def person(request):
    username = request.GET.get('username')
    user = User.objects.get(username=username)
    return render(request, 'user/personinfo.html', context={
        'user': user,
        'title': '个人信息',
    })


# 购物车删减
def add_cart(request):
    goods_id = request.GET.get('goodsid')
    way = request.GET.get('way')
    user_id = request.session.get('userid')

    users = Cart.objects.filter(user_id_id=user_id)

    carts = users.filter(goods_id_id=goods_id)
    data = {
        'total_price': sum_price(users)
    }

    num = 0
    if carts.exists():
        cart = carts.first()
        data['goodid'] = cart.goods_id_id
        data['code'] = 200
        if way == 'add':
            cart.goods_num += 1
            num = cart.goods_num

            cart.save()
        elif way == 'sub':
            cart.goods_num -= 1
            num = cart.goods_num

            if cart.goods_num == 0:
                cart.delete()
            else:
                cart.save()

    else:
        if way == 'add':
            cart = Cart()
            cart.goods_id_id = goods_id
            cart.user_id_id = user_id
            num = 1
            data['goodid'] = cart.goods_id_id
            cart.save()
        elif way == 'sub':
            data['code'] = 201

    # data['cartid'] = cartid
    data['msg'] = 'ok'
    data['goods_num'] = num

    return JsonResponse(data=data)

# 购物车中的商品是否选中
def select(request):
    cartid = request.GET.get('cartid')
    cart = Cart.objects.get(pk=cartid)

    data = {
        'code': 200
    }
    try:
        if cart.is_select == True:
            cart.is_select = False
        else:
            cart.is_select = True

        data['flag'] = cart.is_select

        cart.save()

    except Exception as e:
        print(e)
        redirect(reverse('app:cart'))
    userid = request.session.get('userid')
    carts = Cart.objects.filter(user_id_id=userid)
    total_price = sum_price(carts=carts)
    data['total_price'] = total_price
    print('+' * 50 )
    print(cart.id,cart.is_select)
    print('+' * 50 )
    return JsonResponse(data=data)


# 全选和全不选
def select_all(request):
    userid = request.session.get('userid')
    way = request.GET.get('way')
    data = {}
    carts = Cart.objects.filter(user_id_id=userid)
    if way == 'all':
        data['code'] = 200
        for cart in carts:
            if cart.is_select == False:
                cart.is_select = True
                cart.save()

        total_price = sum_price(carts=carts)
        data['total_price'] = total_price
        # print(total_price)

    elif way == 'null':
        data['total_price'] = 0
        data['code'] = 200
        print(data['total_price'])
        for cart in carts:
            if cart.is_select == True:
                cart.is_select = False
                cart.save()
    else:
        data['code'] = 201

    print(data['total_price'])
    return JsonResponse(data=data)

# 下单
def make_order(request):
    userid = request.session.get('userid')
    # print(userid)
    carts = Cart.objects.filter(user_id_id=userid).filter(is_select=True)

    # 订单表
    order = Order()
    order.price = sum_price(carts)
    order.o_user_id = userid
    order.save()

    # 订单商品表
    for cart in carts:
        order_goods = OrderGoods()
        order_goods.o_order = order
        order_goods.goods = cart.goods_id
        order_goods.goods_num = cart.goods_num
        order_goods.save()
        cart.delete()

    # print(order.ordergoods_set.all())
    data = {
        'code': 200,
        'msg': 'ok',
        'order': order,
    }
    return render(request, 'order/order_detail.html', context=data)


def pay(request):
    orderid = request.GET.get('orderid')
    try:
        order = Order.objects.get(pk=orderid)

        order.status = True
        order.save()

        data = {
            'code': 200,
            'msg': 'ok',
            'price': order.price,
        }
    except Exception as e:
        print(e)
        data = {
            'code': 201,
        }

    return JsonResponse(data=data)


def alipay(request):
    orderid = request.GET.get('orderid')
    print(orderid)

    # 构建支付的科幻  AlipayClient
    alipay_client = AliPay(
        appid=ALIPAY_APPID,
        app_notify_url=None,  # 默认回调url
        app_private_key_string=APP_PRIVATE_KEY,
        alipay_public_key_string=ALIPAY_PUBLIC_KEY,  # 支付宝的公钥，验证支付宝回传消息使用，不是你自己的公钥,
        sign_type="RSA",  # RSA 或者 RSA2
        debug=False  # 默认False
    )
    # 使用Alipay进行支付请求的发起

    subject = "SAM购物商城"

    # 电脑网站支付，需要跳转到https://openapi.alipay.com/gateway.do? + order_string
    order_string = alipay_client.api_alipay_trade_page_pay(
        out_trade_no="110",
        total_amount= Order.objects.get(pk=orderid).price,
        subject=subject,
        return_url="http://www.baidu.com",
        notify_url="http://www.baidu.com"  # 可选, 不填则使用默认notify url
    )

    # 客户端操作

    return redirect("https://openapi.alipaydev.com/gateway.do?" + order_string)
    # return HttpResponse('支付宝')