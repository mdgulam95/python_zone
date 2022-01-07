class square:
    

    def init(self,side:int)->None:
        self.side=side

    def area(self):
        area=self.side**2
        print(f'the area of square with {self.side} is :{area}')

if __name__== '__main__':
    print('this code is used to find area of square')
    obj=square()
    side=int(input('enter the side of square'))
    obj.init(side)
    obj.area()

   