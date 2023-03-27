from boto3.dynamodb.conditions import Attr

from connect import forecast

'''get items with some expressions'''
scan = forecast.scan(
    FilterExpression = Attr('weather').contains('sunny') and Attr('temperature').eq('11')
)

'''
Описание функция после Attr: 
eq - equls | ne - not equal | le - less than or equal | lt - less than | ge - greater than or equal
| gt - greater than | not_null - not null | null - null  | contains -  Checks for a subsequence, or value in a set. 
| not_contains - Checks for absence of a subsequence, or absence of a value in a set.
| begin_with - check for a prefix (как у string )
| in - Checks for matching elements in a list.
| between - Greater than or equal to the first value, and less than or equal to the second value
'''

print(scan['Items'])