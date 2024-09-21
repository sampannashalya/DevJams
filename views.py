from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse,Http404,HttpResponseRedirect
from .models import TestModel,TeachingRegistration,Education
from .forms import NameForm,VolenteerForm,EducationForm
from django.urls import reverse
import requests
from bs4 import BeautifulSoup
import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry


def home(request):
    return render(request, "LearnServe/home.html")


def volenteer_info(request):
    session = requests.Session()
    retry = Retry(connect=6, backoff_factor=0.5)
    adapter = HTTPAdapter(max_retries=retry)
    session.mount('http://', adapter)
    session.mount('https://', adapter)

    url = "https://sdgs.un.org/goals"
    session.get(url)
    r = requests.get(url)
    htmlcontent = r.content
    # print(htmlcontent)

    soup = BeautifulSoup(htmlcontent, 'html.parser')
    # print(soup.prettify)
    list_store = []
    context = {}
    title = soup.title

    # print(title)
    anchors = soup.find_all('a')
    all_links = set()

    for link in soup.find_all('a'):
        list_store.append(link.get('href'))
    context['list'] = list_store

    return render(request, 'LearnServe/rand.html', context)


def get_volenteering(request):
    context = {}
    form = VolenteerForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        url = reverse('volenteer_info')
        return HttpResponseRedirect(url)
    else:
        form = VolenteerForm()
        # print("hello world")
    context['forms'] = form
    context['variable'] = 'volenteering'
    return render(request, "LearnServe/forms.html", context)


def teaching_info(request):
    context = {}
    user_name=request.user.get_username()
    edu_obj=Education.objects.filter(name=user_name)
    return HttpResponse(user_name)
    teachers = TeachingRegistration.objects.filter(subject_taught=subject_choice)
    context['teachers'] = teachers
    return render(request, "LearnServe/teachers_info.html", context)


def teachers(request):
    context = {}
    form = NameForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        url = reverse('teaching_info')
        return HttpResponseRedirect(url)
    else:
        form = NameForm()
        # print("hello world")
    context['forms'] = form
    context['variable'] = 'teaching'
    return render(request, "LearnServe/forms.html", context)


def education(request):
    context = {}
    form = EducationForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        url = reverse('teaching_info')
        return HttpResponseRedirect(url)
    else:
        form = EducationForm()
    context['forms'] = form
    context['variable'] = 'education'
    rand = TeachingRegistration.objects.all()
    return render(request, "LearnServe/forms.html", context)



def details(request,question_id):
    question = get_object_or_404(question, pk=question_id)
    render(request, "LearnServe/details.html",{"question":question})
