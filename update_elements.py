from connect import forecast

'''update 1 element'''
response = forecast.update_item(Key={'weather': 'rain',
                                     'number': '3'},
                                UpdateExpression='set temperature= :n',
                                ExpressionAttributeValues={
                                    ':n': "-10"
                                })

'''for updating several element use arrays'''