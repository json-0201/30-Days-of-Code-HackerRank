# Enter your code here. Read input from STDIN. Print output to STDOUT
T=int(input())

for i in range(0,T):
    S=str(input())
    print(S[::2], S[1::2])
