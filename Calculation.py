def add (x , y):       #defn of a functn add with 2 args x and y 
    result = x + y      # value of x + y is stored in variable result
    print(result)       #printing x + y
    
# additon of n1 and n2  
n1 = int(input("enter x "))         # taking input from user as x. Converting this to int and storing it in variable n1
n2 = int(input("ënter y "))#taking input from user as y. Converting this to int and storing it in variable n2
print("add")
add(n1 , n2)               #calling the functn add along with passing n1 and n2 as 2 argument(args) 

def subtract (x,y):
    result = x - y
    print(result)

#subtraction of n1 and n2
n1 = int(input("enter x "))
n2 = int(input("enter y "))
print("subtract")
subtract(n1,n2)
    