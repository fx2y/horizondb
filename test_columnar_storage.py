import unittest
from storage import ColumnarStorage


class TestColumnarStorage(unittest.TestCase):
    def setUp(self):
        self.storage = ColumnarStorage()

    def test_add_column(self):
        self.storage.add_column('name', ['Alice', 'Bob', 'Charlie'])
        self.assertEqual(self.storage.get_column('name'), ['Alice', 'Bob', 'Charlie'])

    def test_get_column(self):
        self.storage.add_column('name', ['Alice', 'Bob', 'Charlie'])
        self.assertEqual(self.storage.get_column('name'), ['Alice', 'Bob', 'Charlie'])
        self.assertIsNone(self.storage.get_column('age'))

    def test_remove_column(self):
        self.storage.add_column('name', ['Alice', 'Bob', 'Charlie'])
        self.storage.add_column('age', [25, 30, 35])
        self.storage.remove_column('age')
        self.assertIsNone(self.storage.get_column('age'))
        self.assertEqual(self.storage.get_column('name'), ['Alice', 'Bob', 'Charlie'])

    def test_compression(self):
        self.storage.add_column('name', ['Alice', 'Bob', 'Charlie'])
        compressed_data = self.storage.columns['name']
        self.assertNotEqual(compressed_data, ['Alice', 'Bob', 'Charlie'])
        decompressed_data = self.storage.get_column('name')
        self.assertEqual(decompressed_data, ['Alice', 'Bob', 'Charlie'])


if __name__ == '__main__':
    unittest.main()
