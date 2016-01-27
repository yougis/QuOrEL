from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from django.contrib.gis import admin
from leaflet.admin import LeafletGeoAdmin

# Register your models here.
from .models import Document, Mention, Observation, Sondage, Operation, Sequence, Unite




class DocumentResource(resources.ModelResource):

    class Meta:
        model = Document
    

class DocumentAdmin(ImportExportModelAdmin):
    resource_class = DocumentResource
    list_display = ('nom_document','auteur','annee','traitement')
    fieldsets = [
        (None, {'fields': (
          ('nom_document','auteur','annee'),          
          'commentaire',
          'traitement',
        )         
        }),
    ]
    pass

class MentionResource(resources.ModelResource):

    class Meta:
        model = Mention

class MentionAdmin(ImportExportModelAdmin):
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
    resource_class = MentionResource
    pass

class OperationResource(resources.ModelResource):

    class Meta:
        model = Operation

class OperationAdmin(ImportExportModelAdmin):    
    list_display = ('nom_operation','type_operation')
    resource_class = OperationResource
    pass

class SondageResource(resources.ModelResource):

    class Meta:
        model = Sondage


class SondageAdmin(ImportExportModelAdmin):
    list_display = ('nom_sondage','operation')
    resource_class = SondageResource
    pass

class ObservationResource(resources.ModelResource):

    class Meta:
        model = Observation

class ObservationAdmin(ImportExportModelAdmin):
    list_display = ('nom_observation','type_observation','sondage','sequence','acces_possible')
    resource_class = ObservationResource
    pass

class UniteResource(resources.ModelResource):

    class Meta:
        model = Unite

class UniteAdmin(ImportExportModelAdmin):
    list_display = ('nom_unite','profondeur','epaisseur','texture_1','texture_2','couleur','nuance_couleur','valeur_couleur','tache','carbonate','type_carbon','structure_1','taille_structure','structure_2','sous_structure','compacite','inclusion','mobilier','interpretation_sedimentaire','interpretation_pedologique','interface','echantillon','autre')
    resource_class = UniteResource
    pass


class SequenceResource(resources.ModelResource):

    class Meta:
        model = Sequence

class SequenceAdmin(ImportExportModelAdmin):    
    list_display = ('nom_sequence',)
    filter_horizontal = ("unite",)
    resource_class = SequenceResource
    pass



admin.site.register(Document, DocumentAdmin)
admin.site.register(Mention, MentionAdmin)
admin.site.register(Observation, LeafletGeoAdmin)
admin.site.register(Sondage, LeafletGeoAdmin)
admin.site.register(Operation, OperationAdmin)
admin.site.register(Sequence, SequenceAdmin)
admin.site.register(Unite, UniteAdmin)
