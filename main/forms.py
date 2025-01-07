from django import forms
from main.models import Institution, InstitutionDetails, State, Year

class InstitutionForm(forms.ModelForm):
    

    class Meta:
        model = Institution
        fields = (
            'name',
            'address',
            'state',
            'pincode',       
        )
       

class InstitutionDetailForm(forms.ModelForm):
    def clean_res_students(self):
        res_students = self.cleaned_data['res_students']
        total_students = self.cleaned_data['total_students']
        if res_students > total_students:
            raise forms.ValidationError("طعام و قیام طلباء کل طلباء سے زیادہ نہیں ہو سکتے")
        return res_students
     
    class Meta:
        model= InstitutionDetails
        fields =[
                'year',
                'moh_name',
                'moh_phone', 
                'safir_name', 
                'safir_phone', 
                'safir_aadhar', 
                'taalim', 
                'total_students',
                'res_students',
                'total_teachers',
                'donation_day',
                'serial_no',
                'halka_code',
                'ijazat_status',
                'next_donation_year',
                'comments',
                'safir_photo',
        ]
        widgets = {
            'serial_no': forms.NumberInput(attrs={'readonly': 'readonly'})
        }

class StateForm(forms.ModelForm):
    class Meta:
        model = State
        fields = (
            
            'name',    
        )

class YearForm(forms.ModelForm):
    class Meta:
        model = Year
        fields = (
            'english',
            'hijri',
            'is_current_year'
        )
        widgets = {
            'is_current_year': forms.CheckboxInput()
        }
    