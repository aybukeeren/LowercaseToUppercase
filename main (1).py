'''
1-read text from user
2-change lowercase letters in text to uppercase

'''
def read():
    readUserStr = input("Enter the text => ")
    return(readUserStr)
text = read()

listTextLovver = []
listTextUpper = []
def convert(text):
    for i in text:
        listTextLovver.append(i)
    for i in range(len(text)):
        if ord("A") <= ord(listTextLovver[i]) <= ord("Z"):
            listTextUpper.append(listTextLovver[i])
        add = 0
        if ord("a") <= ord(listTextLovver[i]) <= ord("z"):
            add = ord(listTextLovver[i]) - (ord("a") - ord("A"))
            listTextUpper.append(chr(add))
            
convert(text)

def output(listTextUpper):
    print("text uppercase =>",end=' ')
    for i in range(len(listTextUpper)):
        print(listTextUpper[i],end='')

output(listTextUpper)

    
    
    
    


