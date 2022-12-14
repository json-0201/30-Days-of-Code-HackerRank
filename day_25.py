# Enter your code here. Read input from STDIN. Print output to STDOUT

T = int(input())
for i in range(T):
    
    # for each input
    n = int(input())
    
    # define range for primality check
    rng = range(2, int(n**0.5) + 1)
    
    # define condition (not divisible within range, not 1)
    prime = sum((n % i) == 0 for i in rng) == 0 and n != 1
    
    # print result
    print("Prime") if prime else print("Not prime")
