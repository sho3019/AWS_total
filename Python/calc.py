#from aws2 import input
from aws3 import input
import sys

def calc(operation, num1, num2):
    ans = 0

    if(operation == "plus"):
        ans = num1 + num2

    elif(operation == "minus"):
        ans = num1 - num2

    elif(operation == "cross"):
        ans = num1 * num2

    elif(operation == "devision"):
        ans = num1 / num2
    
    else:
        sys.exit("error")
    
    return ans


num1 = input.num1
num2 = input.num2
operation = input.operation
ans = calc(operation, num1, num2)
print(ans)




#error_flag = 0
#operation = "plus"
#num1 = 1
#num2 = 2

#ans = calc(operation, num1, num2, erroflag)
#print(ans)
    
