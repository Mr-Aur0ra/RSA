import gmpy2
import random
from Crypto.Util.number import *
from flag import flag

def generate_key(1024):
    p = getPrime(1024)
    r = random.randint(2, 10)
    s = random.randint(r, 1024)
    while True:
        e = random.randint(3, p**r*(p-1))
        if gmpy2.gcd(e, p**s*(p-1)) == 1:
        	break
    pubkey = (long(e), long(p**r))   #返回e和p^r
    return pubkey

def crypt(msg, pubkey):
    e, n = pubkey             #e,n=p^r
    m = bytes_to_long(msg)    
    assert m < n - 1
    enc = pow(m, e, n)       
    return long_to_bytes(enc)

nbit = 1024
pubkey = generate_key(1024)
print 'pubkey =', pubkey  #输出e和p^r
msg = flag值   
enc = crypt(msg, pubkey)  

print 'enc =\n', enc.encode('base64')