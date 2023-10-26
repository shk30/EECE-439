from django.shortcuts import render, get_object_or_404, redirect
from .models import Contact
from .forms import ContactForm
from django.http import HttpResponse

def contact_list(request):
    contacts = Contact.objects.all()
    return render(request, 'main/contact_list.html', {'contacts': contacts})

def contact_detail(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    return render(request, 'main/contact_detail.html', {'contact': contact})

from django.shortcuts import get_object_or_404

def contact_create(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            profession1 = form.cleaned_data['profession1']
            profession2 = form.cleaned_data['profession2']
            if profession1 == profession2:
                error_message = "Profession 1 and Profession 2 cannot be the same."
                return HttpResponse(error_message)
            else:
                form.save()
                return redirect('contact_list')
    else:
        form = ContactForm()
    return render(request, 'main/contact_create.html', {'form': form})


def contact_update(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    if request.method == 'POST':
        form = ContactForm(request.POST, instance=contact)
        if form.is_valid():
            form.save()
            return redirect('contact_detail', pk=pk)
    else:
        form = ContactForm(instance=contact)
    return render(request, 'main/contact_update.html', {'form': form, 'contact': contact})

def contact_delete(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    if request.method == 'POST':
        contact.delete()
        return redirect('contact_list')
    return render(request, 'main/contact_confirm_delete.html', {'contact': contact})
