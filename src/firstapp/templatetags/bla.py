from django import template
register = template.Library()

@register.simple_tag(takes_context=True)
def my_tag(context, index, *args, **kwargs):
    return repr(context['shoes'][int(index)])

