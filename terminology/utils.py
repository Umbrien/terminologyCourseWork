from django.db.models import QuerySet
from models import Term


def term_unicode__icontains(name: str) -> QuerySet:
    """icontains which works with unicode"""

    # creating empty QuerySet
    search_set = Term.objects.none()
    for query in Term.objects.all():
        if name.upper() in query.name.upper():
            # append to QuerySet
            search_set |= Term.objects.filter(name__contains=query.name)

    return search_set