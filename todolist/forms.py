from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _

from .models import todolist

class todolistform(ModelForm):
    class Meta:
        model = todolist
        fields = ['title', 'description', 'task_status']
        labels = {
            'title': _('Title'),
            'description': _('Description'),
            'task_status': _('Status')
        }
        
        help_texts = {
            'title': _('Enter task title'),
            'description': _('Enter task description'),
            'task_status': _('Select task status')
        }
        
        error_messages = {
            'title': {
                'required': _('Please fill it')
            },
            'description': {
                'required': _('Please fill it')
            },
        }