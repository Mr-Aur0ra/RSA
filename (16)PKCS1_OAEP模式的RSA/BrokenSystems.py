from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from secret import flag
import os
rsa = RSA.generate(2048)  #生成RSA
public_key = rsa.publickey().exportKey()  #提取公钥格式
f=open("public.key","w")  #打开指定的文件
f.write(public_key.decode()) #写入公钥
f.close()

rsakey=RSA.importKey(open("public.key","r").read())  #打开公钥文件
rsa = PKCS1_OAEP.new(rsakey) # PKCS1_OAEP模式
msg=rsa.encrypt(flag.encode()) #
f=open("message","wb")
f.write(msg)
f.close()




