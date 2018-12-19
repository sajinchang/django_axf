# -*- coding: utf-8 -*-
# @Time    : 18-12-18 下午6:52
# @Author  : SamSa
# @Email   : sajinde@qq.com
# @File    : views_contstant.py
# @statement:


ALLTYPE = '0'
# 排序
DEFAULT = '0'
ORDER_PRICE_UP = '1'
ORDER_PRICE_DOWN = '2'
ORDER_SALE_UP = '3'
ORDER_SALE_DOWN = '4'


def sum_price(carts):
    total_price = 0
    for cart in carts:
        if cart.is_select:
            price = cart.goods_num * cart.goods_id.price
            total_price += price

    return '{:.2f}'.format(total_price)
    # return total_price