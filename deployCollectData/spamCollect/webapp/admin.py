from django.contrib import admin
# Register your models here.
from .models import Messages, ModelUser, Contact,spamsMessage
admin.site.register(Contact)
admin.site.register(Messages)
admin.site.register(ModelUser)
admin.site.register(spamsMessage)
