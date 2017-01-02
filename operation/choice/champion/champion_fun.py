#!/usr/bin/env python
#encoding:UTF-8
import random
import numpy as np
from mycmp import *

"""
        锦标赛 方式选择, 选择个体编号

        indicateValue  为  individual_layer_value
        {个体号码:[个体所属层号， 个体两边的距离总值]}
"""
def champion(indicateValue, choiceNum):
    ###锦标赛参数6, 一次选择的窗口大小
    winNum=6

    ###构建列表      [(层号， 距离, 索引), ]
    valueList=[]
    for k, v in indicateValue.items():
        valueList.append((v[0], v[1], k))

    ###列表 记录保存的个体序号
    nextRemain=[]

    for i in xrange(choiceNum):
        tempList=[]
        tempList.extend(random.sample(valueList, winNum))
        tempList.sort(cmp=mycmp)

        nextRemain.append(tempList[0][-1])
    
    ###返回选择的序号
    return nextRemain


if __name__=="__main__":
    xN=20
    yN=3
    indicateValue={0:[1,2.1], 1:[1,2.2], 2:[1,2.3], 3:[1,2.4], 4:[1,2.5], 5:[1,2.6], 6:[1,2.7], 7:[1,2.8], 8:[1,2.9], 9:[1,3.0], 10:[0,2.1], 11:[0,2.2], 12:[0,2.3], 13:[0,2.4], 14:[0,2.5], 15:[0,2.6], 16:[0,2.7], 17:[0,2.8], 18:[0,2.9], 19:[0,3.0]}

    print champion(indicateValue, 10)


