#!/usr/bin/python
#coding:utf-8

import gmpy2
from Crypto.Util.number import long_to_bytes

def egcd(a,b):
    if b==0:
        return a,1,0
    else:
        g,x,y=egcd(b,a%b)
        return g,y,x-a//b*y

e1 = 17
e2 = 65537
n = n1 = n2 = 0x00b0bee5e3e9e5a7e8d00b493355c618fc8c7d7d03b82e409951c182f398dee3104580e7ba70d383ae5311475656e8a964d380cb157f48c951adfa65db0b122ca40e42fa709189b719a4f0d746e2f6069baf11cebd650f14b93c977352fd13b1eea6d6e1da775502abff89d3a8b3615fd0db49b88a976bc20568489284e181f6f11e270891c8ef80017bad238e363039a458470f1749101bc29949d3a4f4038d463938851579c7525a69984f15b5667f34209b70eb261136947fa123e549dfff00601883afd936fe411e006e4e93d1a00b0fea541bbfc8c5186cb6220503a94b2413110d640c77ea54ba3220fc8f4cc6ce77151e29b3e06578c478bd1bebe04589ef9a197f6f806db8b3ecd826cad24f5324ccdec6e8fead2c2150068602c8dcdc59402ccac9424b790048ccdd9327068095efa010b7f196c74ba8c37b128f9e1411751633f78b7b9e56f71f77a1b4daad3fc54b5e7ef935d9a72fb176759765522b4bbc02e314d5c06b64d5054b7b096c601236e6ccf45b5e611c805d335dbab0c35d226cc208d8ce4736ba39a0354426fae006c7fe52d5267dcfb9c3884f51fddfdf4a9794bcfe0e1557113749e6c8ef421dba263aff68739ce00ed80fd0022ef92d3488f76deb62bdef7bea6026f22a1d25aa2a92d124414a8021fe0c174b9803e6bb5fad75e186a946a17280770f1243f4387446ccceb2222a965cc30b3929L
c1=int(open('./flag.enc1','rb').read().encode('hex'),16)  
c2=int(open('./flag.enc2','rb').read().encode('hex'),16)  

assert n1==n2

# s1=gmpy2.invert(e1,e2)
s1=egcd(e1,e2)[1]
s2=egcd(e1,e2)[2]

#此处判断s1和s2是否小于0，因为pow()函数里s1和s2不能为负，
if(s1<0):
    s1=-s1
    c1=gmpy2.invert(c1,n)#若s1为负,s1取正，c1取逆
if(s2<0):
    s2=-s2
    c2=gmpy2.invert(c2,n)

m=pow(c1,s1,n) * pow(c2,s2,n) %n
print(long_to_bytes(m))
