import unittest

from addition import addfunction

class TestSum(unittest.TestCase):
    def test_list_int(self):
        """
        Test case to add two numbers
        """
        input1=200
        input2=300
        result1=addfunction(input1,input2)
        self.assertEqual(result1,50)

        input3=600
        input4=300
        result2=addfunction(input3,input4)
        self.assertEqual(result2,1000)
        

if __name__ == '__main__':
    unittest.main()