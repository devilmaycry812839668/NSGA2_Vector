#!/usr/bin/env python
#encoding:UTF-8 
import numpy as np

"""
    单点交叉
"""
def cross(population, alfa):
    cross_indicate=np.arange(population.shape[0])
    np.random.shuffle(cross_indicate)

    #两两交叉的个体索引位置
    locate_cross=cross_indicate[0:int(population.shape[0]*alfa)]

    #两两交叉的交叉点位置
    point_cross=np.random.randint(1, population.shape[1], len(locate_cross)/2)

    for i in xrange(0, len(locate_cross)/2):
        #需要交叉的行号 
        var_0=locate_cross[i*2]
        var_1=locate_cross[i*2+1]

        #需要交叉的位置
        var_p=point_cross[i]

        population[[var_0, var_1],0:var_p]=population[[var_1, var_0],0:var_p]


###以下是测试用例
if __name__=="__main__":
    np.random.seed(0)
    xN=20
    yN=3
    alfa=0.6
    population=np.random.randint(0,1000, xN*yN).reshape(xN, yN)*1.0

    ###运行函数
    cross(population, alfa)
    print population




