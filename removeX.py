

#s = “XabcdXeXfX”
#s=”abc”
#Remove X from S
#Print the string

def remove(s):
    result = s.replace('X',"")
    return result
s1 = 'abcdXeXfX'
s2 = 'abcdefX'
print(remove(s1))
print(remove(s2))

