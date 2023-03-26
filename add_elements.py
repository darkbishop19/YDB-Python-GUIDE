from datetime import date, datetime, timedelta

from connect import forecast

# add 1 element
#
# response = forecast.put_item(
#     Item = {
#         'weather': "rain",
#         'number': "1",
#         'date': f"{date.today()}",
#         'temperature': "10",
#         'time': f'{datetime.now().strftime("%H:%M:%S")}'
#     }
# )



#add 1 element with row data

# response = forecast.put_item(
#     Item = {
#         'weather': "rain",
#         'number': "2",
#         'data': f"{date.today()+timedelta(days=1)}",
#         'temperature': "0",
#         'time': f'{datetime.now().strftime("%H:%M:%S")}',
#         'feels': "cold"
#     }
# )


# add several elements
#
# Items = [
#     {
#         'weather': "rain",
#         'number': "3",
#         'data': f"{date.today()+timedelta(days=2)}",
#         'temperature': "-3",
#         'time': f'{datetime.now().strftime("%H:%M:%S")}'
#     },
#     {
#         'weather': "neutral",
#         'number': "4",
#         'data': f"{date.today()+timedelta(days=3)}",
#         'temperature': "0",
#         'time': f'{datetime.now().strftime("%H:%M:%S")}'
#     },
#     {
#         'weather': "rain",
#         'number': "5",
#         'data': f"{date.today()+timedelta(days=4)}",
#         'temperature': "4",
#         'time': f'{datetime.now().strftime("%H:%M:%S")}'
#     },
#     {
#         'weather': "sunny",
#         'number': "6",
#         'data': f"{date.today()+timedelta(days=5)}",
#         'temperature': "11",
#         'time': f'{datetime.now().strftime("%H:%M:%S")}'
#     },
#     {
#         'weather': "sunny",
#         'number': "7",
#         'data': f"{date.today()+timedelta(days=6)}",
#         'temperature': "12",
#         'time': f'{datetime.now().strftime("%H:%M:%S")}'
#     },
# ]
#
# for i in Items:
#     response = forecast.put_item(
#         Item={
#             'weather': i['weather'],
#             'number': i['number'],
#             'data': i['data'],
#             'temperature': i['temperature'],
#             'time': i["time"]
#         }
#     )


print(datetime.now().strftime("%H:%M:%S"))
print(date.today())
print(date.today()+timedelta(days=1))
