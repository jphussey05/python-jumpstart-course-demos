import requests

def main():
    # print the header
    print_header()
    # get zip from user

    zipcode = input('What zipcode do you want the weather for? ')

    # get html from web

    get_html(zipcode)

    # parse the html
    # display the forecast
    print('hello from main')


def print_header():
    print('-'*30)
    print('          WEATHER APP')
    print('-'*30)
    print()


def get_html(zipcode):
    url = 'https://www.wunderground.com/weather-forecast/{}'.format(zipcode)


if __name__ == "__main__":
    main()
