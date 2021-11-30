from django.shortcuts import render


def view_bag(request):
    '''
    View to render the users bag
    '''
    return render(request, 'bag/bag.html')