from django.contrib import admin

# Register your models here.
from .models import Document, Mention, Observation, Sondage, Operation, Sequence, Unite

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


class MentionAdmin(admin.ModelAdmin):

	list_display = ('mention','document','page')
	
	fieldsets = [
        (None, 
        {'fields': (
        	('mention','commentaire'),
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
	list_display = ('nom_unite','profondeur','epaisseur','texture_1','texture_2','couleur','nuance_couleur','valeur_couleur','taches','carbonate','type_carbon','structure_1','taille_structure','structure_2','sous_structure','compacite','inclusion','mobilier','interpretation_sedimentaire','interpretation_pedologique','interface','echantillon','autre')

class SequenceAdmin(admin.ModelAdmin):
	list_display = ('nom_sequence',)
	filter_horizontal = ("unite",)


admin.site.register(Document, DocumentAdmin)
admin.site.register(Mention, MentionAdmin)
admin.site.register(Observation, ObservationAdmin)
admin.site.register(Sondage, SondageAdmin)
admin.site.register(Operation, OperationAdmin)
admin.site.register(Sequence, SequenceAdmin)
admin.site.register(Unite, UniteAdmin)
