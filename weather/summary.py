def gpt_summary(weather):
    #imports
    import os
    import sys
    from openai import OpenAI
    from dotenv import load_dotenv
    load_dotenv()
    ###
    api_gpt=os.getenv('api_gpt')
    
    client = OpenAI(api_key=api_gpt)
    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        store=True,
        messages=[
            {"role": "user", "content": f"{weather}what kind of day will it be? finish this line 'it will be a' don't quote your response, dont mention place name."}
        ]
    )

    res_sum=completion.to_dict()['choices'][0]['message']['content']
    return res_sum

def weather_summary(w_json,desc='', temp=''):
    phrase={
        'description':f'Expect {desc}',
        'temperature':f'with temperature at {round(temp-273.15, 2)}°C or {round((temp-273.15)*9/5+32, 2)}°F'
    }

    gpt_responce=gpt_summary(w_json)

    return phrase['description']+' '+phrase['temperature']+' '+gpt_responce


if __name__=='__main__':
    weather_summary()
    gpt_summary()