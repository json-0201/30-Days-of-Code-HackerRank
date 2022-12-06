#Write your code here

class Calculator:
    def power(self,a,b):
        self.a = a
        self.b = b
        
        if self.a<0 or self.b<0:
            raise Exception ("n and p should be non-negative")
        return self.a**self.b
                

myCalculator=Calculator()
T=int(input())
for i in range(T):
    n,p = map(int, input().split())
    try:
        ans=myCalculator.power(n,p)
        print(ans)
    except Exception as e:
        print(e)
