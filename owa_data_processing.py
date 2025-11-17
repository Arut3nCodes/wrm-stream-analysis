from datetime import datetime

def process_owa_data(data):
    processed_data = []
    date = datetime.fromtimestamp(data['current']['dt']).strftime("%Y-%m-%d %H:%M")
    weather_info = {
        'timestamp': date,
        'temperature': data['current']['temp'],
        'feels_like': data['current']['feels_like'],
        'pressure': data['current']['pressure'],
        'humidity': data['current']['humidity'],
        'dew_point': data['current']['dew_point'],
        'clouds': data['current']['clouds'],
        'wind_speed': data['current']['wind_speed'],
        'wind_deg': data['current']['wind_deg'],
        'weather_main': data['current']['weather'][0]['main'],
        'weather_description': data['current']['weather'][0]['description'],
        'rain': data['current']['rain'] if 'rain' in data['current'] else 0.0,
        'snow': data['current']['snow'] if 'snow' in data['current'] else 0.0
    }
    processed_data.append(weather_info)
    return processed_data