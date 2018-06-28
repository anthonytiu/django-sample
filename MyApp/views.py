from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

class MyView(View):
    def get(self, request):
        # <view logic>
        try:
            return render(request, 'index.html', {})
        except:
            return HttpResponse('Page not found!')