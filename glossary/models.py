from django.db import models

class Franchises(models.Model):
    title = models.CharField(db_column='Title', primary_key=True, max_length=45)  # Field name made lowercase.
    sphere = models.CharField(max_length=45)

    class Meta:
        managed = True
        db_table = 'franchises'


class LanqFran(models.Model):
    lanquage = models.ForeignKey('Lanquages', on_delete=models.CASCADE, db_column='lanquage', blank=True, null=True)
    franchise = models.ForeignKey(Franchises,  on_delete=models.CASCADE, db_column='franchise', blank=True, null=True)




class Lanquages(models.Model):
    lanquage = models.CharField(db_column='Lanquage', primary_key=True, max_length=30)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'lanquages'


class OriginalWords(models.Model):
    wordid = models.AutoField(db_column='wordID', primary_key=True)  # Field name made lowercase.
    word = models.CharField(max_length=50, blank=True, null=True)
    transcryption = models.CharField(max_length=100, blank=True, null=True)
    special_information = models.CharField(max_length=200, blank=True, null=True)
    franchise = models.ForeignKey(Franchises, on_delete=models.PROTECT, db_column='franchise')
    original_lanquage = models.ForeignKey(Lanquages, on_delete=models.PROTECT, db_column='original_lanquage', blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'original_words'


class UkrTrans(models.Model):
    word_id = models.AutoField(primary_key=True)
    original = models.OneToOneField(OriginalWords, on_delete=models.PROTECT, db_column='original_ID')  # Field name made lowercase.
    transcryption = models.CharField(max_length=100, blank=True, null=True)
    word = models.CharField(max_length=45)
    special_information = models.CharField(max_length=450, blank=True, null=True)
    franchise = models.ForeignKey(Franchises, on_delete=models.PROTECT, db_column='franchise')

    class Meta:
        managed = True
        db_table = 'ukr_trans'
        unique_together = (('word_id', 'original'),)


