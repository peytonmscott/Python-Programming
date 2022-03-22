import list_tools
import unittest


class ListToolsTest(unittest.TestCase):
    def test_all_even(self):
        self.assertEqual(list_tools.all_even([]), [])
        self.assertEqual(list_tools.all_even([1, 2, 3, 4]), [2, 4])
        self.assertEqual(list_tools.all_even([17, 21, 37, 18, 14, 19, 12, 9, -98, 100, -13, -11]),
                         [18, 14, 12, -98, 100])

    def test_all_not_multiple(self):
        self.assertEqual(list_tools.all_not_multiple([], 10), [])
        self.assertEqual(list_tools.all_not_multiple([1, 2, 3, 4], 2), [1, 3])
        self.assertEqual(list_tools.all_not_multiple([17, 21, 37, 18, 14, 19, 12], 7),
                         [17, 37, 18, 19, 12])

    def test_max_from_2_tuples(self):
        self.assertEqual(list_tools.max_from_2_tuples([]), None)
        self.assertEqual(list_tools.max_from_2_tuples([(1, 2), (-1, 13)]), (1, 13))
        self.assertEqual(list_tools.max_from_2_tuples([(-100, -500), (-300, -200), (-50, -700)]), (-50, -200))
        self.assertEqual(list_tools.max_from_2_tuples([(0, 0)]), (0, 0))
        self.assertEqual(list_tools.max_from_2_tuples([(10, 20), (13, 23), (16, 26), (5, 5)]), (16, 26))
        self.assertEqual(list_tools.max_from_2_tuples([(0, 0), (0, 0), (0, 0)]), (0, 0))
        self.assertEqual(list_tools.max_from_2_tuples([(-5, -6), (-5, -6), (-5, -6)]), (-5, -6))

    def test_lower_case_words(self):
        self.assertEqual(list_tools.lower_case_words("Every good boy does fine"),
                         ["every", "good", "boy", "does", "fine"])
        self.assertEqual(
            list_tools.lower_case_words("Words     are SEPARATed by     ONE or      more space characters"),
            ["words", "are", "separated", "by", "one", "or", "more", "space", "characters"])
        self.assertEqual(list_tools.lower_case_words(""), [])

    def test_baby_names(self):
        self.assertEqual(list_tools.baby_names(["Mark", "Allen", "Steve"], "Smith"),
                         ["Mark Allen Smith", "Mark Steve Smith",
                          "Allen Mark Smith", "Allen Steve Smith",
                          "Steve Mark Smith", "Steve Allen Smith"])
        self.assertEqual(list_tools.baby_names(["Sue", "Betty", "Wilma"], "Jones"),
                         ["Sue Betty Jones", "Sue Wilma Jones",
                          "Betty Sue Jones","Betty Wilma Jones",
                          "Wilma Sue Jones", "Wilma Betty Jones"])
