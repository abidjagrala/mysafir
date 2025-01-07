import django_filters 
from django import forms
from main.models import InstitutionDetails, Year

# class InstitutionFilter(django_filters.FilterSet):
#     year = django_filters.ModelMultipleChoiceFilter(
#         queryset=Year.objects.all(),
#         widget=forms.CheckboxSelectMultiple(),
#     )

#     class Meta:
#         model = InstitutionDetails
#         fields = ("year", )

class InstitutionFilter(django_filters.FilterSet):
    years = Year.objects.all()
    year = django_filters.ModelChoiceFilter(queryset=years, empty_label='All',)
    donation_day = django_filters.NumberFilter()
    moh_phone = django_filters.NumberFilter()
    safir_phone = django_filters.NumberFilter()
    safir_aadhar = django_filters.NumberFilter()
    institution_id = django_filters.NumberFilter()




    class Meta:
        model = InstitutionDetails
        fields = ('year', 'donation_day', 'moh_phone', 'safir_phone', 'safir_aadhar', 'institution_id')