from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from GEN import GEN_Constants, GEN_Constants_model
from django.contrib.auth.models import AbstractUser
from django.contrib.postgres.fields import ArrayField

from django.contrib.auth.models import User
from django.template.defaultfilters import slugify

import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir)
from GEN import dbconstants
from django.contrib.auth.models import AbstractUser


import element_types



class UserProfileInfo(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    gender = models.CharField(max_length=10, unique=False, choices=dbconstants.GENDER_SET, default=dbconstants.GENDER_MALE)
    guardian = models.ForeignKey('self', on_delete=models.CASCADE, null = True, unique= False, related_name="user_guardian",  blank=True)
    age = models.CharField(max_length=2, unique=False, null = True)
    user_m_status = models.CharField(max_length=3, choices=dbconstants.M_STATUS_TYPES, default = dbconstants.M_STATUS_NOT_TESTED)
    phone_primary = models.CharField(max_length=10, unique=False, default=dbconstants.VAL_STR_DEFAULT)
    phone_secondary = models.CharField(max_length=10, unique=False, default=dbconstants.VAL_STR_DEFAULT)
    location_area = models.CharField(max_length=80, unique=False, default=dbconstants.VAL_STR_DEFAULT)
    location_sublocality = models.CharField(max_length=80, unique=False, default=dbconstants.VAL_STR_DEFAULT)
    location_locality = models.CharField(max_length=80, unique=False, default=dbconstants.VAL_STR_DEFAULT)
    symptom_total = models.IntegerField(default=0)
    location_city = models.CharField(max_length=80, unique=False, default=dbconstants.VAL_STR_DEFAULT)
    location_state = models.CharField(max_length=80, unique=False, choices=dbconstants.STATE_LIST, default=dbconstants.STATE_TAMIL_NADU)
    location_pincode = models.CharField(max_length=6, unique=False, default="601201")
    location_latitude = models.CharField(max_length=30, unique=False, default=dbconstants.VAL_STR_DEFAULT, null=True)
    location_longitude = models.CharField(max_length=30, unique=False, default=dbconstants.VAL_STR_DEFAULT, null=True)
    user_language = models.CharField(max_length=3, choices=dbconstants.USER_LANGUAGE, default = dbconstants.USER_LG_ENGLISH)
    user_type = models.CharField(max_length=3, choices=dbconstants.USER_TYPES, default = dbconstants.USER_TYPE_CONSUMER)
    user_status = models.CharField(max_length=2, choices=dbconstants.USER_STATUS, default=dbconstants.USER_STATUS_ACTIVE)
    status = models.CharField(max_length=2, choices=dbconstants.STATUS,  default=dbconstants.STATUS_ACTIVE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.user.username)


class UserLocationLog(models.Model):

    user = models.OneToOneField(UserProfileInfo, on_delete=models.CASCADE)
    location_latitude = models.CharField(max_length=30, unique=False, default=dbconstants.VAL_STR_DEFAULT)
    location_langitude = models.CharField(max_length=30, unique=False, default=dbconstants.VAL_STR_DEFAULT)
    status = models.CharField(max_length=2, choices=dbconstants.STATUS,  default=dbconstants.STATUS_ACTIVE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.user.username)




class C19SymptomSet(models.Model):

    # slug = models.SlugField(unique=True, max_length=8)
    name = models.CharField(max_length=50, default=dbconstants.VAL_STR_DEFAULT, null=True)
    name_tamil = models.CharField(max_length=50, default=dbconstants.VAL_STR_DEFAULT, null=True)
    seviarity = models.IntegerField(default=0)
    note = models.CharField(max_length=250)
    # status = models.CharField(max_length=2, choices=dbconstants.STATUS,  default=dbconstants.STATUS_ACTIVE)
    # created_at = models.DateTimeField(auto_now_add=True)
    # updated_at = models.DateTimeField(auto_now=True)
    is_available = models.BooleanField(default=True)


    def __str__(self):
        return str(self.name)




class UserHealthProfile(models.Model):

    user = models.ForeignKey(UserProfileInfo, on_delete=models.CASCADE, null=True)
    symptom = models.ForeignKey(C19SymptomSet, on_delete=models.CASCADE, null=True)
    note = models.CharField(max_length=250, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.note)



class ItemMeasuementUnit(models.Model):

    # slug = models.SlugField(unique=True, max_length=8)
    name = models.CharField(max_length=50, default=dbconstants.VAL_STR_DEFAULT, null=True)
    note = models.CharField(max_length=250)
    # status = models.CharField(max_length=2, choices=dbconstants.STATUS,  default=dbconstants.STATUS_ACTIVE)
    # created_at = models.DateTimeField(auto_now_add=True)
    # updated_at = models.DateTimeField(auto_now=True)
    is_available = models.BooleanField(default=True)


    def __str__(self):
        return str(self.name)





class Order(models.Model):

    # slug = models.SlugField(unique=True, max_length=8)
    order_id = models.CharField(max_length=15, unique=True)
    user_customer = models.ForeignKey(UserProfileInfo,  related_name='user_customer', on_delete=models.CASCADE)
    # user_delivery_agent = models.ForeignKey(UserProfileInfo, limit_choices_to={'user_type': dbconstants.USER_TYPE_DELIVERY_AGENT},  related_name='user_delivery_agent', on_delete=models.CASCADE)
    delivery_charges = models.FloatField(max_length=5, default=1.0)
    status_note = models.CharField(max_length=200, default=dbconstants.VAL_STR_DEFAULT, null=True)
    status = models.CharField(max_length=3, choices=dbconstants.ORDER_STATUS,  default=dbconstants.ORDER_PLACED)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return str(self.order_id)


class ProductCategory(models.Model):

    name = models.CharField(max_length=200, unique=False)
    name_tamil = models.CharField(max_length=200, unique=False)
    pic = models.ImageField(upload_to='profile_pics', blank=True)
    status_note = models.CharField(max_length=200, unique=False)
    is_available = models.BooleanField(default=True)
    slug = models.SlugField(null=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(ProductCategory, self).save(*args, **kwargs)

    def __str__(self):
            return str(self.name)




class ProductBase(models.Model):
    name = models.CharField(max_length=200, unique=False)
    name_tamil = models.CharField(max_length=200, unique=False)
    status_note = models.CharField(max_length=200, unique=False)
    is_available = models.BooleanField(default=True)
    product_category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    slug = models.SlugField(null=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(ProductBase, self).save(*args, **kwargs)

    def __str__(self):
            return str(self.name)




class Product(models.Model):

    name = models.CharField(max_length=200, unique=False)
    name_tamil = models.CharField(max_length=200, unique=False)
    pic = models.ImageField(upload_to='profile_pics', blank=True)
    is_available = models.BooleanField(default=True)
    price = models.IntegerField(default=0, blank=True)
    base_measurement_unit = models.ForeignKey(ItemMeasuementUnit, on_delete=models.CASCADE)
    show_price = models.BooleanField(default=False)
    priority = models.CharField(max_length=3, choices=dbconstants.PRIORITY_LIST,  default=dbconstants.PRIORIT_05)
    status_note = models.CharField(max_length=200, unique=False)
    status_tamil = models.CharField(max_length=200, unique=False)
    product_base = models.ForeignKey(ProductBase, on_delete=models.CASCADE, unique=False, blank=True)
    measurement_unit = models.ManyToManyField(ItemMeasuementUnit,  related_name='mrp_umo', blank=True)
    slug = models.SlugField(null=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Product, self).save(*args, **kwargs)

    def __str__(self):
            return str(self.name)

# class PriceLog(models.Model):
#     slug = models.SlugField(null=True)
#     name = models.CharField(max_length=200, unique=False)
#
#     def save(self, *args, **kwargs):
#         self.slug = slugify(self.name)
#         super(Product, self).save(*args, **kwargs)
#
#     def __str__(self):
#             return str(self.name)


class OrderItem(models.Model):

    # slug = models.SlugField(unique=True, max_length=8)
    order_item_id = models.CharField(max_length=15, unique=True)
    item_name = models.CharField(max_length=60)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, blank=True)
    item_quantity = models.PositiveSmallIntegerField(default=1)
    item_price = models.FloatField(max_length=5, default=1.0)
    status_note = models.CharField(max_length=200, unique=False)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    measurement_unit = models.ForeignKey(ItemMeasuementUnit, related_name='measurement_unit', on_delete=models.CASCADE, default="", unique=False)
    status = models.CharField(max_length=3, choices=dbconstants.O_ITEM_STATUS, default=dbconstants.O_ITEM_PLACED)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return str(self.order_item_id)



class OrderItemLog(models.Model):

    order_item = models.ForeignKey(OrderItem, on_delete=models.CASCADE)
    status = models.CharField(max_length=3, choices=dbconstants.O_ITEM_STATUS, default=dbconstants.O_ITEM_PLACED)
    updated_at = models.DateTimeField(auto_now=True)
    status_note = models.CharField(max_length=200, unique=False)

    def __str__(self):
        return str(self.status)

class OrderLog(models.Model):

    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    status = models.CharField(max_length=3, choices=dbconstants.ORDER_STATUS,  default=dbconstants.ORDER_PLACED)
    updated_at = models.DateTimeField(auto_now=True)
    status_note = models.CharField(max_length=200, unique=False)

    def __str__(self):
        return str(self.status)


# ==========================================

# ==============
# GEN - CMN
# ==============

# ==============
# ==============

# verbose_name = "Place Holder"
# max_length = "max_length"
# help_text = "Data Type"
# max_length=8, help_text=GEN_Constants.MOD_DT_SLUG, verbose_name="verbose_name1"
# def getName():
#     return  'verbose_name="verbose_name3"';


class CMN_CommunicationVirtualModel(models.Model):

    slug = models.SlugField(max_length=element_types.getMaxLength(element_types.MOD_DT_SLUG), help_text=element_types.getDataType(element_types.MOD_DT_SLUG), verbose_name=element_types.getLabel(element_types.MOD_DT_SLUG), unique=True)
    communication_type = models.CharField(max_length=element_types.getMaxLength(element_types.MOD_DT_CHOICE_LIMITED), help_text=element_types.getDataType(element_types.MOD_DT_CHOICE_LIMITED), verbose_name="Communication Type", choices=GEN_Constants.GEN_COMMUNICATION_TYPES, default=GEN_Constants.PERSONAL)
    is_person = models.BooleanField(help_text=element_types.getDataType(element_types.MOD_DT_BOOL), verbose_name="Is actual person", default=True)
    communication_channel_key = models.CharField(max_length=element_types.getMaxLength(element_types.MOD_DT_CHOICE_LIMITED), help_text=element_types.getDataType(element_types.MOD_DT_CHOICE_LIMITED), verbose_name=element_types.getLabel(element_types.MOD_DT_CHOICE_LIMITED), choices=GEN_Constants.GEN_COMMUNICATION_CHANNEL_TYPES, default=GEN_Constants.PHONE)
    communication_channel_value = models.CharField(max_length=element_types.getMaxLength(element_types.MOD_DT_TEXT), help_text=element_types.getDataType(element_types.MOD_DT_TEXT), verbose_name="Details", null=True)
    # ArrayField(
    #     ArrayField(
    #         models.CharField(max_length=element_types.getMaxLength(element_types.MOD_DT_TEXT), help_text=element_types.getDataType(element_types.MOD_DT_TEXT), verbose_name=element_types.getLabel(element_types.MOD_DT_TEXT), blank=True),
    #         size=8,
    #     ),
    #     help_text=element_types.getDataType(element_types.MOD_DT_TEXT), verbose_name="Communication Channel Value",
    #     size=8, blank=True, null=True
    # )


    # created_at = models.DateTimeField(auto_now_add=True)
    # updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
            return str(self.slug)


class CMN_CommunicationPhysicalModel(models.Model):
    slug = models.SlugField(max_length=element_types.getMaxLength(element_types.MOD_DT_SLUG), help_text=element_types.getDataType(element_types.MOD_DT_SLUG), verbose_name=element_types.getLabel(element_types.MOD_DT_SLUG), unique=True)
    communication_type = models.CharField(max_length=element_types.getMaxLength(element_types.MOD_DT_CHOICE_LIMITED), help_text=element_types.getDataType(element_types.MOD_DT_CHOICE_LIMITED), verbose_name="Communication Type", choices=GEN_Constants.GEN_COMMUNICATION_TYPES, default=GEN_Constants.ENTERPRISE)
    is_person = models.BooleanField(help_text=element_types.getDataType(element_types.MOD_DT_BOOL), verbose_name="Is actual person", default=True)
    address_line_01 = models.CharField(max_length=element_types.getMaxLength(element_types.MOD_DT_TEXT), help_text=element_types.getDataType(element_types.MOD_DT_TEXT), verbose_name="Address Line 1")
    address_line_02 =  models.CharField(max_length=element_types.getMaxLength(element_types.MOD_DT_TEXT), help_text=element_types.getDataType(element_types.MOD_DT_TEXT), verbose_name="Address Line 2")
    city = models.CharField(max_length=element_types.getMaxLength(element_types.MOD_DT_TEXT), help_text=element_types.getDataType(element_types.MOD_DT_TEXT), verbose_name="City")
    district = models.CharField(max_length=element_types.getMaxLength(element_types.MOD_DT_TEXT), help_text=element_types.getDataType(element_types.MOD_DT_TEXT), verbose_name="District")
    state = models.CharField(max_length=element_types.getMaxLength(element_types.MOD_DT_TEXT), help_text=element_types.getDataType(element_types.MOD_DT_TEXT), verbose_name="State")
    country = models.CharField(max_length=element_types.getMaxLength(element_types.MOD_DT_TEXT), help_text=element_types.getDataType(element_types.MOD_DT_TEXT), verbose_name="Country")
    pincode = models.CharField(max_length=element_types.getMaxLength(element_types.MOD_DT_PINCODE), help_text=element_types.getDataType(element_types.MOD_DT_PINCODE), verbose_name="Pincode")

    # created_at = models.DateTimeField(auto_now_add=True)
    # updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
            return str(self.slug)

# ==============
# GEN - EPS
# ==============

class EPS_EnterpriseProfileModel(models.Model):
    slug = models.SlugField(max_length=element_types.getMaxLength(element_types.MOD_DT_SLUG), help_text=element_types.getDataType(element_types.MOD_DT_SLUG), verbose_name=element_types.getLabel(element_types.MOD_DT_SLUG), unique=True)
    name = models.CharField(max_length=element_types.getMaxLength(element_types.MOD_DT_NAME), help_text=element_types.getDataType(element_types.MOD_DT_NAME), verbose_name=element_types.getLabel(element_types.MOD_DT_NAME))
    GST_number = models.CharField(max_length=50, help_text=element_types.getDataType(element_types.MOD_DT_TEXT), verbose_name=element_types.getLabel(element_types.MOD_DT_TEXT))
    PAN_number = models.CharField(max_length=50, help_text=element_types.getDataType(element_types.MOD_DT_TEXT), verbose_name=element_types.getLabel(element_types.MOD_DT_TEXT))
    credit_limit = models.IntegerField( help_text=element_types.getDataType(element_types.MOD_DT_NUMBER), verbose_name=element_types.getLabel(element_types.MOD_DT_NUMBER))

    # created_at = models.DateTimeField(auto_now_add=True)
    # updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
            return str(self.slug)

class EPS_EnterpriseMetaModel(models.Model):
    slug = models.SlugField(unique=True, max_length=8)
    enterprise_profile = models.ForeignKey(EPS_EnterpriseProfileModel, related_name='ep', on_delete=models.CASCADE)
    communication_virtual_slugs = models.ForeignKey(CMN_CommunicationVirtualModel, related_name='ecv', on_delete=models.CASCADE)
    communication_physical = models.ForeignKey(CMN_CommunicationPhysicalModel, related_name='ecp', on_delete=models.CASCADE)
    parent_enterprise_meta = models.ForeignKey('self', on_delete=models.CASCADE)

    # created_at = models.DateTimeField(auto_now_add=True)
    # updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
            return str(self.slug)

# enterprise_profile_slug
# communication_virtual_slugs
# communication_physical_slugs
# parent_enterprise_meta_slug
# contact_person_user_meta_slugs
