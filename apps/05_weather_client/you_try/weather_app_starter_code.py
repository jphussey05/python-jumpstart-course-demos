def print_header():
    print('--------------------------------')
    print('          WEATHER APP')
    print('--------------------------------')
    print()


def get_html(zipcode):
    # URL to hit is -- http://www.wunderground.com/weather-forecast/{}
    # Add the zipcode to this URL with a string format

    # Use Requests to handle the GET and response from web server
    # Return the response object's text
    pass


def get_weather_from_html(html):
    # Code to parse the HTML response with BeautifulSoup goes here
    # Cadets will need to utilize the developer tools of their favorite web browser
    # in order to find the appropriate class selectors to identify the element in question

    # Extract the city
    # Extract the temperature
    # Extract the scale (Fahrenheit or Celsius)
    # Extract the conditions

    # Clean up the data's extra newlines, etc.
    # Return the data back to the main function with an appropriate data structure
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
