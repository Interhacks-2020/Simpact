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

from ..forms import BusinessSignUpForm, CompanyPerks
from ..models import User

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
