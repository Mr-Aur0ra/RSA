#!/usr/bin/env python
# -*- coding: utf-8 -*-
__Auther__ = 'M4x'

from pwn import *
from hashlib import sha256
from gmpy2 import invert, iroot
from libnum import xgcd, invmod
#  context.log_level = "debug"

def brute(cipher):
    #  success("cipher -> {}".format(cipher))
    #  print type(cipher) 
    for a in xrange(0, 0xff):
        for b in xrange(0, 0xff):
            for c in xrange(0, 0xff):
                x = chr(a) + chr(b) + chr(c)
                if sha256(x).hexdigest()[0: 8] == cipher:
                    #  success("x -> {}".format(x))
                    return x
    print "not found"

def rsa(n, p, q, e, c):
    assert n == p * q

    d = invert(e, (p - 1) * (q - 1))
    m = pow(c, d, n)

    return m

def commonN(n, e1, c1, e2, c2):
    s1, s2, _ = xgcd(e1, e2)
    if s1 < 0:
        s1 = -s1
        c1 = invmod(c1, n)
    if s2 < 0:
        s2 = -s2
        c2 = invmod(c2, n)
    m = (pow(c1, s1, n) * pow(c2, s2, n)) % n
    return m

def broadcast(n1, n2 ,n3, c1, c2, c3):
    n = [n1, n2, n3]
    C = [c1, c2, c3]
    N = 1
    for i in n:
        N *= i

    Ni = []
    for i in n:
        Ni.append(N / i)

    T = []
    for i in xrange(3):
        T.append(long(invert(Ni[i], n[i])))

    X = 0
    for i in xrange(3):
        X += C[i] * Ni[i] * T[i]

    m3 = X % N
    m = iroot(m3, 3)
    return m[0]


fmt = lambda m: hex(m).replace("L", "")

if __name__ == "__main__":
    io = remote("39.107.33.90", 9999)
    
    token = "icq9bae582b7f5d9ab6caed7d40150be"
    io.sendlineafter(":", token)

    io.recvuntil("=='")
    cipher = io.recvuntil("'", drop = True)
    x = brute(cipher)
    io.sendlineafter(")=", x.encode('hex'))
    success("Level 0 Clear!")

    io.recvuntil("# n=")
    n = int(io.recvuntil("\n", drop = True), 16)
    io.recvuntil("# e=")
    e = int(io.recvuntil("\n", drop = True), 16)
    io.recvuntil("# c=")
    c = int(io.recvuntil("\n", drop = True), 16)
    p =  289540461376837531747468286266019261659
    q = 306774653454153140532319815768090345109
    m = fmt(rsa(n, p, q, e, c))    
    io.sendlineafter("m=", m)
    success("Level 1 Clear!")

    io.recvuntil("# n=")
    n = int(io.recvuntil("\n", drop = True), 16)
    io.recvuntil("# e=")
    e = int(io.recvuntil("\n", drop = True), 16)
    io.recvuntil("# c=")
    c = int(io.recvuntil("\n", drop = True), 16)
    d = 42043
    m = pow(c, d, n)
    io.sendlineafter("m=", fmt(m))
    success("Level 2 Clear!")

    x = 3704324190009897835
    io.sendlineafter("x=", fmt(x))
    success("Level 3 Clear!")

    #  context.log_level = "debug"
    io.recvuntil("# n=")
    n = int(io.recvuntil("\n", drop = True), 16)
    io.recvuntil("# e=")
    e = int(io.recvuntil("\n", drop = True), 16)
    io.recvuntil(")=")
    npnq = int(io.recvuntil("\n", drop = True), 16)
    io.recvuntil("# c=")
    c = int(io.recvuntil("\n", drop = True), 16)
    p = 114791494681514143990268371423282183138226784645868909558224024738011633713833580549522009721245299751435183564384247261418984397745114977301564583085777881485180217075670585703780063072373569054286277474670485124459902688373648390826470893613150198411843162021692225644621249349903453125961550887837378298881
    m = rsa(n, p, n / p, e, c)
    io.sendlineafter("m=", fmt(m))
    success("Level 4 Clear!")

    io.recvuntil("# n=")
    n = int(io.recvuntil("\n", drop = True), 16)
    io.recvuntil("# e=")
    e = int(io.recvuntil("\n", drop = True), 16)
    io.recvuntil("# c=")
    c = int(io.recvuntil("\n", drop = True), 16)
    p = 743675299
    q = 120393827811847730665892922601047874074897457839754965824187553709286586875999984122668238470178081377988439748992735957987417809407665405412580451688753139556272709693049760814986485709769800614157806922562929660004878835280427602632657375319022388348710785821982994403660254841027504457789884082670526620753
    m = rsa(n, p, q, e, c)
    io.sendlineafter("m=", fmt(m))
    success("Level 5 Clear!")

    m = 1040065794283452835234332386718771782674284350646994660717501540629408351835476084209765388377794921102504315677880363816181535636530953053269277563867522157300904962146145717252718887520146030078204232460775L
    io.sendlineafter("m=", fmt(m))
    success("Level 6 Clear!")

    io.recvuntil("# n1=")
    n1 = int(io.recvuntil("\n", drop = True), 16)
    io.recvuntil("# e1=")
    e1 = int(io.recvuntil("\n", drop = True), 16)
    io.recvuntil("# c1=")
    c1 = int(io.recvuntil("\n", drop = True), 16)
    io.recvuntil("# n2=")
    n2 = int(io.recvuntil("\n", drop = True), 16)
    io.recvuntil("# e2=")
    e2 = int(io.recvuntil("\n", drop = True), 16)
    io.recvuntil("# c2=")
    c2 = int(io.recvuntil("\n", drop = True), 16)
    p = 172556869675477627998498055209836071784247150005171563227746896156122872188366409207785861691629822624239290434962401079375795926547190033528901472629460098214484911362406299395686098456884802352767604762878851834535300869832185076070001884294619607750730223241159644270340312192959960438465036924150469626273
    q1 = 132351070426725062043554691080648210190952108157658335988407251230007075283172499240825840919032041018784725171991038079646749244434399109751200470150528052302049968282955114052567000382702788528085267361900807404612963675383296948833387201551997975485346080119293646868147213281855400241807127491238274887591
    q2 = 142712204088308994057536283419724413794506016166476894328600394909477811164746138340181564452439035177705892406900049909054445185976447566687912817760888522575392942071446149843167125603211027327213321217046810724727383186248415705825602583825139689729004506328064673686005047611032077069064661986088327406489
    m = rsa(n1, p, q1, e1, c1)
    io.sendlineafter("m1=", fmt(m))
    success("Level 6 Clear!")

    m = rsa(n2, p, q2, e2, c2)
    io.sendlineafter("m2=", fmt(m))
    success("Level 7 Clear!")

    #  context.log_level = "debug"
    io.recvuntil("# n=")
    n = int(io.recvuntil("\n", drop = True), 16)
    io.recvuntil("e1=")
    e1 = int(io.recvuntil("\n", drop = True), 16)
    io.recvuntil("c1=")
    c1 = int(io.recvuntil("\n", drop = True), 16)
    io.recvuntil("e2=")
    e2 = int(io.recvuntil("\n", drop = True), 16)
    io.recvuntil("c2=")
    c2 = int(io.recvuntil("\n", drop = True), 16)
    m = commonN(n, e1, c1, e2, c2)
    io.sendlineafter("m=", fmt(m))
    success("Level 8 Clear!")

    io.recvuntil("# n1=")
    n1 = int(io.recvuntil("\n", drop = True), 16)
    io.recvuntil("c1=")
    c1 = int(io.recvuntil("\n", drop = True), 16)
    io.recvuntil("n2=")
    n2 = int(io.recvuntil("\n", drop = True), 16)
    io.recvuntil("c2=")
    c2 = int(io.recvuntil("\n", drop = True), 16)
    io.recvuntil("n3=")
    n3 = int(io.recvuntil("\n", drop = True), 16)
    io.recvuntil("c3=")
    c3 = int(io.recvuntil("\n", drop = True), 16)
    m = broadcast(n1, n2, n3, c1, c2, c3)
    io.sendlineafter("m=", fmt(int(m)))
    success("Level 9 Clear!")


    io.interactive()
    io.close()
