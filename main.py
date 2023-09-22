from storage import ColumnarStorage

# create a new columnar storage
storage = ColumnarStorage()

# add columns to the storage
storage.add_column('name', ['Alice', 'Bob', 'Charlie'])
storage.add_column('age', [25, 30, 35])
storage.add_column('salary', [50000, 60000, 70000])

# get a column from the storage
name_column = storage.get_column('name')
print(name_column)  # ['Alice', 'Bob', 'Charlie']

# remove a column from the storage
storage.remove_column('salary')
