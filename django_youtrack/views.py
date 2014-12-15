# -*- encoding: utf-8 -*-
from django.core.urlresolvers import reverse
from django.views.generic import FormView
from dj_youtrack.forms import IssueForm


class HomeView(FormView):
    template_name = 'base.html'
    form_class = IssueForm

    def get_form_kwargs(self):
        kwargs = super(HomeView, self).get_form_kwargs()
        kwargs['project'] = 'HD'
        return kwargs

    def form_valid(self, form):
        form.submit()
        return super(HomeView, self).form_valid(form)

    def get_success_url(self):
        return reverse('home')