from django.contrib import admin

# Register your models here.
from .models import Document, Mension, Observation, Sondage, Operation, Sequence, Unite

class DocumentAdmin(admin.ModelAdmin):
    list_display = ('nom_document','auteur','annee','traitement')
    fieldsets = [
        (None, {'fields': (
        	('nom_document','auteur','annee'),        	
        	'commentaire',
        	'traitement',
       	)
       	
       	}),
    ]


class MensionAdmin(admin.ModelAdmin):

	list_display = ('mension','document','page')
	
	fieldsets = [
        (None, 
        {'fields': (
        	('mension','commentaire'),
        	('page','document'),
        	'sequence',    	
       	),}
       	,)]
	filter_horizontal = ("sequence",)


class OperationAdmin(admin.ModelAdmin):
	list_display = ('nom_operation','type_operation')


class SondageAdmin(admin.ModelAdmin):
	list_display = ('nom_sondage','operation')


class ObservationAdmin(admin.ModelAdmin):
	list_display = ('nom_observation','type_observation','sondage','sequence','acces_possible')


class UniteAdmin(admin.ModelAdmin):
	list_display = ('nom_unite','couleur','carbonate','taches','texture','structure')


class SequenceAdmin(admin.ModelAdmin):
	list_display = ('nom_sequence',)
	filter_horizontal = ("unite",)


admin.site.register(Document, DocumentAdmin)
admin.site.register(Mension, MensionAdmin)
admin.site.register(Observation, ObservationAdmin)
admin.site.register(Sondage, SondageAdmin)
admin.site.register(Operation, OperationAdmin)
admin.site.register(Sequence, SequenceAdmin)
admin.site.register(Unite, UniteAdmin)