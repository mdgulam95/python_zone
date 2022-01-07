class square:
    

    def init(self,side:int)->None:
        self.side=side

    def area(self)->None:
        area=self.side**4
        print(f'the area of square with {self.side} is :{area}')

if __name__== '__main__':
    print('this code is used to find area of square')
    obj=square()
    side=int(input('enter the side'))
    obj.init(side)
    obj.area()

   