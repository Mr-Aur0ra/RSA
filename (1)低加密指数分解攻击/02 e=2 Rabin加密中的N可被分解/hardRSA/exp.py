#!/usr/bin/python
#coding:utf-8

import gmpy2
import libnum

e = 2
n = 87924348264132406875276140514499937145050893665602592992418171647042491658461
p = 275127860351348928173285174381581152299
q = 319576316814478949870590164193048041239
c=int(open('./flag.enc','rb').read().encode('hex'),16)

mp=pow(c,(p+1)/4,p)
mq=pow(c,(q+1)/4,q)
yp=gmpy2.invert(p,q)
yq=gmpy2.invert(q,p)
r=(yp*p*mq+yq*q*mp)%n
rr=n-r
s=(yp*p*mq-yq*q*mp)%n
ss=n-s
print libnum.n2s(r)
print libnum.n2s(rr)
print libnum.n2s(s)
print libnum.n2s(ss)
