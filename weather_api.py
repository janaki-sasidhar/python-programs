import requests,json,pprint,datetime,pytz
def credentials():
    api_key=""
    city_name=input("Enter the city name ...  ")
    return weather(api_key,city_name)


def time_stamp_convert(unixtime):
    # get time in tz
    tz = pytz.timezone('Asia/Kolkata')
    dt = datetime.datetime.fromtimestamp(unixtime, tz)
    # print it
    return dt.strftime('%Y-%m-%d %H:%M:%S %Z%z')

def kelvin_to_celsius(kelvin):
    return kelvin-273.15

def weather(api_key,city_name):
    url=f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}"
    response = json.loads(requests.get(url).content)
    try:
        #pprint.pprint(response)

        country = response['sys']['country']

        city_name=response['name']

        temparature_present = kelvin_to_celsius(response['main']['temp'])

        temparature_feels_like=kelvin_to_celsius(response['main']['feels_like'])

        humidity=response['main']['humidity']

        description=response['weather'][0]['description']

        present_time = time_stamp_convert(response['dt'])

        sunrise = time_stamp_convert(response['sys']['sunrise'])

        sunset = time_stamp_convert(response['sys']['sunset'])

        latitude = response['coord']['lat']

        longitude = response['coord']['lon']

        print("The weather info is : ")
        print(f"""
        City                  : {city_name.capitalize()}
        Country               : {country.capitalize()}
        present_time          : {present_time}
        temparature_present   : {temparature_present:.2f}
        telmarature_feelslike : {temparature_feels_like:.2f}
        description           : {description} 
        humidity              : {humidity}
        sunrise               : {sunrise}
        sunset                : {sunset}
        latitude              : {latitude}
        longitude             : {longitude}
        """)

    except Exception:
        print("Error ... please read the below information")
        #pprint.pprint(response)
        print(f"Error Message : {response['message']}")



if __name__ == "__main__":
    credentials()