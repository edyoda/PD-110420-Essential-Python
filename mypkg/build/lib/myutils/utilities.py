def add(val1,val2):
    try:
        result = val1 + val2
        return result
    except : 
        return "Invalid Input"

def sub(val1,val2):
    return val1 - val2

def mul(val1,val2):
    return val1 * val2

def div(val1,val2):
    return val1 / val2


#Add:
# Positive  : 
#     1. 10,10 => 20 
#     2. 10.5 ,10.5 = > 21
#     3. "Python" + "Java" => "PythonJava"
#     4. 10,"Python" => "Invalid input"
#     5. {1:1,2:4,3:9} + {1:1,2:4,3:9} => "Invalid input 
#     6. {10,20,30} + {10,20,30,40,50} => "Invalid input 

# pip install pytest 


