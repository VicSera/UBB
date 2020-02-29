import unittest

from CustomList.CustomList import CustomList


class CustomListTests(unittest.TestCase):
    def test__count__empty_list__0__ok(self):
        custom_list = CustomList()

        self.assertEqual(0, custom_list.count)

    def test__get_item__empty_list__exception(self):
        custom_list = CustomList()

        self.assertRaises(IndexError, custom_list.__getitem__, 1)

    def test__get_item__not_empty_list__existing_index__no_exception(self):
        custom_list = CustomList()
        custom_list.append(1)

        self.assertEqual(1, custom_list[0])

    def test__append__count_changes(self):
        custom_list = CustomList()
        custom_list.append(1)

        self.assertEqual(1, custom_list.count)

    def test__delitem__existing_index__count_updates(self):
        custom_list = CustomList()
        custom_list.append(1)
        del custom_list[0]

        self.assertEqual(0, custom_list.count)

    def test__delitem__existing_index__element_returned(self):
        custom_list = CustomList()
        custom_list.append(1)
        deleted = custom_list[0]
        del custom_list[0]

        self.assertEqual(1, deleted)

    def test__delitem__non_existing_index__exception(self):
        custom_list = CustomList()

        self.assertRaises(IndexError, custom_list.__delitem__, 0)

    def test__iter__no_elements__0_iterations(self):
        custom_list = CustomList()
        count = 0

        for object in custom_list:
            count += 1

        self.assertEqual(count, 0)

    def test__iter__5_elements__5_iterations(self):
        custom_list = CustomList()
        custom_list.append(1)
        custom_list.append(1)
        custom_list.append(1)
        custom_list.append(1)
        custom_list.append(1)

        count = 0

        for object in custom_list:
            count += 1

        self.assertEqual(count, 5)

    def test__iter__3_elements_before_delete__2_iterations(self):
        custom_list = CustomList()
        custom_list.append(1)
        custom_list.append(1)
        custom_list.append(1)
        del custom_list[0]

        count = 0

        for object in custom_list:
            count += 1

        self.assertEqual(count, 2)

    def test__setitem__existing_index__successful_update(self):
        custom_list = CustomList()
        custom_list.append(1)
        custom_list[0] = 2

        self.assertEqual(2, custom_list[0])

    def test__setitem__non_existing_index__index_error(self):
        custom_list = CustomList()

        self.assertRaises(IndexError, custom_list.__setitem__, 0, 0)

    def test__sort__unsorted_list__ascending(self):
        custom_list = CustomList()
        custom_list.append(3)
        custom_list.append(2)
        custom_list.append(1)
        CustomList.sort(custom_list, lambda x, y: x <= y)

        self.assertEqual(custom_list[0], 1)

    def test__sort__unsorted_list__descending(self):
        custom_list = CustomList()
        custom_list.append(1)
        custom_list.append(2)
        custom_list.append(3)
        CustomList.sort(custom_list, lambda x, y: x >= y)

        self.assertEqual(custom_list[0], 3)

    def test__sort__wrong_list_type__exception(self):
        self.assertRaises(TypeError, CustomList.sort, [], None)

    def test__filter__all_pass__count_same(self):
        custom_list = CustomList()
        custom_list.append(1)
        custom_list.append(2)
        custom_list.append(3)

        initial_count = 3

        CustomList.filter(custom_list, lambda x: x < 4)

        self.assertEqual(initial_count, custom_list.count)

    def test__filter__all_fail__count_0(self):
        custom_list = CustomList()
        custom_list.append(1)
        custom_list.append(2)
        custom_list.append(3)


        CustomList.filter(custom_list, lambda x: x == 4)

        self.assertEqual(0, custom_list.count)