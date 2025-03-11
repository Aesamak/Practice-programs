def break_camel_case(s):
    result = []
    for char in s:
        if char.isupper() and result:  
            result.append(' ')
        result.append(char)  
    return ''.join(result)


print(break_camel_case("McDonald"))  
             
