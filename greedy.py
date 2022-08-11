# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

n, m, k = map(int,input().split())

data = list(map(int,input().split()))

data.sort()
first = data[-1]
second = data[-2]
'''
result = 0

while True :
    if m == 0 :
        break
    
    for i in range(k) :
        result += first
        m -= 1
    
        if m == 0 :
            break
        
    result += second
    m -= 1

print(result)
'''

f = int(m/(k+1)) * k + m%(k+1)
s = m - first

result = first * f + second * s

print(result)