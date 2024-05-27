def find_duplicate_words(input_string):
    words=input_string.split()
    word_count={}
    for word in words:
        if word in word_count:
            word_count[word]+=1
        else:
            word_count[word]=1
    duplicates ={word:count for word,count in word_count.items() if count >1}
    return duplicates

input_string = "this is a test this test is only a test"
result = find_duplicate_words(input_string)
print(result)