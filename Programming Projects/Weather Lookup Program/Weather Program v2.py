import requests

# File: Week12 - Weather Program.py
# Name: Adrian Rybinski
# Date: February 29, 2020
# Course: DSC 510 - Introduction to Programming
# Assignment: 12.1
# Desc: Weather program allowing users to lookup the forecast in their desired area/location.zip


key = ''  # Make sure to enter your API key here before proceeding.


# function for the city name being the preferred search option
def city_main(city_name):
    url = "https://api.openweathermap.org/data/2.5/weather?"
    url_params = {'q': city_name, 'units': 'imperial', 'appid': key}  # parameters for the url API call
    conn_ok(url, url_params)
    response = requests.get(url=url, params=url_params)
    x = response.json()
    pretty_print(x)


# function for the zip code being the preferred search option
def zip_main(zip_code):
    url = "https://api.openweathermap.org/data/2.5/weather?"
    url_params = {'zip': zip_code, 'units': 'imperial', 'appid': key}  # parameters for the url API call
    conn_ok(url, url_params)
    response = requests.get(url=url, params=url_params)
    x = response.json()
    pretty_print(x)


# function used to format the output as well as manage any changes to the message content
def pretty_print(x):
    print('\nCurrently, in {}, {} the temperature is {} degrees Fahrenheit and {}.'.format(x['name'], x['sys']['country'], x['main']['temp'], x['weather'][0]['main']))
    print('The expected HIGH temperature today will be {} degrees Fahrenheit with a LOW temperature of {} degrees Fahrenheit.'.format(x['main']['temp_max'], x['main']['temp_min']))
    print('For those looking to go outside, the temperature will feel like {} degrees Fahrenheit.'.format(x['main']['feels_like']))
    print('Humidity will be {} % with wind speeds reaching {} mph.'.format(x['main']['humidity'], x['wind']['speed']))


# used to create a new message for user at the end of the run and check for invalid entries.
def try_again():
    while True:
        again = input("\nWould you like to search again? Y or N: ").lower()
        try:
            if again not in ('y', 'n'):
                raise ValueError
        except ValueError:
            print('Invalid Entry.  Please enter Y or N.')
        else:
            if again == 'n':
                print("\nThank you for using our service.")
                print("Please consider us for your future weather needs.")
                break
            elif again == 'y':
                main()
        break


# check connection status
def conn_ok(url, url_params):
    try:
        response = requests.get(url=url, params=url_params)
        if response.status_code == 200:  # Good status, program will proceed.
            pass
        elif response.status_code == 404:  # Error where city or zip is ot found.
            print('City Name or Zip Code was not found in our database.  Please try again.')
            main()
    except requests.exceptions.RequestException as e:
        print('Something just went wrong on our end or there is an issue with your internet connection.  Try again later.\nSee error details below:')
        print(str(e))


# main function to run the entire program.
def main():
    try:
        done = False
        # loop to continue with the program until the done option is selected
        while not done:
            search_pref = input("How would you like to start your search? Please enter ZIP or CITY. Enter DONE to quit: ").lower()
            # runs the city_main function if user selects to use city for search
            if search_pref == 'city':
                city_name = input("Enter city name: ").lower()
                city_main(city_name)
                try_again()
                break
            # runs the zip_main function if user selects to use zip for search
            elif search_pref == 'zip':
                zip_name = input("Enter ZIP code: ").lower()
                zip_main(zip_name)
                try_again()
                break
            # will present an exit message when user decides not to go forward
            elif search_pref == 'done':
                done = True
                print("\nThank you for using our service.")
                print("Please consider us for your future weather needs.")
            # check in case user enters something other than zip, city, or done
            else:
                print("\nInvalid entry. Enter ZIP or CITY to search. Enter DONE to quit.")
    except:
        pass


if __name__ == '__main__':
    print("Welcome to the Weather Center.")
    print('The source of the most up to date weather information.\n')
    main()
