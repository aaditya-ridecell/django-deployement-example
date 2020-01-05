from django import template

register = template.Library()


#Using decorater
@register.filter(name='cut')
def cut(value, arg):
    """
    This cuts of all values of arg from string!
    """
    return value.replace(arg, '')


#Without using decorater

# def cut(value, arg):
#     """
#     This cuts of all values of arg from string!
#     """
#     return value.replace(arg, '')

# #Register the function to call it in the html
# register.filter('cut', cut)
