from django.contrib import admin
from django.urls import path
from django.http import HttpResponseRedirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.views import LogoutView

# Define your Django models here

# Custom admin site class

urlpatterns = [
    path('admin/logout/', LogoutView.as_view(), name='admin_logout'),
]

# Register your models here.

class CustomModelAdmin(admin.ModelAdmin):
    def changelist_view(self, request, extra_context=None):
        response = super().changelist_view(request, extra_context=extra_context)
        try:
            qs = response.context_data['cl'].queryset
            count = qs.count()
            response['total_count'] = count
            response.context_data['total_count'] = count
        except (AttributeError, KeyError):
            pass
        return response
