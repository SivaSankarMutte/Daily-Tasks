i=input()
alp=''
sym=''
num=''
print("Given string is:",i)
for i in s:
    if(i.isalpha()):
        alp+=i+" "
    elif(i.isalnum()):
        num+=i+" "
    else:
        sym+=i+" "
print("Alphabets in",s,":",alp)
print("Numbers in",s,":",num)
print("Special characters in",s,":",sym)
