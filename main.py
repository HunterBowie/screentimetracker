from constants import CATEGORY_JSON_FILE, SCREEN_TIME_CSV_FILE

with open(SCREEN_TIME_CSV_FILE, "r") as csv_file:
    raw_data = csv_file.read()
    raw_data = raw_data.split("\n")
    raw_data.pop(0)
    data = []
    for row in raw_data:
        new_row = row.split(",")
        new_row = new_row[0].strip(), new_row[1].strip(), int(
            new_row[2].strip())
        data.append(new_row)

    print(data)
