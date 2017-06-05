# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class Characters(models.Model):
    name = models.TextField(primary_key=True, unique=True, blank=True)
    wins = models.IntegerField(blank=True, null=True)
    losses = models.IntegerField(blank=True, null=True)
    mu = models.FloatField(blank=True, null=True)
    sigma = models.FloatField(blank=True, null=True)

    class Meta:
        db_table = 'characters'


class DjangoMigrations(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        db_table = 'django_migrations'


class Fights(models.Model):
    matchid = models.IntegerField(primary_key=True, db_column='matchId', unique=True, blank=True)  # Field name made lowercase.
    redname = models.TextField(db_column='redName', blank=True, null=True)  # Field name made lowercase.
    bluename = models.TextField(db_column='blueName', blank=True, null=True)  # Field name made lowercase.
    winner = models.TextField(blank=True, null=True)
    redbets = models.IntegerField(db_column='redBets', blank=True, null=True)  # Field name made lowercase.
    bluebets = models.IntegerField(db_column='blueBets', blank=True, null=True)  # Field name made lowercase.
    redmuchange = models.FloatField(db_column='redMuChange', blank=True, null=True)  # Field name made lowercase.
    bluemuchange = models.FloatField(db_column='blueMuChange', blank=True, null=True)  # Field name made lowercase.
    redsigmachange = models.FloatField(db_column='redSigmaChange', blank=True, null=True)  # Field name made lowercase.
    bluesigmachange = models.FloatField(db_column='blueSigmaChange', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'fights'


class History(models.Model):
    redname = models.TextField(db_column='redName', blank=True, null=True)  # Field name made lowercase.
    bluename = models.TextField(db_column='blueName', blank=True, null=True)  # Field name made lowercase.
    redwins = models.IntegerField(db_column='redWins', blank=True, null=True)  # Field name made lowercase.
    bluewins = models.IntegerField(db_column='blueWins', blank=True, null=True)  # Field name made lowercase.
    totalfights = models.IntegerField(db_column='totalFights', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'history'
        unique_together = (('redname', 'bluename'),)
