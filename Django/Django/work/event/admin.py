from django.contrib import admin,messages
from .models import *
from datetime import date
from django.utils.translation import gettext_lazy as _

#custom filter hedha  
class ParticipantFilter(admin.SimpleListFilter):
    #esm el filter
    title = 'Participants'
    
    parameter_name = 'participants'

    def lookups(self, request, model_admin):
        return (
            ('no', 'No Participants'),
            ('yes', 'There are Participants'),
        )

    def queryset(self, request, queryset):
        if self.value() == 'no':
            return queryset.filter(participant__isnull=True)
        if self.value() == 'yes':
            return queryset.filter(participant__isnull=False)


class EventDateFilter(admin.SimpleListFilter):
    #esm el filter
    title = 'Event DATE'
    
    parameter_name = 'evt_date'

    def lookups(self, request, model_admin):
        return (
            ('past', _('Past events')),
            ('today', _('Today events')),
            ('future', _('Upcoming events')),
        )

    def queryset(self, request, queryset):
        if self.value() == 'past':
            return queryset.filter(evt_date__lt=date.today())
        elif self.value() == 'today':
            return queryset.filter(evt_date=date.today())
        elif self.value() == 'future':
            return queryset.filter(evt_date__gt=date.today())
        
        
#lina na3mlou fel interface ajout kel field esmou paricipant ka titre we fih nejmou najoutiw barcha les participants       
class ParticipationInline(admin.TabularInline):
    model = participants
    readonly_fields=('date_participation',)
    #hedha pardefaut i5arjelk ka3ba mouch zouz dropdown
    extra = 1
    can_delete=False
    classes =['collapse']
    

# Change state to true with actions:
def set_Accept(ModelAdmin , request , queryset):
    rows_updated =  queryset.update(state=True)
            
    if (rows_updated ==1): 
        msg = " 1 event was"

    else:
        msg = f"{rows_updated}  events were  "

    messages.success(request,f'{msg} successfully updated' )




# Change state to false with actions:
def set_Refuse(ModelAdmin , request , queryset):
    rows_updated =  queryset.update(state=False)
            
    if (rows_updated ==1): 
        message = " 1 event was"

    else:
        message = f"{rows_updated}  events were  "

    messages.success(request,f'{message} successfully updated' )


set_Accept.short_description = "raj3 True"

set_Refuse.short_description = "raj3 False"

# Register your models here.
@admin.register(Event)
class EventAdmin(admin.ModelAdmin):

    #chmich nwariw fe lista el baraniya
    list_display=('title', 'description' ,'image', 'evt_date','category','state' ,'organisateur','event_nbr_participant')
     
    #hedhya list filter 3al imin ta5atr b ama crietere
    list_filter = (  
      'category','state','title',ParticipantFilter,EventDateFilter
        
    )


    
    inlines =[ ParticipationInline]
 
    #izidek bar de recherche fe westha bech tlawej
    autocomplete_fields=['organisateur']

    #kima fieldsets ama hedhi mats9mhomch b section ex: EventDESc we DAtes
    #fields =(('title','category') , 'description')

    #ma3ndkch el 7a9 t3mrhom
    readonly_fields=('created_date','updated_date')
    #fel interface bel azra9 tjina event description we dates wel fields eli mich nwarihom
    fieldsets = ( 
        
        ('Event DESC', {
                'fields': ('title' ,'category','state','organisateur' , 'image'),
        }),
        ('Les Dates' , {
        'fields':('evt_date','created_date','updated_date'),
        }),
                 
                 
                 
                 )
    
    #hedhi el pagination n9oloulou kol 2 pages
    list_per_page = 5
    #hedhya sort descending 7asb e titre alphabetic
    ordering = ['-title']
    #hedhom les actions eli mawjudin fou9 e lista par example 7atna ki yznel ya3Ml update wa7du true lel false
    actions = [set_Accept , set_Refuse]


    #el fct count 
    def event_nbr_participant(self,obj):
        count = obj.participant.count()
        return count 
    


    event_nbr_participant.short_description = 'Nob particpant'



admin.site.register(participants) 