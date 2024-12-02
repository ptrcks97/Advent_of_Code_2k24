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

def is_row_safe_with_dampener(row):
    if is_row_safe(row):
        return True
    for i in range(len(row)):
        new_row = row[:i] + row[i+1:]
        if is_row_safe(new_row):
            return True
    return False

def count_safe_rows_with_dampener(filename):
    with open(filename, mode='r') as file:
        reader = csv.reader(file)
        rows = list(reader)
    
    safe_count = 0
    for row in rows:
        if is_row_safe_with_dampener(row):
            safe_count += 1
    
    return safe_count

filename = './output.csv'
safe_count = count_safe_rows_with_dampener(filename)
print(f"Anzahl sicherer Zeilen (mit Problem Dampener): {safe_count}")