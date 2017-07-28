import unittest
from unittest.mock import patch
from unittest.mock import Mock
from asyncio import *

from aiohttp.test_utils import unittest_run_loop

from aclass import AClass




class AClassTest(unittest.TestCase):

    def setUp(self):
        self.loop = new_event_loop()
        set_event_loop(None)

    @unittest_run_loop
    @patch("aclass.AClass.return_sum")
    async def test_subtract(self,mock_sum):

        a_obj = AClass()
        mock_sum.return_value=5
        print(mock_sum)
        print(mock_sum.return_value)

        ret_val =  await a_obj.subtract(10,5)

        self.assertEqual(ret_val,mock_sum.return_value)



if __name__=="__main__":
    unittest.main()





