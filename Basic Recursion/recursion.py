class Recursion:
    def printNameNTime(self ,i ,x):
        
        if(i > x):
            return
        print("this is " , i , "times")
        self.printNameNTime(i + 1, x)
    

    def linearlyPrint(self ,i , x ):
        if(i > x):
            return
        print("this is " , i , "times")
        self.printNameNTime(i + 1, x)
    
    def reverslyPrint(self ,i , x ):
        if(i > x):
            return
        print("this is " , x , "times")
        self.reverslyPrint(i, x- 1)
    
    def backTracking(self ,i , x ):
        if(i < 1):
            return
        
        self.backTracking(i - 1 , x)
        print(i)

r = Recursion()
# r.printNameNTime(1, 5)
# r.reverslyPrint(1,5)
r.backTracking(5,5)
