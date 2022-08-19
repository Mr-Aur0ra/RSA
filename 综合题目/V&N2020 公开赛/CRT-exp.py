#/usr/bin/python
#coding:utf-8

import hashlib
from functools import reduce
from Crypto.Util.number import *

ms = [getRandomNBitInteger(128) for i in range(8)]   #getRandomNBitInteger(128):  返回2**(128-1) ~ (2**128)-1之间的随机数
                                                     #ms: 返回8组2**(128-1) ~ (2**128)-1之间的随机数
p = reduce(lambda x,y: x*y, ms)                      #reduce(): 会对参数序列中的元素进行累积  
                                                     #例如：reduce(add, [1,2,3,4,5]) 表示计算列表和：1+2+3+4+5=15
                                                     #例如：reduce(lambda x, y: x+y, [1,2,3,4,5])  # 使用lambda匿名函数计算列表和：1+2+3+4+5=15
                                                     #p=reduce(lambda x,y: x*y, ms)就表示使用lambda匿名函数对ms中的值进行累乘，结果存到p中(值特别大)
x = getRandomRange(1, p)            #返回随机数n，n需要满足：1 <= n < p
cs = [x % m  for m in ms]           #x对ms中的每个元素都进行取余运算
                                    #例如：ms = [3L, 3L, 2L, 2L, 2L, 2L, 2L, 2L]   x = 340L        
                                    #     cs = [x % m  for m in ms] = [1L, 1L, 0L, 0L, 0L, 0L, 0L, 0L]   #其中340 % 3 = 1，340 % 2 = 0    
                                    # 也就可以表述为下面的cs与ms的关系               
#cs与ms的关系：
#x % ms[0] = cs[0]
#x % ms[1] = cs[1]
#x % ms[2] = cs[2]
#x % ms[3] = cs[3]
#x % ms[4] = cs[4]
#x % ms[5] = cs[5]
#x % ms[6] = cs[6]
#x % ms[7] = cs[7]

# 根据上述关系可以列出线性同余方程组
# 通过中国剩余定理，可求得该方程组的多个解sol(下面解题脚本中的变量名)
# 从多个解中筛选包含字符串"4b93deeb"的解，即可得到正确的flag

flag = "flag{" + hashlib.sha256(str(x).encode()).hexdigest() + "}"
print "输出一下flag格式："+flag  #每次输出的flag都不同





#题目内容如下：
#题目给出：
# ms = [284461942441737992421992210219060544764, 218436209063777179204189567410606431578, 288673438109933649911276214358963643204, 239232622368515797881077917549177081575, 206264514127207567149705234795160750411, 338915547568169045185589241329271490503, 246545359356590592172327146579550739141, 219686182542160835171493232381209438048]
# cs = [273520784183505348818648859874365852523, 128223029008039086716133583343107528289, 5111091025406771271167772696866083419, 33462335595116820423587878784664448439, 145377705960376589843356778052388633917, 128158421725856807614557926615949143594, 230664008267846531848877293149791626711, 94549019966480959688919233343793910003]
# 且断言：assert("4b93deeb" in flag)
# 也就是只要满足这个条件，此时输出的flag就是真的flag



#解题脚本：
#CRT()函数上面的函数均为CRT的内部函数，也就是通过python实现的
import hashlib
​
def egcd(a, b):
    '''
    Extended Euclidean Algorithm.
    returns x, y, gcd(a,b) such that ax + by = gcd(a,b).
    '''
    u, u1 = 1, 0
    v, v1 = 0, 1
    while b:
        q, r = divmod(a, b)
        u, u1 = u1, u - q * u1
        v, v1 = v1, v - q * v1
        a, b = b, r
    return u, v, a
​
def gcd(a,b):
    '''
    Calculate the Greatest Common Divisor of a, b.
    '''
    # a, b = (b, a) if a < b else (a, b)
    while b:
        a, b = b, a % b
    return a
​
def LinearCongruenceSolver(a, c, m):
    '''
    Solve x such that `a * x ≡ c (mod m)` ,
    returns all the possible *x*s (mod m), None if no solution.
    '''
    g = gcd(a, m)
    if c % g:
        return None
    u0 = egcd(a, m)[0]
    return [(c * u0 + k * m) // g % m for k in range(g)]
​

def CRT(ai, mi):
    '''
    Chinese Remainder Theorem.
    solve x such that `x ≡ ai[0] (mod mi[0]) ...` .
    '''
    assert(isinstance(mi, list) and isinstance(ai, list))
    a_s, m = set([ai[0]]), mi[0]
    for a1, m1 in zip(ai[1:], mi[1:]):
        # print(f"m1: {m1}")
        new_as = set()
        for a in a_s:
            ks = LinearCongruenceSolver(m, a1 - a, m1)
            if not ks:
                continue
            for k in ks:
                new_as.add(a + k*m)
        a_s = new_as
        m = m * m1
    return a_s, m
#以上全为python如何实现CRT函数​

ms = [284461942441737992421992210219060544764, 218436209063777179204189567410606431578, 288673438109933649911276214358963643204, 239232622368515797881077917549177081575, 206264514127207567149705234795160750411, 338915547568169045185589241329271490503, 246545359356590592172327146579550739141, 219686182542160835171493232381209438048]
cs = [273520784183505348818648859874365852523, 128223029008039086716133583343107528289, 5111091025406771271167772696866083419, 33462335595116820423587878784664448439, 145377705960376589843356778052388633917, 128158421725856807614557926615949143594, 230664008267846531848877293149791626711, 94549019966480959688919233343793910003]​
​
sol = CRT(cs, ms) #通过CRT求得多个解
for x in sol[0]:
    if "4b93deeb" in  hashlib.sha256(str(x).encode()).hexdigest():
        print(x)
        flag = "flag{" + hashlib.sha256(str(x).encode()).hexdigest() + "}"
        print(flag)
        break