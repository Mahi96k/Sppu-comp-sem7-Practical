def fibonacci_iterative(nterms): 
    a, b = 0, 1 
    sequence = [] 
    for _ in range(nterms): 
        sequence.append(a) 
        a, b = b, a + b 
    return sequence 
try: 
    nterms = int(input("Enter the number of Fibonacci terms: ")) 
    if nterms <= 0: 
        print("PLEASE ENTER A POSITIVE INTEGER") 
    else: 
        print("FIBONACCI SEQUENCE:") 
        result = fibonacci_iterative(nterms) 
        for num in result: 
            print(num)
except ValueError: 
    print("INVALID INPUT! Please enter a valid integer.")
