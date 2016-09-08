#-*- coding: UTF-8 -*- 。
'''
Created on 2016年9月7日

@author: xieb
'''
import bs4

class Fib(object):
    def __call__(self,num):
        a,b,L=0,1,[]
        for x in range(num):
            L.append(a)
            a,b=b,a+b
        return L

f = Fib()
print f(10)