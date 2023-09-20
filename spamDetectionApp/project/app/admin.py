from django.contrib import admin
from .models import Messages, ModelUser, Contact,spamsMessage
admin.site.register(Contact)
admin.site.register(Messages)
admin.site.register(ModelUser)
admin.site.register(spamsMessage)
