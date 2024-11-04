# Problem Statement Reverse a string without using the loops 

# The best alternate or the only alternate of loops is recursion

""" 
Eg : input = 'abcd'
expected op = dcba

rev(bcd)+a
rev(cd)+b+a
rev(d)+c+b+a
d+c+b+a
dcba
"""

def reverse_string(input_string):
    if len(input_string) == 0 or len(input_string) == 1:
        return input_string
    else:
        return reverse_string(input_string[1:]) + input_string[0]
    
print(reverse_string('abadsd'))