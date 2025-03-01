def w_current(lat, lon):
    #imports
    import requests as rq
    from .api import api_weather
    ###
    if type(lat) is float and type(lon) is float:
        r=rq.get(f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_weather()}')
        req_code=r.status_code
        if req_code>=200 and req_code<300:
            json_info=r.json()
            #return weather information
            return json_info
        elif req_code>=300 and req_code<400:
            raise TypeError('URL for the weather API has been changed')
        elif req_code>=400 and req_code<500:
            return 'Unable to find location'
        else:
            return req_code
    else:
        raise ValueError(f'Invalid lat or lon param, given Lon={lon}, Lat={lat}')
