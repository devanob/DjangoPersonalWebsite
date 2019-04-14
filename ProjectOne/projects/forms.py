from django import forms
import datetime
from django.db.models import Q
from projects.models import Project

def getYears():
    year = datetime.datetime.today().year
    yearIntRange = year - 2018 + 1
    YEARS = [ (year - offset, year - offset) for offset in range(yearIntRange)]
    YEARS= [("", "YEAR")]+ YEARS
    return tuple(YEARS)

YEARS = getYears()
MONTHS = (("", "MONTH"),(1,"JANURARY") , (2, "FEBURARY") , (3, "MARCH"), (4, "APRIL"),
        (5,"MAY") , (6, "JUNE") , (7, "JULY"), (8, "AUGUST"), 
        (9, "SEPTEMBER"),(10,"OCTOBER") , (11, "NOVEMBER") , (12, "DECEMBER"))


class SearchProjectForm(forms.Form):
    model = Project
    search_year = forms.ChoiceField(widget=forms.Select(attrs={'class': 'selectpicker form-control form-control-lg'}),
                                            choices=YEARS, required= False)
    search_month = forms.ChoiceField(initial="MONTH",widget=forms.Select(attrs={'class': 'selectpicker form-control form-control-lg'}),
                                            choices=MONTHS, required= False)                                       
    search_project_text = forms.CharField(label='Search Project',required= False,
        widget=forms.TextInput(attrs={'class': 'form-control form-control-lg','placeholder': 'Search...'},
       ),
        max_length=100)

    def clean_search_year(self):
        year = self.cleaned_data['search_year']
        if(year):
            try: 
                return int(year)
            except ValueError:
                raise forms.ValidationError("Year Is Not Valid")
        else:
            return None
    def clean_search_month(self):
        month = self.cleaned_data['search_month']
        if month:
            try: 
                return int(month)
            except ValueError:
                raise forms.ValidationError("Month Is Not Valid")
        else:
            return None
    def clean_search_project_text(self):
        textSearch = self.cleaned_data['search_project_text']
        try: 
            return textSearch.strip()
        except ValueError:
            raise forms.ValidationError("Text Is Not Valid")

    def generateSearchQuery(self):
        print("Hrllo")
        modelInstance = self.model.objects.all()
        if self.cleaned_data['search_project_text']:
            searchText = self.cleaned_data['search_project_text']
            print("Search: "+ searchText)
            modelInstance = modelInstance.filter(Q(projectName__icontains=searchText) 
                            | Q(description__icontains=searchText))

        if self.cleaned_data['search_year']:
            year = self.cleaned_data['search_year']
            modelInstance = modelInstance.filter(last_updated__year=year)

        if self.cleaned_data['search_month']:
            month = self.cleaned_data['search_month']
            modelInstance = modelInstance.filter(last_updated__month=month)
        return modelInstance
            