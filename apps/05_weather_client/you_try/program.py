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


def find_city_and_state_from_location(city: str):
    return city.split('\n')[0].strip()


def get_weather_from_html(html):
    soup = bs4.BeautifulSoup(html, 'html.parser')
    city = soup.find(id='location').find('h1').get_text()
    condition = soup.find(id='curCond').find(class_='wx-value').get_text()
    temp = soup.find(id='curTemp').find(class_='wx-value').get_text()
    scale = soup.find(id='curTemp').find(class_='wx-unit').get_text()

    city = cleanup_text(city)
    city = find_city_and_state_from_location(city)
    condition = cleanup_text(condition)
    temp = cleanup_text(temp)
    scale = cleanup_text(scale)

    # print(city.strip())
    # print(condition.strip())
    # print(temp, scale)
    return WeatherReport(cond=condition, temp=temp, scale=scale, loc=city)

def main():
    # print the header
    print_header()
    # get zip from user

    zipcode = input('What zipcode do you want the weather for? ')

    # get html from web

    html = get_html(zipcode)
    report = get_weather_from_html(html)

    print('The temp in {} is {} and {} {}'.format(
        report.loc,
        report.cond,
        report.temp,
        report.scale
    ))

    # display the forecast


def print_header():
    print('-' * 30)
    print('          WEATHER APP')
    print('-' * 30)
    print()


def get_html(zipcode):
    url = 'https://www.wunderground.com/weather-forecast/{}'.format(zipcode)
    response = requests.get(url)

    return response.text


if __name__ == "__main__":
    main()
