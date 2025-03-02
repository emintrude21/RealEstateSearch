# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.contrib.auth.models import User

class SavedSale(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, db_column = 'user_id')
    sale_id = models.CharField(db_column = 'sale_id', max_length=100)

    class Meta:
        managed = False
        db_table = 'saved_sales'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Homesforrent(models.Model):
    #ï_zpid = models.TextField(db_column='ï»¿zpid', blank=True, null=True)  
    id = models.IntegerField(db_column='id', blank=True, null=False, primary_key=True)
    zpid = models.TextField(db_column='ï»¿zpid', blank=True, null=True)  
    status_type = models.TextField(db_column='Status Type', blank=True, null=True)  
    status_text = models.TextField(db_column='Status Text', blank=True, null=True)  
    time_on_zillow = models.TextField(db_column='Time On Zillow', blank=True, null=True)  
    price = models.TextField(db_column='Price', blank=True, null=True)  
    area = models.TextField(db_column='Area', blank=True, null=True)  
    price_per_sqft = models.TextField(db_column='Price Per Sqft', blank=True, null=True)  
    zestimate = models.TextField(db_column='Zestimate', blank=True, null=True)  
    zestimate_price_per_sqft = models.TextField(db_column='Zestimate Price Per Sqft', blank=True, null=True)  
    rent_zestimate = models.TextField(db_column='Rent Zestimate', blank=True, null=True)  
    lot_area = models.TextField(db_column='Lot Area', blank=True, null=True)  
    lot_area_unit = models.TextField(db_column='Lot Area Unit', blank=True, null=True)  
    beds = models.TextField(db_column='Beds', blank=True, null=True)  
    bathrooms = models.TextField(db_column='Bathrooms', blank=True, null=True)
    address = models.TextField(db_column='Address', blank=True, null=True)  
    street = models.TextField(db_column='Street', blank=True, null=True)  
    city = models.TextField(db_column='City', blank=True, null=True)  
    state = models.TextField(db_column='State', blank=True, null=True)  
    zipcode = models.IntegerField(db_column='Zipcode', blank=True, null=True) 
    latitude = models.FloatField(db_column='Latitude', blank=True, null=True)  
    longitude = models.FloatField(db_column='Longitude', blank=True, null=True)  
    broker_name = models.TextField(db_column='Broker Name', blank=True, null=True)  
    is_zillow_owned = models.TextField(db_column='is zillow owned', blank=True, null=True)  
    sold_date = models.TextField(db_column='Sold Date', blank=True, null=True)  
    sold_price = models.TextField(db_column='Sold Price', blank=True, null=True)  
    image_url = models.TextField(db_column='Image URL', blank=True, null=True) 
    detail_url = models.TextField(db_column='Detail URL', blank=True, null=True)  
    search_page_url = models.TextField(db_column='Search Page URL', blank=True, null=True) 
    agent_email = models.TextField(db_column = 'email', blank = True, null = True)

    class Meta:
        managed = False
        db_table = 'homesforrent'


class Homesforsale(models.Model):
    #ï_zpid = models.IntegerField(db_column='ï»¿zpid', blank=True, null=True)  
    id = models.IntegerField(db_column='id', blank=True, null=False, primary_key=True)
    zpid = models.IntegerField(db_column='ï»¿zpid', blank=True, null=True)  
    status_type = models.TextField(db_column='Status Type', blank=True, null=True)  
    status_text = models.TextField(db_column='Status Text', blank=True, null=True)
    time_on_zillow = models.TextField(db_column='Time On Zillow', blank=True, null=True)  
    price = models.IntegerField(db_column='Price', blank=True, null=True)  
    area = models.IntegerField(db_column='Area', blank=True, null=True)  
    price_per_sqft = models.IntegerField(db_column='Price Per Sqft', blank=True, null=True)  
    zestimate = models.TextField(db_column='Zestimate', blank=True, null=True)  
    zestimate_price_per_sqft = models.TextField(db_column='Zestimate Price Per Sqft', blank=True, null=True)  
    rent_zestimate = models.TextField(db_column='Rent Zestimate', blank=True, null=True)  
    lot_area = models.FloatField(db_column='Lot Area', blank=True, null=True)  
    lot_area_unit = models.TextField(db_column='Lot Area Unit', blank=True, null=True)  
    beds = models.IntegerField(db_column='Beds', blank=True, null=True)  
    bathrooms = models.IntegerField(db_column='Bathrooms', blank=True, null=True)  
    address = models.TextField(db_column='Address', blank=True, null=True)  
    street = models.TextField(db_column='Street', blank=True, null=True)  
    city = models.TextField(db_column='City', blank=True, null=True)  
    state = models.TextField(db_column='State', blank=True, null=True)  
    zipcode = models.IntegerField(db_column='Zipcode', blank=True, null=True)  
    latitude = models.FloatField(db_column='Latitude', blank=True, null=True) 
    longitude = models.FloatField(db_column='Longitude', blank=True, null=True)  
    broker_name = models.TextField(db_column='Broker Name', blank=True, null=True)  
    is_zillow_owned = models.TextField(db_column='is zillow owned', blank=True, null=True) 
    sold_date = models.TextField(db_column='Sold Date', blank=True, null=True)  
    sold_price = models.TextField(db_column='Sold Price', blank=True, null=True) 
    image_url = models.TextField(db_column='Image URL', blank=True, null=True)  
    detail_url = models.TextField(db_column='Detail URL', blank=True, null=True)
    search_page_url = models.TextField(db_column='Search Page URL', blank=True, null=True)
    description = models.TextField(db_column='description', blank=True, null=True)
    built_in = models.TextField(db_column='BuiltIn', blank=True, null=True)
    est_pay = models.TextField(db_column='EstPay', blank=True, null=True)
    residence_type = models.TextField(db_column='ResidenceType', blank=True, null=True)
    price_per_sqft = models.TextField(db_column='pricePerSqft', blank=True, null=True)
    full_bathroom = models.TextField(db_column='fullBathroom', blank=True, null=True)
    half_bathroom = models.TextField(db_column='halfBathroom', blank=True, null=True)
    basement = models.TextField(db_column='Basement', blank=True, null=True)
    flooring = models.TextField(db_column='Flooring', blank=True, null=True)
    heating = models.TextField(db_column='Heating', blank=True, null=True)
    cooling = models.TextField(db_column='Cooling', blank=True, null=True)
    appliances = models.TextField(db_column='Appliances', blank=True, null=True) 
    interior_features = models.TextField(db_column='InteriorFeatures', blank=True, null=True)
    parking = models.TextField(db_column='Parking', blank=True, null=True)
    property = models.TextField(db_column='Property', blank=True, null=True)
    lot = models.TextField(db_column='Lot', blank=True, null=True)
    construction_type = models.TextField(db_column='ConstruType', blank=True, null=True)
    material = models.TextField(db_column='Material', blank=True, null=True)
    utility = models.TextField(db_column='Utility', blank=True, null=True)
    community = models.TextField(db_column='Community', blank=True, null=True)
    location = models.TextField(db_column='Location', blank=True, null=True)
    agency_fee = models.TextField(db_column='AgencyFee', blank=True, null=True)
    walk_score = models.TextField(db_column='WalkScore', blank=True, null=True)
    transit_score = models.TextField(db_column='TransitScore', blank=True, null=True)
    bike_score = models.TextField(db_column='Bikescore', blank=True, null=True)
    basement2 = models.TextField(db_column='Basement2', blank=True, null=True)
    inte1 = models.TextField(db_column='Inte1', blank=True, null=True)
    inte2 = models.TextField(db_column='Inte2', blank=True, null=True)
    inte3 = models.TextField(db_column='Inte3', blank=True, null=True)
    inte4 = models.TextField(db_column='Inte4', blank=True, null=True)
    park1 = models.TextField(db_column='Park1', blank=True, null=True)
    park2 = models.TextField(db_column='Park2', blank=True, null=True)
    park3 = models.TextField(db_column='Park3', blank=True, null=True)
    park4 = models.TextField(db_column='Park4', blank=True, null=True)
    prop1 = models.TextField(db_column='Prop1', blank=True, null=True)
    prop2 = models.TextField(db_column='Prop2', blank=True, null=True)
    prop3 = models.TextField(db_column='Prop3', blank=True, null=True)
    prop4 = models.TextField(db_column='Prop4', blank=True, null=True)
    constype1 = models.TextField(db_column='ConsType1', blank=True, null=True)
    constype2 = models.TextField(db_column='ConsType2', blank=True, null=True)
    material1 = models.TextField(db_column='Material1', blank=True, null=True)
    material2 = models.TextField(db_column='Material2', blank=True, null=True)
    utility1 = models.TextField(db_column='Utility1', blank=True, null=True)
    utility2 = models.TextField(db_column='Utility2', blank=True, null=True)
    utility3 = models.TextField(db_column='Utility3', blank=True, null=True)
    utility4 = models.TextField(db_column='Utility4', blank=True, null=True)
    community1 = models.TextField(db_column='Community1', blank=True, null=True)
    community2 = models.TextField(db_column='Community2', blank=True, null=True)
    community3 = models.TextField(db_column='Community3', blank=True, null=True)
    community4 = models.TextField(db_column='Community4', blank=True, null=True)
    openhousedate = models.TextField(db_column='openhousedate', blank=True, null=True)
    openhousetime = models.TextField(db_column='openhousetime', blank=True, null=True)
    walk_status = models.TextField(db_column='walk_status', blank=True, null=True)
    bike_status = models.TextField(db_column='bike_status', blank=True, null=True)
    transit_status = models.TextField(db_column='transit_status', blank=True, null=True)
    agent_email = models.TextField(db_column = 'agentEmail', blank = True, null = True)

    class Meta:
        managed = False
        db_table = 'homesforsale'


class Homessold(models.Model):
    #ï_zpid = models.IntegerField(db_column='ï»¿zpid', blank=True, null=True)  
    id = models.IntegerField(db_column='id', blank=True, null=False, primary_key=True)
    zpid = models.IntegerField(db_column='ï»¿zpid', blank=True, null=True)  
    status_type = models.TextField(db_column='Status Type', blank=True, null=True) 
    status_text = models.TextField(db_column='Status Text', blank=True, null=True)  
    time_on_zillow = models.TextField(db_column='Time On Zillow', blank=True, null=True)  
    price = models.IntegerField(db_column='Price', blank=True, null=True)  
    area = models.TextField(db_column='Area', blank=True, null=True) 
    price_per_sqft = models.TextField(db_column='Price Per Sqft', blank=True, null=True)  
    zestimate = models.TextField(db_column='Zestimate', blank=True, null=True)
    zestimate_price_per_sqft = models.TextField(db_column='Zestimate Price Per Sqft', blank=True, null=True)  
    rent_zestimate = models.IntegerField(db_column='Rent Zestimate', blank=True, null=True) 
    lot_area = models.TextField(db_column='Lot Area', blank=True, null=True)  
    lot_area_unit = models.TextField(db_column='Lot Area Unit', blank=True, null=True)  
    beds = models.TextField(db_column='Beds', blank=True, null=True) 
    bathrooms = models.TextField(db_column='Bathrooms', blank=True, null=True) 
    address = models.TextField(db_column='Address', blank=True, null=True)  
    street = models.TextField(db_column='Street', blank=True, null=True)  
    city = models.TextField(db_column='City', blank=True, null=True)  
    state = models.TextField(db_column='State', blank=True, null=True)  
    zipcode = models.IntegerField(db_column='Zipcode', blank=True, null=True)  
    latitude = models.FloatField(db_column='Latitude', blank=True, null=True)
    longitude = models.FloatField(db_column='Longitude', blank=True, null=True) 
    broker_name = models.TextField(db_column='Broker Name', blank=True, null=True)  
    is_zillow_owned = models.TextField(db_column='is zillow owned', blank=True, null=True)  
    sold_date = models.TextField(db_column='Sold Date', blank=True, null=True)  
    sold_price = models.IntegerField(db_column='Sold Price', blank=True, null=True)  
    image_url = models.TextField(db_column='Image URL', blank=True, null=True)  
    detail_url = models.TextField(db_column='Detail URL', blank=True, null=True)  
    search_page_url = models.TextField(db_column='Search Page URL', blank=True, null=True)
    agent_email = models.TextField(db_column = 'email', blank = True, null = True)

    class Meta:
        managed = False
        db_table = 'homessold'

class Specialvalues(models.Model):
    address = models.TextField(db_column='Address', blank=True, null=True)
    special1 = models.TextField(db_column='special1', blank=True, null=True)
    special2 = models.TextField(db_column='special2', blank=True, null=True)
    special3 = models.TextField(db_column='special3', blank=True, null=True)
    special4 = models.TextField(db_column='special4', blank=True, null=True)
    special5 = models.TextField(db_column='special5', blank=True, null=True)
    special6 = models.TextField(db_column='special6', blank=True, null=True)
    special7 = models.TextField(db_column='special7', blank=True, null=True)
    special8 = models.TextField(db_column='special8', blank=True, null=True)
    special9 = models.TextField(db_column='special9', blank=True, null=True)
    special10 = models.TextField(db_column='special10', blank=True, null=True)
    id = models.IntegerField(db_column='id', blank=True, null=False, primary_key=True)

    class Meta:
        managed = False
        db_table = 'special_values'

class Post(models.Model):
    id = models.IntegerField(db_column = 'id', blank = True, null = False, primary_key = True)
    title = models.TextField(db_column = 'title', blank = True, null = True)
    slug = models.TextField(db_column = 'slug', blank = True, null = True)
    intro = models.TextField(db_column = 'intro', blank = True, null = True)
    body = models.TextField(db_column = 'body', blank = True, null = True)
    image = models.TextField(db_column = 'image', blank = True, null = True)
    date_added = models.DateTimeField(db_column = 'dateAdded', blank = True, null = True)

    class Meta:
        managed = False
        db_table = 'blogs'

class Comment(models.Model):
    id = models.IntegerField(db_column = 'id', blank = True, null = False, primary_key = True)
    name = models.TextField(db_column = 'name', blank = True, null = True)
    email = models.TextField(db_column = 'email', blank = True, null = True)
    body = models.TextField(db_column = 'body', blank = True, null = True)
    date_added = models.DateTimeField(db_column = 'dateAdded', blank = True, null = True)

    class Meta:
        managed = False
        db_table = 'Comment'

class Agent(models.Model):
    #user = models.OneToOneField(AuthUser, on_delete=models.CASCADE, primary_key=True, db_column = 'id')
    username = models.CharField(db_column = 'username', unique=True, max_length=150)
    state = models.TextField(db_column = 'state', blank = True, null = True)
    city = models.TextField(db_column = 'city', blank = True, null = True)
    agent_name = models.TextField(db_column = 'agentName', blank = True, null = True)
    agency = models.TextField(db_column = 'agency', blank = True, null = True)
    specialities = models.TextField(db_column = 'specialities', blank = True, null = True)
    about_me = models.TextField(db_column = 'aboutMe', blank = True, null = True)
    broker_address = models.TextField(db_column = 'brokerAddress', blank = True, null = True)
    cellphone = models.TextField(db_column = 'cellphone', blank = True, null = True)
    brokerphone = models.TextField(db_column = 'brokerphone', blank = True, null = True)
    screenname = models.TextField(db_column = 'screenname', blank = True, null = True)
    member_since = models.TextField(db_column = 'memberSince', blank = True, null = True)
    licenses = models.TextField(db_column = 'Licenses', blank = True, null = True)
    other_licenses = models.TextField(db_column = 'otherLicenses', blank = True, null = True)
    language1 = models.TextField(db_column = 'Language1', blank = True, null = True)
    language2 = models.TextField(db_column = 'Language2', blank = True, null = True)
    image_url = models.TextField(db_column = 'ImageURL', blank = True, null = True)
    email = models.TextField(db_column = 'email', blank = True, null = True)

    class Meta:
        managed = False
        db_table = 'agentinfo'