from django.shortcuts import render
import json  # import json to load json data to python dictionary
import urllib.request  # urllib.request to make a request to api
  
  
def index(request):
    if request.method == 'POST':
        city = request.POST['city']
        city = city.replace(" ", "+")
        
        # source contain JSON data from API
        source = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q=' + city + '&appid=c52960f66e4698756653f502d3048286'+'&units=metric').read()
        
        # converting JSON data to a dictionary
        list_of_data = json.loads(source)
  
        # data for variable list_of_data
        data = {
            'city': city.replace("+", " "),
            "country_code": str(list_of_data['sys']['country']),
            "temp": str(list_of_data['main']['temp']) + '°C',
            "pressure": str(list_of_data['main']['pressure'])+'hPa',
            "humidity": str(list_of_data['main']['humidity'])+'%',
            "description": str(list_of_data['weather'][0]['description']),
            "icon": str(list_of_data['weather'][0]['icon']),
            "clouds": str(list_of_data['clouds']['all'])+'%',
        }
        print(data)
    else:
        data ={}

        
    return render(request, "index.html", data)
