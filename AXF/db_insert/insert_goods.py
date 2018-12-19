# -*- coding: utf-8 -*-
# @Time    : 18-12-16 下午10:54
# @Author  : SamSa
# @Email   : sajinde@qq.com
# @File    : insert_goods.py
# @statement:将数据插入goods表
import pymysql


def main():

    con = pymysql.connect(
        host='localhost',
        port=3306,
        password='123456',
        user='root',
        charset='utf8',
        database='axf',
    )
    cur = con.cursor()

    count = 0
    try:
        with open('data', 'r', encoding='utf-8') as fp:
            for line in fp:
                cur.execute(line)
                count += 1
        con.commit()
    except Exception as e:
        print(e)
    finally:
        cur.close()
        con.close()

    print('------the end -------\t\t\t',count)


if __name__ == '__main__':
    main()