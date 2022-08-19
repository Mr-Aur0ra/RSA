def partial_p(p0, kbits, n):  
    PR.<x> = PolynomialRing(Zmod(n))  
    nbits = n.nbits()  
    f = 2^kbits*x + p0  
    f = f.monic()  
    roots = f.small_roots(X=2^(nbits//2-kbits), beta=0.3)  # find root < 2^(nbits//2-kbits) with factor >= n^0.3  
    if roots:  
        x0 = roots[0]  
        p = gcd(2^kbits*x0 + p0, n)  
        return ZZ(p)  
  
  
def find_p(d0, kbits, e, n):  
    X = var('X')  
  
  
    for k in xrange(1, e+1):  
        results = solve_mod([e*d0*X - k*X*(n-X+1) + k*n == X], 2^kbits)  
        for x in results:  
            p0 = ZZ(x[0])  
            p = partial_p(p0, kbits, n)  
            if p:  
                return p  
if __name__ == '__main__':
    # n(必须为整形才可计算) = 0x51fb3416aa0d71a430157d7c9853602a758e15462e7c08827b04cd3220c427bbb8199ed4f5393dae43f013b68732a685defc17497f0912c886fa780dfacdfbb1461197d95a92a7a74ade874127a61411e14a901382ed3fb9d62c040c0dbaa374b5a4df06481a26da3fca271429ff10a4fc973b1c82553e3c1dd4f2f37dc24b3bL
    # d0=给出的部分d(必须为整形才可计算) = 0x17c4b18f1290b6a0886eaa7bf426485a3994c5b71186fe84d5138e18de7e060db57f9580381a917fdfd171bfd159825a7d1e2800e2774f5e4449d17e6723749bL
    e = 3
    n = 57569201048993475052349187244752169754165154575782760003851777813767048953051839288528137121670999884309849815765999616346303792471518639080697166767644957046582385785721102370288806038187956032505761532789716009522131450217010629338000241936036185205038814391205848232364006349213836317806903032515194407739
    nbits = n.nbits()
    kbits = floor(nbits*0.5)
    print "kbits : ", kbits 
    d0 = 1244848677959253796774387650148978357579294769878147704641867595620534030329181934099194560059806799908134954814673426128260540575360296026444649631806619
    print "lower %d bits (of %d bits) is given" % (kbits, nbits)

    p = find_p(d0, kbits, e, n)
    print "found p: %d" % p
    q = n//p
    # print d
    print "完整的d是:"+str(inverse_mod(e, (p-1)))
