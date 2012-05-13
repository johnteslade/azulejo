import unittest
from mock import patch
import azulejo
import keybinder

class MyTest(unittest.TestCase):

    @patch.object(keybinder, 'bind')
    def test_something(self, mock_my_method):
	   
        def side_effect(key, dispatcher, dispatcher_params):
            print "Sideffect 2 called {} {} {}".format(key, dispatcher, dispatcher_params)   
            return False

        mock_my_method.side_effect = side_effect

        azulejo.run(False)


if __name__ == '__main__':
    unittest.main()



