from django.contrib.auth.mixins import LoginRequiredMixin, AccessMixin
from django.core.exceptions import ImproperlyConfigured
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy

class AuthGroupRequiredMixin(LoginRequiredMixin, AccessMixin):
    groups_required = []  # Por defecto, la lista de grupos requeridos está vacía

    def dispatch(self, request, *args, **kwargs):
        if not self.groups_required:
            raise ImproperlyConfigured("AuthGroupRequiredMixin requires a non-empty 'groups_required' list to be set.")

        if not request.user.is_authenticated:
            return self.handle_no_permission()

        if not request.user.groups.filter(name__in=self.groups_required).exists():
            messages.error(request,'No tiene acceso a este modulo')
            #return self.handle_no_permission()            
            return HttpResponseRedirect(reverse_lazy('login'))   
         
        return super().dispatch(request, *args, **kwargs)
    
