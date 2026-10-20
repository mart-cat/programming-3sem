import unittest
from app import gen_bin_tree


class TestGenBinTree(unittest.TestCase):
    def test_height_zero(self):
        tree = gen_bin_tree(0, 8)
        self.assertEqual(tree, {"value": 8, "left": None, "right": None})

    def test_height_one(self):
        tree = gen_bin_tree(1, 8)
        self.assertEqual(tree["left"]["value"], 12)
        self.assertEqual(tree["right"]["value"], 64)

    def test_height_two(self):
        tree = gen_bin_tree(2, 8)
        self.assertEqual(tree["left"]["left"]["value"], 18)


if __name__ == "__main__":
    unittest.main()
