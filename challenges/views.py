from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

monthly_challenges = {
    "january": "Read at least one book this month!",
    "february": "Try a new recipe every week!",
    "march": "Do 10 minutes of meditation daily!",
    "april": "Spend 30 minutes a day learning a new language!",
    "may": "Do 25 push-ups daily!",
    "june": "Write in a journal every day!",
    "july": "Practice a new hobby for at least 30 minutes daily!",
    "august": "Drink at least 8 cups of water every day!",
    "september": "Declutter one area of your home each day!",
    "october": "Avoid sugary snacks for the entire month!",
    "november": "Compliment at least one person every day!",
    "december": "Practice gratitude by listing three things you're thankful for daily!"
}

# Create your views here.


def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())

    if month > len(months):
        return HttpResponseNotFound("Invalid month")

    redirect_month = months[month - 1]
    redirect_path = reverse("month-challenge", args=[redirect_month]) # /challenge/january
    return HttpResponseRedirect(redirect_path)


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return HttpResponse(challenge_text)
    except:
        return HttpResponseNotFound("This month is not supported!")
