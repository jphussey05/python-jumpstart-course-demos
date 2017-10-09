import requests
import bs4
from collections import namedtuple

WeatherReport = namedtuple('WeatherReport',
                           'cond, temp, scale, loc')


def cleanup_text(text: str):
    if not text:
        return text

    text = text.strip()
    return text


def get_weather_from_html(html):
    soup = bs4.BeautifulSoup(html, 'html.parser')
    city = soup.find(class_='region-content-header').find('h1').get_text()
    condition = soup.find(class_='condition-icon').find('p').get_text()
    temp = soup.find(class_='wu-unit-temperature').find(class_='wu-value').get_text()
    scale = soup.find(class_='wu-unit-temperature').find(class_='wu-label').get_text()

    city = cleanup_text(city)
    condition = cleanup_text(condition)
    temp = cleanup_text(temp)
    scale = cleanup_text(scale)

    return WeatherReport(cond=condition, temp=temp, scale=scale, loc=city)


def print_header():
    print('------------------------------')
    print('          WEATHER APP')
    print('------------------------------')
    print()


def get_html(zipcode):
    url = 'https://www.wunderground.com/weather-forecast/{}'.format(zipcode)
    response = requests.get(url)

    return response.text


def main():
    print_header()
    zipcode = input('What zipcode do you want the weather for? ')
    html = get_html(zipcode)
    report = get_weather_from_html(html)

    print('The temp in {} is {} {} and the current condition is {}'.format(
        report.loc,
        report.temp,
        report.scale,
        report.cond
    ))


if __name__ == "__main__":
    main()
