import sys
args = sys.argv
if(len(args) == 4 ):
    from aws2 import input
elif(len(args) == 2 or len(args) == 7):
    from aws2_new import input
else:
    from aws3 import input
    

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
        #ans = "error" 
    
    return ans


num1 = input.num1
num2 = input.num2
operation = input.operation
ans = calc(operation, num1, num2)
print("answer : " + str(ans)) 

#テスト時仕様    
#num1 = 0
#num2 = 0
#operation = "plus"
#ans = calc(operation, num1, num2)