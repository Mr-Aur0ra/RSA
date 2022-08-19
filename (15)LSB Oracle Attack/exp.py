from pwn import *
from hashlib import md5
import decimal
a = 0
def oracle(num):
    p.recvuntil("Please input your option:")
    p.sendline("D")
    p.recvuntil("Your encrypted message:")
    p.sendline(str(num))
    p.recvuntil("The plain of your decrypted message is ")
    lsb = p.recv(3)
    return lsb == 'odd'

def partial(c,e,n):
    k = n.bit_length()
    decimal.getcontext().prec = k  # for 'precise enough' floats
    lo = decimal.Decimal(0)
    hi = decimal.Decimal(n)
    for i in range(k):
        if not oracle(c):
            hi = (lo + hi) / 2
        else:
            lo = (lo + hi) / 2
        c = (c * pow(2, e, n)) % n
        print i, int(hi - lo)
    return int(hi)

s = "0123456789abcdefABCDEF"
p = remote("127.0.0.1","9991")
p.recvuntil("[*] Please find a string that md5(str + ")
salt = p.recv(4)
p.recvuntil("[0:5] == ")
part_hash = p.recv(5)
found = 0
for i in s:
    for j in s:
        for k in s:
            for l in s:
                for m in s:
                    ss = i+j+k+l+m
                    if md5(ss+salt).hexdigest()[:5] == part_hash:
                        found = 1
                        break
                if found:
                    break
            if found:
                break
        if found:
            break
    if found:
        break

p.recvuntil("> ")
p.sendline(ss)
p.recvuntil("Guess the Secrets 3 times, Then you will get the flag!\n")
for i in range(3):
    R = p.recvline().strip()
    p.recvuntil("n = ")
    n = eval(p.recvline().strip())
    p.recvuntil("e = ")
    e = eval(p.recvline().strip())
    p.recvuntil("The Encypted secret:")
    p.recvuntil("c = ")
    c = eval(p.recvline().strip())
    c_of_2 = pow(2,e,n)
    m = partial((c*c_of_2)%n,e,n)
    p.recvuntil("Please input your option:")
    p.sendline("G")
    p.recvuntil('The secret:')
    p.sendline(str(m))
    s = p.recvline().strip()
    print(s)
    log.success(s+' '+R+" success!")
p.interactive()

