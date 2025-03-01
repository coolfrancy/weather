
###forecast
#return dictionary for today and return list for forecast
def forecast(lat,lon):
    #imports
    import requests as rq
    from .api import api_weather
    import datetime as dt
    ###
    if type(lat) is float and type(lon) is float:
        r=rq.get(f'https://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={api_weather()}&cnt=40')
        req_code=r.status_code
        if req_code>=200 and req_code<300:
            json_info=r.json()
            #return weather information
            return json_info['list']
        elif req_code>=300 and req_code<400:
            raise TypeError('URL for the weather API has been changed')
        elif req_code>=400 and req_code<500:
            return 'Unable to find location'
        else:
            return req_code
    else:
        raise ValueError(f'Invalid lat or lon param, given Lon={lon}, Lat={lat}')


#parse the json to get your date
def parse(json, form):
    import datetime as dt


    if json==[]:
        return 'No information in json'

    #checks for today
    if form==dt.datetime.today().date():
        today_forecasts={}
        today=dt.datetime.today().date()

        for entry in json:
            date, time=entry['dt_txt'].split(' ')
            if date == str(today):
                today_forecasts[time]=entry

        return today_forecasts

    else:
        #checks for later dates
        for entry in json:
            if entry['dt_txt']==form:
                return entry 
        return f'couldnt find date in json {form}'

#gives you the next 5 days dates
def show_dates():
    import datetime as dt
    cur=dt.date.today()
    res=[cur]
    for num in range(1,5):
        res.append(cur+dt.timedelta(days=num))
    return res

if __name__=='__main__':
    forecast(25.7617,80.1918), show_dates()


#######

