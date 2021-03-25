from django.shortcuts import render, redirect
from django.http  import HttpResponse,Http404
import datetime as dt
from .models import Post,tags
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required

# Create your views here.
def welcome(request):
    all_quote = Post.objects.all()
    return render(request, 'welcome.html')

def quote_of_day(request):
    date = dt.date.today()
    quotes = Post.todays_quotes()
    return render(request, 'all-quotes/today-quotes.html', {'date':date,'quotes':quotes})

def convert_dates(dates):

    # Function that gets the weekday number for the date.
    day_number = dt.date.weekday(dates)

    days = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']

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
        assert False

    if date == dt.date.today():
        return redirect(quote_of_day)

    quotes = Post.days_quotes(date)
    return render(request, 'all-quotes/past-quotes.html', {'date': date,'quotes':quotes})

def search_results(request):

    if 'post' in request.GET and request.GET["post"]:
        search_term = request.GET.get("post")
        searched_posts = Post.search_by_title(search_term)
        message = f"{search_term}"

        return render(request, 'all-quotes/search.html',{"message":message,"posts": searched_posts})

    else:
        message = "You haven't searched for any term"
        return render(request, 'all-quotes/search.html',{"message":message})

@login_required(login_url='/accounts/login/')
def post(request,post_id):
    try:
        post = Post.objects.get(id = post_id)
    except DoesNotExist:
        raise Http404()
    return render(request,"all-quotes/post.html", {"post":post})