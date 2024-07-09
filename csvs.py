import csv

def read_csv(path: str) -> list[list[int]]:
    board: list[list[int]] = []
    with open(path) as csv_file:
        reader = csv.reader(csv_file, delimiter=',')
        count = 0
        for row in reader:
            for val in row:
                if val == '':
                    continue
                val = int(val.strip())
                if val == 0:
                    board.append([1,2,3,4,5,6,7,8,9])
                else:
                    board.append([val])
                count += 1
    return board
