from django.shortcuts import render
from .models import Course
from .forms import ContactCourse

def index(request):
    courses = Course.objects.all()
    template_name = 'courses/index.html'
    context = {'courses':courses}
    return render(request, template_name, context)

# def details(request, pk):
#     course = Course.objects.get(pk=pk)
#     context = {'course': course}
#     template_name = 'courses/details.html'
#     return render(request, template_name, context)

def details(request, slug):
    course = Course.objects.get(slug=slug)
    context = {}
    if request.method == 'POST':
        form = ContactCourse(request.POST)
        if form.is_valid():
            context['is_valid'] = True
            form.send_mail(course)
            form = ContactCourse()
    else:
        form = ContactCourse()
    context['form'] = form
    context['course'] = course
    template_name = 'courses/details.html'
    return render(request, template_name, context)



