from django_filters import FilterSet, CharFilter, DateFilter

from django import forms
from marketface.models import Product


class BlogFilter(FilterSet):
    name = CharFilter(lookup_expr='icontains', label='Title',
                      widget=forms.TextInput(attrs={'class': 'form-control'}))
    # start_date = DateFilter(field_name='created', lookup_expr='gt',
    #                         label='Start Date', widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}))
    # end_date = DateFilter(field_name='created', lookup_expr='lt',
    #                       label='End Date', widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}))

    class Meta:
        model = Product
        fields = {
            'name': ['icontains'],
        }
