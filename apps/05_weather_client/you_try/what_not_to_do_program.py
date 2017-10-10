import requests
import bs4


def get_weather_from_html(html):
    soup = bs4.BeautifulSoup(html, 'html.parser')
    city = soup.find(class_='region-content-header').find('h1').get_text()
    condition = soup.find(class_='condition-icon').find('p').get_text()
    temp = soup.find(class_='wu-unit-temperature').find(class_='wu-value').get_text()
    scale = soup.find(class_='wu-unit-temperature').find(class_='wu-label').get_text()

    weather_report = {'city': city.strip(),
                      'condition': condition.strip(),
                      'temp': temp.strip(),
                      'scale': scale.strip()}

    return weather_report


def print_header():
    print('------------------------------')
    print('          WEATHER APP')
    print('------------------------------')
    print()


def get_html(zipcode):
    url = 'http://www.wunderground.com/weather-forecast/{}'.format(zipcode)
    print('Fetching {}'.format(url))
    response = requests.get(url)

    return response


def main():
    print_header()
    # zipcode = input('What zipcode do you want the weather for? ')


    zipcodes = ["{:05}".format(i) for i in range(1000, 99999)]
    for zipcode in zipcodes:
        html = get_html(zipcode)
        if html.status_code != 404:
            report = get_weather_from_html(html.text)
            print('The temp in {} is {} {} and the current condition is {}'.format(
                report['city'],
                report['temp'],
                report['scale'],
                report['condition']
            ))


if __name__ == "__main__":
    main()
