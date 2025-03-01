from get_cord import get_cord
from get_forecast import forecast

place=input('where would you like to search ')
future=input('how far would you like to see ')

cord=get_cord(place)
w_json=(forecast(lon=cord[0],lat=cord[1],ahead=future))

#gets important information from jason
main=w_json.get('main',False)
temp=main.get('temp', False) if main else False
temp_feel=main.get('feels_like', False) if main else False
humid=main.get('humidity', False) if main else False


weather=w_json.get('weather', False) 
w_description=weather[0]('description', False) if weather else False
wind=w_json.get('wind', False)
wind_speed=wind.get('speed', False) if wind else False
wind_gust=wind.get('gust', False) if wnd else False
visible=w_json('visibility', False)
########


#for the temp
print(f'Temperature: {temp}k with a feels like temperature of {temp_feel}k')
print(f'Weather: {w_description}')
print(f'Wind: Wind speed of {wind_speed} with gusts up to {wind_gust}')
print(f'visibility of {visible}')

#addchatgpt summary






