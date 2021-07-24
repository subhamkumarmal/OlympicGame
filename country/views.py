from django.shortcuts import render
from django.http import HttpResponse
from .models import CountryGame

# Create your views here.
def country(request):

    countries=CountryGame.objects.all()
    print(countries[0].country_flag)
    params={"countries":countries}
    return render(request,"country/index.html",params)

def countryDetails(request):
    return render(request,'country/addCountry.html')

def postDetails(request):
    obj=CountryGame()
    obj.country_name =request.POST.get('countryname')
    obj.country_represnt=request.POST.get('countryrepresent')
    obj.country_noTeams=request.POST.get('noteams')
    obj.country_flag="country/images"+request.POST.get('img')
    obj.save()
    return HttpResponse("your from has been submited successfully...")
