from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from .libs import tree_builder, graph_builder
from StudentFeedback.settings import DIRECTOR_GROUP


@login_required
def director(request, category, year, branch, sub, subsub):

    if not request.user.groups.filter(name=DIRECTOR_GROUP).exists():
        return render(request, 'feedback/invalid_user.html')

    template = 'analytics/director.html'
    context = {'category': category, 'year': year, 'branch': branch, 'sub': sub, 'subsub': subsub,
               'year_objs': tree_builder.getTree()}

    graph = graph_builder.Graph(category, year, branch, sub, subsub)
    graph.build()

    context['graph'] = graph


    return render(request, template, context)