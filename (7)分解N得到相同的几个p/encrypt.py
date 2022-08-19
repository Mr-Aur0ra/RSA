import gmpy2
import random
from Crypto.Util.number import *
from flag import flag

def generate_key(nbit):
    p = getPrime(nbit)
    r = random.randint(2, 10)
    s = random.randint(r, nbit)
    while True:
        e = random.randint(3, p**r*(p-1))
        if gmpy2.gcd(e, p**s*(p-1)) == 1:
        	break
    pubkey = (long(e), long(p**r))
    return pubkey

def crypt(msg, pkey):
    e, n = pkey
    m = bytes_to_long(msg)
    assert m < n - 1
    enc = pow(m, e, n)
    return long_to_bytes(enc)

nbit = 1024
pubkey = generate_key(nbit)
print 'pubkey =', pubkey
msg = flag
enc = crypt(msg, pubkey)
print 'enc =\n', enc.encode('base64')