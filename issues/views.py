
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Issue


class IssueListView(ListView):
    model = Issue
    template_name = 'issue_list.html'

class IssueDetailView(DetailView):
    model = Issue
    template_name = 'issue_detail.html'

from .forms import IssueForm

class IssueCreateView(CreateView):
    model = Issue
    template_name = 'issue_form.html'
    form_class = IssueForm

class IssueUpdateView(UpdateView):
    model = Issue
    template_name = 'issue_form.html'
    form_class = IssueForm

class IssueDeleteView(DeleteView):
    model = Issue
    template_name = 'issue_confirm_delete.html'
    success_url = '/issues/'
