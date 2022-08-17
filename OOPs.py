class power  :                                    
    def __init__(self):                           
        pass
    def pow(self,x,n):                            
        exponential=0
        n_value = n 
        x_value = x 
        exponential = x_value**n_value
        return exponential
x=int(input("Enter x value: "))
n=int(input("Enter n value: "))
obj = power()                                     
answer = obj.pow(x,n)                             
print(f"{x} power {n} value is : {answer}")       
