#!/usr/bin/python
# -*-coding:utf-8 -*-
__author__ = 'yuntong'

"""
说明:根据拼音首字母匹配姓名
库:汉字转拼音库: https://github.com/cleverdeng/pinyin.py
"""

from pinyin import PinYin
import sys
import xlrd
import xlwt
import os

reload(sys)
sys.setdefaultencoding('utf-8')
def zcf(namelist):
    """
    :param namelist:
    :return If the match returns a list of numbers, else return None:
    """
    nlist = []
    flag = 0
    test = PinYin()
    test.load_word()
    key = raw_input("关键词  :  ")
    for x in range(len(namelist)):
        #print namelist[x]
        t = test.hanzi2pinyin(str(namelist[x]))
        charnum = len(list(namelist[x].decode('utf-8')))
        flag2 = True
        if len(key) == charnum:
            #print str(len(key)) + " " + str(charnum)
            for xx in range(charnum):
                 flag2 = (t[xx][0] == key[xx]) and flag2
        else:
            continue
        if flag2 is True:
            flag += 1
            nlist.append(x)    
    if flag == 0:
        return None
    else:
        return nlist

if __name__ == "__main__":
    
    test2 = ["王朗", "诸葛孔明", "孙悟空","猪八戒","罗贯中",  "傻和尚","曹雪芹", "沙和尚", "牛魔王", "白骨精", "诸葛孔明"]
    match = zcf(test2)
    if match is not None:
        print match
        for num2 in range(len(match)):
                print test2[match[num2]]
    else:
        print "未匹配"

# 从xls文件中读取第二列姓名数据
#    prepareList_u = []
#    dnn = {}
#    name = "5"
#    fname = name + ".xls"
#    book = xlrd.open_workbook(fname)
#    sh=book.sheet_by_index(0)
#    nrows = sh.nrows
#    ncols = sh.ncols
#    for dataUpBound in range(nrows):
#        try:
#            originalData = sh.cell_value(rowx=dataUpBound,colx=1)
#            number = sh.cell_value(rowx=dataUpBound,colx=0)
#            dnn[number] = originalData
#            prepareList_u.append(originalData)
#        except:
#            continue
#            os.system(ls)
#    print "所在文件 ： " +  name +  "\n样本数：" + str(len(prepareList_u))
#    print len(dnn)
#    match = zcf(prepareList_u)
#    if match is not None:
#        print match
#        for num2 in range(len(match)):
#                #match_data = {}
#                value = str(prepareList_u[match[num2]])
#                #keys = [dnn[0] for dnn in dnn.items() if value in dnn[1] ] 
#                print value + " " 
#    else:
#        print "未匹配"
