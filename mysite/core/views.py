from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect, get_object_or_404

from mysite.core.forms import SignUpForm, SignUpFormag, AllocatingForm
from .models import Book, Profiles, Orphanagedetails
from .forms import BookForm, OrphanForm


@login_required
def home(request, template_name='waste_list.html'):
    book = Book.objects.filter(user=request.user)
    data={}
    data['object_list'] = book
    return render(request, template_name, data)

@login_required
def orphangaedets(request, template_name='orp_det.html'):
    orph = Orphanagedetails.objects.all()
    data = {}
    data['obj_list'] = orph
    return render(request, template_name, data)

@login_required
def addnew(request, template_name='book_form.html'):
    form = BookForm(request.POST or None, request.FILES)
    if form.is_valid():
        book = form.save(commit=False)
        book.user = request.user
        book.save()
        return redirect('home')
    return render(request, template_name, {'form':form})

@login_required
def addorphan(request, template_name='orph_add_form.html'):
    form = OrphanForm(request.POST or None)
    if form.is_valid():
        book = form.save(commit=False)
        book.user = request.user
        book.save()
        return redirect('orphanagedet')
    return render(request, template_name, {'form':form})

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()  # load the profile instance created by the signal
            user.profile.birth_date = form.cleaned_data.get('birth_date')
            user.profile.usertype = form.cleaned_data.get('usertype')
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect('login')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

def signupag(request):
    if request.method == 'POST':
        form = SignUpFormag(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()  # load the profile instance created by the signal
            user.profile.birth_date = form.cleaned_data.get('birth_date')
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect('login')
    else:
        form = SignUpFormag()
    return render(request, 'signup.html', {'form': form})

def archi(request):
    render(request,'architecture.html',{})
	
@login_required
def updates(request, pk, template_name='book_form_update.html'):
    if request.user.is_superuser:
        book= get_object_or_404(Book, pk=pk)
    else:
        book= get_object_or_404(Book, pk=pk, user=request.user)
    form = BookForm(request.POST or None, request.FILES, instance=book)
    if form.is_valid():
        form.save()
        return redirect('home')
    return render(request, template_name, {'form':form})

@login_required
def deletes(request, pk, template_name='book_confirm_delete.html'):
    if request.user.is_superuser:
        book= get_object_or_404(Book, pk=pk)
    else:
        book= get_object_or_404(Book, pk=pk, user=request.user)
    if request.method=='POST':
        book.delete()
        return redirect('home')
    return render(request, template_name, {'object':book})

@login_required
def updateorp(request, pk, template_name='orp_form.html'):
    if request.user.is_superuser:
        orpd = get_object_or_404(Orphanagedetails, pk=pk)
    else:
        orpd = get_object_or_404(Orphanagedetails, pk=pk)
    form = OrphanForm(request.POST or None, instance=orpd)
    if form.is_valid():
        form.save()
        return redirect('orphanagedet')
    return render(request, template_name, {'form':form})

@login_required
def deleteorp(request, pk, template_name='orp_confirm_delete.html'):
     if request.user.is_superuser:
        orpd=get_object_or_404(Orphanagedetails, pk=pk)
     else:
        orpd = get_object_or_404(Orphanagedetails, pk=pk)
     if request.method=='POST':
        orpd.delete()
        return redirect('orphanagedet')
     return render(request, template_name, {'object':orpd})
	 
	 
@login_required
def allocatedet(request, pk, template_name='allocate.html'):
    bk=get_object_or_404(Book, pk=pk)
    bks=Book.objects.get(pk=pk)
    orph = Orphanagedetails.objects.values('oname')
    form = AllocatingForm(request.POST or None, instance=bk)
    if form.is_valid():
        form.save()
        return redirect('home')
    return render(request, template_name, {'form':form})

@login_required
def chartsview(request, chart_type, cha_type):
    if cha_type == 'weight':
        book = Book.objects.all()
    elif cha_type == 'totppl':
        book = Orphanagedetails.objects.all()
    data = {}
    data['book_obj'] = book
    data['chart_type'] = chart_type
    data['cha_obj'] = cha_type
    return render(request, 'chart.html', data)