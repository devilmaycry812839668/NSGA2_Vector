#!/usr/bin/env python
#encoding:UTF-8
import numpy as np
from createControlSet.control_set_fun import controlSet
from champion.champion_fun import champion 

#对种群进行评估，即求出其当前非支配解集
def estimate(population, functionObject):
    ###为函数对象赋值新的种群个体
    functionObject.population=population

    #计算新种群目标函数数值，并建立矩阵 funScore
    funScore=np.vstack((functionObject.objFun_1(), functionObject.objFun_2()))
    funScore=np.transpose(funScore)

    #所求个体索引列表
    indicateList=[]

    #输入函数数值矩阵，求得个体 分层和拥挤距离 字典
    #函数调用
    individual_layer_value=controlSet(funScore)

    for k, v in individual_layer_value.items():
        if v[0]==0:
            indicateList.append(k)

    score=np.hstack((np.arange(population.shape[0]).reshape(population.shape[0], 1), funScore))
    return score[indicateList, ].tolist() 

#选择操作的入口函数
def choice(population, functionObject, choiceNum):
    ###为函数对象赋值新的种群个体
    functionObject.population=population

    #计算新种群目标函数数值，并建立矩阵 funScore
    funScore=np.vstack((functionObject.objFun_1(), functionObject.objFun_2()))
    funScore=np.transpose(funScore)

    #输入函数数值矩阵，求得个体 分层和拥挤距离 字典
    individual_layer_value=controlSet(funScore)

    #采用锦标赛方式选择个体, 保留到下一代的个体序号
    next_remain=champion(individual_layer_value, choiceNum)

    #返回新种群
    return population[next_remain, ]


