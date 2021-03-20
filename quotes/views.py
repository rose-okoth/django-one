from django.http  import HttpResponse
import datetime as dt

# Create your views here.
def welcome(request):
    return HttpResponse('Welcome to the Quotes Nation')

def quote_of_day(request):
    date = dt.date.today()

    # Function for converting dates to find exact day.
    day = convert_dates(date)

    html = f'''
        <html>
            <body>
                <h1> Quote for {day} {date.day}-{date.month}-{date.year}</h1>
            </body>
        </html>
            '''
    return HttpResponse(html) 

def convert_dates(dates):

    # Function that gets the weekday number for the date.
    day_number = dt.date.weekday(dates)

    days = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday',"Sunday"]

    # Returning the actual day of the week.
    day = days[day_number]
    return day