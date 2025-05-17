from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView

from .models import Review
from .forms import ReviewForm
from estate_agency.models import User


# Create your views here.
def review(request):
    reviews = Review.objects.order_by('-created_at')[:5]
    return render(request, 'reviews/review.html',
                  {"reviews": reviews})


class ReviewCreateView(LoginRequiredMixin, CreateView):
    model = Review
    form_class = ReviewForm
    template_name = 'form.html'
    success_url = reverse_lazy('reviews')

    def form_valid(self, form):
        form.instance.author = User.objects.get(user=self.request.user)
        return super().form_valid(form)


class ReviewListView(LoginRequiredMixin, ListView):
    model = Review
    template_name = 'reviews/review.html'
    context_object_name = 'reviews'

    def get_queryset(self):
        try:
            profile = User.objects.get(user=self.request.user)
        except User.DoesNotExist:
            raise Http404("Профиль пользователя не найден.")
        return Review.objects.filter(author=profile)
