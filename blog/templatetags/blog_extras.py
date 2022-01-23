from django.contrib.auth import get_user_model
from django import template

register = template.Library()
user_model = get_user_model()

@register.filter
def author_details(author):
    if not isinstance(author, user_model):
    # return empty string as safe default 
        return ""

    if author.first_name and author.last_name:
        name = f"{author.first_name} {author.last_name}"

    else:
        name = f"{author.username}"
    
    return name
