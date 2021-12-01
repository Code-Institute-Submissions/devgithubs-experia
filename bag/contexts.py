from django.conf import settings

def bag_contents(request):
    '''
    Context processor to make checkout contents available
    to every template/app across website.
    '''

    bag_items = []
    total = 0
    count = 0



    context = {
        'bag_items': bag_items,
        'total': total,
        'count': count,
    }

    return context