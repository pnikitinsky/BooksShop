from django.shortcuts import render
from .forms import contactForm
from django.core.mail import send_mail
from django.conf import settings


def contact(request):
    title = 'Contact'
    form = contactForm(request.POST or None)
    confirm_message = None
    name = None
    # Validate form
    if form.is_valid():
        name = form.cleaned_data['name']
        comment = form.cleaned_data['comment']
        subject = 'Message from BooksShop.com'
        message = '%s %s' % (comment, name)
        emailFrom = form.cleaned_data['email']
        emailTo = [settings.EMAIL_HOST_USER]
        # Had to comment it since i don't heve any email proxy
        # send_mail(subject, message, emailFrom, emailTo, fail_silently=False)
        title = 'Thanks'
        confirm_message = f"Thanks for the message {name}. We will get right back to you."
        form = None

    context = {'title': title, 'confirm_message': confirm_message,
               'form': form, 'name': name}
    template = 'contact.html'
    return render(request, template, context)
