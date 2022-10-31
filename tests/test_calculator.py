from unittest import TestCase, main

from main import calculator


class CalculatorTest(TestCase):
    def test_plus(self):
        self.assertEqual(calculator('2+2'), 4)

    def test_minus(self):
        self.assertEqual(calculator('5-2'), 3)

    def test_multiply(self):
        self.assertEqual(calculator('2*3'), 6)

    def test_divide(self):
        self.assertEqual(calculator('2/2'), 1)

    def test_no_sign(self):
        with self.assertRaises(ValueError) as e:
            calculator('test')
        self.assertEqual('Expression should have one of following signs "+-/*"', e.exception.args[0])

    def test_two_sign(self):
        with self.assertRaises(ValueError) as e:
            calculator('2+2+2')
        self.assertEqual('Expression should contain two integers and one sign', e.exception.args[0])

    def test_many_sign(self):
        with self.assertRaises(ValueError) as e:
            calculator('2+2*2')
        self.assertEqual('Expression should contain two integers and one sign', e.exception.args[0])


    def test_no_ints(self):
        with self.assertRaises(ValueError) as e:
            calculator('2+2+2.5')
        self.assertEqual('Expression should contain two integers and one sign', e.exception.args[0])

    def test_strings(self):
        with self.assertRaises(ValueError) as e:
            calculator('a+b')
        self.assertEqual('Expression should contain two integers and one sign', e.exception.args[0])


if __name__ == '__main__':
    main()

