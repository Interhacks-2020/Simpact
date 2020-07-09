from django.contrib.auth import login 
from django.shortcuts import redirect
from django.views.generic import CreateView

from ..forms import VolunteerSignUpForm
from ..models import User

class VolunteerSignupView(CreateView):
    model = User
    form_class = VolunteerSignUpForm
    template_name = 'registration/volunteerSignUpForm.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'volunteer'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('volunteer:dashboard')