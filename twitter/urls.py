from django.urls import path

from twitter.views import CreateTwitterIntegrationView

urlpatterns = [
    path('create/', CreateTwitterIntegrationView.as_view(), name='create_twitter_integration')
]
