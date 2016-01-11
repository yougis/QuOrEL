from __future__ import unicode_literals
import uuid

from django.db import models
from django.core.validators import MaxValueValidator
from django.utils.encoding import python_2_unicode_compatible

# Create your models here.
@python_2_unicode_compatible
class Document(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nom_document = models.CharField(max_length=100)
    auteur = models.CharField(max_length=100)
    annee = models.PositiveIntegerField(validators=[MaxValueValidator(2016)])
    commentaire = models.TextField(blank=True, null=True)
    traitement = models.BooleanField()

    def __str__(self):
    	return self.nom_document

@python_2_unicode_compatible
class Unite(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nom_unite = models.CharField(max_length=100)
    couleur_choix =  (
    ('blanc','blanc'),
    ('noir','noir'),
    ('brun','brun'),
    ('jaune','jaune'),
    ('orange','orange'),
    ('rouge','rouge'),
    ('vert','vert'),
    ('bleu','bleu'),
    ('rouille','rouille'),
    ('clair','clair'),
    )
    couleur = models.CharField(max_length=10,
    	choices=couleur_choix,
    	default='indéfini'
    	)
    couleur_MSCC = models.CharField(max_length=100)
    carbonate = models.BooleanField()
    taches = models.TextField(blank=True, null=True)
    texture_choix =  (
    ('caillouteux','caillouteux'),
    ('graveleux','graveleux'),
    ('sableux','sableux'),
    ('limoneux','limoneux'),
    ('argileux','argileux'),
    )
    texture = models.CharField(max_length=20,
    	choices=texture_choix,
    	default='indéfini'
    	)
    structure_choix =  (
    ('massive','massive'),
    ('lamellaire','lamellaire'),
    ('polyyédrique','polyyédrique'),
    ('prismatique','prismatique'),
    ('grossière','grossière'),
    ('fine','fine'),
    )
    structure = models.CharField(max_length=20,
    	choices=structure_choix,
    	default='indéfini'
    	)
    inclusion = models.CharField(max_length=100)
    mobilier = models.TextField(blank=True, null=True)
    perturbation = models.TextField(blank=True, null=True)
    autre = models.TextField(blank=True, null=True)

    def __str__(self):
    	return self.nom_unite


@python_2_unicode_compatible
class Sequence(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nom_sequence = models.CharField(max_length=100)
    unite = models.ManyToManyField(Unite)
    
    def __str__(self):
    	return self.nom_sequence  + ' ID :  ' + format(self.id)

@python_2_unicode_compatible
class Mension(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    mension = models.TextField()
    page = models.CharField(max_length=20)
    commentaire = models.TextField(blank=True, null=True)
    document = models.ForeignKey(Document, blank=True, null=True)
    sequence =  models.ManyToManyField(Sequence)

    def __str__(self):
    	return self.mension

@python_2_unicode_compatible
class Operation(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nom_operation = models.CharField(max_length=100)
    type_op_choix =  (
    ('fouille préventive','fouille préventive'),
    ('diagnostic préventif','diagnostic préventif'),
    ('fouille programmée','fouille programmée'),
    ('carrière','carrière'),
    ('autre chantier','autre chantier'),
    ('autre','autre'),
    )
    type_operation = models.CharField(max_length=25,
    	choices=type_op_choix,
    	default='indéfini'
    	)

    def __str__(self):
    	return self.nom_operation + ' : ' + self.type_operation



@python_2_unicode_compatible  # only if you need to support Python 2
class Sondage(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nom_sondage = models.CharField(max_length=100)
    operation = models.ForeignKey(Operation, blank=True, null=True)

    def __str__(self):
    	return self.nom_sondage


@python_2_unicode_compatible
class Observation(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nom_observation = models.CharField(max_length=100)
    type_obs_choix = (
    ('log','log'),
    ('coupe','coupe'),
    ('plan','plan'),
    )
    type_observation = models.CharField(max_length=5,
    	choices=type_obs_choix,
    	default='indéfini'
    	)
    sondage = models.ForeignKey(Sondage, blank=True, null=True)
    sequence = models.ForeignKey(Sequence, blank=True, null=True)

    acces_possible = models.BooleanField()

    def __str__(self):
    	return self.nom_observation