import csv

def is_row_safe(row):
    tmp_value = None
    direction = None
    for value in row:
        value = int(value)
        if tmp_value is not None:
            diff = value - tmp_value
            if direction is None:
                if diff > 0:
                    direction = "up"
                elif diff < 0:
                    direction = "down"
            if not (1 <= abs(diff) <= 3):
                return False
            if (direction == "up" and diff < 0) or (direction == "down" and diff > 0):
                return False
        tmp_value = value
    return True
def count_safe_rows(filename):
    with open(filename, mode='r') as file:
        reader = csv.reader(file)
        rows = list(reader)
    safe_list = [is_row_safe(row) for row in rows]
    safe_count = sum(1 for safe in safe_list if safe)
    return safe_count
filename = './output.csv'
safe_count = count_safe_rows(filename)
print(f"Anzahl sicherer Zeilen: {safe_count}")
