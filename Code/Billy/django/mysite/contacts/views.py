from django.shortcuts import render, get_object_or_404, reverse
from .models import Contact
from django.http import HttpResponse, HttpResponseRedirect

def index(request):
    cards = Contact.objects.order_by('last_name')
    context = {
        'cards': cards
    }
    return render(request, 'contacts/index.html', context)

def detail(request, card_id):
    # card = Contact.objects.get(pk=card_id)
    card = get_object_or_404(Contact, pk=card_id)
    context = {
        'card': card
    }
    return render(request, 'contacts/detail.html', context)

def entry_page(request):
    return render(request, 'contacts/submit_contact.html')

def submit_contact(request):
    first_name = request.POST['first_name']
    last_name = request.POST['last_name']
    age = request.POST['age']
    birthday = request.POST['birthday']
    phone_number = request.POST['phone_number']
    is_cell = request.POST['is_cell']
    comments = request.POST['comments']
    new_card = Contact(first_name=first_name, last_name=last_name, age=age,
        birthday=birthday, phone_number=phone_number, is_cell=is_cell, comments=comments)
    new_card.save()
    return HttpResponseRedirect(reverse('contacts:detail', args=(new_card.id,)))
