from gmpy2 import is_prime
from os import urandom
import base64

def bytes_to_num(b):
	return int(b.encode('hex'), 16)
	
def num_to_bytes(n):
	b = hex(n)[2:-1]
	b = '0' + b if len(b)%2 == 1 else b
	return b.decode('hex')

def get_a_prime(l):
	random_seed = urandom(l)

	num = bytes_to_num(random_seed)
	
	while True:
		if is_prime(num):
			break
		num+=1
	return num

def encrypt(s, e, n):
	p = bytes_to_num(s)
	p = pow(p, e, n)
	return num_to_bytes(p).encode('hex')	

def separate(n):
	p = n % 4
	t = (p*p) % 4
	return t == 1
	
f = open('flag.txt', 'r')
flag = f.read()
		
msg1 = ""
msg2 = ""
for i in range(len(flag)):
	if separate(i):
		msg2 += flag[i]
	else:
		msg1 += flag[i]

p1 = get_a_prime(128)
p2 = get_a_prime(128)
p3 = get_a_prime(128)
n1 = p1*p2
n2 = p1*p3
e = 0x1001
c1 = encrypt(msg1, e, n1)
c2 = encrypt(msg2, e, n2)
print(c1)
print(c2)

e1 = 0x1001
e2 = 0x101
p4 = get_a_prime(128)
p5 = get_a_prime(128)
n3 = p4*p5
c1 = num_to_bytes(pow(n1, e1, n3)).encode('hex')
c2 = num_to_bytes(pow(n1, e2, n3)).encode('hex')
print(c1)
print(c2)

print(base64.b64encode(num_to_bytes(n2)))
print(base64.b64encode(num_to_bytes(n3)))
