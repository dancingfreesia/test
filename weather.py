from darksky import forecast
from datetime import date, timedelta

SHANGHAI = 31.2206, 121.6342

weekday = date.today()
with forecast('fd725930535286827feb2f596bb8c3d7', *SHANGHAI) as shanghai:
    print(shanghai.daily.summary)
    print("------------")
    for day in shanghai.daily:
        day = dict(day = date.strftime(weekday, '%a'),
                sum = day.summary,
                tempMin = day.temperatureMin,
                tempMax = day.temperatureMax
                )
        print('{day}: {sum} Temp range: {tempMin} - {tempMax}'.format(**day))
        weekday += timedelta(days=1)
