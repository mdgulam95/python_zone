def validate_greet():
    name=input('enter a users name')
    owner='pyspiders'
    if name==owner:
        password=input('enter the password')
        if password=='root':
            print('welcome to pyspiders')
        else:
            print('password incorrect')
    else:
        print('please get the owner,you are not them')
validate_greet()       
