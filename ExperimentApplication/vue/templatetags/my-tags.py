from django import template

register = template.Library()

@register.filter
def index(sequence, position):
    return sequence[position]

@register.filter
def dicIndex(dictionairy, index):
    return dictionairy.get(index)