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





