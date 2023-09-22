import pickle
import zlib


class ColumnarStorage:
    def __init__(self):
        self.columns = {}

    def add_column(self, column_name, column_data):
        compressed_data = zlib.compress(pickle.dumps(column_data))
        self.columns[column_name] = compressed_data

    def get_column(self, column_name):
        compressed_data = self.columns.get(column_name)
        if compressed_data is None:
            return None
        column_data = pickle.loads(zlib.decompress(compressed_data))
        return column_data

    def remove_column(self, column_name):
        if column_name in self.columns:
            del self.columns[column_name]
