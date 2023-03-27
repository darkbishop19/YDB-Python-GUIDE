from connect import forecast
import pandas

scan = forecast.scan()
items = scan['Items']
data = pandas.DataFrame(items)
data.to_excel('output.xlsx', index=False)

