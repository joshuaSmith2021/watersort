import unittest

import watersort


class WatersortTests(unittest.TestCase):
    def test_basic_tube_methods_01(self):
        tube = watersort.Tube(4, [2, 2, 3, 4])

        self.assertTrue(tube.is_full())
        self.assertFalse(tube.is_empty())
        self.assertEqual(tube.peek(), 4)
        self.assertEqual(tube.pop(), 4)
        self.assertFalse(tube.is_full())
        self.assertEqual(tube.pop(), 3)
        self.assertEqual(tube.pop(), 2)
        self.assertEqual(tube.pop(), 2)
        self.assertEqual(tube.pop(), None)
        self.assertTrue(tube.is_empty())

        tube.push(3)
        self.assertFalse(tube.is_empty())
        self.assertFalse(tube.is_full())
        self.assertEqual(tube.peek(), 3)

        self.assertRaises(AssertionError, lambda: tube.push(2))

        tube.push(3)
        tube.push(3)
        tube.push(3)

        self.assertRaises(AssertionError, lambda: tube.push(3))

        self.assertTrue(tube.is_full())

        tube = watersort.Tube(0, [])
        self.assertEqual(tube.peek(), None)

        self.assertRaises(AssertionError, lambda: watersort.Tube(0, [0]))

    def test_basic_dump_01(self):
        source = watersort.Tube(4, [2, 2, 2, 4])
        destination = watersort.Tube(4, [])

        self.assertEqual(watersort.tube_dump(source, destination), 1)
        self.assertListEqual(destination.contents, [4])
        self.assertEqual(watersort.tube_dump(source, destination), 0)


if __name__ == '__main__':
    unittest.main()
