__author__ = 'Akhil'

from feedback.models import *

def get_years():
    years = Classes.objects.values_list('year').distinct().order_by('year')
    return [str(x[0]) for x in years]


def get_branches(year):
    branches = Classes.objects.filter(year=int(year)).values_list('branch').order_by('branch').distinct()
    return [x[0] for x in branches]


def get_sections(year, branch):
    sections = Classes.objects.filter(year=int(year), branch=branch).values_list('section').order_by('branch').distinct()
    return [x[0] for x in sections]

def get_subjects(year, branch):
    classes = Classes.objects.filter(year=int(year), branch=branch)
    cfs = ClassFacSub.objects.all()
    subjects = []
    for cls in classes:
        subs = cfs.filter(class_id=cls)
        for sub in subs:
            sub_name = sub.subject_id.name
            if sub_name not in subjects:
                subjects.append(sub_name)
    return subjects

def get_faculty(year, branch, section):
    classes = Classes.objects.filter(year=int(year), branch=branch, section=section)
    cfs = ClassFacSub.objects.all()
    subjects = []
    for cls in classes:
        subs = cfs.filter(class_id=cls)
        for sub in subs:
            sub_name = sub.faculty_id.name
            if sub_name not in subjects:
                subjects.append(sub_name)
    return subjects