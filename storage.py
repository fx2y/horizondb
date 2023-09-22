class ColumnarStorage:
    def __init__(self):
        self.columns = {}

    def add_column(self, column_name, column_data):
        self.columns[column_name] = column_data

    def get_column(self, column_name):
        return self.columns.get(column_name)

    def remove_column(self, column_name):
        if column_name in self.columns:
            del self.columns[column_name]
