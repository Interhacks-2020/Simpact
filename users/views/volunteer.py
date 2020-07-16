from django.contrib.auth import login 
from django.shortcuts import redirect
from django.views.generic import CreateView
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.db.models import Count

from ..decorators import volunteer_required
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator

from ..forms import VolunteerSignUpForm
from ..models import User

class VolunteerSignupView(CreateView):
    model = User
    form_class = VolunteerSignUpForm
    template_name = 'registration/volunteerSignUpForm.html'
    #find out what this reverse_lazy is 
    #success_url = reverse_lazy('')

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'volunteer'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('volunteer:dashboard')


'''

@method_decorator([login_required, volunteer_required], name = 'dispatch')
class VolunteerDashboardView(UpdateView):
    model = Volunteer
    form_class = VolunteerDashboardForm
    template_name = 'templates/users/VDashboard.html'

@login_required
@volunteer_required
def volunteer_dashboard(request, pk):
    dashboard = get_object_or_404(VDashboard, pk = pk)
    volunteer = request.user.volunteer

    return render(request, 'users/volunteers/VDashboard.html', {
        'dashboard' : dashboard
    })

'''

