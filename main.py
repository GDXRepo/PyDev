import sys

bytes = sys.getsizeof(3**9090001)
mb = bytes / 1024 / 1024
print(f"размер равен {mb:.2f} MB")
