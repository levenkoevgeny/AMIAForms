import django_filters
from training.models import ResultData, Teacher, Group
from testing.models import Subject, Subdivision, Testing
from django import forms


myDateInput = forms.DateInput(format=('%Y-%m-%d'), attrs={'type':'date'})


class ResultDataFilter(django_filters.FilterSet):

    learner_fio = django_filters.CharFilter(lookup_expr='icontains')
    group = django_filters.ModelMultipleChoiceFilter(queryset=Group.objects.all())
    who_conducts = django_filters.ModelMultipleChoiceFilter(queryset=Teacher.objects.all())
    test = django_filters.ModelMultipleChoiceFilter(queryset=Testing.objects.all())
    subject = django_filters.ModelMultipleChoiceFilter(queryset=Subject.objects.all(), field_name='test__subject')
    test_date_start = django_filters.DateFilter(widget=myDateInput, field_name='test_date__date', lookup_expr='gte')
    test_date_end = django_filters.DateFilter(widget=myDateInput, field_name='test_date__date', lookup_expr='lte')

    class Meta:
        model = ResultData
        fields = ['learner_fio', 'test']