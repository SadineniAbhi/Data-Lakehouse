import pyarrow.parquet as pq

table = pq.read_table("/home/abhi/data-lake/data/flights/flights.parquet")
print(table.schema)
