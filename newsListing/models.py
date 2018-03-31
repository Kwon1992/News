# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class ArticleEntries(models.Model):
    id = models.IntegerField(primary_key=True)
    aid = models.CharField(max_length=10)
    title = models.CharField(max_length=60)
    content = models.TextField()
    adate = models.CharField(db_column='aDate', max_length=20)  # Field name made lowercase.
    nurl = models.CharField(db_column='nUrl', max_length=120)  # Field name made lowercase.
    purl = models.CharField(db_column='pUrl', max_length=120)  # Field name made lowercase.
    subclass = models.CharField(db_column='subClass', max_length=10)  # Field name made lowercase.
    nclass = models.CharField(db_column='nClass', max_length=10)  # Field name made lowercase.
    press = models.CharField(max_length=10)
    pdf = models.CharField(max_length=20)
    html = models.CharField(max_length=20)
    numcomment = models.CharField(db_column='numComment', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'article_entries'
