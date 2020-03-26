from django.conf import settings
from django.views.generic import TemplateView


class TwitterOauthFlow:
    @staticmethod
    def get_oauth_url():
        return 'https://api.twitter.com/oauth/authorize?oauth_token=' + settings.TWITTER_API_KEY


class CreateTwitterIntegrationView(TemplateView):
    template_name = 'twitter/create_twitter_integration.html'

    def get_context_data(self, **kwargs):
        context = super(CreateTwitterIntegrationView, self).get_context_data(**kwargs)
        context['twitter_url'] = TwitterOauthFlow.get_oauth_url()
        return context
