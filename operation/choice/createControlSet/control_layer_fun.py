#!/usr/bin/env python
#encoding:UTF-8
import numpy as np
import random

"""
    输入：支配关系字典 control_dict
    {个体号码：[支配其的个数， 被其支配的个体列表]}

    输出:分层字典 control_layer
    {0:[3,1,4], 1:[2,0]}
"""
def controlLayer(control_dict):
    #支配集分层, 层号初始化
    i=0

    #分层字典 control_layer
    control_layer={}

    while control_dict!={}:
        #取出当前种群非支配个体，放入第i层
        control_layer[i]=[]
        for k, v in control_dict.items():
            if v[0]==0:
                control_layer[i].append(k)

        ###将被 第i层支配的个体 支配数减1
        for k in control_layer[i]:
            #val[0] 支配 k 的个体数 
            #val[1] 个体 k 支配的个体列表
            val=control_dict.pop(k)
            for v in val[1]:
                control_dict[v][0]=control_dict[v][0]-1
        i=i+1
    return control_layer


if __name__=="__main__":
    control_dict={0: [7, []], 1: [3, [0, 2, 5]], 2: [6, [0, 5]], 3: [3, [0, 2, 5, 6]], 4: [0, [0, 1, 2, 3, 5, 6, 7, 8]], 5: [8, []], 6: [5, [5]], 7: [3, [0, 2, 5, 6]], 8: [2, [0, 1, 2, 3, 5, 6, 7]], 9: [0, [0, 1, 2, 3, 5, 6, 7, 8]]}
    print controlLayer(control_dict)


