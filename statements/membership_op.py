string='abcd....xyz'
# in is the membership op
print('a'in string)
print('this is the op of previous expression')
#simple linear search prog
string=input('enter your string ->')
char=input('enter the char to be searched in the given string ->')
if char in string:
    print('"{}"is present in the given "{}"'.format(char,string))
else:
    print(char,'is not present in given string')