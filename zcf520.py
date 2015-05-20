#!/usr/bin/python
# -*-coding:utf-8 -*-
__author__ = 'yuntong'

"""
说明:根据拼音首字母匹配姓名
库:汉字转拼音库: https://github.com/cleverdeng/pinyin.py
"""

from pinyin import PinYin
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
def zcf(namelist):
    """
    :param namelist:
    :return If the match returns a list of numbers, else return None:
    """
    flag = 0
    test = PinYin()
    test.load_word()
    key = raw_input("关键词  :  ")
    for x in range(len(namelist)):
        t = test.hanzi2pinyin(str(namelist[x]))
        charnum = len(list(namelist[x].decode('utf-8')))
        flag2 = True
        if len(key) == charnum:
            for xx in range(charnum):
                 flag2 = (t[xx][0] == key[xx]) and flag2
        else:
            continue
        if flag2 is True:
            flag += 1
            return x
    if flag == 0:
        return None

if __name__ == "__main__":
    test2 = ["王朗", "诸葛孔明", "孙悟空","猪八戒","罗贯中", "曹雪芹", "沙和尚", "牛魔王", "白骨精", "诸葛孔明"]
    match = zcf(test2)
    if match is not None:
        print test2[match]
    else:
        print "未匹配"
