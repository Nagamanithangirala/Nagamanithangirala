name = input('enter a name')
print('entered a name')

reverse = ""
for i in name:
    reverse = i + reverse

    print('Reversed value of {} is {} '. format(name,reverse))
