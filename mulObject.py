#!/usr/bin/env python
#encoding:UTF-8
import numpy as np
import random
from fun.funUserDefine import *
from operation.cross.cross_fun import cross
from operation.change.change_fun import change
from operation.choice.choice_fun import choice
###评估函数，输出当前种群的非支配解
from operation.choice.choice_fun import estimate

#200个个体, 30个变量， 变量数值范围0到2**14
#交叉概率0.6， 编译概率0.1
xN=200
yN=30
alfa=0.9
belta=0.1

random.seed(0)
np.random.seed(0)

#测试population
#population=np.random.randint(0,1000, xN*yN).reshape(xN, yN)*1.0
population=np.random.rand(xN, yN)
functionObject=ZDT1(population)

old_population=population.copy()
cross(population, alfa)
"""
    np.array([1]*30)  各变量范围 0~1
    np.array([1,5,10,1])  各变量范围 0~1, 0~5, 0~10, 0~1
"""
change(population, np.array([1]*30), belta)
new_population=population
temp_population=np.vstack((old_population, new_population))
 
###运行200次
for i in xrange(200):
    #输出 非支配个体数
    print len(estimate(new_population, functionObject))

    old_population=new_population
    #选择出 200个个体作为下一代种群
    new_population=choice(temp_population, functionObject, 200)
    
    cross(new_population, alfa)
    change(new_population, np.array([1]*30), belta)
    temp_population=np.vstack((old_population, new_population))

#输出最终种群的 非支配解
print estimate(new_population, functionObject)




