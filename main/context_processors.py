from .models import*

def conutries(request):
    countries = Country.objects.all()[:12]
    l = len(countries)
    return {
        'countries_left': countries[:l // 2],
        'countries_right': countries[l // 2:],
            }