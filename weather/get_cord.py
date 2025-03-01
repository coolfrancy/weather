def get_cord(place):
    #imp.orts
    import requests
    from .api import api_weather
    #####

    r=requests.get(f'http://api.openweathermap.org/geo/1.0/direct?q={place}&appid={api_weather()}')
    #checks if we got good response
    req_code = r.status_code
    if req_code>=200 and req_code<300:
        #check if api return information
        if r.json()==[]:
            return 'Theres no info for this location'
        else:
            lon=r.json()[0]['lon']
            lat=r.json()[0]['lat']
            return lat,lon
    elif req_code>=300 and req_code<400:
        raise TypeError('URL for the cord API has been changed')
    elif req_code>=400 and req_code<500:
        return 'Unable to find location'
    else:
        return status_code

if __name__=='__main__':
    get_cord('miami')