#!/usr/bin/env python
#encoding:UTF-8 
import numpy as np

"""
    均匀变异, 变异 belta=0.1
"""
def change(population, numRange, belta):
    """
        population 种群,向量
        numRange   变量的范围,向量
    """
    #种群个数
    populationSum=population.shape[0]*population.shape[1]

    #变异个数
    changeNum=int(populationSum*belta)

    #变异的横纵坐标向量
    locate=np.random.randint(0, populationSum, changeNum)
    column=locate/population.shape[1]
    row=locate%population.shape[1]

    #numRange[row] 考虑不同属性范变量列的范围
    population[column, row]=np.random.rand(changeNum)*numRange[row]

###以下是测试用例
if __name__=="__main__":
    np.random.seed(0)
    xN=20
    yN=3
    belta=0.1
    population=np.random.rand(xN*yN).reshape(xN, yN)

    print population
    print '-'*20
    ###运行函数
    change(population,np.array([1, 1, 1]), belta)
    print population

