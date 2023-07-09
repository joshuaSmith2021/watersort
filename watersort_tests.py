import unittest

import watersort


class WatersortTests(unittest.TestCase):
    def test_basic_tube_methods_01(self):
        tube = watersort.Tube(4, [2, 2, 3, 4])

        self.assertTrue(tube.is_full())
        self.assertFalse(tube.is_empty())
        self.assertFalse(tube.is_complete())
        self.assertEqual(tube.peek(), 4)
        self.assertEqual(tube.pop(), 4)
        self.assertFalse(tube.is_full())
        self.assertEqual(tube.pop(), 3)
        self.assertEqual(tube.pop(), 2)
        self.assertEqual(tube.pop(), 2)
        self.assertEqual(tube.pop(), None)
        self.assertTrue(tube.is_empty())
        self.assertTrue(tube.is_complete())

        tube.push(3)
        self.assertFalse(tube.is_complete())
        self.assertFalse(tube.is_empty())
        self.assertFalse(tube.is_full())
        self.assertEqual(tube.peek(), 3)

        self.assertRaises(AssertionError, lambda: tube.push(2))

        tube.push(3)
        tube.push(3)
        tube.push(3)

        self.assertRaises(AssertionError, lambda: tube.push(3))

        self.assertTrue(tube.is_full())
        self.assertTrue(tube.is_complete())

        tube = watersort.Tube(0, [])
        self.assertEqual(tube.peek(), None)

        self.assertRaises(AssertionError, lambda: watersort.Tube(0, [0]))

    def test_basic_dump_01(self):
        source = watersort.Tube(4, [2, 2, 2, 4])
        destination = watersort.Tube(4, [])

        self.assertEqual(watersort.tube_dump(source, destination), 1)
        self.assertListEqual(destination.contents, [4])
        self.assertEqual(watersort.tube_dump(source, destination), 0)

    def test_basic_level_01(self):
        tubes = [
            watersort.Tube(4, [1, 2, 1, 2]),
            watersort.Tube(4, [2, 1, 2, 1]),
            watersort.Tube(4, []),
            watersort.Tube(4, [])
        ]

        level = watersort.Level(tubes)
        moves = [x for x in level.possible_moves()]

        self.assertListEqual(moves, [(0, 2), (0, 3), (1, 2), (1, 3)])

    def test_tube_strings_01(self):
        tube = watersort.Tube(4, [2, 4, 1])
        self.assertEqual(tube.to_csv(), '2,4,1,')
        self.assertEqual(str(tube), '[2, 4, 1]')

    def test_tube_strings_empty(self):
        tube = watersort.Tube(4, [])
        self.assertEqual(tube.to_csv(), ',,,')
        self.assertEqual(str(tube), '[]')

    def test_tube_loads_01(self):
        tube_csv = '4,2,3,1'
        tube = watersort.Tube.load_string(tube_csv)

        self.assertEqual(tube.peek(), 1)
        self.assertTrue(tube.is_full())
        self.assertFalse(tube.is_complete())

        self.assertEqual(tube.pop(), 1)
        self.assertFalse(tube.is_full())
        self.assertEqual(tube.pop(), 3)
        self.assertEqual(tube.pop(), 2)
        self.assertEqual(tube.pop(), 4)
        self.assertTrue(tube.is_empty())


if __name__ == '__main__':
    unittest.main()
