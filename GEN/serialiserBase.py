from rest_framework import serializers
from GEN import dbconstants
from .models import UserProfileInfo, CMN_CommunicationVirtualModel, CMN_CommunicationPhysicalModel, ProductCategory, Product, ProductBase, ItemMeasuementUnit, OrderItem, C19SymptomSet, UserHealthProfile, Order

class ProductSuggestionListSerializer(serializers.ModelSerializer):
    # first_name = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ('name', 'name_tamil', 'slug')
        # exclude = ['user']
    # def get_first_name(self, obj):
    #     return obj.user.first_name


class UserProfileSuggestionSerializer(serializers.ModelSerializer):
    first_name = serializers.SerializerMethodField()

    class Meta:
        model = UserProfileInfo
        fields = ('first_name', 'phone_primary')
        # exclude = ['user']
    def get_first_name(self, obj):
        return obj.user.first_name

class UserProfileInfoSerializer(serializers.ModelSerializer):
    first_name = serializers.SerializerMethodField()

    class Meta:
        model = UserProfileInfo
        fields = ('first_name', 'phone_primary', 'location_area', 'location_sublocality', 'location_locality', 'location_city', 'location_pincode')
        # exclude = ['user']
    def get_first_name(self, obj):
        return obj.user.first_name


class UserHealthProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserHealthProfile
        fields = ('user', 'symptom')
        exclude = ['user']



class C19SymptomSetSerializer(serializers.ModelSerializer):
    class Meta:
        model = C19SymptomSet
        fields = ['id', 'name', 'name_tamil', 'seviarity']
        depth = 0


class OrderItemSerializer(serializers.ModelSerializer):

    measurement_unit = serializers.SerializerMethodField()
    item_name = serializers.SerializerMethodField()
    item_img = serializers.SerializerMethodField()

    def get_measurement_unit(self, obj):

        # measurement_un = ItemMeasuementUnit.objects.get(pk=obj.measurement_unit)
        return str(obj.measurement_unit)
        # order_items_s = OrderItemSerializer(order_items, many=True).data
        # return order_items_s
        #
        # return "Kg"

    def get_item_img(self, obj):
        if(obj.product):
            return "/media/"+str(obj.product.pic)
        else:
            return ""

    def get_item_name(self, obj):
        return str(obj.item_name)

    class Meta:
        model = OrderItem
        fields = ['item_name', 'item_quantity', 'measurement_unit', 'item_img']



class OrderSerializer(serializers.ModelSerializer):
    order_item = serializers.SerializerMethodField()
    delivery_status = serializers.SerializerMethodField()
    status_text = serializers.SerializerMethodField()

    class Meta:
        model = Order
        fields = ['order_id', 'delivery_charges', 'status_text', 'delivery_status', 'order_item']
        depth = 0


    def get_delivery_status(self, obj):

        if obj.status == dbconstants.ORDER_PLACED:
            return "Order has been placed successfully. Customer Executive will call in some time"
        elif obj.status == dbconstants.ORDER_CONFIRMED_BY_CUSTOMER:
            return "Order will be delivered by the 11 Am tomorrow"
        elif obj.status == dbconstants.ORDER_PICKEDUP:
            return "Order pickedup and the delivery executive is on his way"
        elif obj.status == dbconstants.ORDER_CANCELLED:
            return "Order cancelled"



    def get_status_text(self, obj):

        return dbconstants.ORDER_STATUS_DISPLAY[obj.status]

    def get_order_item(self, obj):

        order_items = OrderItem.objects.filter(order=obj).order_by('-created_at')

        order_items_s = OrderItemSerializer(order_items, many=True).data
        return order_items_s

class ItemMeasuementUnitSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemMeasuementUnit
        fields = ['id', 'name', 'note']
        depth = 0


class ProductCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCategory
        fields = ['id', 'pic', 'name', 'name_tamil', 'status_note']
        depth = 0

class ProductBaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductBase
        fields = ['id','name', 'name_tamil', 'status_note', 'product_category']
        depth = 0



class ProductSerializer(serializers.ModelSerializer):

    name = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ['id', 'pic', 'name', 'name_tamil', 'base_measurement_unit', 'price', 'show_price', 'status_note', 'slug', 'priority', 'product_base', 'measurement_unit']
        # fields = '__all__'
        depth = 0

    def get_name(self, obj):
        if self.context["language"] == "ta":
            return str(obj.name_tamil)
        else:
            return str(obj.name)




# name": "Jercey Millk",
#             "name_tamil": "Jercey Millk",
#             "status_note": "Milk",
#             "is_available": true,
#             "slug": "jercey-millk"
#
# class DynamicFieldsModelSerializer(serializers.ModelSerializer):
#     """
#     A ModelSerializer that takes an additional `fields` argument that
#     controls which fields should be displayed.
#     """
#
#     def __init__(self, *args, **kwargs):
#         # Instantiate the superclass normally
#         super(DynamicFieldsModelSerializer, self).__init__(*args, **kwargs)
#
#         # fields = self.context['request'].query_params.get('fields')
#         fields = kwargs.get("fields")
#         if fields:
#             fields = fields.split(',')
#             # Drop any fields that are not specified in the `fields` argument.
#             allowed = set(fields)
#             existing = set(self.fields.keys())
#             for field_name in existing - allowed:
#                 self.fields.pop(field_name)


class CMN_CommunicationVirtualModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = CMN_CommunicationVirtualModel
        fields = '__all__'


class CMN_CommunicationPhysicalModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = CMN_CommunicationPhysicalModel
        fields = '__all__'
        # , 'communication_type'
        # fields = ['address_line_01']
    def create(self, validated_data):
        print("testta")
        cMN_CommunicationPhysicalModel = CMN_CommunicationPhysicalModel.objects.create(**validated_data)
        return cMN_CommunicationPhysicalModel

    def update(self, instance, validated_data):
        print("testtau")
        # cMN_CommunicationPhysicalModel = CMN_CommunicationPhysicalModel.objects.create(**validated_data)
        # cMN_CommunicationPhysicalModel.save()
        # instance.

        field_arr = []
        #
        # form_fields = ["CMN_CommunicationVirtualModel__slug", "CMN_CommunicationVirtualModel__communication_type", "CMN_CommunicationVirtualModel__communication_channel_key", "CMN_CommunicationVirtualModel__communication_channel_value", "CMN_CommunicationPhysicalModel__communication_type", "CMN_CommunicationPhysicalModel__address_line_01", "CMN_CommunicationPhysicalModel__address_line_02", "CMN_CommunicationPhysicalModel__city", "CMN_CommunicationPhysicalModel__district", "CMN_CommunicationPhysicalModel__state", "CMN_CommunicationPhysicalModel__pincode"]
        # serializer = EnterPriseForm()
        # form_fields = []
        # field_arr =getSerilalierField(serializer,field_arr, "Parent", form_fields)
        #
        # for i in field_arr:
        #     print(i["cn"])
        #     name = i["cn"]
        #     # instance.name = validated_data.get(name, instance.name)
        #
        #
        # print(field_arr)

        instance.slug = validated_data.get("slug", instance.slug)
        instance.communication_type = validated_data.get("communication_type", instance.communication_type)
        instance.is_person = validated_data.get("is_person", instance.is_person)
        instance.address_line_01 = validated_data.get("address_line_01", instance.address_line_01)
        instance.address_line_02 = validated_data.get("address_line_02", instance.address_line_02)
        instance.city = validated_data.get("city", instance.city)
        instance.district = validated_data.get("district", instance.district)
        instance.state = validated_data.get("state", instance.state)
        instance.country = validated_data.get("country", instance.country)
        instance.pincode = validated_data.get("pincode", instance.pincode)

        instance.save()


        return instance

class CMN_CommunicationVirtualModelSerializer(serializers.ModelSerializer):

    # full_name = serializers.SerializerMethodField()
    # full_name = serializers.IntegerField(required=True)

    class Meta:
        model = CMN_CommunicationVirtualModel
        fields = '__all__'
        # fields = ['slug', 'communication_type']
        # extra_kwargs = {'slug': {'required': False}}

    def create(self, validated_data):
        print("testta")
        cMN_CommunicationVirtualModel = CMN_CommunicationVirtualModel.objects.create(**validated_data)
        return cMN_CommunicationVirtualModel





def getSerilalierField(serializer_obj,field_arr, model ,form_fields ):
    for field_name, field_obj in serializer_obj.get_fields().items():

        if 'Serializer' in field_obj.__class__.__name__ and field_obj.__class__.__name__ != 'SerializerMethodField':
            field_arr=getSerilalierField(field_obj, field_arr, field_obj.__class__.__name__, form_fields)
        else:
            # print(field_name)
            # name_final = model.replace("ModelSerializer", "Model")+"__"+field_name
            # name_final = name_final.replace("SerializerModel__", "Model__")
            # if name_final in form_fields:
            each_obj ={}
            # each_obj['model'] = model
            each_obj['cn'] = field_name
            each_obj['dt'] = field_obj.help_text
            each_obj['dt_r'] = field_obj.__class__.__name__
            each_obj['required'] = field_obj.required


            # if hasattr(field_obj, 'verbose_name'):
            #     each_obj['lb'] = field_obj.verbose_name
            # else:
            #     v_name = field_name.replace("_"," ")
            #     each_obj['lb'] = v_name
            #
            # if hasattr(field_obj, 'choices'):
            #    each_obj['choices'] = field_obj.choices
               # each_obj['dt'] = 'MOD_DT_CHOICES'
            # if hasattr(field_obj, 'label'):
            #    each_obj['lb'] = field_obj.label
            field_arr.append(each_obj)
    return field_arr;



class EnterPriseForm(serializers.Serializer):

    # fields =  ['slug']
    # fields=['slug']


    communication_virtual = CMN_CommunicationVirtualModelSerializer()
    communication_physical = CMN_CommunicationPhysicalModelSerializer()

# class GenericSerializer():

# class frm_enterprise(serializers.ModelSerializer):

# class GeneralViewSet(viewsets.ModelViewSet):
#
#      def get_queryset(self):
#          model = self.kwargs.get('model')
#          return model.objects.all()
#
#      def get_serializer_class(self):
#          GeneralSerializer.Meta.model = self.kwargs.get('model')
#          return GeneralSerializer

def serializer_factory(model, base=serializers.ModelSerializer,
                       fields=None, exclude=None):
    attrs = {'model': model}
    if fields is not None:
        attrs['fields'] = fields
    if exclude is not None:
        attrs['exclude'] = exclude

    parent = (object,)
    if hasattr(base, 'Meta'):
        parent = (base.Meta, object)
    Meta = type(str('Meta'), parent, attrs)
    if model:
        class_name = model.__name__ + 'Serializer'
    else:
        class_name = 'Serializer'
    return type(base)(class_name, (base,), {'Meta': Meta, })







# class DynamicFieldsSerializerMixin(object):
#
#     def __init__(self, *args, **kwargs):
#         # Don't pass the 'fields' arg up to the superclass
#         fields = kwargs.pop('fields', None)
#
#         # Instantiate the superclass normally
#         super(DynamicFieldsSerializerMixin, self).__init__(*args, **kwargs)
#
#         if fields is not None:
#             # Drop any fields that are not specified in the `fields` argument.
#             allowed = set(fields)
#             existing = set(self.fields.keys())
#             for field_name in existing - allowed:
#                 self.fields.pop(field_name)


class DynamicFieldsModelSerializer(serializers.ModelSerializer):
    """
    A ModelSerializer that takes an additional `fields` argument that
    controls which fields should be displayed.
    """

    def __init__(self, *args, **kwargs):
        # Don't pass the 'fields' arg up to the superclass
        fields = kwargs.pop('fields', None)

        # Instantiate the superclass normally
        super(DynamicFieldsModelSerializer, self).__init__(*args, **kwargs)

        if fields is not None:
            # Drop any fields that are not specified in the `fields` argument.
            allowed = set(fields)
            existing = set(self.fields)
            for field_name in existing - allowed:
                self.fields.pop(field_name)
