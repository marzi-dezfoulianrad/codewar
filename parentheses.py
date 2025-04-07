#The goal of this exercise is to convert a string to a new string where each character in the new string is
#"(" if that character appears only once in the original string, or ")" 
# if that character appears more than once in the original string. Ignore capitalization when determining 
# if a character is a duplicate.

def duplicate_encode(string):
    result = ""  
    string_lower = string.lower()  
    for char in string:
        if string_lower.count(char.lower()) == 1:  
            result += "("
        else:
            result += ")"
    return result  

answer = "hello" 
print(duplicate_encode(answer)) 


