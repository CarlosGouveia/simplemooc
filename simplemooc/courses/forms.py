from django import forms
from django.core.mail import send_mail
from django.conf import settings
from simplemooc.core.mail import send_email_template

class ContactCourse(forms.Form):
    name = forms.CharField(label='Nome', max_length=100)
    email = forms.EmailField(label='E-mail')
    message = forms.CharField(label='Mensagem/Dúvida', widget=forms.Textarea(attrs={'placeholder': 'Digite uma mensagem...'}))

    def send_mail(self, course):
        subject = '[%s] Contato' % course
        context = {
            'name': self.cleaned_data['name'],
            'email': self.cleaned_data['email'],
            'message': self.cleaned_data['message'],
        }

        template_nome = 'courses/contact_email.html'
        send_email_template(
            subject,
            template_nome,
            context,
            [settings.CONTACT_EMAIL]
        )