from django import template
import html
register = template.Library()


@register.filter(name='unescapse') 
def fixing(str):
    return html.unescape("&#x27;'" )