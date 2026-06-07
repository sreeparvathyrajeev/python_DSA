# Given a string str containing digits and characters A, B, C. The characters A, B, C represent bitwise AND, OR and XOR respectively. 
# The task is to evaluate the expression in the string and return the result.
def binary_operation(str):
    lst= list(str)
    if len(lst) ==0:
        return -1
    result = int(lst[0])
    for i in range(1,len(lst),2):
        if lst[i] == "A":
            result= result & int(lst[i+1])
        elif lst[i] == "B":
            result = result | int(lst[i+1])
        elif lst[i] == "C":
            result = result ^ int(lst[i+1])
        
    return result

if __name__ == "__main__":
    str=input()
    print(binary_operation(str))   