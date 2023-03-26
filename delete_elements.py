from connect import forecast

# delete 1 Item
with forecast.batch_writer() as batch:
    batch.delete_item(
        Key={
            'weather': 'rain',
            'number': '10'
        }
    )
