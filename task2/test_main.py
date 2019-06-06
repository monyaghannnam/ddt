import unittest2
import sys
import json
from main import *
import HTMLTestRunner

sys.path.append("../..")

class TestFunctions(unittest2.TestCase):
    """
    firt  methods are  positive test cases with valid int data set
    last 3 methods are negative test cases with invalid data set
    """
    def test_add_empty(self):
        # test equality when array_length = 0 && copy with add some elements
        with app.test_request_context():
            out = get(0)
            expected = (json.loads(out.get_data(as_text=True)))['arr']
            copy = expected[:]
            if len(copy) == 0:
                for i in range(0, random.randint(0, 10)):
                    copy.append(random.randint(0, 10))

            actual = copy
            self.assertEqual(expected,actual)

    def test_add_first(self):
        # test equality when array_length has at least one element && copy array with add one element at first
        with app.test_request_context():
            out = get(1)
            expected = (json.loads(out.get_data(as_text=True)))['arr']
            copy = expected[:]
            copy.insert(0,random.randint(0, 10))
            actual = copy
            self.assertEqual(expected, actual)

    def test_del_first(self):
        # test equality when array_length =1 && copy array with delete one element at first
        with app.test_request_context():
            out = get(1)
            expected = (json.loads(out.get_data(as_text=True)))['arr']
            copy = expected[:]
            del copy[0]
            actual = copy
            self.assertEqual(expected, actual)

    def test_add_last(self):
        # test equality when copied array with add one element at last
        with app.test_request_context():
            out = get(1)
            expected = (json.loads(out.get_data(as_text=True)))['arr']
            copy = expected[:]
            copy.append(random.randint(0, 10))
            actual = copy
            self.assertEqual(expected, actual)

    def test_del_last(self):
        # test equality when copied array with delete one element at last
        with app.test_request_context():
            out = get(1)
            expected = (json.loads(out.get_data(as_text=True)))['arr']
            copy = expected[:]
            del copy[-1]
            actual = copy
            self.assertEqual(expected, actual)

    def test_diff_value(self):
        # test equality when copied array with same size but diff values
        with app.test_request_context():
            out = get(3)
            expected = (json.loads(out.get_data(as_text=True)))['arr']
            copy = expected[:]
            random.shuffle(copy)
            actual = copy
            self.assertEqual(expected, actual)

    def test_empty_list(self):
        # test equality when copied array is empty
        with app.test_request_context():
            out = get(0)
            expected = (json.loads(out.get_data(as_text=True)))['arr']
            copy = expected[:]
            actual = copy
            self.assertEqual(expected, actual)
    def test_None_list(self):
        # test equality when copied array is None
        with app.test_request_context():
            out = get(5)
            expected = (json.loads(out.get_data(as_text=True)))['arr']
            copy = expected[:]
            copy =None
            actual = copy
            self.assertEqual(expected, actual)

    def test_get_negative_str(self):
        # test equality when array_length = string
        with app.test_request_context():
            out = get('4')
            actual = json.loads(out.get_data(as_text=True))
            expected = "array_length must be non-negative int"
            actual = actual['result']
            self.assertEqual(expected, actual)

    def test_get_negative_num(self):
        # test equality when array_length = -num
        with app.test_request_context():
            out = get(-3)
            actual = json.loads(out.get_data())
            expected = "array_length cant be negative"
            actual = actual['result']
            self.assertEqual(expected, actual)

    def test_get_negative_None(self):
        # test equality when array_length = None
        with app.test_request_context():
            out = get(None)
            actual = json.loads(out.get_data())
            expected = "array_length cant be negative"
            actual = actual['result']
            self.assertEqual(expected, actual)


if __name__ == '__main__':
    HTMLTestRunner.main()