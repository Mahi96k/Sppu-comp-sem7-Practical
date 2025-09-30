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
        print("\nFIBONACCI SEQUENCE:") 
        result = fibonacci_iterative(nterms) 
        for num in result: 
            print(num) 
        # Display Time and Space Complexity Info 
        print("\nTime Complexity: O(n)") 
        print("Explanation: The loop runs 'n' times, so it scales linearly with input size.\n") 
        print("Space Complexity: O(n)") 
        print("Explanation: We store 'n' Fibonacci numbers in a list, using linear space.") 
except ValueError: 
    print("INVALID INPUT! Please enter a valid integer.") 
