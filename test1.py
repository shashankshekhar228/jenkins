import unittest

from addition import addfunction

class TestSum(unittest.TestCase):
    def test_list_int(self):
        """
        Test case to add two numbers
        """
        input1=20
        input2=30
        result1=addfunction(input1,input2)
        self.assertEqual(result1,50)

        input3=60
        input4=30
        result2=addfunction(input3,input4)
        self.assertEqual(result2,90)

        input5=160
        input6=40
        result3=addfunction(input5,input6)
        self.assertEqual(result3,200)
        

if __name__ == '__main__':
    unittest.main()