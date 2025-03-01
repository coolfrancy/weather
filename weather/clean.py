
def user_format(w_json):
    from .summary import weather_summary


    #gets important information from json
    main=w_json.get('main',False)
    temp=main.get('temp', False) if main else False
    temp_feel=main.get('feels_like', False) if main else False
    humid=main.get('humidity', False) if main else False


    weather=w_json.get('weather', False) 
    w_description=weather[0].get('description', False) if weather else False
    wind=w_json.get('wind', False)
    wind_speed=wind.get('speed', False) if wind else False
    wind_gust=wind.get('gust', False) if wind else False
    visible=w_json.get('visibility', False)
    ########

    #turns json info into phrases
    weather_str={
        'temp_str':f'Temperature: {temp}°k',
        'feel_temp_str':f'Feels like: {temp_feel}°k',
        'humid_str':f'Humidity: {humid}%',
        'wind_str':f'Wind: Wind speed of {wind_speed}m/s with gusts up to {wind_gust}m/s',
        'weather_str':f'Weather: {w_description}',
        'visibility_str':f'visibility: {visible}m'
        
    }
    

    formated_weather=[]
    for info in weather_str.values():
        if 'False' in info:
            continue
        else:
            formated_weather.append(info)
    
    #adds summary at the end
    conclusion = weather_summary(w_json=w_json,desc=w_description, temp=temp)
    formated_weather.append('<br>'+conclusion)


    return formated_weather


#this is for the whole of today
def multi_user_format(m_json):

    mdn=[]
    for tod, w_json in m_json.items():

        hours, minute=tod.split(':', 1)

        if int(hours)==21:
            tod_str='Night'
        elif int(hours)==9:
            tod_str='Morning'
        elif int(hours)==15:
            tod_str='Afternoon'
        else:
            continue
            
        mdn.append('<br>'+tod_str+'<br>'+'<br>'.join(user_format(w_json=w_json)))
    return '<br>'.join(mdn)



if __name__=='__main__':
    user_format(), multi_user_format()