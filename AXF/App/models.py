from django.db import models

# Create your models here.

class Main(models.Model):
    img = models.CharField(max_length=255)
    name = models.CharField(max_length=64)
    trackid = models.CharField(max_length=16)

    '''
    img     name        trackid
    '''
    class Meta:
        abstract = True


class Wheel(Main):

    '''轮播图'''
    class Meta:
        db_table = 'axf_wheel'


class Nav(Main):

    '''导航栏'''
    class Meta:
        db_table = 'axf_nav'


class MustBuy(Main):

    '''每日必买'''
    class Meta:
        db_table = 'axf_mustbuy'


class Shop(Main):

    '''热销'''
    class Meta:
        db_table = 'axf_shop'


class MainShow(Main):

    # 主要商品
    categoryid = models.CharField(max_length=16)
    brandname = models.CharField(max_length=32)

    img1 = models.CharField(max_length=255)
    childcid1 = models.CharField(max_length=16)
    productid1 = models.CharField(max_length=16)
    longname1 = models.CharField(max_length=128)
    price1 = models.CharField(max_length=16)
    marketprice1 = models.CharField(max_length=16)

    img2 = models.CharField(max_length=255)
    childcid2 = models.CharField(max_length=26)
    productid2 = models.CharField(max_length=26)
    longname2 = models.CharField(max_length=228)
    price2 = models.CharField(max_length=26)
    marketprice2 = models.CharField(max_length=26)

    img3 = models.CharField(max_length=255)
    childcid3 = models.CharField(max_length=36)
    productid3 = models.CharField(max_length=36)
    longname3 = models.CharField(max_length=328)
    price3 = models.CharField(max_length=36)
    marketprice3 = models.CharField(max_length=36)

    class Meta:
        db_table = 'axf_mainshow'


class FoodType(models.Model):
    # 食物种类
    typeid = models.CharField(max_length=16)
    typename = models.CharField(max_length=32)
    childtypenames = models.CharField(max_length=256)
    typesort = models.IntegerField()

    class Meta:
        db_table = 'axf_foodtypes'


class User(models.Model):
    # 用户模型
    username = models.CharField(max_length=64, unique=True)
    password = models.CharField(max_length=256)
    nickname = models.CharField(max_length=64)
    address = models.CharField(max_length=128)
    img = models.ImageField(upload_to='%Y/%m/%d/%H/%M/%S/icons')
    level = models.IntegerField(default=1)
    token = models.CharField(max_length=256)
    active = models.BooleanField(default=False)
    is_delete = models.BooleanField(default=True)
    email = models.CharField(max_length=64)

    class Meta:
        db_table = 'user'


class Goods(models.Model):
    # 商品表
    productid = models.CharField(max_length=16)
    productimg = models.CharField(max_length=128)
    productname = models.CharField(max_length=64)
    productlongname = models.CharField(max_length=128)
    isxf = models.IntegerField(default=0)
    pmdesc = models.IntegerField(default=0)
    specifics = models.CharField(max_length=32)
    price = models.FloatField()
    marketprice = models.FloatField()
    categoryid = models.IntegerField()
    childcid = models.IntegerField()
    childcidname = models.CharField(max_length=64)
    dealerid = models.CharField(max_length=32)
    storenums = models.IntegerField()
    productnum = models.IntegerField()

    class Meta:
        db_table = 'axf_goods'


class Cart(models.Model):
    goods_num = models.IntegerField(default=1)
    is_select = models.BooleanField(default=True)

    user_id = models.ForeignKey(User)
    goods_id = models.ForeignKey(Goods)

    class Meta:
        db_table = 'cart'


# 订单表
class Order(models.Model):
    # o_cart = models.ForeignKey(Cart)
    o_user = models.ForeignKey(User)
    price = models.FloatField()

    order_time = models.DateTimeField(auto_now=True)
    # 支付状态,默认未支付
    status = models.BooleanField(default=False)

    class Meta:
        db_table = 'order'


# 订单商品表
class OrderGoods(models.Model):
    o_order = models.ForeignKey(Order)
    goods = models.ForeignKey(Goods)
    goods_num = models.IntegerField()

    class Meta:
        db_table = 'order_goods'