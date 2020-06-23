from mock import patch
import unittest
from get_answer import answer
unittest = unittest


class Test(unittest.TestCase):
    # get_input will return 'yes' during this test
    @patch('get_answer.get_input', return_value='yes')
    def test_answer_yes(self, input):
        self.assertEqual(answer(), 'you entered yes')

    @patch('get_answer.get_input', return_value='no')
    def test_answer_no(self, input):
        self.assertEqual(answer(), 'you entered no')


if __name__ == '__main__':
    unittest.main()
