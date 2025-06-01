#!/usr/bin/python
#coding:utf-8

import gmpy2
from Crypto.Util.number import long_to_bytes

lines = open('tmp.txt','r').readlines()

e1 = e2 = 65537

c1 = int(lines[2],16)
c2 = int(lines[6],16)
n1 = int(lines[0])
n2 = int(lines[4])

p1=p2=gmpy2.gcd(n1,n2)
assert p1 == p2 != 1
q1=n1/p1
q2=n2/p2

d1=gmpy2.invert(e1,(p1-1)*(q1-1))
d2=gmpy2.invert(e2,(p2-1)*(q2-1))

m1=pow(c1,d1,n1)
m2=pow(c2,d2,n2)
flag=long_to_bytes(m1)+long_to_bytes(m2)
print flag
