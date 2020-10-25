'''
Created on Dec 14, 2011

@author: pablocelayes
'''

import ContinuedFractions, Arithmetic, RSAvulnerableKeyGenerator

def hack_RSA(e,n):
    '''
    Finds d knowing (e,n)
    applying the Wiener continued fraction attack
    '''
    frac = ContinuedFractions.rational_to_contfrac(e, n)
    convergents = ContinuedFractions.convergents_from_contfrac(frac)
    
    for (k,d) in convergents:
        
        #check if d is actually the key
        if k!=0 and (e*d-1)%k == 0:
            phi = (e*d-1)//k
            s = n - phi + 1
            # check if the equation x^2 - s*x + n = 0
            # has integer roots
            discr = s*s - 4*n
            if(discr>=0):
                t = Arithmetic.is_perfect_square(discr)
                if t!=-1 and (s+t)%2==0:
                    print("Hacked!")
                    return d

# TEST functions

def test_hack_RSA():
    print("Testing Wiener Attack")
    times = 5
    
    while(times>0):
        e,n,d = RSAvulnerableKeyGenerator.generateKeys(1024)
        print("(e,n) is (", e, ", ", n, ")")
        print("d = ", d)
    
        hacked_d = hack_RSA(e, n)
    
        if d == hacked_d:
            print("Hack WORKED!")
        else:
            print("Hack FAILED")
        
        print("d = ", d, ", hacked_d = ", hacked_d)
        print("-------------------------")
        times -= 1
    
if __name__ == "__main__":
    #test_is_perfect_square()
    #print("-------------------------")
    test_hack_RSA()
    n = 0xb8f7a195cb86975af32e510bb09d7ff247c60bdd0882c8506a95fe57a3a776c6aa9c2d8a4d07f1df373b53a025cd040280c4c6694f9c49c67eccea96180b0b9a04d69ecac4b4722aa44f338f5373e7b94078509c12904f449d3adc1993dc5644724832db83e77f85fd89c5432af3d255906365dedf93daadbfe187aca80d812aa19518da087f2122c22914a71c2a83d915048d74535265ca97eb9d17cf633c79083df4a9ca583111a7adb0b5efd1d2f8dd1b9df1f0eefc0becbbc0c483e4c5c87ef8f959e2d4f953cae8c05d00c9e20a4a48745809ac43dcb0cd7eda85b98db86108968a20bb3c503393b4f3f9db93fb18e69d1e9fe6da345a97694edcc443b24d6de015e9d9d417501bf876906da58ab2754a2f7c1f025a79f0f61d38d95152f0cf6a2b71742330949cac40277fce77f8b5413654c0e5c22fbc2fb37409b580e4b8f1c0f330f325e18ed8470c2ddb11fae3fc16ea4aed8ef024bf147a3fe3e6d97abd877891d180ee742d2e4475f778fbd7aa0b546749dab39b4a3dd86f64996a2e26c69d9d69421604aecf629b8f81bb8fdae43536834c5fc37ce3331417a24f3a3a212aab69cc44a5a78d87d99691641941bb347a962a9585a1bcec890fc536d80574020b96c3e484ce5b8b1ca6ed0793fd042b3b730cbf21c06b6464ece083dd0ec9bb54f583b282b417233ec0a84de1f02e3143ae454cbc699723d0f2f1
    e = 0x4f448c385063502780a1b573a657e0216c30e44874bc1df7cfbf81243c2198df23cb05fd858d43c10dc829f16de8278fec3d49f6a145b187190c61b55fbd2b16ba70393782bd2ef4d99e28bc6bfdfd557c3a84de8665a18d14e03963c8f3bb0549bc30bcb162d12cf3edc0b63213a01fb2cabacd9182bdba06a18d28ff35d3b4e92ab0c966d1b7e05aeafdd51b95d0816d11a5922e9ef64863543d8e716df9a7ebf6100684955db8e236fb54111e60e69c7135bd38fac7bbce78a090c0a343558026c63dfd1cc102ee01726087275a976c514db0e39afb6463b573bc86f074e1d0501854aee54a45627ae52ebd1a06d3b03a0bf767ad39e687b359c07493a2eb19920368a2768e14deb2270419b0c7405ae778f139a412a96a685d91069f9b121b1dc94b04f687fbd3f5e1efd1cadda047b29123779866fc75672da83889fc93af1359c8e18cde40a5f9ca830a6050a0d4ec82c1ec4803c6d4c6de261622ec1620c9c73399db24b67bd4b141fb409a394bd5bf754d6a251f026c66985ee4d99d679ae626f7a550918458183a13e4b3f260239b8d4d0b1344b2e8bf1c57438134f493713c937b13dc42ca97bd34866a8bcab3b29f3b1667940228e3dfc484a0137287a7f9f86ab9d3402132ebf9f7e0af1bb8faefaedf41362b079f1d9d2ba6fc7a0eb6838fbcc31e1a067321cd7a61239db3310ee1fa8053c9eabf4fe6ee44bd83eb9c5b5e05afc60a7c33d198dd41b0cbef06c68f1e07028bd008bb4accebec1465190dfa0445eb883dd9829eb1929ed1d8f4294d692e03598630ffd8d0e2e908ab1e9f8492533a5266d49fc533b03e0548cf31f7f1d3fb60615868fed93a92d5aca8c33967c7334c56e5174961dce2e15b92314bfa7bc1e0400e023dbc3373
    d = hack_RSA(e,n)
    print "This id d:",d


    


        
    
