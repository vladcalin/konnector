from django.shortcuts import render


from django.views.generic import TemplateView


class FacebookView(TemplateView):
    template_name = 'facebook/facebook.html'

