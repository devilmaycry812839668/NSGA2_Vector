#!/usr/bin/env python
#encoding:UTF-8
"""
本文件为多目标优化算法的多目标函数文件，父亲函数Model
所有目标函数的输入变量均为矩阵numpy

目标函数为:双目标函数， 三目标函数
"""
import numpy as np
from abc import ABCMeta, abstractmethod

#父亲抽象类
class objectFun(object):
    #定义为抽象类
    __metaclass__=ABCMeta

    def __init__(self, population):
        self.__population=population

    @property
    def population(self):
        return self.__population

    @population.setter
    def population(self, population):
        self.__population=population


########################################## 
#子代 二目标函数抽象类
class objectFun_2(objectFun):
    #定义为抽象类
    __metaclass__=ABCMeta

    #目标函数个数
    objFunNum=2

    @abstractmethod
    def objFun_1(self):
        pass

    @abstractmethod
    def objFun_2(self):
        pass
  
#子代 三目标函数抽象类
class objectFun_3(objectFun):
    #定义为抽象类
    __metaclass__=ABCMeta

    #目标函数个数
    objFunNum=3

    @abstractmethod
    def objFun_1(self):
        pass

    @abstractmethod
    def objFun_2(self):
        pass
 
    @abstractmethod
    def objFun_3(self):
        pass
 


############################################
###以下是测试用例，测试抽象父亲函数
###unit test
if __name__=="__main__":

    class obj3(objectFun_3):
        def objFun_1(self):
            return self.population+1
        def objFun_2(self):
            return self.population+2
        def objFun_3(self):
            return self.population+3
  
    inputData=np.arange(100)
    o3=obj3(inputData)
 
    print o3.population
    print o3.objFun_1()
    print o3.objFun_2()
    print o3.objFun_3()

    o3.population=np.arange(200)
 
    print o3.population
    print o3.objFun_1()
    print o3.objFun_2()
    print o3.objFun_3()


