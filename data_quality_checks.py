# Implement pre-read checks with parquet(in Python)

import pyarrow.parquet as pq

parquet_file_path = "titanic.parquet"

try:
    parquet_file = pq.ParquetFile(parquet_file_path)
    metadata = parquet_file.metadata

    # Check 1: Row Count (Integrity)
    num_rows = metadata.num_rows
    print(f"Number of rows: {num_rows}")
    if num_rows == 0:
        raise ValueError("Parquet file is empty")

    # Check 2: Schema/Column Names (Conformity)
    schema = parquet_file.schema.to_arrow_schema()
    column_names = schema.names
    print(f"Schema Check: {len(column_names)}, columns: {column_names}")

    # Check 3: Check for valid Column Names
    expected_column = "Sex"

    if expected_column not in column_names:
        raise KeyError(f"Missing expected column: {expected_column}")

    # Check the data type of specific column
    age_dtype = schema.field('Age').type

    if not str(age_dtype).startswith('float') and not str(age_dtype).startswith('double'):
        print(f"WARNING: 'Age' column type is {age_dtype}, expected a numeric type.")

except FileNotFoundError:
    print(f"Parquet file {parquet_file_path} not found")
except Exception as e:
    print("An error occurred during metadata check: {e}")