def print_operation_table(operation, num_rows=6, num_columns=6):
   for row in range(1, num_rows + 1):
      for col in range(1, num_columns + 1):
            print(str(operation(row, col)).rjust(4), end='')
      print()

print_operation_table(lambda x, y: x * y, 6, 6)