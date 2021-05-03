from django.contrib.auth.models import Group 
from django import template

register = template.Library() 

@register.filter(name='has_group') 
def has_group(user, STUDENT):
    group = Group.objects.filter(name=STUDENT)
    if group:
        group = group.first()
        return group in user.groups.all()
    else:
        return False


@register.filter(name='has_groupp') 
def has_groupp(user, TEACHER):
    group = Group.objects.filter(name=TEACHER)
    if group:
        group = group.first()
        return group in user.groups.all()
    else:
        return False