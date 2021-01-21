# -*- coding: utf-8 -*-
"""
Created on Thu Jan 21 10:32:59 2021
Poisson Distribution
A random variable X that has a Poisson distribution represents 
the number of events occurring in a fixed time interval with 
a rate parameters λ. λ tells you the rate at which the number of 
events occur.  The average and variance is λ
@author: Roy
"""


import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

lam = 5
n = np. arange(0, 26)
y= stats.poisson.pmf(n, lam)
plt.plot(n, y, 'o-')
plt.title ("500 years")
plt.show()