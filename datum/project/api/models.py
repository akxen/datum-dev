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
    runno = models.IntegerField()
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


class DispatchReportRegionSolution(models.Model):
    row_id = models.IntegerField(primary_key=True)
    settlementdate = models.DateTimeField()
    runno = models.IntegerField()
    regionid = models.CharField(max_length=10)
    intervention = models.IntegerField()
    rrp = models.FloatField()
    eep = models.FloatField()
    rop = models.FloatField()
    apcflag = models.IntegerField()
    marketsuspendedflag = models.IntegerField()
    totaldemand = models.FloatField()
    demandforecast = models.FloatField()
    dispatchablegeneration = models.FloatField()
    dispatchableload = models.FloatField()
    netinterchange = models.FloatField()
    excessgeneration = models.FloatField()
    lower5mindispatch = models.FloatField()
    lower5minimport = models.FloatField()
    lower5minlocaldispatch = models.FloatField()
    lower5minlocalprice = models.FloatField()
    lower5minlocalreq = models.FloatField()
    lower5minprice = models.FloatField()
    lower5minreq = models.FloatField()
    lower5minsupplyprice = models.FloatField()
    lower60secdispatch = models.FloatField()
    lower60secimport = models.FloatField()
    lower60seclocaldispatch = models.FloatField()
    lower60seclocalprice = models.FloatField()
    lower60seclocalreq = models.FloatField()
    lower60secprice = models.FloatField()
    lower60secreq = models.FloatField()
    lower60secsupplyprice = models.FloatField()
    lower6secdispatch = models.FloatField()
    lower6secimport = models.FloatField()
    lower6seclocaldispatch = models.FloatField()
    lower6seclocalprice = models.FloatField()
    lower6seclocalreq = models.FloatField()
    lower6secprice = models.FloatField()
    lower6secreq = models.FloatField()
    lower6secsupplyprice = models.FloatField()
    raise5mindispatch = models.FloatField()
    raise5minimport = models.FloatField()
    raise5minlocaldispatch = models.FloatField()
    raise5minlocalprice = models.FloatField()
    raise5minlocalreq = models.FloatField()
    raise5minprice = models.FloatField()
    raise5minreq = models.FloatField()
    raise5minsupplyprice = models.FloatField()
    raise60secdispatch = models.FloatField()
    raise60secimport = models.FloatField()
    raise60seclocaldispatch = models.FloatField()
    raise60seclocalprice = models.FloatField()
    raise60seclocalreq = models.FloatField()
    raise60secprice = models.FloatField()
    raise60secreq = models.FloatField()
    raise60secsupplyprice = models.FloatField()
    raise6secdispatch = models.FloatField()
    raise6secimport = models.FloatField()
    raise6seclocaldispatch = models.FloatField()
    raise6seclocalprice = models.FloatField()
    raise6seclocalreq = models.FloatField()
    raise6secprice = models.FloatField()
    raise6secreq = models.FloatField()
    raise6secsupplyprice = models.FloatField()
    aggregatedispatcherror = models.FloatField()
    availablegeneration = models.FloatField()
    availableload = models.FloatField()
    initialsupply = models.FloatField()
    clearedsupply = models.FloatField()
    lowerregimport = models.FloatField()
    lowerreglocaldispatch = models.FloatField()
    lowerreglocalreq = models.FloatField()
    lowerregreq = models.FloatField()
    raiseregimport = models.FloatField()
    raisereglocaldispatch = models.FloatField()
    raisereglocalreq = models.FloatField()
    raiseregreq = models.FloatField()
    raise5minlocalviolation = models.FloatField()
    raisereglocalviolation = models.FloatField()
    raise60seclocalviolation = models.FloatField()
    raise6seclocalviolation = models.FloatField()
    lower5minlocalviolation = models.FloatField()
    lowerreglocalviolation = models.FloatField()
    lower60seclocalviolation = models.FloatField()
    lower6seclocalviolation = models.FloatField()
    raise5minviolation = models.FloatField()
    raiseregviolation = models.FloatField()
    raise60secviolation = models.FloatField()
    raise6secviolation = models.FloatField()
    lower5minviolation = models.FloatField()
    lowerregviolation = models.FloatField()
    lower60secviolation = models.FloatField()
    lower6secviolation = models.FloatField()
    raise6secrrp = models.FloatField()
    raise6secrop = models.FloatField()
    raise6secapcflag = models.IntegerField()
    raise60secrrp = models.FloatField()
    raise60secrop = models.FloatField()
    raise60secapcflag = models.IntegerField()
    raise5minrrp = models.FloatField()
    raise5minrop = models.FloatField()
    raise5minapcflag = models.IntegerField()
    raiseregrrp = models.FloatField()
    raiseregrop = models.FloatField()
    raiseregapcflag = models.IntegerField()
    lower6secrrp = models.FloatField()
    lower6secrop = models.FloatField()
    lower6secapcflag = models.IntegerField()
    lower60secrrp = models.FloatField()
    lower60secrop = models.FloatField()
    lower60secapcflag = models.IntegerField()
    lower5minrrp = models.FloatField()
    lower5minrop = models.FloatField()
    lower5minapcflag = models.IntegerField()
    lowerregrrp = models.FloatField()
    lowerregrop = models.FloatField()
    lowerregapcflag = models.IntegerField()
    raise6secactualavailability = models.FloatField()
    raise60secactualavailability = models.FloatField()
    raise5minactualavailability = models.FloatField()
    raiseregactualavailability = models.FloatField()
    lower6secactualavailability = models.FloatField()
    lower60secactualavailability = models.FloatField()
    lower5minactualavailability = models.FloatField()
    lowerregactualavailability = models.FloatField()
    lorsurplus = models.FloatField()
    lrcsurplus = models.FloatField()

    class Meta:
        managed = False
        db_table = 'dispatch_report_region_solution'
        app_label = 'reports'


class DispatchReportInterconnectorSolution(models.Model):
    row_id = models.IntegerField(primary_key=True)
    settlementdate = models.DateTimeField()
    runno = models.IntegerField()
    interconnectorid = models.CharField(max_length=10)
    intervention = models.IntegerField()
    meteredmwflow = models.FloatField()
    mwflow = models.FloatField()
    mwlosses = models.FloatField()
    marginalvalue = models.FloatField()
    violationdegree = models.FloatField()
    importlimit = models.FloatField()
    exportlimit = models.FloatField()
    marginalloss = models.FloatField()
    exportgenconid = models.CharField(max_length=20)
    importgenconid = models.CharField(max_length=20)
    fcasexportlimit = models.FloatField()
    fcasimportlimit = models.FloatField()

    class Meta:
        managed = False
        db_table = 'dispatch_report_interconnector_solution'
        app_label = 'reports'


class DispatchReportConstraintSolution(models.Model):
    row_id = models.IntegerField(primary_key=True)
    settlementdate = models.DateTimeField()
    runno = models.IntegerField()
    constraintid = models.CharField(max_length=20)
    intervention = models.IntegerField()
    rhs = models.FloatField()
    marginalvalue = models.FloatField()
    violationdegree = models.FloatField()

    class Meta:
        managed = False
        db_table = 'dispatch_report_constraint_solution'
        app_label = 'reports'


class P5MinCaseSolution(models.Model):
    row_id = models.IntegerField(primary_key=True)
    run_datetime = models.DateTimeField()
    startinterval_datetime = models.DateTimeField()
    intervention = models.IntegerField()
    totalobjective = models.FloatField()
    nonphysicallosses = models.IntegerField()
    totalareagenviolation = models.FloatField()
    totalinterconnectorviolation = models.FloatField()
    totalgenericviolation = models.FloatField()
    totalramprateviolation = models.FloatField()
    totalunitmwcapacityviolation = models.FloatField()
    total5minviolation = models.FloatField()
    totalregviolation = models.FloatField()
    total6secviolation = models.FloatField()
    total60secviolation = models.FloatField()
    totalenergyconstrviolation = models.FloatField()
    totalenergyofferviolation = models.FloatField()
    totalasprofileviolation = models.FloatField()
    totalfaststartviolation = models.FloatField()
    lastchanged = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'p5min_case_solution'
        app_label = 'reports'
