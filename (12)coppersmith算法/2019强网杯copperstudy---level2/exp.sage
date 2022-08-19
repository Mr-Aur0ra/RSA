n = 0x241ac918f708fff645d3d6e24315e5bb045c02e788c2b7f74b2b83484ce9c0285b6c54d99e2a601a386237d666db2805175e7cc86a733a97aeaab63486133103e30c1dca09741819026bd3ea8d08746d1d38df63c025c1793bdc7e38d194a30b492aadf9e31a6c1240a65db49e061b48f1f2ae949ac9e7e0992ed24f9c01578dL  
p_fake = 0x2c1e75652df018588875c7ab60472abf26a234bc1bfc1b685888fb5ded29ab5b93f5105c1e9b46912368e626777a873200000000000000000000000000000000L  
   
pbits = 1024  
kbits = 130  
pbar = p_fake & (2^pbits-2^kbits)  
print "upper %d bits (of %d bits) is given" % (pbits-kbits, pbits)  
   
PR.<x> = PolynomialRing(Zmod(n))  
f = x + pbar  
   
x0 = f.small_roots(X=2^kbits, beta=0.4)[0]  # find root < 2^kbits with factor >= n^0.3  
print hex(int(x0 + pbar))  
