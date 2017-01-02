#!/usr/bin/env python
#encoding:UTF-8
import numpy as np
from funModel import *
### 以下为具体实现函数
### 需要用户自定义函数，继承与上面的模板抽象函数
#######################################################
class ZDT1(objectFun_2):
    #ZDT1函数
    def gFun(self):
        N=self.population.shape[1]-1
        return 1+np.sum(self.population[:,1:], axis=1)*1.0/N

    def objFun_1(self):
        return 10000-self.population[:,0]

    def objFun_2(self):
        temp=1-np.sqrt(self.population[:,0]/self.gFun())
        return 10000-self.gFun()*temp

###测试函数  如下
if __name__=="__main__":
    np.random.seed(0)
    zdt1=ZDT1(np.random.rand(20, 3))
    print zdt1.objFun_1()
    print zdt1.objFun_2()






