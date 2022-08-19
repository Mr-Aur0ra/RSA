#!/usr/bin/python
#coding:utf-8

def fix_py():
    # decode encryption.encrypted
    s1 = 'abdefghijklmpqrtuvwxyz' 
    s2 = 'dmenwfoxgpyhirasbktclu'
    f1 = open('encryption.encrypted')
    with open('encryption.py','w') as f2:
        for i in f1.readlines():
            tmp = ''
            for j in i:
                tmp += s2[s1.index(j)] if j in s1 else j
            f2.write(tmp)

def main():
    fix_py()

if __name__=="__main__":
    main()
