from main.models import Year, State, Year, InstitutionDetails, Institution

def get_current_year(request):
    current_year = Year.objects.get(is_current_year=True)
    return {'current_year':current_year}