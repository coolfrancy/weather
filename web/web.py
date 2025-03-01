from flask import Flask, render_template, request
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '/workspaces/weather/')))

from weather.get_cord import get_cord
from weather.get_forecast import show_dates, forecast, parse
from weather.clean import user_format, multi_user_format
from weather.cur_weather import w_current


app=Flask(__name__)
#calculates th next 5 days dates
days=show_dates()

@app.route('/')
def home():
    return render_template('home.html')

#looks for future forecast.
@app.route('/future', methods=['post'])
def future():
    return render_template('future.html'
    ,d_2=days[1],
    d_3=days[2],
    d_4=days[3])


@app.route('/future-search', methods=['post'])
def search():
    #get information back from user
    location=request.form.get('Location')
    date_num=request.form.get('numbers')
    tod=request.form.get('days')
    location_cord=get_cord(location)
    #get the forecast
    res=forecast(lat=location_cord[0],lon=location_cord[1])

    #time of day dctionary
    tod_dic={
        'morning':'09:00:00',
        'afternoon':'15:00:00',
        'night':'21:00:00'
    }
    # parse through to get your date weather
    form=f'{days[int(date_num)]} {tod_dic[tod.lower()]}'
    w_json=parse(res, form)

    formated_list= user_format(w_json=w_json)
    return location+'<br>'+'<br>'+('<br>').join(formated_list)
 
###
#looks for todays weather
@app.route("/today", methods=['post'])
def today():
    return render_template('today.html')

@app.route("/today_weather", methods=['POST'])
def today_search():
    place=request.form.get('Location')
    lat, lon=get_cord(place)
    #gives you the forecasts for today
    today_forecasts=forecast(lat, lon)
    #gives you the current weather
    today_weather=w_current(lat, lon)
    formated_list= user_format(w_json=today_weather)
    
    tod_weather_list=parse(today_forecasts, days[0])


    final = place+'<br>'+'<br>'+'Now'+'<br>'+('<br>').join(formated_list)+'<br>'+'<br>'+ multi_user_format(m_json=tod_weather_list)
    return final

   

if __name__ == '__main__':
    app.run(debug=True, port=5000)