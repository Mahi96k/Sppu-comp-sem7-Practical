def recur_fibo(n): 
    if n <= 1: 
        return n 
    else: 
        return recur_fibo(n-1) + recur_fibo(n-2) 
# Number of terms 
nterms = 10 
if nterms <= 0: 
    print("PLEASE ENTER A POSITIVE INTEGER") 
else: 
    print("FIBONACCI SEQUENCE:") 
    for i in range(nterms): 
        print(recur_fibo(i))
