from django.shortcuts import render


def help(request):
    '''renders the help page'''
    template = 'help/help.html'
    return render(request, template)


def contact_us(request):
    '''renders the contact-us page'''
    template = 'help/contact-us.html'
    return render(request, template)