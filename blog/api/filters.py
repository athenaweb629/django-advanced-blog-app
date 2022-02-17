from django_filters import rest_framework as filters
from blog.models import Post

class PostFilterSet(filters.FilterSet):
    # Allow Clients to Search for Posts between certain django_filters
    # Client can choose to set one or both Post date search fields
    # Accepts date being searched from
    published_from = filters.DateFilter(
        field_name="published_at", lookup_expr="gte", label="Published Date From"
    )
    # Accepts date being searched to
    published_to = filters.DateFilter(
        field_name="published_at", lookup_expr="lte", label="Published Date To"
    )
    # Searches a User's Email (Case insensitive lookup - doesn't need EXACT email to search)
    author_email = filters.CharFilter(
        field_name="author__email",
        lookup_expr="icontains",
        label="Author Email Contains",
    )
    # Searches inside Post Summary (AKA the preview featured on the index page)
    summary = filters.CharFilter(
        field_name="summary",
        lookup_expr="icontains",
        label="Summary Contains",
    )
    # Searches inside Post Content (AKA the actual post, featured on detail page)
    content = filters.CharFilter(
        field_name="content",
        lookup_expr="icontains",
        label="Content Contains",
    )

    class Meta:
        model = Post
        fields = ["author", "tags"]


# Django-Filter and the FilterSet Class

# The Official DRF Integration documentation: 
#   https://django-filter.readthedocs.io/en/stable/guide/rest_framework.html

# NOTE: fields instantiated with field_name and (usually) the lookup_expr. label is optional

# NOTE: provides two new arguements that can be used in the URL query params
# to look at just published_from (see above), it would be 
# applied to the queryset by joinging the field_name to the lookup_expr
# IE: to get all posts published in August, the query params would be,
#   ?published_from=2021-08-01&published_to=2021-08-31
# Which would be applied to the queryset like so, 
#   Post.objects.filter(published_at__gte="2021-08-01").filter(published_at__lte="2021-08-31") 

# NOTE: author_email (see PostFilterSet.author_email)
# To Allow searching for only an EXACT email, use the CharField filter:
#    author_email = filters.CharFilter(field_name="author__email", label="Author Email")