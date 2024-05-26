#!/usr/bin/env python3

def print_fibonacci(length):
    fibonacci_seq = []
    if length > 0:
        fibonacci_seq.append(0)
    if length >= 2:
        fibonacci_seq.append(1)
        for i in range(2, length):
            fibonacci_seq.append(fibonacci_seq[-1] + fibonacci_seq[-2])

    print(fibonacci_seq)
    
print_fibonacci(10)  
