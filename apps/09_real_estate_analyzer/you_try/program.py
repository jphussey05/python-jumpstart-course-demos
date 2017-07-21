import os


def main():
    print_header()
    filename = get_data_file()
    data = load_file(filename)
    query_data(data)


def print_header():
    print('------------------------------')
    print(' REAL ESTATE DATA MINING APP')
    print('------------------------------')
    print()


def get_data_file():
    base_folder = os.path.dirname(__file__)
    return os.path.join(base_folder, 'data', 'SacramentoRealEstateTransactions2008.csv')


def query_data(data):
    pass


def load_file(filename):
    with open(filename, 'r', encoding='utf-8') as fin:
        header = fin.readline()
        print('found header: ' + header)

        lines = []
        for line in fin:
            line_data = line.split(',')
            lines.append(line_data)

        print(lines[:5])


if __name__ == '__main__':
    main()
