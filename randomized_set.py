import random
import unittest


class RandomizedSet:
    """Data Structure which supports insert, delete and get-random element in O(1).

    Duplicates not allowed

    Usage:
        >>> r = RandomizedSet()
        >>> r.insert(1)
        True
        >>> r.insert(2)
        True
        >>> r.random()
        1
        >>> r.insert(2)
        False
        >>> r.delete(2)
        True
        >>> r.insert(3)
        True
        >>> r.random()
        3

    Attributes:
        elements (list): List of elements inserted.
        index_map (dict): Dictionary maintaining element with its index in the elements(list).

    """

    def __init__(self):
        self.elements = []
        self.index_map = {}

    def insert(self, value):
        """Insert value into the Set.

        If `value` is already present in the set, return False. (since its a duplicate)
        else insert the value into the Set and return True.

        """
        if value in self.index_map:
            return False

        self.elements.append(value)
        index = len(self.elements) - 1
        self.index_map[value] = index
        return True

    def delete(self, value):
        """Delete value from the Set.

        If `value` is already present in the set, delete it and return True
        else return False.

        Approach to get O(1) delete
        1. Swap the last_element in the list with value
        2. Then adjust the last element's index in the `index_map`
        3. Pop the last element in the list
        4. Delete the value from `index_map`

        """
        if value not in self.index_map:
            return False

        index = self.index_map[value]
        last_index = len(self.elements) - 1

        self.elements[index], self.elements[last_index] = (
            self.elements[last_index],
            self.elements[index],
        )
        # Reset the index of the swapped element which is now at location `index`.
        self.index_map[self.elements[index]] = index
        # Now that the element-to-delete is in the last slot, pop the element from list.
        self.elements.pop()
        # Remove element from index-map
        self.index_map.pop(value, None)
        return True

    def random(self):
        """Return random element from the Set."""
        if self.elements:
            return random.choice(self.elements)


class TestRandomizedSet(unittest.TestCase):
    def test_insert(self):
        random_set = RandomizedSet()
        self.assertTrue(random_set.insert(1))
        self.assertTrue(random_set.insert(2))
        self.assertTrue(random_set.insert(3))
        self.assertTrue(random_set.insert(4))
        self.assertFalse(random_set.insert(2))

    def test_delete(self):
        random_set = RandomizedSet()
        random_set.insert(2)
        self.assertTrue(random_set.delete(2))
        self.assertFalse(random_set.delete(2))
        self.assertFalse(random_set.delete(10))

    def test_random(self):
        random_set = RandomizedSet()
        self.assertIsNone(random_set.random())
        random_set.insert(1)
        random_set.insert(2)
        random_set.insert(3)
        random_set.insert(4)
        self.assertIn(random_set.random(), (1, 2, 3, 4))


if __name__ == "__main__":
    unittest.main()
