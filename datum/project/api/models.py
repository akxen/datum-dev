from django.db import models


class DispatchSCADA(models.Model):
    row_id = models.IntegerField(primary_key=True)
    settlementdate = models.DateTimeField()
    duid = models.CharField(max_length=20)
    scadavalue = models.FloatField()

    class Meta:
        managed = False
        db_table = 'dispatch_scada'
        app_label = 'reports'
