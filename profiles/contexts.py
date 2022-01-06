# from django.conf import settings
# from experiences.models import Experiences
# from django.shortcuts import get_object_or_404


# def wish_contents(request):
#     '''
#     Context processor to make checkout contents available
#     to every template/app across website.
#     '''

#     wish_items = []

#     ''' get current session bag, if empty, create empty dict.'''
#     wishes = request.session.get('wishes', {})

#     for item_id in wishes:
#         product = get_object_or_404(Experiences, pk=item_id)
#         print(product)
#         wish_items.append({
#             'item_id': item_id,
#             'product': product,
#         })
#         print(wish_items)

#     context = {
#         'wish_items': wish_items,
#     }
#     print(f'{wishes} context wish')
#     return context