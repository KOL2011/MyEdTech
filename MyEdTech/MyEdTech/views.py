from django.urls import reverse
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required

@login_required
def streams(request):
    return render(request, 'streams.html')
@login_required
def mytags(request):
    return render(request, 'playlists.html')
@login_required
def blogs(request):
    return render(request, 'blogs.html')

class TestPage(TemplateView):
    template_name = 'test.html'

class ThanksPage(TemplateView):
    template_name = 'thanks.html'

class HomePage(TemplateView):
    template_name = 'index.html'

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect(reverse("test"))
        return super().get(request, *args, **kwargs)
