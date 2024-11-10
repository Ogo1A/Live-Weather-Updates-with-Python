from bs4 import BeautifulSoup  # Fixed the spelling mistake
import requests

# Fixed the User-Agent header string
header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}

def weather(city):
    # No need for city.replace("","+") -- removed that
    res = requests.get(f'https://www.google.com/search?q={city}&oq={city}&aqs=chrome.0.35i39l2j0l4j46j69i60.6128j1j7&sourceid=chrome&ie=UTF-8', headers=header)
    print("Searching......\n")
    
    # Fixed the spelling mistake and used BeautifulSoup correctly
    soup = BeautifulSoup(res.text, 'html.parser')
    
    try:
        # Extract the location, time, and weather information
        location = soup.select('#wobs_loc')[0].getText().strip()
        time = soup.select('#wob_dts')[0].getText().strip()
        info = soup.select('#wob_dc')[0].getText().strip()
        weather = soup.select('#wob_tem')[0].getText().strip()  # Fixed the .strip() issue
        
        # Print the results
        print(location)
        print(time)
        print(info)
        print(weather + "°C")
    except IndexError:
        print("Sorry, couldn't retrieve the weather data. Please try another city.")

# Take input from the user
city = input("Enter the Name of any city>>")
city = city + " weather"  # Adding "weather" to the search term
weather(city)
