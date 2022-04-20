from django import forms
from django.core.mail import mail_managers,BadHeaderError
from django.core.exceptions import ValidationError

class ContactForm(forms.Form):
    '''Class to construct a form for contact page'''

    email=forms.EmailField(initial='youremail@email.com')
    text=forms.CharField(widget=forms.Textarea)

    FEEDBACK='F'
    CORRECTION='C'
    SUPPORT='S'

    REASON_CHOICES=(
        (FEEDBACK,'Feedback'),
        (CORRECTION,'Correction'),
        (SUPPORT,'Support'),
    )

    reason=forms.ChoiceField(choices=REASON_CHOICES,initial=FEEDBACK)

    def send_email(self):
        reason=self.cleaned_data.get('reason')
        reason_dict=dict(self.REASON_CHOICES)
        full_reason=reason_dict.get(reason)
        email=self.cleaned_data.get('email')
        text=self.cleaned_data.get('text')
        body=f"Message From :{email}\n {text}"

        try:
            mail_managers(full_reason,body)
        except BadHeaderError:
            self.add_error(None,ValidationError('Mail Could not be sent',code='badheader'))
            return False
        else:
            return True

        

