# partial_m.sage

n = 0x79982a272b9f50b2c2bc8b862ccc617bb39720a6dc1a22dc909bbfd1243cc0a03dd406ec0b1a78fa75ce5234e8c57e0aab492050906364353b06ccd45f90b7818b04be4734eeb8e859ef92a306be105d32108a3165f96664ac1e00bba770f04627da05c3d7513f5882b2807746090cebbf74cd50c0128559a2cc9fa7d88f7b2d
e = 3

m = randrange(n)
c = pow(m, e, n)

beta = 1
epsilon = beta^2/7

nbits = n.nbits()
kbits = floor(nbits*(beta^2/e-epsilon))
#mbar = m & (2^nbits-2^kbits)
mbar = 0xfedcba98765432100000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
c = 0x381db081852c92d268b49a1b9486d724e4ecf49fc97dc5f20d1fad902b5cdfb49c8cc1e968e36f65ae9af7e8186f15ccdca798786669a3d2c9fe8767a7ae938a4f9115ae8fed4928d95ad550fddd3a9c1497785c9e2279edf43f04601980aa28b3b52afb55e2b34e5b175af25d5b3bd71db88b3b31e48a177a469116d957592c
print "upper %d bits (of %d bits) is given" % (nbits-kbits, nbits)

PR.<x> = PolynomialRing(Zmod(n))
f = (mbar + x)^e - c

print m
x0 = f.small_roots(X=2^kbits, beta=1)[0]  # find root < 2^kbits with factor = n
print mbar + x0
print x0
