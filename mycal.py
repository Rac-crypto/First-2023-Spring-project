# mycal is a file calculating the Greatest common denominator without using the Euclidian formula
import math
import unittest


class pyMath:
    def mathLib():
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
        gcd = math.gcd(a,b)
        print("The GCD is ", gcd)
    mathLib()

if __name__ == '__main__':
    unittest.main()