"""Main page views -- basically static pages"""
from django.views.generic import View
from django.shortcuts import render

class Index(View):
    """Displays welcome page"""
    def get(self, request, *args, **kwargs):
        return render(request, 'pages/index.html')