import csv
import pandas

def useCSV(input_file):
    csv_reader = csv.reader(input_file, delimiter=',')
    for row in csv_reader:
        print(row)


def usePandas(input_file):
    df = pandas.read_csv(input_file)
    print(df)


if __name__ == '__main__':

    input_file = open('/Users/deepak.jayaprakash/cities.csv')
    # useCSV(input_file)
    usePandas(input_file)
