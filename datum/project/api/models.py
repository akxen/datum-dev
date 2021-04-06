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


class DispatchReportCaseSolution(models.Model):
    row_id = models.IntegerField(primary_key=True)
    settlementdate = models.DateTimeField()
    runno = models.IntegerField(max_length=20)
    intervention = models.IntegerField()
    casesubtype = models.CharField(max_length=3)
    solutionstatus = models.IntegerField()
    spdversion = models.CharField(max_length=20)
    nonphysicallosses = models.IntegerField()
    totalobjective = models.FloatField()
    totalareagenviolation = models.FloatField()
    totalinterconnectorviolation = models.FloatField()
    totalgenericviolation = models.FloatField()
    totalramprateviolation = models.FloatField()
    totalunitmwcapacityviolation = models.FloatField()
    total5minviolation = models.FloatField()
    totalregviolation = models.FloatField()
    total6secviolation = models.FloatField()
    total60secviolation = models.FloatField()
    totalasprofileviolation = models.FloatField()
    totalfaststartviolation = models.FloatField()
    totalenergyofferviolation = models.FloatField()
    lastchanged = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'dispatch_report_case_solution'
        app_label = 'reports'
