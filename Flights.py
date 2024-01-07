import requests
from bs4 import BeautifulSoup

userAgent = 'Mozilla/5.0 (X11; Linux x86_64; rv:10.0) Gecko/20100101 Firefox/10.0'
headers = {'User-Agent': userAgent}

class Flights:
    def __init__(self, from_location, to_location, day_of_departure, type_of_trip):
        self.from_location = from_location
        self.to_location = to_location
        self.day_of_departure = day_of_departure
        self.type_of_trip = type_of_trip

    def get_flights(self):
        url = f"https://www.google.com/search?q=flights+from+{self.from_location}+to+{self.to_location}+on+{self.day_of_departure}+{self.type_of_trip}"
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.content, 'html.parser')

        airline_name = soup.find_all(class_="ps0VMc")
        time_taken = soup.find_all(class_="sRcB8")
        connection_status = soup.find_all(class_="u85UCd")
        price = soup.find_all(class_="GARawf")

        data = []

        for i in range(0, 10):
            try:
                data.append({
                    "airline_name": airline_name[i].text,
                    "time_taken": time_taken[i].text,
                    "connection_status": connection_status[i].text,
                    "price": price[i].text
                })
            except:
                pass
        
        return data

flights = Flights("pune", "goa", "2023-8-1", "oneway")
print(flights.get_flights())
