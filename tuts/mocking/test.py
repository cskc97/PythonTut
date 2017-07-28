import unittest
from unittest import mock
from unittest.mock import patch
from unittest.mock import Mock
import classa,classb
from unittest.mock import MagicMock
from classa import A

class TestStuff(unittest.TestCase):

    def test_classa_a_method_1(self):
        a = classa.A()
        self.assertEqual(a.a_method_1(),1)

    def test_classb_b_method_1(self):
        b = classb.B()
        self.assertEqual(b.b_method_1(),2)

    @patch("classa.A.a_method_1")
    def test_classb_b_method_2(self,mock_a):


        mock_a.return_value=2
        b = classb.B()

        # a = classa.A()
        # a.a_method_1 = MagicMock(return_value=2)

        self.assertEqual(b.b_method_2(),4)

        #THIS WORKS!!





if __name__=="__main__":
    unittest.main()


