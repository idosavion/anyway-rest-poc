# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.contrib.gis.db import models


class AccidentHourRaw(models.Model):
    id = models.IntegerField(primary_key=True)
    year = models.IntegerField()
    provider_code = models.IntegerField()
    accident_hour_raw_hebrew = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'accident_hour_raw'
        unique_together = (('id', 'year', 'provider_code'),)


class AccidentMonth(models.Model):
    id = models.IntegerField(primary_key=True)
    year = models.IntegerField()
    provider_code = models.IntegerField()
    accident_month_hebrew = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'accident_month'
        unique_together = (('id', 'year', 'provider_code'),)


class AccidentSeverity(models.Model):
    id = models.IntegerField(primary_key=True)
    year = models.IntegerField()
    provider_code = models.IntegerField()
    accident_severity_hebrew = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'accident_severity'
        unique_together = (('id', 'year', 'provider_code'),)


class AccidentType(models.Model):
    id = models.IntegerField(primary_key=True)
    year = models.IntegerField()
    provider_code = models.IntegerField()
    accident_type_hebrew = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'accident_type'
        unique_together = (('id', 'year', 'provider_code'),)


class Addr(models.Model):
    gid = models.AutoField(primary_key=True)
    tlid = models.BigIntegerField(blank=True, null=True)
    fromhn = models.CharField(max_length=12, blank=True, null=True)
    tohn = models.CharField(max_length=12, blank=True, null=True)
    side = models.CharField(max_length=1, blank=True, null=True)
    zip = models.CharField(max_length=5, blank=True, null=True)
    plus4 = models.CharField(max_length=4, blank=True, null=True)
    fromtyp = models.CharField(max_length=1, blank=True, null=True)
    totyp = models.CharField(max_length=1, blank=True, null=True)
    fromarmid = models.IntegerField(blank=True, null=True)
    toarmid = models.IntegerField(blank=True, null=True)
    arid = models.CharField(max_length=22, blank=True, null=True)
    mtfcc = models.CharField(max_length=5, blank=True, null=True)
    statefp = models.CharField(max_length=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'addr'


class Addrfeat(models.Model):
    gid = models.AutoField(primary_key=True)
    tlid = models.BigIntegerField(blank=True, null=True)
    statefp = models.CharField(max_length=2)
    aridl = models.CharField(max_length=22, blank=True, null=True)
    aridr = models.CharField(max_length=22, blank=True, null=True)
    linearid = models.CharField(max_length=22, blank=True, null=True)
    fullname = models.CharField(max_length=100, blank=True, null=True)
    lfromhn = models.CharField(max_length=12, blank=True, null=True)
    ltohn = models.CharField(max_length=12, blank=True, null=True)
    rfromhn = models.CharField(max_length=12, blank=True, null=True)
    rtohn = models.CharField(max_length=12, blank=True, null=True)
    zipl = models.CharField(max_length=5, blank=True, null=True)
    zipr = models.CharField(max_length=5, blank=True, null=True)
    edge_mtfcc = models.CharField(max_length=5, blank=True, null=True)
    parityl = models.CharField(max_length=1, blank=True, null=True)
    parityr = models.CharField(max_length=1, blank=True, null=True)
    plus4l = models.CharField(max_length=4, blank=True, null=True)
    plus4r = models.CharField(max_length=4, blank=True, null=True)
    lfromtyp = models.CharField(max_length=1, blank=True, null=True)
    ltotyp = models.CharField(max_length=1, blank=True, null=True)
    rfromtyp = models.CharField(max_length=1, blank=True, null=True)
    rtotyp = models.CharField(max_length=1, blank=True, null=True)
    offsetl = models.CharField(max_length=1, blank=True, null=True)
    offsetr = models.CharField(max_length=1, blank=True, null=True)
    the_geom = models.LineStringField(srid=4269, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'addrfeat'


class AgeGroup(models.Model):
    id = models.IntegerField(primary_key=True)
    year = models.IntegerField()
    provider_code = models.IntegerField()
    age_group_hebrew = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'age_group'
        unique_together = (('id', 'year', 'provider_code'),)


class Bg(models.Model):
    gid = models.AutoField()
    statefp = models.CharField(max_length=2, blank=True, null=True)
    countyfp = models.CharField(max_length=3, blank=True, null=True)
    tractce = models.CharField(max_length=6, blank=True, null=True)
    blkgrpce = models.CharField(max_length=1, blank=True, null=True)
    bg_id = models.CharField(primary_key=True, max_length=12)
    namelsad = models.CharField(max_length=13, blank=True, null=True)
    mtfcc = models.CharField(max_length=5, blank=True, null=True)
    funcstat = models.CharField(max_length=1, blank=True, null=True)
    aland = models.FloatField(blank=True, null=True)
    awater = models.FloatField(blank=True, null=True)
    intptlat = models.CharField(max_length=11, blank=True, null=True)
    intptlon = models.CharField(max_length=12, blank=True, null=True)
    the_geom = models.MultiPolygonField(srid=4269, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bg'


class CasualtiesCosts(models.Model):
    id = models.IntegerField()
    injured_type = models.CharField(max_length=-1)
    injured_type_hebrew = models.CharField(max_length=-1)
    injuries_cost_k = models.IntegerField()
    year = models.IntegerField()
    data_source_hebrew = models.CharField(max_length=-1)

    class Meta:
        managed = False
        db_table = 'casualties_costs'


class Cities(models.Model):
    symbol_code = models.IntegerField()
    name = models.CharField(max_length=100)
    search_heb = models.CharField(unique=True, max_length=100)
    search_eng = models.CharField(max_length=100, blank=True, null=True)
    search_priority = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'cities'


class CitiesVehiclesRegistered(models.Model):
    id = models.IntegerField(blank=True, null=True)
    city_id = models.IntegerField(blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    name_eng = models.CharField(max_length=100, blank=True, null=True)
    search_name = models.CharField(max_length=100, blank=True, null=True)
    motorcycle = models.IntegerField(blank=True, null=True)
    special = models.IntegerField(blank=True, null=True)
    taxi = models.IntegerField(blank=True, null=True)
    bus = models.IntegerField(blank=True, null=True)
    minibus = models.IntegerField(blank=True, null=True)
    truck_over3500 = models.IntegerField(blank=True, null=True)
    truck_upto3500 = models.IntegerField(blank=True, null=True)
    private = models.IntegerField(blank=True, null=True)
    population_year = models.IntegerField(blank=True, null=True)
    population = models.IntegerField(blank=True, null=True)
    total = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cities_vehicles_registered'


class ColumnsDescription(models.Model):
    id = models.IntegerField(primary_key=True)
    year = models.IntegerField()
    provider_code = models.IntegerField()
    column_description = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'columns_description'
        unique_together = (('id', 'year', 'provider_code'),)


class County(models.Model):
    gid = models.AutoField(unique=True)
    statefp = models.CharField(max_length=2, blank=True, null=True)
    countyfp = models.CharField(max_length=3, blank=True, null=True)
    countyns = models.CharField(max_length=8, blank=True, null=True)
    cntyidfp = models.CharField(primary_key=True, max_length=5)
    name = models.CharField(max_length=100, blank=True, null=True)
    namelsad = models.CharField(max_length=100, blank=True, null=True)
    lsad = models.CharField(max_length=2, blank=True, null=True)
    classfp = models.CharField(max_length=2, blank=True, null=True)
    mtfcc = models.CharField(max_length=5, blank=True, null=True)
    csafp = models.CharField(max_length=3, blank=True, null=True)
    cbsafp = models.CharField(max_length=5, blank=True, null=True)
    metdivfp = models.CharField(max_length=5, blank=True, null=True)
    funcstat = models.CharField(max_length=1, blank=True, null=True)
    aland = models.BigIntegerField(blank=True, null=True)
    awater = models.FloatField(blank=True, null=True)
    intptlat = models.CharField(max_length=11, blank=True, null=True)
    intptlon = models.CharField(max_length=12, blank=True, null=True)
    the_geom = models.MultiPolygonField(srid=4269, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'county'


class CountyLookup(models.Model):
    st_code = models.IntegerField(primary_key=True)
    state = models.CharField(max_length=2, blank=True, null=True)
    co_code = models.IntegerField()
    name = models.CharField(max_length=90, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'county_lookup'
        unique_together = (('st_code', 'co_code'),)


class CountysubLookup(models.Model):
    st_code = models.IntegerField(primary_key=True)
    state = models.CharField(max_length=2, blank=True, null=True)
    co_code = models.IntegerField()
    county = models.CharField(max_length=90, blank=True, null=True)
    cs_code = models.IntegerField()
    name = models.CharField(max_length=90, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'countysub_lookup'
        unique_together = (('st_code', 'co_code', 'cs_code'),)


class Cousub(models.Model):
    gid = models.AutoField(unique=True)
    statefp = models.CharField(max_length=2, blank=True, null=True)
    countyfp = models.CharField(max_length=3, blank=True, null=True)
    cousubfp = models.CharField(max_length=5, blank=True, null=True)
    cousubns = models.CharField(max_length=8, blank=True, null=True)
    cosbidfp = models.CharField(primary_key=True, max_length=10)
    name = models.CharField(max_length=100, blank=True, null=True)
    namelsad = models.CharField(max_length=100, blank=True, null=True)
    lsad = models.CharField(max_length=2, blank=True, null=True)
    classfp = models.CharField(max_length=2, blank=True, null=True)
    mtfcc = models.CharField(max_length=5, blank=True, null=True)
    cnectafp = models.CharField(max_length=3, blank=True, null=True)
    nectafp = models.CharField(max_length=5, blank=True, null=True)
    nctadvfp = models.CharField(max_length=5, blank=True, null=True)
    funcstat = models.CharField(max_length=1, blank=True, null=True)
    aland = models.DecimalField(max_digits=14, decimal_places=0, blank=True, null=True)
    awater = models.DecimalField(max_digits=14, decimal_places=0, blank=True, null=True)
    intptlat = models.CharField(max_length=11, blank=True, null=True)
    intptlon = models.CharField(max_length=12, blank=True, null=True)
    the_geom = models.MultiPolygonField(srid=4269, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cousub'


class CrossDirection(models.Model):
    id = models.IntegerField(primary_key=True)
    year = models.IntegerField()
    provider_code = models.IntegerField()
    cross_direction_hebrew = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cross_direction'
        unique_together = (('id', 'year', 'provider_code'),)


class CrossLocation(models.Model):
    id = models.IntegerField(primary_key=True)
    year = models.IntegerField()
    provider_code = models.IntegerField()
    cross_location_hebrew = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cross_location'
        unique_together = (('id', 'year', 'provider_code'),)


class CrossMode(models.Model):
    id = models.IntegerField(primary_key=True)
    year = models.IntegerField()
    provider_code = models.IntegerField()
    cross_mode_hebrew = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cross_mode'
        unique_together = (('id', 'year', 'provider_code'),)


class DayInWeek(models.Model):
    id = models.IntegerField(primary_key=True)
    year = models.IntegerField()
    provider_code = models.IntegerField()
    day_in_week_hebrew = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'day_in_week'
        unique_together = (('id', 'year', 'provider_code'),)


class DayNight(models.Model):
    id = models.IntegerField(primary_key=True)
    year = models.IntegerField()
    provider_code = models.IntegerField()
    day_night_hebrew = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'day_night'
        unique_together = (('id', 'year', 'provider_code'),)


class DayType(models.Model):
    id = models.IntegerField(primary_key=True)
    year = models.IntegerField()
    provider_code = models.IntegerField()
    day_type_hebrew = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'day_type'
        unique_together = (('id', 'year', 'provider_code'),)


class DidntCross(models.Model):
    id = models.IntegerField(primary_key=True)
    year = models.IntegerField()
    provider_code = models.IntegerField()
    didnt_cross_hebrew = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'didnt_cross'
        unique_together = (('id', 'year', 'provider_code'),)


class DirectionLookup(models.Model):
    name = models.CharField(primary_key=True, max_length=20)
    abbrev = models.CharField(max_length=3, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'direction_lookup'


class Discussions(models.Model):
    id = models.BigIntegerField(blank=True, null=True)
    type = models.IntegerField(blank=True, null=True)
    title = models.CharField(max_length=100, blank=True, null=True)
    created = models.DateTimeField(blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    identifier = models.CharField(max_length=50, blank=True, null=True)
    geom = models.PointField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'discussions'


class District(models.Model):
    id = models.IntegerField(primary_key=True)
    year = models.IntegerField()
    provider_code = models.IntegerField()
    district_hebrew = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'district'
        unique_together = (('id', 'year', 'provider_code'),)


class DrivingDirections(models.Model):
    id = models.IntegerField(primary_key=True)
    year = models.IntegerField()
    provider_code = models.IntegerField()
    driving_directions_hebrew = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'driving_directions'
        unique_together = (('id', 'year', 'provider_code'),)


class Edges(models.Model):
    gid = models.AutoField(primary_key=True)
    statefp = models.CharField(max_length=2, blank=True, null=True)
    countyfp = models.CharField(max_length=3, blank=True, null=True)
    tlid = models.BigIntegerField(blank=True, null=True)
    tfidl = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    tfidr = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    mtfcc = models.CharField(max_length=5, blank=True, null=True)
    fullname = models.CharField(max_length=100, blank=True, null=True)
    smid = models.CharField(max_length=22, blank=True, null=True)
    lfromadd = models.CharField(max_length=12, blank=True, null=True)
    ltoadd = models.CharField(max_length=12, blank=True, null=True)
    rfromadd = models.CharField(max_length=12, blank=True, null=True)
    rtoadd = models.CharField(max_length=12, blank=True, null=True)
    zipl = models.CharField(max_length=5, blank=True, null=True)
    zipr = models.CharField(max_length=5, blank=True, null=True)
    featcat = models.CharField(max_length=1, blank=True, null=True)
    hydroflg = models.CharField(max_length=1, blank=True, null=True)
    railflg = models.CharField(max_length=1, blank=True, null=True)
    roadflg = models.CharField(max_length=1, blank=True, null=True)
    olfflg = models.CharField(max_length=1, blank=True, null=True)
    passflg = models.CharField(max_length=1, blank=True, null=True)
    divroad = models.CharField(max_length=1, blank=True, null=True)
    exttyp = models.CharField(max_length=1, blank=True, null=True)
    ttyp = models.CharField(max_length=1, blank=True, null=True)
    deckedroad = models.CharField(max_length=1, blank=True, null=True)
    artpath = models.CharField(max_length=1, blank=True, null=True)
    persist = models.CharField(max_length=1, blank=True, null=True)
    gcseflg = models.CharField(max_length=1, blank=True, null=True)
    offsetl = models.CharField(max_length=1, blank=True, null=True)
    offsetr = models.CharField(max_length=1, blank=True, null=True)
    tnidf = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    tnidt = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    the_geom = models.MultiLineStringField(srid=4269, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'edges'


class EmbeddedReports(models.Model):
    id = models.IntegerField(primary_key=True)
    report_name_english = models.CharField(max_length=-1)
    report_name_hebrew = models.CharField(max_length=-1, blank=True, null=True)
    url = models.CharField(max_length=-1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'embedded_reports'
        unique_together = (('id', 'report_name_english'),)


class EngineVolume(models.Model):
    id = models.IntegerField(primary_key=True)
    year = models.IntegerField()
    provider_code = models.IntegerField()
    engine_volume_hebrew = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'engine_volume'
        unique_together = (('id', 'year', 'provider_code'),)


class Faces(models.Model):
    gid = models.AutoField(primary_key=True)
    tfid = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    statefp00 = models.CharField(max_length=2, blank=True, null=True)
    countyfp00 = models.CharField(max_length=3, blank=True, null=True)
    tractce00 = models.CharField(max_length=6, blank=True, null=True)
    blkgrpce00 = models.CharField(max_length=1, blank=True, null=True)
    blockce00 = models.CharField(max_length=4, blank=True, null=True)
    cousubfp00 = models.CharField(max_length=5, blank=True, null=True)
    submcdfp00 = models.CharField(max_length=5, blank=True, null=True)
    conctyfp00 = models.CharField(max_length=5, blank=True, null=True)
    placefp00 = models.CharField(max_length=5, blank=True, null=True)
    aiannhfp00 = models.CharField(max_length=5, blank=True, null=True)
    aiannhce00 = models.CharField(max_length=4, blank=True, null=True)
    comptyp00 = models.CharField(max_length=1, blank=True, null=True)
    trsubfp00 = models.CharField(max_length=5, blank=True, null=True)
    trsubce00 = models.CharField(max_length=3, blank=True, null=True)
    anrcfp00 = models.CharField(max_length=5, blank=True, null=True)
    elsdlea00 = models.CharField(max_length=5, blank=True, null=True)
    scsdlea00 = models.CharField(max_length=5, blank=True, null=True)
    unsdlea00 = models.CharField(max_length=5, blank=True, null=True)
    uace00 = models.CharField(max_length=5, blank=True, null=True)
    cd108fp = models.CharField(max_length=2, blank=True, null=True)
    sldust00 = models.CharField(max_length=3, blank=True, null=True)
    sldlst00 = models.CharField(max_length=3, blank=True, null=True)
    vtdst00 = models.CharField(max_length=6, blank=True, null=True)
    zcta5ce00 = models.CharField(max_length=5, blank=True, null=True)
    tazce00 = models.CharField(max_length=6, blank=True, null=True)
    ugace00 = models.CharField(max_length=5, blank=True, null=True)
    puma5ce00 = models.CharField(max_length=5, blank=True, null=True)
    statefp = models.CharField(max_length=2, blank=True, null=True)
    countyfp = models.CharField(max_length=3, blank=True, null=True)
    tractce = models.CharField(max_length=6, blank=True, null=True)
    blkgrpce = models.CharField(max_length=1, blank=True, null=True)
    blockce = models.CharField(max_length=4, blank=True, null=True)
    cousubfp = models.CharField(max_length=5, blank=True, null=True)
    submcdfp = models.CharField(max_length=5, blank=True, null=True)
    conctyfp = models.CharField(max_length=5, blank=True, null=True)
    placefp = models.CharField(max_length=5, blank=True, null=True)
    aiannhfp = models.CharField(max_length=5, blank=True, null=True)
    aiannhce = models.CharField(max_length=4, blank=True, null=True)
    comptyp = models.CharField(max_length=1, blank=True, null=True)
    trsubfp = models.CharField(max_length=5, blank=True, null=True)
    trsubce = models.CharField(max_length=3, blank=True, null=True)
    anrcfp = models.CharField(max_length=5, blank=True, null=True)
    ttractce = models.CharField(max_length=6, blank=True, null=True)
    tblkgpce = models.CharField(max_length=1, blank=True, null=True)
    elsdlea = models.CharField(max_length=5, blank=True, null=True)
    scsdlea = models.CharField(max_length=5, blank=True, null=True)
    unsdlea = models.CharField(max_length=5, blank=True, null=True)
    uace = models.CharField(max_length=5, blank=True, null=True)
    cd111fp = models.CharField(max_length=2, blank=True, null=True)
    sldust = models.CharField(max_length=3, blank=True, null=True)
    sldlst = models.CharField(max_length=3, blank=True, null=True)
    vtdst = models.CharField(max_length=6, blank=True, null=True)
    zcta5ce = models.CharField(max_length=5, blank=True, null=True)
    tazce = models.CharField(max_length=6, blank=True, null=True)
    ugace = models.CharField(max_length=5, blank=True, null=True)
    puma5ce = models.CharField(max_length=5, blank=True, null=True)
    csafp = models.CharField(max_length=3, blank=True, null=True)
    cbsafp = models.CharField(max_length=5, blank=True, null=True)
    metdivfp = models.CharField(max_length=5, blank=True, null=True)
    cnectafp = models.CharField(max_length=3, blank=True, null=True)
    nectafp = models.CharField(max_length=5, blank=True, null=True)
    nctadvfp = models.CharField(max_length=5, blank=True, null=True)
    lwflag = models.CharField(max_length=1, blank=True, null=True)
    offset = models.CharField(max_length=1, blank=True, null=True)
    atotal = models.FloatField(blank=True, null=True)
    intptlat = models.CharField(max_length=11, blank=True, null=True)
    intptlon = models.CharField(max_length=12, blank=True, null=True)
    the_geom = models.MultiPolygonField(srid=4269, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'faces'


class Featnames(models.Model):
    gid = models.AutoField(primary_key=True)
    tlid = models.BigIntegerField(blank=True, null=True)
    fullname = models.CharField(max_length=100, blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    predirabrv = models.CharField(max_length=15, blank=True, null=True)
    pretypabrv = models.CharField(max_length=50, blank=True, null=True)
    prequalabr = models.CharField(max_length=15, blank=True, null=True)
    sufdirabrv = models.CharField(max_length=15, blank=True, null=True)
    suftypabrv = models.CharField(max_length=50, blank=True, null=True)
    sufqualabr = models.CharField(max_length=15, blank=True, null=True)
    predir = models.CharField(max_length=2, blank=True, null=True)
    pretyp = models.CharField(max_length=3, blank=True, null=True)
    prequal = models.CharField(max_length=2, blank=True, null=True)
    sufdir = models.CharField(max_length=2, blank=True, null=True)
    suftyp = models.CharField(max_length=3, blank=True, null=True)
    sufqual = models.CharField(max_length=2, blank=True, null=True)
    linearid = models.CharField(max_length=22, blank=True, null=True)
    mtfcc = models.CharField(max_length=5, blank=True, null=True)
    paflag = models.CharField(max_length=1, blank=True, null=True)
    statefp = models.CharField(max_length=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'featnames'


class GeoArea(models.Model):
    id = models.IntegerField(primary_key=True)
    year = models.IntegerField()
    provider_code = models.IntegerField()
    geo_area_hebrew = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'geo_area'
        unique_together = (('id', 'year', 'provider_code'),)


class GeocodeSettings(models.Model):
    name = models.TextField(primary_key=True)
    setting = models.TextField(blank=True, null=True)
    unit = models.TextField(blank=True, null=True)
    category = models.TextField(blank=True, null=True)
    short_desc = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'geocode_settings'


class GeocodeSettingsDefault(models.Model):
    name = models.TextField(primary_key=True)
    setting = models.TextField(blank=True, null=True)
    unit = models.TextField(blank=True, null=True)
    category = models.TextField(blank=True, null=True)
    short_desc = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'geocode_settings_default'


class HighlightMarkers(models.Model):
    id = models.IntegerField(blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    created = models.DateTimeField(blank=True, null=True)
    type = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'highlight_markers'


class HospitalTime(models.Model):
    id = models.IntegerField(primary_key=True)
    year = models.IntegerField()
    provider_code = models.IntegerField()
    hospital_time_hebrew = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hospital_time'
        unique_together = (('id', 'year', 'provider_code'),)


class InfographicsDataCache(models.Model):
    news_flash_id = models.BigIntegerField(primary_key=True)
    years_ago = models.IntegerField()
    data = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'infographics_data_cache'
        unique_together = (('news_flash_id', 'years_ago'), ('news_flash_id', 'years_ago'),)


class InfographicsDataCacheTemp(models.Model):
    news_flash_id = models.BigIntegerField(primary_key=True)
    years_ago = models.IntegerField()
    data = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'infographics_data_cache_temp'
        unique_together = (('news_flash_id', 'years_ago'),)


class InjuredAroundSchool(models.Model):
    id = models.BigAutoField(primary_key=True)
    school_id = models.IntegerField(blank=True, null=True)
    school_name = models.TextField(blank=True, null=True)
    school_type = models.TextField(blank=True, null=True)
    school_longitude = models.FloatField(blank=True, null=True)
    school_latitude = models.FloatField(blank=True, null=True)
    school_yishuv_name = models.TextField(blank=True, null=True)
    school_anyway_link = models.TextField(blank=True, null=True)
    accident_year = models.IntegerField(blank=True, null=True)
    distance_in_km = models.FloatField(blank=True, null=True)
    killed_count = models.IntegerField(blank=True, null=True)
    light_injured_count = models.IntegerField(blank=True, null=True)
    rank_in_yishuv = models.IntegerField(blank=True, null=True)
    severly_injured_count = models.IntegerField(blank=True, null=True)
    total_injured_killed_count = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'injured_around_school'


class InjuredAroundSchoolAllData(models.Model):
    id = models.BigAutoField(primary_key=True)
    school_id = models.FloatField()
    markers_provider_and_id = models.BigIntegerField(blank=True, null=True)
    markers_provider_code = models.FloatField(blank=True, null=True)
    markers_description = models.TextField(blank=True, null=True)
    markers_accident_type = models.FloatField(blank=True, null=True)
    markers_accident_severity = models.FloatField(blank=True, null=True)
    markers_address = models.TextField(blank=True, null=True)
    markers_location_accuracy = models.FloatField(blank=True, null=True)
    markers_road_type = models.FloatField(blank=True, null=True)
    markers_road_shape = models.FloatField(blank=True, null=True)
    markers_day_type = models.FloatField(blank=True, null=True)
    markers_police_unit = models.FloatField(blank=True, null=True)
    markers_mainstreet = models.TextField(db_column='markers_mainStreet', blank=True, null=True)  # Field name made lowercase.
    markers_secondarystreet = models.TextField(db_column='markers_secondaryStreet', blank=True, null=True)  # Field name made lowercase.
    markers_junction = models.TextField(blank=True, null=True)
    markers_one_lane = models.FloatField(blank=True, null=True)
    markers_multi_lane = models.FloatField(blank=True, null=True)
    markers_speed_limit = models.FloatField(blank=True, null=True)
    markers_road_intactness = models.FloatField(blank=True, null=True)
    markers_road_width = models.FloatField(blank=True, null=True)
    markers_road_sign = models.FloatField(blank=True, null=True)
    markers_road_light = models.FloatField(blank=True, null=True)
    markers_road_control = models.FloatField(blank=True, null=True)
    markers_weather = models.FloatField(blank=True, null=True)
    markers_road_surface = models.FloatField(blank=True, null=True)
    markers_road_object = models.FloatField(blank=True, null=True)
    markers_object_distance = models.FloatField(blank=True, null=True)
    markers_didnt_cross = models.FloatField(blank=True, null=True)
    markers_cross_mode = models.FloatField(blank=True, null=True)
    markers_cross_location = models.FloatField(blank=True, null=True)
    markers_cross_direction = models.FloatField(blank=True, null=True)
    markers_video_link = models.TextField(blank=True, null=True)
    markers_road1 = models.FloatField(blank=True, null=True)
    markers_road2 = models.FloatField(blank=True, null=True)
    markers_km = models.FloatField(blank=True, null=True)
    markers_yishuv_symbol = models.FloatField(blank=True, null=True)
    markers_yishuv_name = models.TextField(blank=True, null=True)
    markers_geo_area = models.FloatField(blank=True, null=True)
    markers_day_night = models.FloatField(blank=True, null=True)
    markers_day_in_week = models.FloatField(blank=True, null=True)
    markers_traffic_light = models.FloatField(blank=True, null=True)
    markers_region = models.FloatField(blank=True, null=True)
    markers_district = models.FloatField(blank=True, null=True)
    markers_natural_area = models.FloatField(blank=True, null=True)
    markers_municipal_status = models.FloatField(blank=True, null=True)
    markers_yishuv_shape = models.FloatField(blank=True, null=True)
    markers_street1 = models.FloatField(blank=True, null=True)
    markers_street1_hebrew = models.TextField(blank=True, null=True)
    markers_street2 = models.FloatField(blank=True, null=True)
    markers_street2_hebrew = models.TextField(blank=True, null=True)
    markers_urban_intersection = models.FloatField(blank=True, null=True)
    markers_non_urban_intersection = models.FloatField(blank=True, null=True)
    markers_non_urban_intersection_hebrew = models.TextField(blank=True, null=True)
    markers_accident_year = models.FloatField(blank=True, null=True)
    markers_accident_month = models.FloatField(blank=True, null=True)
    markers_accident_day = models.FloatField(blank=True, null=True)
    markers_accident_hour_raw = models.FloatField(blank=True, null=True)
    markers_accident_hour = models.FloatField(blank=True, null=True)
    markers_accident_minute = models.FloatField(blank=True, null=True)
    markers_x = models.FloatField(blank=True, null=True)
    markers_y = models.FloatField(blank=True, null=True)
    markers_vehicle_type_rsa = models.TextField(blank=True, null=True)
    markers_violation_type_rsa = models.TextField(blank=True, null=True)
    markers_geom = models.PointField(srid=0, blank=True, null=True)
    involved_provider_and_id = models.BigIntegerField(blank=True, null=True)
    involved_provider_code = models.FloatField(blank=True, null=True)
    involved_accident_id = models.BigIntegerField(blank=True, null=True)
    involved_involved_type = models.FloatField(blank=True, null=True)
    involved_license_acquiring_date = models.FloatField(blank=True, null=True)
    involved_age_group = models.FloatField(blank=True, null=True)
    involved_sex = models.FloatField(blank=True, null=True)
    involved_vehicle_type = models.FloatField(blank=True, null=True)
    involved_safety_measures = models.FloatField(blank=True, null=True)
    involved_involve_yishuv_symbol = models.FloatField(blank=True, null=True)
    involved_involve_yishuv_name = models.TextField(blank=True, null=True)
    involved_injury_severity = models.FloatField(blank=True, null=True)
    involved_injured_type = models.FloatField(blank=True, null=True)
    involved_injured_position = models.FloatField(blank=True, null=True)
    involved_population_type = models.FloatField(blank=True, null=True)
    involved_home_region = models.FloatField(blank=True, null=True)
    involved_home_district = models.FloatField(blank=True, null=True)
    involved_home_natural_area = models.FloatField(blank=True, null=True)
    involved_home_municipal_status = models.FloatField(blank=True, null=True)
    involved_hospital_time = models.FloatField(blank=True, null=True)
    involved_medical_type = models.FloatField(blank=True, null=True)
    involved_release_dest = models.FloatField(blank=True, null=True)
    involved_safety_measures_use = models.FloatField(blank=True, null=True)
    involved_late_deceased = models.FloatField(blank=True, null=True)
    involved_car_id = models.FloatField(blank=True, null=True)
    involved_involve_id = models.FloatField(blank=True, null=True)
    involved_accident_year = models.FloatField(blank=True, null=True)
    involved_accident_month = models.FloatField(blank=True, null=True)
    involved_injury_severity_mais = models.FloatField(blank=True, null=True)
    involved_home_yishuv_shape = models.FloatField(blank=True, null=True)
    markers_house_number = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'injured_around_school_all_data'


class InjuredPosition(models.Model):
    id = models.IntegerField(primary_key=True)
    year = models.IntegerField()
    provider_code = models.IntegerField()
    injured_position_hebrew = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'injured_position'
        unique_together = (('id', 'year', 'provider_code'),)


class InjuredType(models.Model):
    id = models.IntegerField(primary_key=True)
    year = models.IntegerField()
    provider_code = models.IntegerField()
    injured_type_hebrew = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'injured_type'
        unique_together = (('id', 'year', 'provider_code'),)


class InjurySeverity(models.Model):
    id = models.IntegerField(primary_key=True)
    year = models.IntegerField()
    provider_code = models.IntegerField()
    injury_severity_hebrew = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'injury_severity'
        unique_together = (('id', 'year', 'provider_code'),)


class Involved(models.Model):
    provider_code = models.IntegerField(blank=True, null=True)
    accident = models.ForeignKey('Markers', models.DO_NOTHING, blank=True, null=True)
    involved_type = models.IntegerField(blank=True, null=True)
    license_acquiring_date = models.IntegerField(blank=True, null=True)
    age_group = models.IntegerField(blank=True, null=True)
    sex = models.IntegerField(blank=True, null=True)
    safety_measures = models.IntegerField(blank=True, null=True)
    injury_severity = models.IntegerField(blank=True, null=True)
    injured_type = models.IntegerField(blank=True, null=True)
    injured_position = models.IntegerField(blank=True, null=True)
    population_type = models.IntegerField(blank=True, null=True)
    home_district = models.IntegerField(blank=True, null=True)
    home_municipal_status = models.IntegerField(blank=True, null=True)
    hospital_time = models.IntegerField(blank=True, null=True)
    medical_type = models.IntegerField(blank=True, null=True)
    release_dest = models.IntegerField(blank=True, null=True)
    safety_measures_use = models.IntegerField(blank=True, null=True)
    late_deceased = models.IntegerField(blank=True, null=True)
    accident_month = models.IntegerField(blank=True, null=True)
    accident_year = models.IntegerField(blank=True, null=True)
    car_id = models.IntegerField(blank=True, null=True)
    home_natural_area = models.IntegerField(blank=True, null=True)
    home_region = models.IntegerField(blank=True, null=True)
    involve_id = models.IntegerField(blank=True, null=True)
    involve_yishuv_symbol = models.IntegerField(blank=True, null=True)
    provider_and_id = models.BigIntegerField(blank=True, null=True)
    involve_yishuv_name = models.TextField(blank=True, null=True)
    vehicle_type = models.IntegerField(blank=True, null=True)
    injury_severity_mais = models.IntegerField(blank=True, null=True)
    home_yishuv_shape = models.IntegerField(blank=True, null=True)
    file_type_police = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'involved'


class InvolvedType(models.Model):
    id = models.IntegerField(primary_key=True)
    year = models.IntegerField()
    provider_code = models.IntegerField()
    involved_type_hebrew = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'involved_type'
        unique_together = (('id', 'year', 'provider_code'),)


class LateDeceased(models.Model):
    id = models.IntegerField(primary_key=True)
    year = models.IntegerField()
    provider_code = models.IntegerField()
    late_deceased_hebrew = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'late_deceased'
        unique_together = (('id', 'year', 'provider_code'),)


class LoaderLookuptables(models.Model):
    process_order = models.IntegerField()
    lookup_name = models.TextField(primary_key=True)
    table_name = models.TextField(blank=True, null=True)
    single_mode = models.BooleanField()
    load = models.BooleanField()
    level_county = models.BooleanField()
    level_state = models.BooleanField()
    level_nation = models.BooleanField()
    post_load_process = models.TextField(blank=True, null=True)
    single_geom_mode = models.BooleanField(blank=True, null=True)
    insert_mode = models.CharField(max_length=1)
    pre_load_process = models.TextField(blank=True, null=True)
    columns_exclude = models.TextField(blank=True, null=True)  # This field type is a guess.
    website_root_override = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'loader_lookuptables'


class LoaderPlatform(models.Model):
    os = models.CharField(primary_key=True, max_length=50)
    declare_sect = models.TextField(blank=True, null=True)
    pgbin = models.TextField(blank=True, null=True)
    wget = models.TextField(blank=True, null=True)
    unzip_command = models.TextField(blank=True, null=True)
    psql = models.TextField(blank=True, null=True)
    path_sep = models.TextField(blank=True, null=True)
    loader = models.TextField(blank=True, null=True)
    environ_set_command = models.TextField(blank=True, null=True)
    county_process_command = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'loader_platform'


class LoaderVariables(models.Model):
    tiger_year = models.CharField(primary_key=True, max_length=4)
    website_root = models.TextField(blank=True, null=True)
    staging_fold = models.TextField(blank=True, null=True)
    data_schema = models.TextField(blank=True, null=True)
    staging_schema = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'loader_variables'


class LocationAccuracy(models.Model):
    id = models.IntegerField(primary_key=True)
    year = models.IntegerField()
    provider_code = models.IntegerField()
    location_accuracy_hebrew = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'location_accuracy'
        unique_together = (('id', 'year', 'provider_code'),)


class Markers(models.Model):
    id = models.IntegerField(primary_key=True)
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    type = models.IntegerField(blank=True, null=True)
    title = models.CharField(max_length=100, blank=True, null=True)
    created = models.DateTimeField(blank=True, null=True)
    provider_code = models.IntegerField()
    description = models.TextField(blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    mainstreet = models.TextField(db_column='mainStreet', blank=True, null=True)  # Field name made lowercase.
    secondarystreet = models.TextField(db_column='secondaryStreet', blank=True, null=True)  # Field name made lowercase.
    junction = models.TextField(blank=True, null=True)
    one_lane = models.IntegerField(blank=True, null=True)
    multi_lane = models.IntegerField(blank=True, null=True)
    speed_limit = models.IntegerField(blank=True, null=True)
    road_width = models.IntegerField(blank=True, null=True)
    road_sign = models.IntegerField(blank=True, null=True)
    road_light = models.IntegerField(blank=True, null=True)
    road_control = models.IntegerField(blank=True, null=True)
    weather = models.IntegerField(blank=True, null=True)
    road_surface = models.IntegerField(blank=True, null=True)
    road_object = models.IntegerField(blank=True, null=True)
    object_distance = models.IntegerField(blank=True, null=True)
    didnt_cross = models.IntegerField(blank=True, null=True)
    cross_mode = models.IntegerField(blank=True, null=True)
    cross_location = models.IntegerField(blank=True, null=True)
    cross_direction = models.IntegerField(blank=True, null=True)
    video_link = models.TextField(blank=True, null=True)
    km = models.FloatField(blank=True, null=True)
    road1 = models.IntegerField(blank=True, null=True)
    road2 = models.IntegerField(blank=True, null=True)
    day_in_week = models.IntegerField(blank=True, null=True)
    day_night = models.IntegerField(blank=True, null=True)
    district = models.IntegerField(blank=True, null=True)
    geo_area = models.IntegerField(blank=True, null=True)
    natural_area = models.IntegerField(blank=True, null=True)
    region = models.IntegerField(blank=True, null=True)
    traffic_light = models.IntegerField(blank=True, null=True)
    yishuv_shape = models.IntegerField(blank=True, null=True)
    yishuv_symbol = models.IntegerField(blank=True, null=True)
    geom = models.PointField(blank=True, null=True)
    accident_day = models.IntegerField(blank=True, null=True)
    accident_hour = models.IntegerField(blank=True, null=True)
    accident_hour_raw = models.IntegerField(blank=True, null=True)
    accident_minute = models.IntegerField(blank=True, null=True)
    accident_month = models.IntegerField(blank=True, null=True)
    accident_year = models.IntegerField()
    non_urban_intersection = models.IntegerField(blank=True, null=True)
    provider_and_id = models.BigIntegerField(blank=True, null=True)
    street1 = models.IntegerField(blank=True, null=True)
    street2 = models.IntegerField(blank=True, null=True)
    urban_intersection = models.IntegerField(blank=True, null=True)
    accident_severity = models.IntegerField(blank=True, null=True)
    accident_type = models.IntegerField(blank=True, null=True)
    day_type = models.IntegerField(blank=True, null=True)
    location_accuracy = models.IntegerField(blank=True, null=True)
    non_urban_intersection_hebrew = models.TextField(blank=True, null=True)
    police_unit = models.IntegerField(blank=True, null=True)
    road_intactness = models.IntegerField(blank=True, null=True)
    road_shape = models.IntegerField(blank=True, null=True)
    road_type = models.IntegerField(blank=True, null=True)
    street1_hebrew = models.TextField(blank=True, null=True)
    street2_hebrew = models.TextField(blank=True, null=True)
    yishuv_name = models.TextField(blank=True, null=True)
    x = models.FloatField(blank=True, null=True)
    y = models.FloatField(blank=True, null=True)
    municipal_status = models.IntegerField(blank=True, null=True)
    vehicle_type_rsa = models.TextField(blank=True, null=True)
    violation_type_rsa = models.TextField(blank=True, null=True)
    house_number = models.IntegerField(blank=True, null=True)
    file_type_police = models.IntegerField(blank=True, null=True)
    km_accurate = models.BooleanField(blank=True, null=True)
    km_raw = models.TextField(blank=True, null=True)
    non_urban_intersection_by_junction_number = models.TextField(blank=True, null=True)
    rsa_severity = models.IntegerField(blank=True, null=True)
    rsa_license_plate = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'markers'
        unique_together = (('id', 'provider_code', 'accident_year'),)


class MedicalType(models.Model):
    id = models.IntegerField(primary_key=True)
    year = models.IntegerField()
    provider_code = models.IntegerField()
    medical_type_hebrew = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'medical_type'
        unique_together = (('id', 'year', 'provider_code'),)


class MultiLane(models.Model):
    id = models.IntegerField(primary_key=True)
    year = models.IntegerField()
    provider_code = models.IntegerField()
    multi_lane_hebrew = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'multi_lane'
        unique_together = (('id', 'year', 'provider_code'),)


class MunicipalStatus(models.Model):
    id = models.IntegerField(primary_key=True)
    year = models.IntegerField()
    provider_code = models.IntegerField()
    municipal_status_hebrew = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'municipal_status'
        unique_together = (('id', 'year', 'provider_code'),)


class Municipalities(models.Model):
    id = models.BigAutoField(primary_key=True)
    heb_name = models.CharField(max_length=100)
    eng_name = models.CharField(max_length=100, blank=True, null=True)
    polygon = models.PolygonField(srid=0)
    symbol = models.IntegerField(blank=True, null=True)
    osm_id = models.IntegerField(blank=True, null=True)
    file_name = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'municipalities'


class NaturalArea(models.Model):
    id = models.IntegerField(primary_key=True)
    year = models.IntegerField()
    provider_code = models.IntegerField()
    natural_area_hebrew = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'natural_area'
        unique_together = (('id', 'year', 'provider_code'),)


class NewsFlash(models.Model):
    id = models.BigAutoField(primary_key=True)
    accident = models.BooleanField()
    author = models.TextField(blank=True, null=True)
    date = models.DateTimeField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    lat = models.FloatField(blank=True, null=True)
    link = models.TextField(blank=True, null=True)
    lon = models.FloatField(blank=True, null=True)
    title = models.TextField(blank=True, null=True)
    source = models.TextField(blank=True, null=True)
    location = models.TextField(blank=True, null=True)
    road1 = models.IntegerField(blank=True, null=True)
    road2 = models.IntegerField(blank=True, null=True)
    resolution = models.TextField(blank=True, null=True)
    tweet_id = models.BigIntegerField(blank=True, null=True)
    district_hebrew = models.TextField(blank=True, null=True)
    non_urban_intersection_hebrew = models.TextField(blank=True, null=True)
    region_hebrew = models.TextField(blank=True, null=True)
    road_segment_name = models.TextField(blank=True, null=True)
    street1_hebrew = models.TextField(blank=True, null=True)
    street2_hebrew = models.TextField(blank=True, null=True)
    yishuv_name = models.TextField(blank=True, null=True)
    organization = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'news_flash'


class ObjectDistance(models.Model):
    id = models.IntegerField(primary_key=True)
    year = models.IntegerField()
    provider_code = models.IntegerField()
    object_distance_hebrew = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'object_distance'
        unique_together = (('id', 'year', 'provider_code'),)


class OneLane(models.Model):
    id = models.IntegerField(primary_key=True)
    year = models.IntegerField()
    provider_code = models.IntegerField()
    one_lane_hebrew = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'one_lane'
        unique_together = (('id', 'year', 'provider_code'),)


class PagcGaz(models.Model):
    seq = models.IntegerField(blank=True, null=True)
    word = models.TextField(blank=True, null=True)
    stdword = models.TextField(blank=True, null=True)
    token = models.IntegerField(blank=True, null=True)
    is_custom = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'pagc_gaz'


class PagcLex(models.Model):
    seq = models.IntegerField(blank=True, null=True)
    word = models.TextField(blank=True, null=True)
    stdword = models.TextField(blank=True, null=True)
    token = models.IntegerField(blank=True, null=True)
    is_custom = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'pagc_lex'


class PagcRules(models.Model):
    rule = models.TextField(blank=True, null=True)
    is_custom = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pagc_rules'


class Place(models.Model):
    gid = models.AutoField(unique=True)
    statefp = models.CharField(max_length=2, blank=True, null=True)
    placefp = models.CharField(max_length=5, blank=True, null=True)
    placens = models.CharField(max_length=8, blank=True, null=True)
    plcidfp = models.CharField(primary_key=True, max_length=7)
    name = models.CharField(max_length=100, blank=True, null=True)
    namelsad = models.CharField(max_length=100, blank=True, null=True)
    lsad = models.CharField(max_length=2, blank=True, null=True)
    classfp = models.CharField(max_length=2, blank=True, null=True)
    cpi = models.CharField(max_length=1, blank=True, null=True)
    pcicbsa = models.CharField(max_length=1, blank=True, null=True)
    pcinecta = models.CharField(max_length=1, blank=True, null=True)
    mtfcc = models.CharField(max_length=5, blank=True, null=True)
    funcstat = models.CharField(max_length=1, blank=True, null=True)
    aland = models.BigIntegerField(blank=True, null=True)
    awater = models.BigIntegerField(blank=True, null=True)
    intptlat = models.CharField(max_length=11, blank=True, null=True)
    intptlon = models.CharField(max_length=12, blank=True, null=True)
    the_geom = models.MultiPolygonField(srid=4269, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'place'


class PlaceLookup(models.Model):
    st_code = models.IntegerField(primary_key=True)
    state = models.CharField(max_length=2, blank=True, null=True)
    pl_code = models.IntegerField()
    name = models.CharField(max_length=90, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'place_lookup'
        unique_together = (('st_code', 'pl_code'),)


class PoliceUnit(models.Model):
    id = models.IntegerField(primary_key=True)
    year = models.IntegerField()
    provider_code = models.IntegerField()
    police_unit_hebrew = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'police_unit'
        unique_together = (('id', 'year', 'provider_code'),)


class PopulationType(models.Model):
    id = models.IntegerField(primary_key=True)
    year = models.IntegerField()
    provider_code = models.IntegerField()
    population_type_hebrew = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'population_type'
        unique_together = (('id', 'year', 'provider_code'),)


class ProviderCode(models.Model):
    provider_code_hebrew = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'provider_code'


class Region(models.Model):
    id = models.IntegerField(primary_key=True)
    year = models.IntegerField()
    provider_code = models.IntegerField()
    region_hebrew = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'region'
        unique_together = (('id', 'year', 'provider_code'),)


class ReleaseDest(models.Model):
    id = models.IntegerField(primary_key=True)
    year = models.IntegerField()
    provider_code = models.IntegerField()
    release_dest_hebrew = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'release_dest'
        unique_together = (('id', 'year', 'provider_code'),)


class ReportProblem(models.Model):
    id = models.BigAutoField(primary_key=True)
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    problem_description = models.TextField(blank=True, null=True)
    signs_on_the_road_not_clear = models.BooleanField(blank=True, null=True)
    signs_problem = models.BooleanField(blank=True, null=True)
    pothole = models.BooleanField(blank=True, null=True)
    no_light = models.BooleanField(blank=True, null=True)
    no_sign = models.BooleanField(blank=True, null=True)
    crossing_missing = models.BooleanField(blank=True, null=True)
    sidewalk_is_blocked = models.BooleanField(blank=True, null=True)
    street_light_issue = models.BooleanField(blank=True, null=True)
    road_hazard = models.BooleanField(blank=True, null=True)
    first_name = models.CharField(max_length=50, blank=True, null=True)
    last_name = models.CharField(max_length=50, blank=True, null=True)
    phone_number = models.CharField(max_length=50, blank=True, null=True)
    email = models.CharField(max_length=100, blank=True, null=True)
    send_to_municipality = models.BooleanField(blank=True, null=True)
    image_data = models.CharField(max_length=-1, blank=True, null=True)
    personal_id = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'report_problem'


class RoadControl(models.Model):
    id = models.IntegerField(primary_key=True)
    year = models.IntegerField()
    provider_code = models.IntegerField()
    road_control_hebrew = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'road_control'
        unique_together = (('id', 'year', 'provider_code'),)


class RoadIntactness(models.Model):
    id = models.IntegerField(primary_key=True)
    year = models.IntegerField()
    provider_code = models.IntegerField()
    road_intactness_hebrew = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'road_intactness'
        unique_together = (('id', 'year', 'provider_code'),)


class RoadLight(models.Model):
    id = models.IntegerField(primary_key=True)
    year = models.IntegerField()
    provider_code = models.IntegerField()
    road_light_hebrew = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'road_light'
        unique_together = (('id', 'year', 'provider_code'),)


class RoadObject(models.Model):
    id = models.IntegerField(primary_key=True)
    year = models.IntegerField()
    provider_code = models.IntegerField()
    road_object_hebrew = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'road_object'
        unique_together = (('id', 'year', 'provider_code'),)


class RoadSegments(models.Model):
    segment_id = models.IntegerField(blank=True, null=True)
    road = models.IntegerField(blank=True, null=True)
    segment = models.IntegerField(blank=True, null=True)
    from_km = models.FloatField(blank=True, null=True)
    from_name = models.TextField(blank=True, null=True)
    to_km = models.FloatField(blank=True, null=True)
    to_name = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'road_segments'


class RoadShape(models.Model):
    id = models.IntegerField(primary_key=True)
    year = models.IntegerField()
    provider_code = models.IntegerField()
    road_shape_hebrew = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'road_shape'
        unique_together = (('id', 'year', 'provider_code'),)


class RoadSign(models.Model):
    id = models.IntegerField(primary_key=True)
    year = models.IntegerField()
    provider_code = models.IntegerField()
    road_sign_hebrew = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'road_sign'
        unique_together = (('id', 'year', 'provider_code'),)


class RoadSurface(models.Model):
    id = models.IntegerField(primary_key=True)
    year = models.IntegerField()
    provider_code = models.IntegerField()
    road_surface_hebrew = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'road_surface'
        unique_together = (('id', 'year', 'provider_code'),)


class RoadType(models.Model):
    id = models.IntegerField(primary_key=True)
    year = models.IntegerField()
    provider_code = models.IntegerField()
    road_type_hebrew = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'road_type'
        unique_together = (('id', 'year', 'provider_code'),)


class RoadWidth(models.Model):
    id = models.IntegerField(primary_key=True)
    year = models.IntegerField()
    provider_code = models.IntegerField()
    road_width_hebrew = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'road_width'
        unique_together = (('id', 'year', 'provider_code'),)


class SafetyMeasures(models.Model):
    id = models.IntegerField(primary_key=True)
    year = models.IntegerField()
    provider_code = models.IntegerField()
    safety_measures_hebrew = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'safety_measures'
        unique_together = (('id', 'year', 'provider_code'),)


class SafetyMeasuresUse(models.Model):
    id = models.IntegerField(primary_key=True)
    year = models.IntegerField()
    provider_code = models.IntegerField()
    safety_measures_use_hebrew = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'safety_measures_use'
        unique_together = (('id', 'year', 'provider_code'),)


class Schools(models.Model):
    id = models.BigAutoField(primary_key=True)
    fcode_type = models.IntegerField(blank=True, null=True)
    yishuv_symbol = models.IntegerField(blank=True, null=True)
    yishuv_name = models.TextField(blank=True, null=True)
    school_name = models.TextField(blank=True, null=True)
    school_latin_name = models.TextField(blank=True, null=True)
    usg = models.IntegerField(blank=True, null=True)
    usg_code = models.IntegerField(blank=True, null=True)
    e_ord = models.FloatField(blank=True, null=True)
    n_ord = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    geom = models.PointField(blank=True, null=True)
    data_year = models.IntegerField(blank=True, null=True)
    prdct_ver = models.DateTimeField(blank=True, null=True)
    x = models.FloatField(blank=True, null=True)
    y = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'schools'


class SchoolsWithDescription(models.Model):
    id = models.BigAutoField(primary_key=True)
    data_year = models.IntegerField(blank=True, null=True)
    school_id = models.IntegerField(blank=True, null=True)
    school_name = models.TextField(blank=True, null=True)
    students_number = models.IntegerField(blank=True, null=True)
    municipality_name = models.TextField(blank=True, null=True)
    yishuv_name = models.TextField(blank=True, null=True)
    sector = models.TextField(blank=True, null=True)
    inspection = models.TextField(blank=True, null=True)
    legal_status = models.TextField(blank=True, null=True)
    reporter = models.TextField(blank=True, null=True)
    geo_district = models.TextField(blank=True, null=True)
    education_type = models.TextField(blank=True, null=True)
    school_type = models.TextField(blank=True, null=True)
    institution_type = models.TextField(blank=True, null=True)
    lowest_grade = models.IntegerField(blank=True, null=True)
    highest_grade = models.IntegerField(blank=True, null=True)
    foundation_year = models.IntegerField(blank=True, null=True)
    location_accuracy = models.TextField(blank=True, null=True)
    geom = models.PointField(blank=True, null=True)
    x = models.FloatField(blank=True, null=True)
    y = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'schools_with_description'


class SchoolsWithDescription2020(models.Model):
    id = models.BigAutoField(primary_key=True)
    school_id = models.IntegerField(blank=True, null=True)
    school_name = models.TextField(blank=True, null=True)
    municipality_name = models.TextField(blank=True, null=True)
    yishuv_name = models.TextField(blank=True, null=True)
    institution_type = models.TextField(blank=True, null=True)
    lowest_grade = models.TextField(blank=True, null=True)
    highest_grade = models.TextField(blank=True, null=True)
    location_accuracy = models.TextField(blank=True, null=True)
    geom = models.PointField(blank=True, null=True)
    x = models.FloatField(blank=True, null=True)
    y = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'schools_with_description2020'


class SecondaryUnitLookup(models.Model):
    name = models.CharField(primary_key=True, max_length=20)
    abbrev = models.CharField(max_length=5, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'secondary_unit_lookup'


class Sex(models.Model):
    id = models.IntegerField(primary_key=True)
    year = models.IntegerField()
    provider_code = models.IntegerField()
    sex_hebrew = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sex'
        unique_together = (('id', 'year', 'provider_code'),)


class SpeedLimit(models.Model):
    id = models.IntegerField(primary_key=True)
    year = models.IntegerField()
    provider_code = models.IntegerField()
    speed_limit_hebrew = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'speed_limit'
        unique_together = (('id', 'year', 'provider_code'),)


class State(models.Model):
    gid = models.AutoField(unique=True)
    region = models.CharField(max_length=2, blank=True, null=True)
    division = models.CharField(max_length=2, blank=True, null=True)
    statefp = models.CharField(primary_key=True, max_length=2)
    statens = models.CharField(max_length=8, blank=True, null=True)
    stusps = models.CharField(unique=True, max_length=2)
    name = models.CharField(max_length=100, blank=True, null=True)
    lsad = models.CharField(max_length=2, blank=True, null=True)
    mtfcc = models.CharField(max_length=5, blank=True, null=True)
    funcstat = models.CharField(max_length=1, blank=True, null=True)
    aland = models.BigIntegerField(blank=True, null=True)
    awater = models.BigIntegerField(blank=True, null=True)
    intptlat = models.CharField(max_length=11, blank=True, null=True)
    intptlon = models.CharField(max_length=12, blank=True, null=True)
    the_geom = models.MultiPolygonField(srid=4269, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'state'


class StateLookup(models.Model):
    st_code = models.IntegerField(primary_key=True)
    name = models.CharField(unique=True, max_length=40, blank=True, null=True)
    abbrev = models.CharField(unique=True, max_length=3, blank=True, null=True)
    statefp = models.CharField(unique=True, max_length=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'state_lookup'


class StreetTypeLookup(models.Model):
    name = models.CharField(primary_key=True, max_length=50)
    abbrev = models.CharField(max_length=50, blank=True, null=True)
    is_hw = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'street_type_lookup'


class Tabblock(models.Model):
    gid = models.AutoField()
    statefp = models.CharField(max_length=2, blank=True, null=True)
    countyfp = models.CharField(max_length=3, blank=True, null=True)
    tractce = models.CharField(max_length=6, blank=True, null=True)
    blockce = models.CharField(max_length=4, blank=True, null=True)
    tabblock_id = models.CharField(primary_key=True, max_length=16)
    name = models.CharField(max_length=20, blank=True, null=True)
    mtfcc = models.CharField(max_length=5, blank=True, null=True)
    ur = models.CharField(max_length=1, blank=True, null=True)
    uace = models.CharField(max_length=5, blank=True, null=True)
    funcstat = models.CharField(max_length=1, blank=True, null=True)
    aland = models.FloatField(blank=True, null=True)
    awater = models.FloatField(blank=True, null=True)
    intptlat = models.CharField(max_length=11, blank=True, null=True)
    intptlon = models.CharField(max_length=12, blank=True, null=True)
    the_geom = models.MultiPolygonField(srid=4269, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tabblock'


class Total(models.Model):
    provider_and_id = models.BigIntegerField(blank=True, null=True)
    actors = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'total'


class TotalWeight(models.Model):
    id = models.IntegerField(primary_key=True)
    year = models.IntegerField()
    provider_code = models.IntegerField()
    total_weight_hebrew = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'total_weight'
        unique_together = (('id', 'year', 'provider_code'),)


class Tract(models.Model):
    gid = models.AutoField()
    statefp = models.CharField(max_length=2, blank=True, null=True)
    countyfp = models.CharField(max_length=3, blank=True, null=True)
    tractce = models.CharField(max_length=6, blank=True, null=True)
    tract_id = models.CharField(primary_key=True, max_length=11)
    name = models.CharField(max_length=7, blank=True, null=True)
    namelsad = models.CharField(max_length=20, blank=True, null=True)
    mtfcc = models.CharField(max_length=5, blank=True, null=True)
    funcstat = models.CharField(max_length=1, blank=True, null=True)
    aland = models.FloatField(blank=True, null=True)
    awater = models.FloatField(blank=True, null=True)
    intptlat = models.CharField(max_length=11, blank=True, null=True)
    intptlon = models.CharField(max_length=12, blank=True, null=True)
    the_geom = models.MultiPolygonField(srid=4269, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tract'


class TrafficLight(models.Model):
    id = models.IntegerField(primary_key=True)
    year = models.IntegerField()
    provider_code = models.IntegerField()
    traffic_light_hebrew = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'traffic_light'
        unique_together = (('id', 'year', 'provider_code'),)


class TrafficVolume(models.Model):
    year = models.IntegerField(blank=True, null=True)
    road = models.IntegerField(blank=True, null=True)
    section = models.IntegerField(blank=True, null=True)
    lane = models.IntegerField(blank=True, null=True)
    month = models.IntegerField(blank=True, null=True)
    day = models.IntegerField(blank=True, null=True)
    day_of_week = models.IntegerField(blank=True, null=True)
    hour = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField()
    status = models.IntegerField(blank=True, null=True)
    duplicate_count = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'traffic_volume'
        unique_together = (('year', 'road', 'section', 'lane', 'month', 'day', 'day_of_week', 'hour'),)


class VehicleAttribution(models.Model):
    id = models.IntegerField(primary_key=True)
    year = models.IntegerField()
    provider_code = models.IntegerField()
    vehicle_attribution_hebrew = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'vehicle_attribution'
        unique_together = (('id', 'year', 'provider_code'),)


class VehicleDamage(models.Model):
    id = models.IntegerField(primary_key=True)
    year = models.IntegerField()
    provider_code = models.IntegerField()
    vehicle_damage_hebrew = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'vehicle_damage'
        unique_together = (('id', 'year', 'provider_code'),)


class VehicleStatus(models.Model):
    id = models.IntegerField(primary_key=True)
    year = models.IntegerField()
    provider_code = models.IntegerField()
    vehicle_status_hebrew = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'vehicle_status'
        unique_together = (('id', 'year', 'provider_code'),)


class VehicleType(models.Model):
    id = models.IntegerField(primary_key=True)
    year = models.IntegerField()
    provider_code = models.IntegerField()
    vehicle_type_hebrew = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'vehicle_type'
        unique_together = (('id', 'year', 'provider_code'),)


class Vehicles(models.Model):
    provider_code = models.IntegerField(blank=True, null=True)
    accident = models.ForeignKey(Markers, models.DO_NOTHING, blank=True, null=True)
    engine_volume = models.IntegerField(blank=True, null=True)
    manufacturing_year = models.IntegerField(blank=True, null=True)
    driving_directions = models.IntegerField(blank=True, null=True)
    vehicle_status = models.IntegerField(blank=True, null=True)
    vehicle_attribution = models.IntegerField(blank=True, null=True)
    vehicle_type = models.IntegerField(blank=True, null=True)
    seats = models.IntegerField(blank=True, null=True)
    total_weight = models.IntegerField(blank=True, null=True)
    provider_and_id = models.BigIntegerField(blank=True, null=True)
    accident_month = models.IntegerField(blank=True, null=True)
    accident_year = models.IntegerField(blank=True, null=True)
    car_id = models.IntegerField(blank=True, null=True)
    vehicle_damage = models.IntegerField(blank=True, null=True)
    file_type_police = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'vehicles'


class WazeAlerts(models.Model):
    id = models.BigAutoField(primary_key=True)
    city = models.TextField(blank=True, null=True)
    confidence = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    lontitude = models.FloatField(blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    magvar = models.IntegerField(blank=True, null=True)
    number_thumbs_up = models.IntegerField(blank=True, null=True)
    report_rating = models.IntegerField(blank=True, null=True)
    reliability = models.IntegerField(blank=True, null=True)
    alert_type = models.TextField(blank=True, null=True)
    alert_subtype = models.TextField(blank=True, null=True)
    uuid = models.TextField(blank=True, null=True)
    street = models.TextField(blank=True, null=True)
    road_type = models.IntegerField(blank=True, null=True)
    geom = models.PointField(srid=0, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'waze_alerts'


class WazeTraficJams(models.Model):
    id = models.BigAutoField(primary_key=True)
    level = models.IntegerField(blank=True, null=True)
    line = models.TextField(blank=True, null=True)
    speed_kmh = models.IntegerField(blank=True, null=True)
    turn_type = models.IntegerField(blank=True, null=True)
    length = models.FloatField(blank=True, null=True)
    type = models.TextField(blank=True, null=True)
    uuid = models.TextField(blank=True, null=True)
    speed = models.IntegerField(blank=True, null=True)
    segments = models.TextField(blank=True, null=True)
    road_type = models.IntegerField(blank=True, null=True)
    delay = models.IntegerField(blank=True, null=True)
    street = models.TextField(blank=True, null=True)
    city = models.TextField(blank=True, null=True)
    end_node = models.TextField(blank=True, null=True)
    blocking_alert_uuid = models.TextField(blank=True, null=True)
    start_node = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    geom = models.LineStringField(srid=0, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'waze_trafic_jams'


class Weather(models.Model):
    id = models.IntegerField(primary_key=True)
    year = models.IntegerField()
    provider_code = models.IntegerField()
    weather_hebrew = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'weather'
        unique_together = (('id', 'year', 'provider_code'),)


class YishuvShape(models.Model):
    id = models.IntegerField(primary_key=True)
    year = models.IntegerField()
    provider_code = models.IntegerField()
    yishuv_shape_hebrew = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'yishuv_shape'
        unique_together = (('id', 'year', 'provider_code'),)


class Zcta5(models.Model):
    gid = models.AutoField(unique=True)
    statefp = models.CharField(max_length=2)
    zcta5ce = models.CharField(primary_key=True, max_length=5)
    classfp = models.CharField(max_length=2, blank=True, null=True)
    mtfcc = models.CharField(max_length=5, blank=True, null=True)
    funcstat = models.CharField(max_length=1, blank=True, null=True)
    aland = models.FloatField(blank=True, null=True)
    awater = models.FloatField(blank=True, null=True)
    intptlat = models.CharField(max_length=11, blank=True, null=True)
    intptlon = models.CharField(max_length=12, blank=True, null=True)
    partflg = models.CharField(max_length=1, blank=True, null=True)
    the_geom = models.GeometryField(srid=4269, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'zcta5'
        unique_together = (('zcta5ce', 'statefp'),)


class ZipLookup(models.Model):
    zip = models.IntegerField(primary_key=True)
    st_code = models.IntegerField(blank=True, null=True)
    state = models.CharField(max_length=2, blank=True, null=True)
    co_code = models.IntegerField(blank=True, null=True)
    county = models.CharField(max_length=90, blank=True, null=True)
    cs_code = models.IntegerField(blank=True, null=True)
    cousub = models.CharField(max_length=90, blank=True, null=True)
    pl_code = models.IntegerField(blank=True, null=True)
    place = models.CharField(max_length=90, blank=True, null=True)
    cnt = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'zip_lookup'


class ZipLookupAll(models.Model):
    zip = models.IntegerField(blank=True, null=True)
    st_code = models.IntegerField(blank=True, null=True)
    state = models.CharField(max_length=2, blank=True, null=True)
    co_code = models.IntegerField(blank=True, null=True)
    county = models.CharField(max_length=90, blank=True, null=True)
    cs_code = models.IntegerField(blank=True, null=True)
    cousub = models.CharField(max_length=90, blank=True, null=True)
    pl_code = models.IntegerField(blank=True, null=True)
    place = models.CharField(max_length=90, blank=True, null=True)
    cnt = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'zip_lookup_all'


class ZipLookupBase(models.Model):
    zip = models.CharField(primary_key=True, max_length=5)
    state = models.CharField(max_length=40, blank=True, null=True)
    county = models.CharField(max_length=90, blank=True, null=True)
    city = models.CharField(max_length=90, blank=True, null=True)
    statefp = models.CharField(max_length=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'zip_lookup_base'


class ZipState(models.Model):
    zip = models.CharField(primary_key=True, max_length=5)
    stusps = models.CharField(max_length=2)
    statefp = models.CharField(max_length=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'zip_state'
        unique_together = (('zip', 'stusps'),)


class ZipStateLoc(models.Model):
    zip = models.CharField(primary_key=True, max_length=5)
    stusps = models.CharField(max_length=2)
    statefp = models.CharField(max_length=2, blank=True, null=True)
    place = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'zip_state_loc'
        unique_together = (('zip', 'stusps', 'place'),)
