from django.shortcuts import render, reverse

def help(request):

    template = 'help/help.html'
    return render(request, template)

def contact_us(request):
    template = 'help/contact-us.html'
    return render(request, template)