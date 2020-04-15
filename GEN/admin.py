from django.contrib import admin
# from GEN.models import CMN_CommunicationVirtualModel, CMN_CommunicationPhysicalModel, EPS_EnterpriseMetaModel, EPS_EnterpriseProfileModel
from GEN.models import UserProfileInfo, ItemMeasuementUnit, Order, ProductCategory, ProductBase, Product, OrderItem, OrderLog, OrderItemLog,C19SymptomSet, UserLocationLog, UserHealthProfile
# Register your models here.


admin.site.register(UserProfileInfo)
admin.site.register(ItemMeasuementUnit)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(OrderLog)
admin.site.register(OrderItemLog)
admin.site.register(ProductCategory)
admin.site.register(ProductBase)
admin.site.register(Product)
admin.site.register(C19SymptomSet)
admin.site.register(UserLocationLog)
admin.site.register(UserHealthProfile)
