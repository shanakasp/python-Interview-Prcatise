def reverse(s):
    result = ""
    for i in s:
       result = i + result
    return result   
    
s = "shanaka"
print("original string:", s)
print("reversed string:", reverse(s))
