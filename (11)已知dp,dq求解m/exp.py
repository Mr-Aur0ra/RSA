#!/usr/bin/python  
#coding:utf-8  
  
import gmpy2  
from Crypto.Util.number import long_to_bytes  
  
c = xxx  
p = xxx  
q = xxx  
dp = xxx  
dq = xxx   
  
InvQ=gmpy2.invert(q,p)  
mp=pow(c,dp,p)  
mq=pow(c,dq,q)  
m=(((mp-mq)*InvQ)%p)*q+mq  
  
print long_to_bytes(m)  