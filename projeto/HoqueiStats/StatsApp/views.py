from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Clube


class IndexView(generic.ListView):
	template_name = 'index.html'
	context_object_name = 'club_list'
	def get_queryset(self):
		return Clube.objects.order_by('-nome')[:5]


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)