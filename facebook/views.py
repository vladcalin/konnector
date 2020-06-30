from django.shortcuts import render

# Create your views here.


# def do_redirect():
#     url = "https://www.facebook.com/v6.0/dialog/oauth?client_id={app-id}&redirect_uri=/&state={state-param}"
#
from django.views.generic import TemplateView


class FacebookView(TemplateView):
    template_name = 'facebook/facebook.html'


def do_login():
    url = "https://graph.facebook.com/v6.0/oauth/access_token?grant_type=fb_exchange_token&" \
          "client_id={app_id}&" \
          "client_secret={app_secret}&" \
          "fb_exchange_token={your_access_token}".format(app_id='2959312947462607',
                                                         app_secret='862af3c28a0540b7ff58fe0cf2dc90eb',
                                                         your_access_token='')
