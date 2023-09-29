from django.shortcuts import render
from rest_framework.views import APIView
# Create your views here. 
class Home(APIView):
    template_name='index.html'
    def get(self,request):
        return render(request,self.template_name)

class Registro(APIView):
    template_name = 'registro.html'

    def get(self, request):
        return render(request, self.template_name)
    
class Reset(APIView):
    template_name = 'reset.html'

    def get(self, request):
        return render(request, self.template_name)