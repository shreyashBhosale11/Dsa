#  Given marks of a student, print on the screen:

# Grade A if marks >= 90
# Grade B if marks >= 70
# Grade C if marks >= 50
# Grade D if marks >= 35
# Fail, otherwise.

class Solution:
    def studentGrade(self, marks):
        if(marks >= 90):
            print("Gread A")
        elif(marks >= 70):
            print("Gread B")
        elif(marks >= 50):
            print("Gread c")
        elif(marks >= 35):
            print("Gread D")
        else:
            print("Fail")
    
    def whichWeekDay(self, day):
        match day:
            case 1:
                print("Monday")
            case 2:
                print("Tuesday")
            case 3:
                print("Wednesday")
            case 4:
                print("Thursday")
            case 5:
                print("Friday")
            case 6:
                print("Saturday")
            case 7:
                print("Sunday")
            case _:
                print("Invalid")   
           


            
        
        


t1 = Solution();
t1.studentGrade(95)
t1.studentGrade(14)


# Given the integer day denoting the day number, print on the screen which day of the week it is. Week starts from Monday and for values greater than 7 or less than 1, print Invalid.

# Ensure only the 1st letter of the answer is capitalised.
