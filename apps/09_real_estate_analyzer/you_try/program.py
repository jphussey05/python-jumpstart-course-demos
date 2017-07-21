import csv
import os
import statistics

from you_try.data_types import Purchase


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


def announce(item, msg):
    print('Pulling item {} for {}'.format(item, msg))
    return item


def query_data(data):
    # if data was sorted by price:
    data.sort(key=lambda p: p.price)

    # most expensive house?
    high_purcahse = data[-1]
    print('The most expensive house is ${:,} with {} beds and {} baths.'.format(
        high_purcahse.price, high_purcahse.beds, high_purcahse.baths))
    # least expensive house?
    low_purchase = data[0]
    print('The least expensive house is ${:,} with {} beds and {} baths.'.format(
        low_purchase.price, low_purchase.beds, low_purchase.baths))

    prices = [purchase.price for purchase in data]
    avg_price = statistics.mean(prices)
    print('The average home price is ${:,}'.format(int(avg_price)))

    two_bed_homes = (purchase for purchase in data if announce(purchase, '2-bedrooms, found{}'
                                                               .format(purchase.beds)) and purchase.beds == 2)

    homes = []
    for h in two_bed_homes:
        if len(homes) > 5:
            break
        homes.append(h)

    avg_price = statistics.mean((announce(p.price, 'price') for p in homes))
    avg_baths = statistics.mean((p.baths for p in homes))
    avg_sqft = statistics.mean((p.sq__ft for p in homes))

    print('AVG price for a 2-bedroom is ${:,}, baths={}, sq_ft={}'
          .format(int(avg_price), round(avg_baths, 1), round(avg_sqft, 1)))


def load_file(filename):
    with open(filename, 'r', encoding='utf-8') as fin:
        reader = csv.DictReader(fin)
        purchases = []
        for row in reader:
            p = Purchase.create_from_dict(row)
            purchases.append(p)

        return purchases


if __name__ == '__main__':
    main()
