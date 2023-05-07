from django.shortcuts import redirect, render
from django.views import View
from django.contrib.auth.decorators import login_required
from .forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin #use to ensure that only authenticated users can access a view
from django.urls import reverse_lazy #provides a form for updating an existing object
from django.views.generic.edit import UpdateView
from django.contrib.auth import get_user_model

User = get_user_model()

@login_required
def user_home(request):
    user = request.user
    context = {'user': user}
    print (context)
    return render(request, "user_home.html", context)

class UserUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    fields = ['first_name', 'last_name', 'email', 'phone_number', 'address']
    template_name = 'user_update_form.html'
    success_url = reverse_lazy('user_home')

class Register(View):

    template_name = 'registration/register.html'

    def get(self, request): 
        context = {
            'form': UserCreationForm() #to handle user registration
            }
        return render(request, self.template_name, context)
    
    def post(self, request): 
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('shop')
        context = {"form": form}
        return render(request, self.template_name, context)