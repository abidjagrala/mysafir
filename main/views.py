from django.shortcuts import render, get_object_or_404, redirect
from main.models import Institution, InstitutionDetails, User, State, Year
from main.filters import InstitutionFilter
from main.forms import InstitutionForm, InstitutionDetailForm, StateForm, YearForm
import os
from django.conf import settings
from django.views.decorators.http import require_POST
from django_htmx.http import retarget
from django.core.paginator import Paginator
# Create your views here.   
def dashboard(request):
    return render(request, 'main/dashboard.html')

def institutionList(request):
    institution_filter= InstitutionFilter(
        request.GET,
        queryset=InstitutionDetails.objects.select_related().all().order_by('-id')
    )
    paginator = Paginator(institution_filter.qs, settings.PAGE_SIZE)
    total_records=Institution.objects.count()
    filter_records=institution_filter.qs.count()
   
    institution_page = paginator.page(1)
    context = {
        'institutions': institution_page,
        'filter': institution_filter,
        'total_records': total_records,
        'filter_records': filter_records,
        
        }
    if request.htmx:
        return render(request, 'main/partials/institution-container.html', context)
    return render(request, 'main/institution-list.html', context)

def getInstitutions(request):
    page = request.GET.get('page', 1)
    institution_filter= InstitutionFilter(
        request.GET,
        queryset=InstitutionDetails.objects.select_related().all().order_by('-id')
    )
    paginator = Paginator(institution_filter.qs, settings.PAGE_SIZE)
    context = {
        'institutions': paginator.page(page)
    }
    return render(
        request,
        'main/partials/institution-container.html#institution_list',
        context
    )

def printInstitutionList(request):
    
   
    
    institution_filter= InstitutionFilter(
        request.GET,
        queryset=InstitutionDetails.objects.select_related().all().order_by('-id')
    )
    # paginator = Paginator(institution_filter.qs, settings.PAGE_SIZE)
    filter_records=institution_filter.qs.count()
    # institution_page = paginator.page(1)
    
    if request.GET['donation_day']  and request.GET['year']:
        donation_day = request.GET.get('donation_day')
        year = Year.objects.get(pk=request.GET.get('year'))
        context = {
            'institutions': institution_filter.qs,
            # 'filter': institution_filter,
            'filter_records': filter_records, 
            'donation_day': donation_day,
            'year': year,
            }
        return render(request, 'main/print-institution-list.html', context)
    context = {
        # 'institutions': institution_page,
        'filter': institution_filter,
        'filter_records': filter_records,
        'message': 'Please select donation day and year to print list'
        }
    return render(request, 'main/institution-list.html', context)

def addInstitution(request):
   
    if request.method == 'POST':
        institution_form = InstitutionForm(request.POST)
        institution_detail_form = InstitutionDetailForm(request.POST, request.FILES)
        if institution_form.is_valid() and institution_detail_form.is_valid():
            institution = institution_form.save()
            institution_detail = institution_detail_form.save(commit=False)
            institution_detail.institution = institution

            photo = request.FILES.get('photo')
            if photo:
                file_path = os.path.join('photos', photo.name)
                final_path = os.path.join(settings.MEDIA_ROOT, file_path)

                with open(final_path, 'wb+') as destination:
                    for chunk in photo.chunks():
                        destination.write(chunk)
                institution_detail.photo = file_path

            institution_detail.save()
            context = {'message': "Institution was added successfully!"}
            return render(request, 'main/partials/institution-success.html', context)
        else:
            print('not valid')
            print(institution_form.errors)
            context = {'iform': institution_form, 'message': "Institution was not added successfully!"}
            # return render(request, 'main/partials/institution-success.html', context)
            response = render(request, 'main/partials/add-institution.html', context)
            return retarget(response, '#institution-container')
        
    context = {
        'iform': InstitutionForm,
        'idform': InstitutionDetailForm,
        
    }
    # return render(request, 'main/partials/add-institution.html', context)
    if request.headers.get('HX-Request') == 'true':
            return render(request,'main/partials/add-institution.html',context)
    else:
           return redirect('institution-list')
    endif 


def maxSerial(request):
    print(request.POST.get('donation_day'))
    donation_day = request.POST.get('donation_day')
    find_max_serial = InstitutionDetails.objects.filter(donation_day=donation_day).order_by('-serial_no').first()
    if find_max_serial is None:
        context = {'idform': InstitutionDetailForm()}  # Pass the form to the context
        return render(request, 'main/partials/serial-number.html', context)  # Update the path accordingly
    max_serial = int(find_max_serial.serial_no)+1
    
    print(max_serial)
    context = {'idform': InstitutionDetailForm(initial={'serial_no': max_serial})}  # Pass the max_serial to the form if needed
    return render(request, 'main/partials/serial-number.html', context)  # Update the path accordingly
    
    
        
   

def addNextYearDetails(request, pk):
    institution = get_object_or_404(Institution, pk=pk)
    idetail = InstitutionDetails.objects.filter(institution=institution).order_by('-id').first()
    idetail.pk = None
    idetail.year = Year.objects.get(pk=idetail.year_id+1)
    if request.method == 'POST':
        institution_detail_form = InstitutionDetailForm(request.POST, request.FILES)
        if institution_detail_form.is_valid():
            
            institution_detail = institution_detail_form.save(commit=False)
            institution_detail.institution = institution

            photo = request.FILES.get('photo')
            if photo:
                file_path = os.path.join('photos', photo.name)
                final_path = os.path.join(settings.MEDIA_ROOT, file_path)

                with open(final_path, 'wb+') as destination:
                    for chunk in photo.chunks():
                        destination.write(chunk)
                institution_detail.photo = file_path
            else:
                institution_detail.safir_photo = idetail.safir_photo
            institution_detail.save()
            context = {'message': "Institution Details was added successfully!"}
            return render(request, 'main/partials/institution-success.html', context)
        else:
            print('not valid')
            
        
    context = {
        'institution': institution,
        'idetail': idetail,
        'idform' : InstitutionDetailForm(instance=idetail)
        }
    # return render(request, 'main/partials/add-next-year-details.html', context)
    if request.headers.get('HX-Request') == 'true':
            return render(request,'main/partials/add-next-year-details.html',context)
    else:
           return redirect('institution-list')
    endif 


    
def viewInstitution(request, pk):
    institution = get_object_or_404(Institution, pk=pk)
    institution_detail = InstitutionDetails.objects.filter(institution=institution).order_by('-id').all()
    context = {'institution': institution, 'idetail': institution_detail}   
   
    
    # return render(request, 'main/partials/view-institution.html', context)
    if request.headers.get('HX-Request') == 'true':
            return render(request,'main/partials/view-institution.html',context)
    else:
           return redirect('institution-list')
    endif    

def editInstitution(request, pk):
    institution_detail = get_object_or_404(InstitutionDetails, pk=pk)
    institution = get_object_or_404(Institution, pk=institution_detail.institution_id)
    
    
    # print(institution.name)
    institution_form = InstitutionForm(instance=institution)
    institution_detail_form = InstitutionDetailForm(instance=institution_detail)   
    if request.method == 'POST':
        
        institution_form = InstitutionForm(request.POST, instance=institution)
        institution_detail_form = InstitutionDetailForm(request.POST, request.FILES, instance=institution_detail)
        # print(institution_detail_form.errors)
        if institution_form.is_valid() and institution_detail_form.is_valid():
            print('valid')
            institution = institution_form.save()
            institution_detail = institution_detail_form.save(commit=False)

            # Handle new photo if uploaded
            photo = request.FILES.get('photo')
            if photo:
                 # Delete the old file if exists
                if institution_detail.photo:
                   old_file_path = os.path.join(settings.MEDIA_ROOT, institution_detail.photo)
                   if os.path.exists(old_file_path):
                       os.remove(old_file_path)
                # Construct new file path and save
                file_path = os.path.join('photos', photo.name)
                final_path = os.path.join(settings.MEDIA_ROOT, file_path)
                
                with open(final_path, 'wb+') as destination:
                    for chunk in photo.chunks():
                         destination.write(chunk)
                institution_detail.photo = file_path

            institution_detail.save()
            context = {'message': "ادارے کی تفصیلات تبدیل کر دی گئیں۔"}
            return render(request, 'main/partials/institution-success.html', context) # Redirect after successful update
        else:
            # print(institution_detail_form.errors)
            context={
                'iform': institution_form,
                'idform': institution_detail_form,
                'idetail': institution_detail,
                'message': 'Resident students can&#x27;t be more than total students',
            }
            # response = render(request, 'main/partials/edit-institution.html', context)
            # return retarget(response, '#institution-container')
           
          
            # context = {'message': "Insitution updated fail!"}
            return render(request, 'main/partials/institution-fail.html', context)
       
    context = {
        'iform': institution_form,
        'idform': institution_detail_form,
        'idetail': institution_detail,
        'institution': institution,
    }
    # return render(request, 'main/partials/edit-institution.html', context)
    if request.headers.get('HX-Request') == 'true':
            return render(request,'main/partials/edit-institution.html',context)
    else:
           return redirect('institution-list')
    endif    
    
def institutionSettings(request):
    states = State.objects.all().order_by('-id')
    years = Year.objects.all()

    context={
        'states': states,
        'years': years,
        'stateform' : StateForm,
        'yearform' : YearForm,
    }
    return render(request, 'main/institution-settings.html', context)

def addState(request):
    states = State.objects.all().order_by('-id')
    state_form = StateForm(request.POST)
    if state_form.is_valid():
        state_form.save()
        context = {'message': "State was added successfully!", 'states': states, 'stateform' : state_form}
        response = render(request, 'main/partials/state-list.html', context)
        return retarget(response, '#stateblock')
    else:
        context = {'message': "State was not added successfully!", 'states': states, 'stateform' : state_form}
        response = render(request, 'main/partials/state-list.html', context)
        return retarget(response, '#stateblock')

def editState(request, pk):
    states = State.objects.all().order_by('-id')
    years = Year.objects.all()
    state = get_object_or_404(State, pk=pk)
    
    state_form = StateForm(instance=state)
    # print(state_form)
    if request.method == 'POST':
        state_form = StateForm(request.POST, instance=state)
        if state_form.is_valid():
            print('valid')
            state_form.save()
            context = {
                'message': "State was updated successfully!",
                'states': states,
                'years': years,
                'stateform' : StateForm,
                }
            response = render(request, 'main/partials/state-list.html', context)
            return retarget(response, '#stateblock')
        else:
            print('not valid')
            context = {
                'message': "State was not updated successfully!",
                'states': states,
                'years': years,
                'stateform' : StateForm,
                
                }
            response = render(request, 'main/partials/state-list.html', context)
            return retarget(response, '#stateblock')
    context = {
        'stateform': state_form,
        'state_id': pk,
        }
    # return render(request, 'main/partials/edit-state-form.html', context)
    if request.headers.get('HX-Request') == 'true':
            return render(request,'main/partials/edit-state-form.html',context)
    else:
           return redirect('institution-settings')
    endif 

def addYear(request):
    years = Year.objects.all()
    year_form = YearForm(request.POST)
    if year_form.is_valid():
        if request.POST['is_current_year']=='on':
            year_form.save(commit=False)
            updated=Year.objects.filter(is_current_year=True).update(is_current_year=False)
            print(updated)
            year_form.save()
        else:
            year_form.save()
            year_form = YearForm()  # Reinitialize the form to be blank
            context = {'message': "Year was added successfully!", 'years': years, 'yearform' : year_form}
            response = render(request, 'main/partials/year-list.html', context)
            return retarget(response, '#yearblock')
    else:
        context = {'message': "Year was not added successfully!", 'years': years, 'yearform' : year_form}
        response = render(request, 'main/partials/year-list.html', context)
        return retarget(response, '#yearblock')

def editYear(request, pk):
    states = State.objects.all().order_by('-id')
    years = Year.objects.all()
    year = get_object_or_404(Year, pk=pk)
    year_form = YearForm(instance=year)
   
    if request.method == 'POST':
        year_form = YearForm(request.POST, instance=year)
        if year_form.is_valid():
           
            if request.POST['is_current_year']=='on':
                year_form.save(commit=False)
                updated=Year.objects.filter(is_current_year=True).update(is_current_year=False)
                print(updated)
                year_form.save()
            else:
                year_form.save()
            context = {
                'message': "Year was updated successfully!",
                'years': years,
                'states': states,
                'yearform' : YearForm,
                }
            response = render(request, 'main/partials/year-list.html', context)
            return retarget(response, '#yearblock')
        else:
            context = {
                'message': "Year was not updated successfully!",
                'years': years,
                'yearform' : YearForm,
                }
            response = render(request, 'main/partials/year-list.html', context)
            return retarget(response, '#yearblock')
    context = {
        'yearform': year_form,
        'year_id': pk,
        }
    # return render(request, 'main/partials/edit-year-form.html', context)
    if request.headers.get('HX-Request') == 'true':
            return render(request,'main/partials/edit-year-form.html',context)
    else:
           return redirect('institution-settings')
    endif 