from django import template

register = template.Library()

# @register.filter(name='remove')
def cut(value, arg):
    """
    This cuts out all values of "arg" from the string!"
    """
    return value.replace(arg, '')

register.filter('cut', cut)
