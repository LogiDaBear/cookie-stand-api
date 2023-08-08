from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)
from .serializers import CookieStandSerializer
from .models import CookieStand
from .permissions import IsOwnerOrReadOnly
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from .models import CookieStand



class CookieStandList(ListCreateAPIView):
    queryset = CookieStand.objects.all()
    serializer_class = CookieStandSerializer
    
class CookieStandDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    queryset = CookieStand.objects.all()
    serializer_class = CookieStandSerializer

class CookieStandList(ListView):
    model = CookieStand
    template_name = 'list.html'  # Change to your actual template name if different.
    context_object_name = 'cookie_stands'
    
    # def post(self, request, *args, **kwargs):
    #     form = CookieStandList(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         return redirect('cookie_stands_list')
    #     # If form is invalid, we can return to the same page and display errors.
    #     return render(request, self.template_name, {'form': form, 'cookie_stands': self.get_queryset()})
