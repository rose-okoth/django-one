from django.http  import HttpResponse,Http404
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

def past_days_quotes(request,past_date):
    try:
        # Converts data from the string Url
        date = dt.datetime.strptime(past_date,'%Y-%m-%d').date()

    except ValueError:
        # Raise 404 error when ValueError is thrown
        raise Http404()

    day = convert_dates(date)
    html = f'''
        <html>
            <body>
                <h1>Quotes for {day} {date.day}-{date.month}-{date.year}</h1>
            </body>
        </html>
            '''
    return HttpResponse(html)