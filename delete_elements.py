from boto3.dynamodb.conditions import Key, Attr

from connect import forecast

# delete 1 item
# with forecast.batch_writer() as batch:
#     batch.delete_item(
#         Key={
#             'weather': 'rain',
#             'number': '10'
#         }
#     )


# delete all items with certain expression
# scan = forecast.scan(
#     FilterExpression=Attr('weather').eq('sunny')
# )
#
# #
# with forecast.batch_writer() as batch:
#     for each in scan['Items']:
#         if int(each['temperature']) < 0:
#             batch.delete_item(
#                 Key={
#                     'weather': each['weather'],
#                     'number': each['number']
#                 }
#             )

# delete all items
# scan = forecast.scan()
# with forecast.batch_writer() as batch:
#     for each in scan['Items']:
#         batch.delete_item(
#             Key={
#                 'weather': each['weather'],
#                 'number': each['number']
#             }
#         )
