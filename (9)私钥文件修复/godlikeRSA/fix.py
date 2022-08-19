#!/usr/bin/python3

import re
from itertools import product
from Crypto.Util.number import GCD, inverse


def solve_linear(a, b, mod):
    if a & 1 == 0 or b & 1 == 0:
        return None
    return (b * inverse(a, mod)) & (mod - 1)  # ??b*a^(-1)%mod


def to_n(s):
    s = re.sub(r"[^0-9a-f]", "", s)
    return int(s, 16)


def msk(s):
    cleaned = "".join(map(lambda x: x[-2:], s.split(":")))   #????????????
    return msk_ranges(cleaned), msk_mask(cleaned), msk_val(cleaned)


def msk_ranges(s):      #    ????????????
    return [range(16) if c == " " else [int(c, 16)] for c in s]    


def msk_mask(s):
    return int("".join("0" if c == " " else "f" for c in s), 16)


def msk_val(s):
    return int("".join("0" if c == " " else c for c in s), 16)

#openssl从公钥提取的N   #openssl rsa -pubin -in pubkey.pem  -text -modulus
N = to_n("""\
00:c0:97:78:53:45:64:84:7d:8c:c4:b4:20:e9:33:
58:67:ec:78:3e:6c:f5:f0:5c:a0:3e:ee:dc:25:63:
d0:eb:2a:9e:ba:8f:19:52:a2:67:0b:e7:6e:b2:34:
b8:6d:50:76:e0:6a:d1:03:cf:77:33:d8:b1:e9:d7:
3b:e5:eb:1c:65:0c:25:96:fd:96:20:b9:7a:de:1d:
bf:fd:f2:b6:bf:81:3e:3e:47:44:43:98:bf:65:2f:
67:7e:27:75:f9:56:47:ba:c4:f0:4e:67:2b:da:e0:
1a:77:14:40:29:c1:a8:67:5a:8f:f5:2e:be:8e:82:
31:3d:43:26:d4:97:86:29:15:14:a9:69:36:2c:76:
ed:b5:90:eb:ec:6f:ce:d5:ca:24:1c:aa:f6:63:f8:
06:a2:62:cb:26:74:d3:5b:82:4b:b6:d5:e0:49:32:
7b:62:f8:05:c4:f7:0e:86:59:9b:f3:17:25:02:aa:
3c:97:78:84:7b:16:fd:1a:f5:67:cf:03:17:97:d0:
c6:69:85:f0:8d:fa:ce:ee:68:24:63:06:24:e1:e4:
4c:f8:e9:ad:25:c7:e0:c0:15:bb:b4:67:48:90:03:
9b:20:7f:0c:17:eb:9d:13:44:ab:ab:08:a5:c3:dc:
c1:98:88:c5:ce:4f:5a:87:9b:0b:bf:bd:d7:0e:a9:
09:59:81:fa:88:4f:59:60:6b:84:84:ad:d9:c7:25:
8c:e8:c0:e8:f7:26:9e:37:95:7c:e1:48:29:0f:51:
e7:bd:98:2f:f6:cc:80:e7:f0:32:0b:89:51:92:4e:
c2:6d:50:53:2b:3b:77:72:d1:bd:1a:1f:92:d7:12:
79:61:61:c5:a4:7e:b3:85:eb:f0:7c:6d:46:03:c5:
e6:d5:81:2c:ba:7e:ea:8d:51:7d:63:55:34:2a:b6:
d4:dc:31:5a:f1:99:e3:dc:8c:83:0b:a2:2a:d5:3c:
41:48:41:54:1a:a9:e8:b6:70:bf:d3:fe:ed:19:17:
14:94:13:b3:17:e3:8b:8e:6f:53:ed:e2:44:e8:4a:
32:d6:5c:0d:a8:80:f5:fc:02:e9:46:55:d5:a4:d3:
e7:c6:30:77:f9:73:e9:44:52:d8:13:9d:5d:bf:9e:
fa:3a:b5:96:79:82:5b:cd:19:5c:06:a9:00:96:fd:
4c:a4:73:88:1a:ec:3c:11:de:b9:3d:e0:50:00:1e:
ac:21:97:a1:96:7d:6b:15:f9:6c:c9:34:7f:70:d7:
9d:2d:d1:48:4a:81:71:f8:12:dd:32:ba:64:31:60:
08:26:4b:09:22:03:83:90:17:7f:f3:a7:72:57:bf:
89:6d:e4:d7:40:24:8b:7b:bd:df:33:c0:ff:30:2e:
e8:6c:1d""")

#这个就是残缺的私钥中的prime1
p_ranges, pmask_msk, pmask_val = msk("""\
 0: e:  :  :  :c :c :  :  :  :b :  :  :  :  :
  :ab: e: 2: 8:c :  :  : 1:6 :6 : 6: f:d9: 0:
8 :5c:7 :06:  :  :  :0 : 3:5 :4b:  :6 :  :  :
2 :  :6 :  :  :  :2 :bc: c:  :85:1 : 1:d : 3:
 1:b4:  : b: 1: 3: d:a :  :  :6e: 0:b :2 :  :
  :b :  :9 :e :  :82:8d:  :  :13:  :  : a: a:
  :  :4 :  :c : f:  :  :7 :e :0a:  :  : b: 5:
  : e:91:3 :  :3c: 9:  : 6:  :  :b5:7d: 1:  :
  :  :  :b :a1:99:6 :4 :3 :c :1a:02:4 :  : 9:
9 :f : d:bd:  :0 :  :  :  :b3:  : 4:  :e9: 9:
  : d:  :  :7 :  :93:  : e:dc:  : 0:  :e7:  :
e :  :2 : b: 2:5 :  :  :  :  : c:5f:  :  :e2:
  :  : 9:  :2a:  : e:  :  :2 :  :9f: 7:3 :  :
b : f:b :  : 8: 7:  :  :f :6 :e :c :  :3 :  :
f7: 5: 8: 5:  :  :  :  :  : 8: e:  :03: c:  :
33:76:e : 1:7 : c:  : 0:  :0b:  : a:  : 2: 9:
  :c8:bf:  :  :06: 7:d5:  :02: c:b :e2: 7:2 :
  :  """)

#这个就是残缺的私钥中的prime2
q_ranges, qmask_msk, qmask_val = msk("""\
 0: f:  :d0: 1:55: 4:31:  : b:c4:8 :  : e: d:
34: 3:f :  :  :  :  : 8:99:1 :  : a:0 :  :4 :
0 :  :f :  :a4:41:2 :  :a :  : 1:  : a: c:  :
  :  : 9:  :  : 2:f4: f:  :  :  :  :1 : 4:9 :
a :  :  :79:0 :  :  :  :  : 2: 8:b :  :4 : 8:
  :9b: 1:  :d :  :f :e4:  :4 :c :e :  :3 :  :
 7:2 :  :d :8 :2 :7 :  :d :67:fc:e : 0:f9: 7:
8 :  :  :  :1 :2f:  :51:  :  :2e:0a: e:3d: 6:
b :  :dd:  : 0:fb:  :f4:  :  :  :b4: 9:c :  :
 a:  :  :  :d :  :  :6b: 2:  :9b: a:60:  :d6:
 0:4f:16:d1:  :  :5 :fc:  :f :  :8 :  :  :  :
 1: 6:e1:9 : e:4 : 6: c: d:d :73: 3:  :  :7 :
  :8 : 9:  :3b:f : 2:  :  :f1: e:  :  :1e:  :
8 :  :  : 6:0 : 4:99:e :  : 5:  :  : 4:  :  :
  : a:81:64:  :7 :f : 9: d:  :9 :  : 7:93:f :
ac:8c:  : 8:  : 0: d: 8:  :7 :  :1d:  :f :  :
1 :a :6 :8 :  :60:  :b3:  :  :  :89:  :  :14:
  :5 """)


#这个就是残缺的私钥中的privateExponent
_, dmask_msk, dmask_val = msk("""\
  :  :  : f:8 :a5:d : 2: 0:b :7 :  : 1:  : 4:
 1:0d:  :3 :  :6 :  :  : b:  :  :  :e :  :  :
0e: 0:db:  :1a:1c:c0:  : e:  :  :99:bc:8 :a5:
7 :7 :7 : b:  :  : 8: 8:  :7 :55: 2:  :  :f :
b2:  :  :b :f :4 :  : 8:  :b :  :  :  : 0:  :
0 :  :6 :9 :  :  :  : b: 4:  : 0: a: 5:07:b :
 9: c:9a: 9:  : 7:9e:  : b:60:f :  :  :  :0 :
  : 3:0 :  :  :  : 1:b :  :  : b: 6:0 :f :  :
  : 2:18: 6: b:1 :  :  :  :  :d3:f3:  :a :  :
 3:  :  :  :  : 3: d: 1: 2:7 :  : d:  : 2: d:
  :  : d:4 :  :d :  :6d: c:a :b6:  :  :  : 1:
69:  : 7:  :89:  :c :8 :61: d:25: 3:7 :1b: 4:
b :  :8 :55:  :49: 1:2 :3 :  :1 :e9:a8: 3:  :
9 :  : 1:f8:d3:  :e :  :d :  :9 :b6:  :  :71:
1 :  :c1:  : b: 1:  : 6:e :  :64:  :  :1a:c :
  : b:  :bf:c :  : 0:  : 8:a :4 :  :26:a :5 :
6 :  :  :  :eb:  :e5: a:  :3e:f9:10:0 :  :  :
 6:0 :  : 8:  : 1:72: c:0 : f:5 : f:9c: 0: e:
 7:b :  :  :  :  :d9: 4:  : e:c :68:  :  :  :
 c:  :3a:  :  :a0:ea: 3: 4:  :72:a :d : 8:  :
  :0d:5 :0 : a: 7:c :bb: 6: 4:a :ce:d :2 : 1:
  :  :17:6 :  : c: b:  : f:  :3 : 5:6 :3 :0e:
  : 7:c :3e: 2: 9: 7: 6: f: e: f: 9:  :f3: 9:
a :c1:6 :  : 1:9 :  :43:  : f: 5:  :0 :27: 4:
4 :a :  :e9:  : 8: 4:3 :8a: 6:16:d5:c : e: e:
  :d : c:b :a8:  : 7:  : 9:  :7 :7d:  :  :  :
  :  :  :4 :2 :  : 3: 3: 6:  :  :  :7b:0 :  :
 e:  :0 :  :a :  : 5:  :  :  : 5:1 :82:c :0d:
4 :2 :fd:36: 5:50:0 :  :  :d : f: 6:  :  :e :
0 :  :  :ce:  :9e:8 :  :0 :d :07:b3:  :  :  :
0 :e4:  :  :68:b :c :  : c:5 :  :  :3 : 7: 2:
 c:e0:  :5 :  :  :b4:  :ef: 7:  :1 :e : 0:f :
  :6 :  :  :  :e0:c :3 :  :  : 3:  : d:  :  :
 3: 3: c: a:  :b : a:71: 3: 0:a :  :4 :5d:  :
0 :4 """)

#这个就是残缺的私钥中的exponent1
_, dpmask_msk, dpmask_val = msk("""\
  : 3:2a:  : d:  :  :  :  :0 :1 : f:  :  : 6:
1 :2 :1b:07: a:e :b :c5:58:7 :  :e8: 7: 1: c:
  : 1:b :a0: 4:0f:5 :67:  :3 :7 :6 :f9:  : c:
  :79: 0:1 :65:  :8 :  :99: d:d :  :2 :9 :0 :
 e:  :0 :  :  :  : d:  :d :7 :6 :a9: a:8b: b:
  :  : 7: a:37:  :  :7 :1 :6 :  :c2: 7:6 :b :
 e:  :  :  :  :  :  :b :3a:5 :  :  :  :  :  :
  :  :  :cd:8 :  : d:  :7 : 3:  : f:e : c:  :
  : a:  :c : f:c : 7:b :5 :  :  :2 :8 :8 :6 :
0a: a:  :  :3 :db:  : 4:00:  : d:  :b : 5:  :
20: 2: 5:  :82:  : 0: 6:  :8a:  :7 :  : 8:  :
 4: 1:  :  :  : 8:46:  :  :  :  :  : 0:f :c8:
2 :  : c:7 :  : 1:  :  :2 : 0: 5:  :  : 1:9b:
 6:9 : 0:74:  :c :  :e :  :  :cb:b :3 :3 :  :
 2:  :  :47:  :2 : 0:5 :  :  : d: 6:83:  :  :
  :c7:  :  :0b:  :  : c:  :3 :8 :  :9 :4 : 7:
5 :c0:fe:  :f9: 1:  :0 : e: 8:02:  : f:  :c :
55:61""")

#这个就是残缺的私钥中的exponent2
_, dqmask_msk, dqmask_val = msk("""\
  :0b:7 :4 :0 : 0:6 : 7:7e:  : 5:  : 7:  : a:
a :d : 0: 6: 4:86:  :  :8 :  :  :  :  :e :8f:
 9:  :  :  : 1:  :2 :  : 7: b:1 :5 : f:  :8 :
  :d :21:  :e : d:  :c9:e : b:  :  :1 :  :  :
  :d :a2:b7:  :  :  :f3:  :42:  :e : c:  :f :
  : 0:f :7 : 4: 5:34:  :4 : c:  :  :8 :d : 8:
5 :af: 3:1d: 5:4 :  :2 :  :6 :c : 6:a :1 :5 :
 a:9 :  :d :  :  :0a:a1:  :f :7 :9 :b :  :  :
 f:2 :27: f:  :0 :f6:4d:  :  :  :  :  :5 :  :
 4:08:  : 5:  : 8: 5:  :  :  :18: 4: 8:57: 2:
 f: a:  :  :a8: f: c:f : e: 1:9 :c : 4:9 :  :
  :  :  :  :  : 1:  :2 :  :d1:  : 6:e : d:  :
  : f:04:2 :8d:  : 3:  :  :b : 8:  :d6:  : 2:
  :  :  :6 :  : f:  :  : 0:6 :  :51:  :48:19:
  :  :  :69:4 : c:  :c :  : f:  :f4:d :  : f:
 d:0 :0d:b :3 : 3:2 :  :  :6 : b:5 :2 :  : c:
 1:5a: f:f :  :  :7e:3e:  :d :f :0 : d: c: 6:
 1""")

#这个就是残缺的私钥中的publicExponent,或者openssl从公钥中提取e
E = 0x10001

def search(K, Kp, Kq, check_level, break_step):
    max_step = 0
    cands = [0] # ????
    for step in range(1, break_step + 1):
        # step???????step?
        max_step = max(step, max_step)

        mod = 1 << (4 * step)
        mask = mod - 1

        cands_next = []
        for p, new_digit in product(cands, p_ranges[-step]):
            pval = (new_digit << ((step - 1) * 4)) | p

            # ????
            if check_level >= 1:
                qval = solve_linear(pval, N & mask, mod)
                if qval is None or not check_val(qval, mask, qmask_msk, qmask_val):
                    continue

            if check_level >= 2:
                val = solve_linear(E, 1 + K * (N - pval - qval + 1), mod)
                if val is None or not check_val(val, mask, dmask_msk, dmask_val):
                    continue

            if check_level >= 3:
                val = solve_linear(E, 1 + Kp * (pval - 1), mod)
                if val is None or not check_val(val, mask, dpmask_msk, dpmask_val):
                    continue

            if check_level >= 4:
                val = solve_linear(E, 1 + Kq * (qval - 1), mod)
                if val is None or not check_val(val, mask, dqmask_msk, dqmask_val):
                    continue

                if pval * qval == N: #????
                    print("Kq =", Kq)
                    print("pwned")
                    print("p =", pval)
                    print("q =", qval)
                    p = pval
                    q = qval
                    d = inverse(E, (p - 1) * (q - 1))
                    print("d =", d)
                    coef = inverse(p, q)

                    from Crypto.PublicKey import RSA
                    print(RSA.construct((N, E, d, p, q, coef)).exportKey().decode())
                    quit()

            cands_next.append(pval)

        if not cands_next:
            return False
        cands = cands_next
    return True


def check_val(val, mask, mask_msk, mask_val):
    test_mask = mask_msk & mask
    test_val = mask_val & mask
    return val & test_mask == test_val

# K = 4695
# Kp = 15700
# Kq = 5155


for K in range(1, E):
    if K % 100 == 0:
        print("checking", K)
    if search(K, 0, 0, check_level=2, break_step=20):
        print("K =", K)
        break

for Kp in range(1, E):
    if Kp % 1000 == 0:
        print("checking", Kp)
    if search(K, Kp, 0, check_level=3, break_step=30):
        print("Kp =", Kp)
        break

for Kq in range(1, E):
    if Kq % 100 == 0:
        print("checking", Kq)
    if search(K, Kp, Kq, check_level=4, break_step=9999):
        print("Kq =", Kq)
        break
