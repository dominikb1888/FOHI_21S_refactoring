import csv


class FundingRaised:
    def __init__(self, filepath="../startup_funding.csv"):
        with open(filepath, "rt") as csvfile:
            self.data = [row for row in csv.DictReader(csvfile)]

    def where(self, options={}):
        return [row for row in self.data if row | options == row]

    def find_by(self, options):
        return next(row for row in self.data if row | options == row)
