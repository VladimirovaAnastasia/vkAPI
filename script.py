import requests
import datetime
import plotly.graph_objects as go

url = 'https://api.vk.com/method/newsfeed.search'

current_day = datetime.datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)

total_count = []
days = []

period = 7
your_query = "Coca-Cola"
your_vk_key = "Введите ваш API ключ"

for item in range(period):
    prev_day = current_day - datetime.timedelta(
        days=1,
        hours=current_day.minute,
        minutes=current_day.minute,
        seconds=current_day.second,
        microseconds=current_day.microsecond)

    payload = {"q": your_query,
               "start_time": prev_day.timestamp(),
               "end_time": current_day.timestamp(),
               "access_token": your_vk_key,
               "v": "5.103"}

    response = requests.get(url, params=payload)
    data = response.json()
    days.append(prev_day.date())
    total_count.append(data['response']['total_count'])

    current_day = prev_day


fig = go.Figure([go.Bar(x=days, y=total_count)])
fig.show()
