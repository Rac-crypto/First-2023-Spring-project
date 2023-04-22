import unittest
class Euclidnum:
    def get_numbers():
        a = int(input("Enter a value for A "))
        b = int(input("Enter a value for B "))
        if a < b:
        #this switches the numbers around, so that the greatest number is always A
            newB = a
            newA = b
            a = newB
            b = newA
        else:
            print("the numbers are in the correct order")
        while b > 0:
        #this implements the euclidian formula, with a while loop that keeps it going until b=0
            remains = a % b
            a = b
            b = remains
        print("the GCD is ", a)
    get_numbers()
if __name__ == '__main__':
    unittest.main()
