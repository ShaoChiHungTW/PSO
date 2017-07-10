# -*- coding: utf-8 -*-
"""
Created on Wed Jul 05 08:45:02 2017

@author: Kiki Hung
"""

##PSO

#n-array
from numpy import array
from random import random
#暫用Function
from math import sin, sqrt
import sys

#Initialize
IterationLimit = 100;
NumberOfParticles = 100;
Dimension = 2;
#自身經驗權重c1
CongnitionFactor = 0.5;
#群體經驗權重c2
SocialFactor = 0.5;
#誤差項指標
Error_Crit = 10**(-5);

rnd = random();

#繼承
class Particle:
    pass

#Function
def F(Param):
    para = Param*10;
    para = Param[0:2]
    num = (sin(sqrt((para[0] * para[0]) + para[1] *para[1]))) *\
    (sin(sqrt((para[0] * para[0]) +(para[1] * para[1])))) - 0.5;
    denom = (1+0.001*((para[0] * para[0]) + (para[1]*para[1])));
    F = 0.5 - (num/denom);
    ErrorF = 1-F;
    return F, ErrorF;

#呼叫
#Initialize Particles
Particles = [];
for i in range(0,NumberOfParticles,1):
    p = Particle()
    p.Param = array( [random() for i in range(Dimension) ] )
    #For Maximize Problem
    #適應值,Obj先存成MinValue
    p.Fitness = (-1)*sys.maxsize;
    #速度
    p.V=0.0;
    
    #加到陣列後面
    Particles.append(p);

#SoFarTheBest->第一隻鳥
SoFarTheBest = Particles[0];
#先把誤差值存成MaxValue
Error = sys.maxsize;

#迭代更新速度及位置
while i < IterationLimit:
    #p隻鳥
    for p in Particles:
        #計算目標函式
        Fitness, Error = F(p.Param);
        
        #p.BestSolution 這隻鳥最好的
        #如果新算出來的解比較好，就把p.Best存成此解
        if Fitness > p.Fitness:
            p.Fitness = Fitness;
            p.BestSolution = p.Param;
       
        #更新最佳解
        if Fitness > SoFarTheBest.Fitness:
            SoFarTheBest = p;
        
        V = p.V + CongnitionFactor * rnd*(p.BestSolution - p.Param) +\
        SocialFactor * rnd * (SoFarTheBest.Param - p.Param);
        p.Param = p.Param + V;
      
    if Error < Error_Crit:
        break  
    
    i = i + 1
    

#Output
print 'Number of Particles : ' , NumberOfParticles
print 'Dimensions : ',Dimension
print 'Error Criterion : ',Error_Crit
print 'Congnition Factor : ',CongnitionFactor
print 'Social Factor : ',SocialFactor
print 'Function : ', F
print 'So Far The Best Fitness : ', SoFarTheBest.Fitness
print 'So Far The Best Parameters : ', SoFarTheBest.Param
print 'Iterations : ', i
for p in Particles:
    print ' Params : %s, Fitness : %s, Best : %s' % (p.Param, p.Fitness, p.BestSolution)