from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse
from django.views.generic import TemplateView, CreateView, UpdateView, DeleteView

from webapp.forms import ReviewForm
from webapp.models import Product, Review


class ReviewView(TemplateView):
    template_name = 'review/review_view.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = self.kwargs.get('pk')
        review = get_object_or_404(Review, pk=pk)
        context['review'] = review
        return context
    
    
class ReviewCreateView(LoginRequiredMixin, CreateView):
    model = Review
    template_name = 'review/review_create.html'
    form_class = ReviewForm
    #
    # def test_func(self):
    #     return self.request.user.has_perm('webapp.delete_review') and self.request.user in self.get_object().project.user.all()

    def form_valid(self, form):
        project = get_object_or_404(Product, pk=self.kwargs.get('pk'))
        review = form.save(commit=False)
        review.project = project
        review.author = self.request.user
        review.save()
        return redirect('project_view', pk=project.pk)


class ReviewUpdateView(UserPassesTestMixin, UpdateView):
    model = Review
    template_name = 'review/review_update.html'
    form_class = ReviewForm

    def test_func(self):
        return self.request.user.has_perm('webapp.update_review') and self.request.user in self.get_object().project.user.all()

    def get_success_url(self):
        return reverse('project_view', kwargs={'pk': self.object.project.pk})


class ReviewDeleteView(UserPassesTestMixin, DeleteView):
    template_name = 'review/review_delete.html'
    model = Review
    context_object_name = 'review'

    def test_func(self):
        return self.request.user.has_perm('webapp.delete_review') and self.request.user in self.get_object().project.user.all()

    def get_success_url(self):
        return reverse('project_view', kwargs={'pk': self.object.project.pk})