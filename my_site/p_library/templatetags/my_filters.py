from django import template

register = template.Library()

@register.filter
def range_(value, start_index=1):
    return range(start_index, value+start_index)

@register.filter
def div( value, arg ):
    value = int( value )
    arg = int( arg )
    if value%arg==0:
    	return value