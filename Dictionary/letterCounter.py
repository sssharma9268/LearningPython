def letter_counter(text):
    text = [c for c in text if c.isalpha()]
    dictionay = dict()

    for c in text:
        c = c.upper()
        if c not in dictionay.keys():
            dictionay[c]=1
        else:
            dictionay[c]+=1;
    return dictionay

text = input("Text: ")

result =  letter_counter(text)
#print(result)

#to print in a better way, here items will return tuples of key, value pairs
for key, value in result.items():
    print("%s => %d" %(key,value))
