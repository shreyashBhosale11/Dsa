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


s1 = Solution()

# s1.pattern1(5)
# s1.pattern2(5)
# s1.pattern3(5)
# s1.pattern4(5)
# s1.pattern5(5)
# s1.pattern6(5)


