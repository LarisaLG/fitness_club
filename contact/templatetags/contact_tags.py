from django import template
from contact.forms import ContactUsForm

register = template.Library()


@register.inclusion_tag('contact/tags/contact-form.html')
def contact_form():
    return {'contact_form': ContactUsForm()}
