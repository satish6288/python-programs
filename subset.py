def substring(s):
    sub=set()
    for i in range(len(s)):
        for j in range(i+1,len(s)+1):
            sub.add(s[i:j])
    return sub
 
s= 'aabbc'
string = substring(s)
print(string)
#distinct
 
#“a”, “aa”, “aab”, “aabb”, “aabbc”, “ab”, “c”, “b”, “abb”, “abbc”, “bb”, “bbc”, “bc”
