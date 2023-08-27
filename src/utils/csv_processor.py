import csv

# from datetime import datetime
from decimal import Decimal


class CSVProcessor:
    def __init__(self) -> None:
        pass

    def parse_decimal(self, value):
        return Decimal(value.replace("R$", "").replace(",", ".").strip())

    def read_csv_and_processes(self, filename):
        #        processed_data = ""
        with open(filename, newline="", encoding="utf-8") as file:
            reader = csv.reader(file, delimiter=",")
            next(reader)
        #        current_date = datetime.now()
        for row in reader:
            print(row)
