name =input('enter a srting/name')
print('original srting',name)
reversedValue = name[: :-1]
print('reversed string',reversedValue)

if(name==reversedValue):
    print('it is a palindrome')
else:
    print('it is not a palindrome')
