#!/usr/bin/env python
#encoding:UTF-8
import numpy as np
import random

"""
拥挤距离计算
输入：
funScore=np.array([[1,2], [2,3], [2,2], [3,2], [4,3], [2,1], [3,1], [3,2], [3,3], [3,4]])

control_layer
{0: [4, 9], 1: [8], 2: [1, 3, 7], 3: [2, 6], 4: [0, 5]}

输出： 字典
individual_layer_value
"""
def crowdingDistance(funScore, control_layer):
    #求出集合中 不同属性的 范围
    maxVector=np.max(funScore, axis=0)
    minVector=np.min(funScore, axis=0)
    rangeVector=(maxVector-minVector)*1.0
    #rangeVector=np.array([1.0, 1.0])

    #生成个体编号
    funNum=funScore.shape[1]
    vectorNum=funScore.shape[0]
    indicateVector=np.arange(vectorNum)

    #生成 输出字典
    individual_layer_value={}
    #k 层号   v 该层个体集合
    for k,v in control_layer.items():
        #m  取出 层个体集合V中的个体
        for m in v:
            individual_layer_value[m]=[k, np.array([0.0]*funNum)]
                          
    #生成 函数值和个体序号 矩阵
    indicateVectorT=indicateVector.reshape(vectorNum,1)
    scoreIndicateMatrix=np.hstack((funScore, indicateVectorT))

    #层号 i
    i=0
    while(i<len(control_layer)):
        listItem=control_layer[i]
        subMatrix=scoreIndicateMatrix[listItem, ]
        #子矩阵转换为 列表
        scoreList=subMatrix.tolist()
        
        #对不同目标函数 计算距离
        for j in xrange(funNum):
            scoreList.sort(key=lambda x:x[j])
            #List两端个体 距离计算
            #两端个体序号 
            leftIndicate=scoreList[0][-1]
            rightIndicate=scoreList[-1][-1]
            #为个体 距离信息列表[1]  第j个函数 距离赋值
            individual_layer_value[leftIndicate][1][j]=100000000
            individual_layer_value[rightIndicate][1][j]=100000000
            #List中间个体 距离计算
            for k in xrange(1, len(scoreList)-1):
                t0=scoreList[k-1][j]
                t2=scoreList[k+1][j]
                kIndicate=scoreList[k][-1]
                individual_layer_value[kIndicate][1][j]+=t2-t0
        #层数自增加1
        i+=1

    for v in individual_layer_value.values(): 
        v[1]=np.sum(v[1]/rangeVector)
    return individual_layer_value
            


if __name__=="__main__":
    funScore=np.array([[1,2], [2,3], [2,2], [3,2], [4,3], [2,1], [3,1], [3,2], [3,3], [3,4]])
    control_layer={0: [4, 9], 1: [8], 2: [1, 3, 7], 3: [2, 6], 4: [0, 5]}
    print crowdingDistance(funScore, control_layer)
   


