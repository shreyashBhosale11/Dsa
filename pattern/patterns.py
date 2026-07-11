class Solution:

    # *****
    # *****
    # *****
    # *****
    # *****

    def pattern1(self, n):
        for i in range (0 ,n):
            for j in range (0 , n):
                print("*" , end="")
            print()

    # *
    # **
    # ***
    # ****
    # *****

    
    def pattern2(self, n):
        for i in range (0 ,n):
            for j in range (0 , i + 1):
                print("*" , end="")
            print()
    
    # 1
    # 12
    # 123
    # 1234
    # 12345

    def pattern3(self, n):
        for i in range (0 ,n):
            for j in range (0 , i + 1):
                print(j+ 1 , end="")
            print()
    
    # 1
    # 22
    # 333
    # 4444
    # 55555

    def pattern4(self, n):
        for i in range (0 ,n):
            for j in range (0 , i + 1):
                print(i+ 1 , end="")
            print()

    # *****
    # ****
    # ***
    # **
    # *  
    
    def pattern5(self, n):
        for i in range (0 ,n):
            for j in range (0 , n- i):
                print("*" , end="")
            print()
            
    # 12345
    # 1234
    # 123
    # 12
    # 1
    def pattern6(self, n):
        for i in range (0 ,n):
            for j in range (0 , n- i):
                print(j+1 , end="")
            print()
    
    
    #     *
    #    ***
    #   *****
    #  *******
    # *********

    def pattern7(self, n):
        for i in range (0 ,n):
            for j in range (0 , n- i- 1):
                print("   " , end="")
            

            for j in range (0 , (i * 2) + 1  ):
                print(" * " , end="")
           

            for j in range (0 , n- i- 1):
                print(" " , end="")
            print()

    # *********
    #  *******
    #   *****
    #    ***
    #     *

    def pattern8(self, n):
        for i in range (0 ,n):
            for j in range (0 , i):
                print("   " , end="")
            

            for j in range (0 , (n*2) -(2*i)-1  ):
                print(" * " , end="")
           

            for j in range (0 , i):
                print("   " , end="")
            print()



    #     * 
    #    ***
    #   *****
    #  *******
    # *********
    # *********
    #  *******
    #   *****
    #    ***
    #     *
    def pattern9(self, n):
        self.pattern7(n)
        self.pattern8(n)

    # *
    # **
    # ***
    # ****
    # *****
    # ****
    # ***
    # **
    # *

    def pattern10(self, n):
        for i in range (1 , 2*n ):
            if(i > n):
                for j in range (1 , 2*n - i ):
                    print("*" , end="")
                print()
            else:
                for j in range (1 , i+1 ):
                    print("*" , end="")
                print()

    # 1 
    # 0 1 
    # 1 0 1 
    # 0 1 0 1 
    # 1 0 1 0 1
    def pattern11(self, n):
        start = 1
        for i in range (0 ,n):
            if(i % 2 == 0):start = 1
            else:start = 0
            for j in range (0 , i + 1):
                print(start , end="")
                start = 1 - start
            print()

    # 1        1
    # 12      21
    # 123    321
    # 1234  4321
    # 1234554321

    def pattern12(self, n):
        for i in range (1 ,n+ 1):
            for j in range (1, i+ 1):
                print( j , end="")
            

            for j in range (0 , (2*n)- (2*i)   ):
                print(" " , end="")
           

            for j in range (i, 0 , -1):
                print( j , end="")
            print()

    # 1 
    # 2 3 
    # 4 5 6 
    # 7 8 9 10 
    # 11 12 13 14 15
    def pattern13(self, n):
        start = 1
        for i in range (0 ,n):
            for j in range (0 , i + 1):
                print(start ," " , end="")
                start += 1
            print()
            
    # A
    # AB
    # ABC
    # ABCD
    # ABCDE
    def pattern14(self, n):
        
        for i in range (0 ,n):
            start = ord('A')
            for j in range (0 , i + 1):
                print(chr(start)  , end="")
                start += 1
            print()

    # ABCDE
    # ABCD
    # ABC
    # AB
    # A
    def pattern15(self, n):
        for i in range (0 ,n):
            start = ord('A')
            for j in range (0 , n- i):
                print(chr(start) , end="")
                start += 1
            print()


    # A
    # BB
    # CCC
    # DDDD
    # EEEEE
    def pattern16(self, n):
        start = ord('A')
        for i in range (0 ,n):
            for j in range (0 , i + 1):
                print(chr(start)  , end="")
            start += 1
            print()

    #     A
    #    ABA
    #   ABCBA
    #  ABCDCBA
    # ABCDEDCBA

    def pattern17(self, n):
        for i in range (0 ,n):
            for j in range (0 , n- i- 1):
                print(" " , end="")
            
            char = ord('A')
            breakpot = (2 * i + 1) // 2 
            for j in range (0 , (i * 2) + 1  ):
                print(chr(char) , end="")
                if( j < breakpot):char += 1
                else: char -= 1

                
           

            for j in range (0 , n- i- 1):
                print(" " , end="")
            print()
    
    def pattern14(self, n):
        
        for i in range (0 ,n):
            start = ord('A')
            for j in range (0 , i + 1):
                print(chr(start)  , end="")
                start += 1
            print()

    # E 
    # D E 
    # C D E 
    # B C D E 
    # A B C D E
    def pattern18(self, n):
        for i in range (0 ,n):
            start = 65 + n - 1 - i
            
            for j in range (start, 65 + n ):
                print(chr(j)  , end="")
                start += 1
            print()
            
    # **********
    # ****  ****
    # ***    ***
    # **      **
    # *        *
    # *        *
    # **      **
    # ***    ***
    # ****  ****
    # **********
    def pattern19(self, n):
        for i in range(0, n):
            # stars 
            for j in range(0 , n-i):
                print("*" , end="")
            # space 
            for j in range(0 , i * 2 ):
                print(" " , end="")
            # stars
            for j in range(0 , n - i):
                print("*" , end="")
            print()
        
        for i in range(0, n):
            # stars 
            for j in range(0 , i + 1):
                print("*" , end="")
            # space 
            for j in range(0 , (2*n)-(2* i) - 2  ):
                print(" " , end="")
            # stars
            for j in range(0 , i + 1 ):
                print("*" , end="")
            print()

    # *        *
    # **      **
    # ***    ***
    # ****  ****
    # **********
    # ****  ****
    # ***    ***
    # **      **
    # *        *
    

    def pattern20(self, n):
        for i in range(0, 2 * n - 1):
            if i < n:
                stars = i + 1
            else:
                stars = 2 * n - 1 - i

            spaces = (2 * n) - (2 * stars)
            for j in range(0 , stars):
                print("*" , end="")
            for j in range(0 , spaces):
                print(" ", end= "")
            for j in range(0 , stars):
                print("*" , end="")
            print()

    # *****
    # *   *
    # *   *
    # *   *
    # *****
    def pattern21(self, n):
        for i in range(0 , n ):
            for j in range(0 , n):
                if(i == 0 or i == n-1 or j== 0 or j == n-1  ):
                    print("*" , end= "")
                else:
                    print(" ", end= "")
            print()

    # 5 5 5 5 5 5 5 5 5 
    # 5 4 4 4 4 4 4 4 5 
    # 5 4 3 3 3 3 3 4 5 
    # 5 4 3 2 2 2 3 4 5 
    # 5 4 3 2 1 2 3 4 5 
    # 5 4 3 2 2 2 3 4 5 
    # 5 4 3 3 3 3 3 4 5 
    # 5 4 4 4 4 4 4 4 5 
    # 5 5 5 5 5 5 5 5 5

    def pattern22(self, n):
        for i in range(0 , 2 *n - 1  ):
            for j in range(0 , 2 *n - 1 ):
                top = i 
                left = j 
                right=  (2 *n - 2)- j
                down = (2 *n - 2)- i
                print(n - min(min(top, down), min(left, right)) , end = "")
            print()


                
            
                


    
    
s1 = Solution()

# s1.pattern1(5)
# s1.pattern2(5)
# s1.pattern3(5)
# s1.pattern4(5)
# s1.pattern5(5)
# s1.pattern6(5)
# s1.pattern7(5)
# s1.pattern8(5)
# s1.pattern9(5)
# s1.pattern10(5)
# s1.pattern11(5)
# s1.pattern12(5)
# s1.pattern13(5)
# s1.pattern14(5)
# s1.pattern15(5)
# s1.pattern16(5)
# s1.pattern17(5)
# s1.pattern18(5)
# s1.pattern19(5)
# s1.pattern20(5)
# s1.pattern21(5)
s1.pattern22(5)














