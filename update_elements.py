from connect import forecast

response = forecast.update_item(Key={'weather': 'rain',
                                     'number': '3'},
                                UpdateExpression='set temperature= :n',
                                ExpressionAttributeValues={
                                    ':n': "-10"
                                })
