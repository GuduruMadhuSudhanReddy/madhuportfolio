from django.core.mail import send_mail
from django.shortcuts import render, redirect
from .forms import ContactForm
from django.conf import settings

def index(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Process the form and send email
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            
            # Compose the email
            email_subject = f"New contact form submission: {subject}"
            email_message = f"Name: {name}\nEmail: {email}\nSubject: {subject}\nMessage:\n{message}"
            recipient_list = ['madhusudhan95981@gmail.com']  # Send to your email (could also send to multiple addresses)

            # Send the email
            send_mail(
                email_subject,
                email_message,
                email,  # Sender's email
                recipient_list,
                fail_silently=False,
            )
            
            # Optionally save the message to the database if you have a model
            form.save()

            # Redirect to a success page or show a success message
            return redirect('success')  # Assuming you have a success URL to redirect to
    else:
        form = ContactForm()

    return render(request, 'index.html', {'form': form})
def success(request):
    return render(request, 'success.html')



# Print the current database settings to check if SQLite is being used
print(settings.DATABASES)
