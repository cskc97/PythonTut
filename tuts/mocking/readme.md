# Mocking and Unit Testing in Python. 

### How mocking happens in Python. A small example with Unit Testing and Magic Mock

#### aclass.py
    class AClass:
    def return_sum(self,num_one,num_two):
        return num_one+num_two

    def subtract(self,num_one,num_two):
        return num_one-num_two
        
#### testaclass.py

    import unittest
    from unittest.mock import patch
    from unittest.mock import Mock

    from aclass import AClass




    class AClassTest(unittest.TestCase):


      @patch("aclass.AClass.return_sum")
      def test_subtract(self,mock_sum):

          a_obj = AClass()
          mock_sum.return_value=5
          print(mock_sum)
          print(mock_sum.return_value)
          self.assertEqual(a_obj.subtract(10,5),mock_sum.return_value)


    if __name__=="__main__":
        unittest.main()
        
#### Output:

    <MagicMock name='return_sum' id='4341535744'>
    .
    5
    ----------------------------------------------------------------------
    Ran 1 test in 0.001s

    OK
    
    
#### Explanation:

mock_sum "mocks" the method return_sum(). printing mock_sum itself prints the object itself, which is an instance of MagicMock. Using the attribute return_value, however, testing can be done.






