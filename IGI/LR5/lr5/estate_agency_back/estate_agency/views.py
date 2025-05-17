from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import EmployeeForm, CustomerForm, OwnerForm
from .models import Employee, User, Customer, Owner


class EmployeeCreateView(LoginRequiredMixin, CreateView):
    model = Employee
    form_class = EmployeeForm
    template_name = 'form.html'
    success_url = reverse_lazy('profile')

    def form_valid(self, form):
        user = User.objects.get(user=self.request.user)

        if Owner.objects.filter(user=user).exists() or Customer.objects.filter(user=user).exists():
            messages.error(self.request,
            "You are already registered as the owner or customer. You can't be an employee."
            "The entered data will not be written to the database.")
            return redirect('profile')

        if Employee.objects.filter(user=user).exists():
            messages.error(self.request, "You are already registered as an employee. "
                                         "The entered data will not be written to the database.")
            return redirect('profile')

        form.instance.user = user

        self.object = form.save(commit=False)
        self.object.image = self.request.FILES.get('image')
        self.object.save()

        auth_user = self.request.user
        auth_user.is_staff = True
        auth_user.save()

        return super().form_valid(form)


class CustomerCreateView(LoginRequiredMixin, CreateView):
    model = Customer
    form_class = CustomerForm
    template_name = 'form.html'
    success_url = reverse_lazy('profile')

    def form_valid(self, form):
        user = User.objects.get(user=self.request.user)

        if Customer.objects.filter(user=user).exists():
            messages.error(self.request,
            "You are already registered as the customer."
            "The entered data will not be written to the database.")
            return redirect('profile')

        form.instance.user = user
        return super().form_valid(form)


class OwnerCreateView(LoginRequiredMixin, CreateView):
    model = Owner
    form_class = OwnerForm
    template_name = 'form.html'
    success_url = reverse_lazy('profile')

    def form_valid(self, form):
        user = User.objects.get(user=self.request.user)

        if Owner.objects.filter(user=user).exists():
            messages.error(self.request,
                           "You are already registered as the owner."
                           "The entered data will not be written to the database.")
            return redirect('profile')

        form.instance.user = user
        return super().form_valid(form)