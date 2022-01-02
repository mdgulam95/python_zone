f=open('gulam.jpeg','rb')

newfile=open('newfile.jpg','wb')
for line in f:
    newfile.write(line)