RSA加密
pow(enc,e,N)

RSA解密
n==>p,q
phi=(p-1)*(q-1)  
d = gmpy2.invert(e,phi)
m=pow(enc,d,n)

本题常规解题思路:
enc已知  n已知  d?==> e已知 ,求phi ==>求p和q
看着加密脚本中多次出现p及p^r，
本打算直接开用p=gmpy2.iroot(n,r)[0] 开多次方根求p，进而求q //根据加密脚本逆运算 未果 开不出来 ╮(╯▽╰)╭

另一种思路:
e太大 可使用算法从e中快速推断出d的值。 可使用Wiener’s Attack进行解d
求出d可直接求m
但是这样也确实解不出来


好吧 正确解题思路：
n==>分解n得到k个p  即n=p**k
phi=(p**k)-(p**k-1)     //由欧拉函数得
d = gmpy2.invert(e,phi)
m=pow(enc,d,n)

欧拉函数学习链接:https://blog.csdn.net/liuzibujian/article/details/81086324
这个数学知识不看还真不行，看这个链接里面的"欧拉函数的几个性质"即可
题目中幂使用的是r而不是k
(python中使用**代表多少次幂)