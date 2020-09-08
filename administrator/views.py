from datetime import date
from decimal import Decimal

from django.shortcuts import render, HttpResponseRedirect, get_object_or_404, HttpResponse
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from .forms import StaffForm, DrugForm
from staffAuth.models import Staff, Role
from .models import Logs, Drug, Sales
from .helpers import generate_ID, send_to_staff, create_log_entry
from .decorators import admin_user_required

# Create your views here.
@login_required
@admin_user_required
def add_staff(request):
    form = StaffForm()
    if request.method == 'POST':
        form = StaffForm(request.POST)
        if form.is_valid():
            # generate staff ID
            staff_ID = generate_ID()
            email = form.cleaned_data['email']
            password = form.cleaned_data['def_password']
            staff = Staff.objects.create_user(email, staff_ID, password)

            # staff Profile automatically created, thanks to signals
            # update profile now
            staff.profile.firstname = form.cleaned_data['firstname']
            staff.profile.lastname = form.cleaned_data['lastname']
            staff.profile.telephone = form.cleaned_data['telephone']
            staff.profile.date_of_birth = form.cleaned_data['date_of_birth']
            staff.profile.role = form.cleaned_data['role']
            staff.save()
            
            # send staff ID and password to staff's mail
            send_to_staff(staff_ID, password, email)
            create_log_entry(request.user.profile.full_name(), f'added staff - {staff.profile.full_name()}')
            return HttpResponseRedirect(reverse('administrator:all_staff'))
        else:
            # show error message
            pass
    return render(request, 'administrator/add_staff.html', {
        'form': form
    })

@login_required
@admin_user_required
def update_staff(request, staff_id):
    staff = Staff.objects.get(id=staff_id)
    roles = Role.objects.all()
    if request.method == 'POST':
        new_role = Role.objects.get(name=request.POST['role'])
        staff.email = request.POST['email']
        staff.profile.firstname = request.POST['firstname']
        staff.profile.lastname = request.POST['lastname']
        staff.profile.telephone = request.POST['telephone']
        staff.profile.role = new_role
        staff.save()
        create_log_entry(request.user.profile.full_name(), f'updated staff - {staff.profile.full_name()}')
        return HttpResponseRedirect(reverse('administrator:all_staff'))
    return render(request, 'administrator/update_staff.html', {
        'staff': staff,
        'roles': roles
        })

@login_required
@admin_user_required
def all_staff(request):
    all_staff = Staff.objects.all()
    return render(request, 'administrator/view_users.html', {
        'all_staff': all_staff
    })

@login_required
@admin_user_required
def logs(request):
    logs = Logs.objects.all()
    return render(request, 'administrator/logs.html', {
        'logs': logs
    })

@login_required
@admin_user_required
def add_drug(request):
    form = DrugForm()
    success = False
    if request.method == 'POST':
        form = DrugForm(request.POST)
        if form.is_valid():
            # create drug
            name = request.POST['name']
            desc = request.POST['description']
            price = request.POST['price']
            qty_left = request.POST['qty_in_stock']
            drug = Drug(name=name, description=desc, price=price, qty_in_stock=qty_left)
            drug.save()
            create_log_entry(request.user.profile.full_name(), f'added drug {drug.name}')
            success = True
            return HttpResponseRedirect(reverse('administrator:add_drug'))
        else:
            # error message
            pass
    return render(request, 'administrator/add_drug.html', {'form': form, 'success': success})

@login_required
def all_drugs(request):
    drugs = Drug.objects.all()
    return render(request, 'administrator/view_drugs.html', {
        'drugs': drugs
    })

@login_required
def update_drug(request, drug_name):
    drug = Drug.objects.get(name=drug_name)
    form = DrugForm(instance=drug)
    if request.method == 'POST':
        form = DrugForm(request.POST, instance=drug)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('administrator:all_drugs'))
    return render(request, 'administrator/update_drug.html', {
        'form': form
    })


@login_required
def sell(request):
    searchItem = request.GET['searchItem']
    drugs = Drug.objects.filter(name__contains=searchItem)

    if request.method == 'POST':
        drug_name = request.POST['drug']
        drug = Drug.objects.get(name=drug_name)
        selling_price = request.POST['s_price']
        seller = request.user
        qty_sold = request.POST['p_qty']
        sales = Sales(drug=drug, selling_price=selling_price, seller=seller, qty_sold=qty_sold)
        sales.save()

        # update drug
        drug.qty_in_stock = int(drug.qty_in_stock) - int(qty_sold)
        drug.save()
    return render(request, 'administrator/index.html', {'drugs': drugs})

def sales_today(request):
    today = date.today()
    all_sales = Sales.objects.filter(period=today)
    total_sales = all_sales.values('selling_price')
    total_quantities = all_sales.values('qty_sold')

    total_price = 0
    # sales
    for i in total_sales:
        total_price += i['selling_price']

    # qty
    total_qty = 0
    for i in total_quantities:
        total_qty += i['qty_sold']

    return render(request, 'administrator/sales_today.html', {
        'all_sales': all_sales,
        'today': today,
        'total_price': total_price,
        'total_qty': total_qty
    })