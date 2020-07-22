from django.contrib.auth import login 
from django.shortcuts import redirect
from django.views.generic import CreateView
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.db.models import Count

from ..decorators import business_required
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator

from ..forms import BusinessSignUpForm

from django.contrib.auth.forms import UserCreationForm
from ..models import User
from django.contrib.auth import get_user_model
User = get_user_model()
#from django.contrib.auth.models import User
#from ..forms import BusinessSignUpForm

'''
from ..forms import BusinessSignUpForm, CompanyPerks

from django.contrib.auth import get_user_model
User = get_user_model()


class BusinessSignupView(CreateView):
    model = User
    form_class = BusinessSignUpForm
    template_name = 'registration/businessSignUpForm.html'
    #find out what this reverse_lazy is 
    #success_url = reverse_lazy('')

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'business'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('business:dashboard')
'''
@login_required
def index(request):
    return render(request,'SimpactApp/index.html')
def sign_up(request):
    context = {}
    form = BusinessSignUpForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            user = form.save()
            login(request,user)
            return render(request,'SimpactApp/index.htmll')
    context['form']=form
    return render(request,'businesslogin.html',context)

'''
@login_required
def index(request):
    return render(request,'SimpactApp/index.html')
def sign_up(request):
    if request.method == "POST":
        form = BusinessSignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = None
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(password=raw_password)
            login(request, user)
            return redirect('index.html')
        else:
            form = BusinessSignUpForm()
        return render(request, 'businesslogin.html', {'form': form})
'''

'''
@method_decorator([login_required, business_required], name = 'dispatch')
class BusinessDashboardView(UpdateView):
    model = Business
    form_class = BusinessDashboardForm
    template_name = 'templates/users/BDashboard.html'


@login_required
@business_required
def business_dashboard(request, pk):
    dashboard = get_object_or_404(VDashboard, pk = pk)
    business = request.user.Business

    return render(request, 'users/business/BDashboard.html', {
        'dashboard' : dashboard
    })

def upload_perks(request, pk):
    perksPage = get_object_or_404(perksForm, pk = pk)
    business = request.user.business
    
    if request.method == 'POST':
        form = NameForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('/perks/')

        else:
            form = NameForm()

        return render(request, 'perksForm.html', {'form' : form})

'''
