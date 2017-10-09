def print_header():
    print('--------------------------------')
    print('          WEATHER APP')
    print('--------------------------------')
    print()


def get_html(zipcode):
    pass


def get_weather_from_html(html):
    pass


def main():
    # print the header
    print_header()

    # get zipcode from user
    zipcode = input('What zipcode do you want the weather for? ')

    # get html from web
    html = get_html(zipcode)

    # parse the html response
    report = get_weather_from_html(html)

    # display the forecast
    print('The weather output will go here :')


if __name__ == '__main__':
    main()
