import csv


class DealSearch:
    def __init__(self, filepath="../startup_funding.csv"):
        with open(filepath, "rt") as csvfile:
            self.data = [row for row in csv.DictReader(csvfile)]

    def _filter(self, options):
        return (row for row in self.data if row | options == row)

    def where(self, options={}):
        return list(DealSearch._filter(self, options))

    def find_by(self, options):
        return next(DealSearch._filter(self, options))
