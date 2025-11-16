from datetime import datetime
def process_wrm_data(data):
    processed_data = []
    date = datetime.now().strftime("%Y-%m-%dT%H:%M")
    for place in data['countries'][0]['cities'][0]['places']:
        if(place['bike'] == False):
            station_info = {
                'id': place['uid'],
                'name': place['name'],
                'latitude': place['lat'],
                'longitude': place['lng'],
                'bikes_total': place['bikes'],
                'bikes_available': place['bikes_available_to_rent'],
                'timestamp': date
            }
            processed_data.append(station_info)
    return processed_data