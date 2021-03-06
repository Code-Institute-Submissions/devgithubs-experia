from django.conf import settings
from experiences.models import Experiences
from django.shortcuts import get_object_or_404


def bag_contents(request):
    '''
    Context processor to make checkout contents available
    to every template/app across website.
    '''

    bag_items = []
    total = 0
    count = 0

    # get current session bag, if empty, create empty dict.
    bag = request.session.get('bag', {})

    for item_id, quantity in bag.items():
        product = get_object_or_404(Experiences, pk=item_id)
        total += quantity * product.price
        count += quantity
        bag_items.append({
            'item_id': item_id,
            'quantity': quantity,
            'product': product,
        })

    context = {
        'bag_items': bag_items,
        'total': total,
        'count': count,
    }

    return context