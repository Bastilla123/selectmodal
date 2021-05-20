from .widgets import selectfilterwidget, multiselectfilterwidget
from django import forms
from .models import Historie

#Demoform for normal Selectfield. User can click on this selectfield and then a modal is open. In models.py in address_link the related table is address so now
# ajax loads adress table but shows only the columns fields=['properties_link','country','birthdate','change_date','letter_salutation','status'] in this order
# and shows ist as a listview. In Modal Pagination 25 per site is shown in bottom right corner. filter=['country','birthdate','properties_link','status'] shows
# in modal on left side a box with a filter form where country,birthdate,properties_link and status is shown.

#Attention this here is a example. I want that the widget with name selectfilterwidget works for all foreignkey relations which i create in future.
class Historieform(forms.ModelForm):
    class Meta:
        model = Historie
        fields = ('historietypelink','historiesubtype_link','historiesource_link','historieproperty_link' )
        widgets = {
            'historietypelink': selectfilterwidget(fields=['status','charfield','integerfield','datetimefield','selectfield','manytomanyfield'],filter=['status','charfield','integerfield','datetimefield','selectfield','manytomanyfield']),
            'historiesubtype_link':selectfilterwidget(fields=['status','charfield','integerfield'],filter=['status']),
            'historiesource_link':multiselectfilterwidget(fields=['status','charfield','integerfield','datetimefield','selectfield','manytomanyfield'],filter=['status','charfield','integerfield','datetimefield','selectfield','manytomanyfield']),
            'historieproperty_link':multiselectfilterwidget(fields=['status','charfield','integerfield'],filter=['status']),
        }

