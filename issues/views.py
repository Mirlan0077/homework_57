from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, DetailView, CreateView, UpdateView, DeleteView
from django.views.generic import ListView
from django.urls import reverse_lazy
from django.views.generic import UpdateView
from .models import Issue
from .forms import IssueForm



class IssueListView(ListView):
    model = Issue
    template_name = 'issue_list.html'
    context_object_name = 'issues'


class IssueDetailView(DetailView):
    model = Issue
    template_name = 'issue_detail.html'
    context_object_name = 'issue'


class IssueCreateView(LoginRequiredMixin, CreateView):
    model = Issue
    form_class = IssueForm
    template_name = 'issue_form.html'
    success_url = reverse_lazy('issue_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Create New Issue'
        return context

class IssueUpdateView(LoginRequiredMixin, UpdateView):
    model = Issue
    form_class = IssueForm
    template_name = 'issue_form.html'
    success_url = reverse_lazy('issue_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Update Issue'
        return context
class IssueDeleteView(LoginRequiredMixin, DeleteView):
    model = Issue
    template_name = 'issue_confirm_delete.html'
    success_url = reverse_lazy('issue_list')