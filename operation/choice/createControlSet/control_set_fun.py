#!/usr/bin/env python
#encoding:UTF-8
from control_relationship_fun import *
from control_layer_fun import *
from crowding_distance_fun import *

"""
输入：
多目标函数数值
funScore=np.array([[1,2], [2,3], [2,2], [3,2], [4,3], [2,1], [3,1], [3,2], [3,3], [3,4]])

输出：
字典  个体：[层号， 拥挤距离]  individual_layer_value
"""
def controlSet(funScore):
    #建立个体支配关系
    control_dict=controlRelationShip(funScore)

    #根据个体支配关系 分层
    control_layer=controlLayer(control_dict)
    
    #根据目标函数数值和分层信息  建立 拥挤距离 字典
    individual_layer_value=crowdingDistance(funScore, control_layer)
    
    return individual_layer_value

if __name__=="__main__":
    funScore=np.array([[1,2], [2,3], [2,2], [3,2], [4,3], [2,1], [3,1], [3,2], [3,3], [3,4]])
    print controlSet(funScore)
