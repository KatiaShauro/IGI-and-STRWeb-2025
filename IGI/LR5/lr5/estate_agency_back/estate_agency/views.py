import requests
from django.shortcuts import render


def index(request):
    appid = '63026ab922acdc159af4d7d5c6adca54'
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=' + appid

    city = 'London'
    res = requests.get(url.format(city)).json()
    # получили конвертирование json формата в словарь

    city_info = {
        'city': city,
        'temp': res["main"]["temp"],
        'icon': res["weather"][0]["icon"]
    }

    context = {'info': city_info}
    return render(request, 'weather/index.html', context)