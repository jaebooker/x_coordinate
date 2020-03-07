from django.db import models
from users.models import User
from django import forms


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project

# class ProjectForm(forms.Form):
#     title= forms.CharField(max_length=20)
#     description = forms.CharField(max_length=5000)
#     number_of_roles = models.IntegerField(default=0)
# class ContactView(FormView):
#     form_class = ContactForm
#     template_name = 'contact-us.html'
#     success_url = reverse_lazy('contact-us')
#
#     def form_valid(self, form):
#         self.send_mail(form.cleaned_data)
#         return super(ContactView, self).form_valid(form)
#
#     def send_mail(self, valid_data):
#         # Send mail logic
#         print(valid_data)
#         pass
class Project(models.Model):
    created_on = model.DateTimeField('date created')
    updated_on = model.DateTimeField('date created')
    title = mode.CharField(max_length=20)
    description = models.CharField(max_length=5000)
    number_of_roles = models.IntegerField(default=0)
    roles_filled = models.IntegerField(default=1)
    contributers = models.ForeignKey(User, on_delete=models.CASCADE)
