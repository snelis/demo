from django.views.generic import TemplateView
from models import Shoe


class MyFirstView(TemplateView):
    template_name = 'firstapp/index.html'

    def get_context_data(self, **kwargs):

        context = super(MyFirstView, self).get_context_data(**kwargs)

        context['hello'] = 'world'
        context['shoes'] = Shoe.objects.filter()

        return context