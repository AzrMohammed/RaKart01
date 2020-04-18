from django.shortcuts import render
from django.contrib.auth import authenticate
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
import json
from .serialiserBase import CMN_CommunicationVirtualModelSerializer, EnterPriseForm, CMN_CommunicationPhysicalModelSerializer, ProductCategorySerializer, ProductSerializer, ProductBaseSerializer, ItemMeasuementUnitSerializer, C19SymptomSetSerializer, UserHealthProfileSerializer, OrderSerializer, UserProfileInfoSerializer, UserProfileSuggestionSerializer, ProductSuggestionListSerializer
from .models import CMN_CommunicationVirtualModel, CMN_CommunicationPhysicalModel,Order,UserProfileInfo,OrderItem,ItemMeasuementUnit, ProductCategory, Product, ProductBase, ItemMeasuementUnit, OrderLog, OrderItemLog, C19SymptomSet, UserHealthProfile
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.models import User
import collections
from django.views.decorators.csrf import csrf_exempt
from django.utils import six
import random
import string
from django.utils import timezone
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required
from GEN import dbconstants
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from GEN.forms import UserFormCustomer, UserProfileInfoForm, UserForm,OrderForm, UserParentForm,  OrderItemForm, IOrderForm, IOrderItemForm, OrderLogForm, OrderItemLogForm, UserHealthProfileForm
from GEN import GEN_Constants, GEN_Constants_model
from django.core import serializers





class CustomerOrder(APIView):

    # def get(self,request):
    #         user_p = UserProfileInfo.objects.get(phone_primary="9080349072")
    #
    #         order_list = Order.objects.filter(user_customer = user_p).order_by('-updated_at')
    #         order_list_s =  OrderSerializer(order_list, many=True)
    #
    #         base_data = {}
    #         base_data["order"] = order_list_s.data
    #         base_data["delivery_text"] = dbconstants.ORDER_STATUS_DISPLAY["OPD"]
    #         # ORDER_STATUS[0]
    #         # base_data["status_text"] = "RECEIVED"
    #
    #         return Response(base_data)

        # phone = "9080349072"
        # user_p = UserProfileInfo.objects.get(phone_primary=phone)
        #
        # order_list = Order.objects.filter(user_customer = user_p).order_by('-updated_at')
        # order_list_s =  OrderSerializer(order_list, many=True)
        #
        #
        # base_data = {}
        # base_data["order"] = order_list_s.data
        # # base_data["delivery_text"] = "Order will bw delivered by 11 AM tomorrow"
        # # base_data["status_text"] = "RECEIVED"
        #
        # return Response(base_data)


    def post(self,request):
        received_json_data=json.loads(request.body)

        print("reee")
        print(received_json_data)

        phone = received_json_data["user_phone"]
        user_p = UserProfileInfo.objects.get(phone_primary=phone)



        order_list = Order.objects.filter(user_customer = user_p).order_by('-updated_at')
        order_list_s =  OrderSerializer(order_list, many=True)


        base_data = {}
        base_data["order"] = order_list_s.data
        base_data["delivery_text"] = "Order will bw delivered by 11 AM tomorrow"
        base_data["status_text"] = "RECEIVED"

        return Response(base_data)

        #
        # category = ProductCategory.objects.filter(is_available=True)
        # serializer_cat = ProductCategorySerializer(category, many=True)
        #
        #
        # itemMeasuementUnit_base = ItemMeasuementUnit.objects.filter(is_available=True)
        # serialiser_itemMeasuementUnit_base = ItemMeasuementUnitSerializer(itemMeasuementUnit_base, many=True)
        #
        # base_data = {}
        #
        # base_data["uom"] = serialiser_itemMeasuementUnit_base.data
        # base_data["category"] = serializer_cat.data
        #
        # return Response(base_data)

    # def post(self,request):
    #     phone = "9080349072"
    #     user_p = UserProfileInfo.objects.get(phone_primary=phone)
    #
    #     order_list = Order.objects.filter(user_customer = user_p).order_by('-updated_at')
    #     order_list_s =  OrderSerializer(order_list, many=True)
    #
    #
    #     base_data = {}
    #     base_data["order"] = order_list_s.data
    #
    #     return Response(base_data)



@csrf_exempt
def order_details(request):
    data = {"SUCCESS":True,"list":[{"card_type":"TITLE","data":{"title_text":"Recent Update"}},{"card_type":"PHONE","data":{"title":"Mr. Manigandan G","sub_title":"Dept Com of Police","phone":[9080349072,9020453454],"photo":"http://192.168.0.103:8000/media/profile_pics/user.png"}},{"card_type":"PHONE","data":{"title":"Mr. Manigandan G","sub_title":"Dept Com of Police","phone":[9080349072,9020453454],"photo":"http://192.168.0.103:8000/media/profile_pics/user.png"}},{"card_type":"SUB_TITLE","data":{"title_text":"Home Remidies"}},{"card_type":"Article","data":{"title":"Home Sanatizers","sub_title":"Steps to make sanatisers in home","URL":"https://www.healthline.com/health/how-to-make-hand-sanitizer","cover_photo":"http://192.168.0.103:8000/media/profile_pics/hand-sanitizer.jpg"}}]}

    return HttpResponse(json.dumps(data), content_type="application/json")

@csrf_exempt
def get_user_suggestion_list(request):
    phone = "908034"
    user_p = UserProfileInfo.objects.filter(phone_primary__startswith=phone)
    order_list_s =  UserProfileSuggestionSerializer(user_p, many=True)

    base_data = {}
    base_data["user_data"] = order_list_s.data

    # ORDER_STATUS[0]
    # base_data["status_text"] = "RECEIVED"
    return HttpResponse(json.dumps({"SUCCESS":False, "RESPONSE_DATA":base_data}),
        content_type="application/json")

@csrf_exempt
def validate_app(request):
        received_json_data=json.loads(request.body)
        print("resssa")
        print(received_json_data)
        # validate_app
        # return HttpResponse(json.dumps({"SUCCESS":False, "RESPONSE_DATA":{"partial":True, "url":"https://www.google.com/"}}),
        #     content_type="application/json")
        return HttpResponse(json.dumps({"SUCCESS":True, "RESPONSE_DATA":{"partial":False}}),
            content_type="application/json")



@csrf_exempt
def get_user_details(request):
    # phone = "9080349072"
    received_json_data=request.POST
    print("resssa")
    print(received_json_data)

    phone = received_json_data["phone"]
    user_p = UserProfileInfo.objects.get(phone_primary=phone)
    order_list_s =  UserProfileInfoSerializer(user_p, many=False)

    base_data = {}
    base_data["user_data"] = order_list_s.data

    # ORDER_STATUS[0]
    # base_data["status_text"] = "RECEIVED"
    return HttpResponse(json.dumps({"SUCCESS":False, "RESPONSE_DATA":base_data}),
        content_type="application/json")

@csrf_exempt
def product_list_suggestion(request):

    # received_json_data=json.loads(request.body)
    # #
    # phone = user["phone"]
    q = "ca"
    user_p = Product.objects.filter(name__contains=q)
# ProductSuggestionListSerializer
    order_list_s =  ProductSuggestionListSerializer(user_p, many=True)

    base_data = {}
    base_data["product_list"] = order_list_s.data

    # ORDER_STATUS[0]
    # base_data["status_text"] = "RECEIVED"
    return HttpResponse(json.dumps({"SUCCESS":False, "RESPONSE_DATA":base_data}),
        content_type="application/json")

def order_list_user(request):

    received_json_data=json.loads(request.body)
    #
    phone = user["phone"]
    # phone = "9080349072"
    user_p = UserProfileInfo.objects.get(phone_primary=phone)

    order_list = Order.objects.filter(user_customer = user_p).order_by('-updated_at')


    return HttpResponse(json.dumps(data_set), content_type="application/json")

    # return render(request, 'GEN/orders_list.html',  { 'orders': orders,  'measurements_list':measurements_list, 'state_list':state_list , 'order_status_list':order_status_list })


    # data = {"SUCCESS":True,"list":[{"card_type":"TITLE","data":{"title_text":"Recent Update"}},{"card_type":"PHONE","data":{"title":"Mr. Manigandan G","sub_title":"Dept Com of Police","phone":[9080349072,9020453454],"photo":"http://192.168.0.103:8000/media/profile_pics/user.png"}},{"card_type":"PHONE","data":{"title":"Mr. Manigandan G","sub_title":"Dept Com of Police","phone":[9080349072,9020453454],"photo":"http://192.168.0.103:8000/media/profile_pics/user.png"}},{"card_type":"SUB_TITLE","data":{"title_text":"Home Remidies"}},{"card_type":"Article","data":{"title":"Home Sanatizers","sub_title":"Steps to make sanatisers in home","URL":"https://www.healthline.com/health/how-to-make-hand-sanitizer","cover_photo":"http://192.168.0.103:8000/media/profile_pics/hand-sanitizer.jpg"}}]}
    #
    # return HttpResponse(json.dumps(data), content_type="application/json")




def getUser(phone):

    received_json_data=json.loads(request.body)

    phone = user["phone"]
    user = UserProfileInfo.objects.get(phone_primary=phone)


    data = {"SUCCESS":True,"list":[{"card_type":"TITLE","data":{"title_text":"Recent Update"}},{"card_type":"PHONE","data":{"title":"Mr. Manigandan G","sub_title":"Dept Com of Police","phone":[9080349072,9020453454],"photo":"http://192.168.0.103:8000/media/profile_pics/user.png"}},{"card_type":"PHONE","data":{"title":"Mr. Manigandan G","sub_title":"Dept Com of Police","phone":[9080349072,9020453454],"photo":"http://192.168.0.106:8000/media/profile_pics/user.png"}},{"card_type":"SUB_TITLE","data":{"title_text":"Home Remidies"}},{"card_type":"Article","data":{"title":"Home Sanatizers","sub_title":"Steps to make sanatisers in home","URL":"https://www.healthline.com/health/how-to-make-hand-sanitizer","cover_photo":"http://192.168.0.103:8000/media/profile_pics/hand-sanitizer.jpg"}}]}

    return HttpResponse(json.dumps(data), content_type="application/json")

@csrf_exempt
def feed_news(request):
    data = {"SUCCESS": True, "list": [{"card_type": "INFO_NEUTRAL", "data":{"title_text": "Title", "details_text": "We are providing only the basic essentials because of the COVID19 situation. All the ondemand supplies will be provided up on order once the situation is over.", "bg_color": "#e58a8a"}}, {"card_type": "TITLE", "data": {"title_text": "Order From Home Details"}}, {"card_type": "PHONE", "data": {"title": "Mr. Manigandan G", "sub_title": "Delivery Agent", "phone": [9080349072, 9020453454], "photo": "http://192.168.0.103:8000/media/profile_pics/user.png"}}, {"card_type": "PHONE", "data": {"title": "Mr. Rahu G", "sub_title": "Business Agent", "phone": [9080349072, 9020453454], "photo": "http://192.168.0.106:8000/media/profile_pics/user.png"}}, {"card_type": "SUB_TITLE", "data": {"title_text": "COVID19 STATUS"}}, {"card_type": "ARTICLE", "data": {"title": "Coronavirus in Tamil", "sub_title": "Dr. V Ramasubramanian | Apollo Hospitals", "URL": "https://www.youtube.com/watch?v=ZezntM6IAvU", "cover_photo": "http://206.189.129.128:8000/media/profile_pics/maxresdefault.jpg"}}]}
    return HttpResponse(json.dumps(data), content_type="application/json")


@csrf_exempt
def feed_contact(request):

    received_json_data=json.loads(request.body)

    print(received_json_data)
    data = {"SUCCESS": True, "list": [{"card_type": "INFO_NEUTRAL", "data":{"title_text": "Notice", "details_text": "We are providing only the basic essentials because of the COVID19 situation. All the ondemand supplies will be provided up on order once the situation is over.", "bg_color": "#e58a8a"}}, {"card_type": "TITLE", "data": {"title_text": "Order From Home Details"}}, {"card_type": "PHONE", "data": {"title": "Ramesh", "sub_title": "Business Agent", "phone": [8144485556], "photo": "http://206.189.129.128:8000/media/profile_pics/user.png"}}]}
    # {"SUCCESS": True, "list": [{"card_type": "INFO_NEUTRAL", "data":{"title_text": "Notice", "details_text": "We are providing only the basic essentials because of the COVID19 situation. All the ondemand supplies will be provided up on order once the situation is over.", "bg_color": "#e58a8a"}}, {"card_type": "TITLE", "data": {"title_text": "Order From Home Details"}}, {"card_type": "PHONE", "data": {"title": "Mr. Manigandan G", "sub_title": "Delivery Agent", "phone": [9080349072, 9020453454], "photo": "http://206.189.129.128:8000/media/profile_pics/user.png"}}, {"card_type": "PHONE", "data": {"title": "Mr. Rahu G", "sub_title": "Business Agent", "phone": [9080349072, 9020453454], "photo": "http://192.168.0.106:8000/media/profile_pics/user.png"}}, {"card_type": "SUB_TITLE", "data": {"title_text": "COVID19 STATUS"}}, {"card_type": "ARTICLE", "data": {"title": "Coronavirus in Tamil", "sub_title": "Dr. V Ramasubramanian | Apollo Hospitals", "URL": "https://www.youtube.com/watch?v=ZezntM6IAvU", "cover_photo": "http://206.189.129.128:8000/media/profile_pics/maxresdefault.jpg"}}]}
    return HttpResponse(json.dumps(data), content_type="application/json")


@csrf_exempt
def submit_symptoms(request):

    received_json_data=json.loads(request.body)

    print(received_json_data)

    user =  received_json_data["user"]
    phone = user["phone"]

    symptom_list = received_json_data["symptom_list"]




    user = UserProfileInfo.objects.get(phone_primary=phone)

    symptom_total = 0

    for symptom_id in symptom_list:
        form_data = {}
        form_data["note"] = "Note"
        symptom = C19SymptomSet.objects.get(id=symptom_id)
        healh_form = UserHealthProfileForm(form_data)

        if healh_form.is_valid():

            symptom_total = symptom_total + int(symptom.seviarity)
            health = healh_form.save(commit=False)
            health.user = user
            health.symptom = symptom
            health.save()


    user.symptom_total = symptom_total
    user.save()

    # print("sypmtont");
    # print("sypmtont=="+str(symptom_total));

    return HttpResponse(json.dumps({"SUCCESS":True, "RESPONSE_MESSAGE":"Status updated"}),
    content_type="application/json")




@csrf_exempt
def change_user_status(request):

    print("came changestat")
    username = request.POST['username']
    user_status = request.POST['user_status']

    user_obj = User.objects.get(username=username)
    user_profile = UserProfileInfo.objects.get(user=user_obj)

    # user_profile = UserProfileInfo.objects.get(username=username)

    if user_status == "AT":
        print("useractive")
        user_status = dbconstants.USER_STATUS_DISABLED
    else:
        user_status = dbconstants.USER_STATUS_ACTIVE
        print("userinactive")
    user_profile.user_status = user_status
    user_profile.save()

    return HttpResponse(json.dumps({"SUCCESS":True, "RESPONSE_MESSAGE":"Status updated"}),
    content_type="application/json")



@csrf_exempt
def alter_order_item(request):
    if request.method == "GET":

         received_json_data = {"order_item_id" : "ODRHSXF1", "item_status":"CANCEL" }

         order_item = OrderItem.objects.get(order_item_id=received_json_data["order_item_id"])

         item_status = received_json_data["item_status"]

         item_status_to_update = order_item.status

         if item_status == "CANCEL":
             item_status_to_update =dbconstants.O_ITEM_REMOVED
         elif item_status == "REJECT":
             item_status_to_update =dbconstants.O_ITEM_REJECTED
         elif item_status == "NOT_AVAILABLE":
             item_status_to_update =dbconstants.O_ITEM_NOT_AVAILABLE


         order_item.status = item_status_to_update
         order_item.save()

    return HttpResponse(json.dumps({"SUCCESS":False, "RESPONSE_MESSAGE":"Status updated successfully"}),
        content_type="application/json")

# getSymptomSet
@csrf_exempt
def alter_order(request):

    if request.method == "GET":

         received_json_data = {"order_id" : "ODRHSXF1", "item_status":"CANCEL" }

         order_item = Order.objects.get(order_id=received_json_data["order_item_id"])

         item_status = received_json_data["item_status"]

         item_status_to_update = order_item.status

         if item_status == "CANCEL":
             item_status_to_update =dbconstants.ORDER_CANCELLED
         elif item_status == "PICKED":
             item_status_to_update =dbconstants.ORDER_PICKEDUP
         elif item_status == "CONFIRMED":
             item_status_to_update =dbconstants.ORDER_CONFIRMED_BY_CUSTOMER
         elif item_status == "DELIVERED":
             item_status_to_update =dbconstants.ORDER_DELIVERED

         order_item.status = item_status_to_update
         order_item.save()

    return HttpResponse(json.dumps({"SUCCESS":False, "RESPONSE_MESSAGE":"Status updated successfully"}),
        content_type="application/json")


# {
# "user":{"phone":9080349072,"location_lat":12.45345345,"location_long":12.98098098,"land_marr":"Near Ayyapan temple"},
# "item_list":[{"product_id":24, "uom_id":7,"quantity":5 },{"product_id":24, "uom_id":7,"quantity":5 }]
# }


@csrf_exempt
def order_create_m(request):

    if request.method == "POST":

        #
        received_json_data=json.loads(request.body)
        print("resssa")
        print(received_json_data)
        # received_json_data={"user":{"phone":9629283679,"location_lat":12.45345345,"location_long":12.98098098,"land_mark":"Near Ayyapan temple"},"item_list":[{"product_id":15, "uom_id":2,"quantity":5 },{"product_id":2, "uom_id":1,"quantity":5 }]}

        user = received_json_data["user"]
        item_list = received_json_data["item_list"]

        # print(user)
        # print(user["land_mark"])

        user_profile = UserProfileInfo.objects.get(phone_primary=user["phone"])

        # order_form = IOrderForm(request.POST, request.FILES, instance=user)
                # fields = ('order_id', 'user_customer', 'delivery_charges')
        order_data = {}
        # order_data["order_id"] = "3343322"
        # order_form.user_customer = user
        order_data["delivery_charges"] = 20
        # order_data["user_customer"] = user

        order_form = IOrderForm(order_data)
        # order_form.order_id = "3343322"

        # order_form.delivery_charges = 20

        if order_form.is_valid():
            order = order_form.save(commit=False)
            order.user_customer = user_profile
            order.order_id = unique_order_id_generator(order)
            order.save()


            for item in item_list:

                # "product_id":24, "uom_id":7,"quantity":5
                        # fields = ('order_item_id', 'product' 'item_name', 'item_quantity', 'order', 'measurement_unit')
                order_item_data = {}

                print("cameotem")
                print(item)
                order_item_data["item_name"] = item['name']
                order_item_data["item_quantity"] = item['quantity']

                order_item_form = IOrderItemForm(order_item_data)

                if order_item_form.is_valid():


                    order_item = order_item_form.save(commit=False)
                    order_item.order = order
                    order_item.order_item_id = unique_order_item_id_generator(order_item)

                    if item['product_id']:
                        order_item.product = Product.objects.get(id = item['product_id'])
                    # print("eachit")
                    # print(order_item.product.measurement_unit[0])
                    # print(order_item.product.measurement_unit)
                    # order_item.measurement_unit = ItemMeasuementUnit.objects.get(id = item['uom_id'])
                    order_item.measurement_unit = ItemMeasuementUnit.objects.get(name = item['uom'])
                    # order_item.measurement_unit = order_item.product.measurement_unit[0]
                    order_item.save()

                    # fields = ('status', 'order_item')
                    order_item_log_data = {}
                    order_item_log_data["status"] = dbconstants.O_ITEM_PLACED

                    order_item_log_form = OrderItemLogForm(order_item_log_data)

                    if order_item_log_form.is_valid():
                        order_item_log = order_item_log_form.save(commit=False)
                        order_item_log.order_item = order_item
                        order_item_log.save()
                    #
                    #     return HttpResponse(json.dumps({"SUCCESS":True, "RESPONSE_MESSAGE":"Order Placed Successfully"}),
                    #         content_type="application/json")
                    # else:
                    #
                    #     return HttpResponse(json.dumps({"SUCCESS":True, "RESPONSE_MESSAGE":"Order Placed Successfully2"}),
                    #         content_type="application/json")




                else:
                    return HttpResponse(json.dumps({"SUCCESS":False, "RESPONSE_MESSAGE":"Error", "ERROR":order_item_form.errors}),
                        content_type="application/json")


            order_log_data = {}
            order_log_data["status"] = dbconstants.ORDER_PLACED

            order_log_form = OrderLogForm(order_log_data)

            if order_log_form.is_valid():
                order_log = order_log_form.save(commit=False)
                order_log.order = order
                order_log.save()

                return HttpResponse(json.dumps({"SUCCESS":True, "RESPONSE_MESSAGE":"Order Placed Successfully"}),
                    content_type="application/json")

                # print(item)

        else:
            return HttpResponse(json.dumps({"SUCCESS":False, "RESPONSE_MESSAGE":"Error", "ERROR":order_form.errors}),
                content_type="application/json")


    # return Response(base_data)


@csrf_exempt
def order_create(request):
        # received_json_data=json.loads(request.body)

        # print(request.POST)
        # if request.method == "POST":
        #     data = request.POST
        #
        #
        #
        #     return HttpResponse(json.dumps({"SUCCESS":False, "RESPONSE_MESSAGE":"Error", "ERROR":{"Name":"Error"}}),content_type="application/json")
        # else:
        #     return HttpResponse(json.dumps({"SUCCESS":False, "RESPONSE_MESSAGE":"Go F*uck yourself", "ERROR":{"Name":"Error"}}),content_type="application/json")


    if request.method == "POST":

        # json.loads(request.body)
        received_json_data=request.POST
        print("resssa")
        print(received_json_data)

        user = received_json_data["user"]
        item_list = received_json_data["item_list"]

        # print(user)
        # print(user["land_mark"])

        user_profile = UserProfileInfo.objects.get(phone_primary=user["phone"])

        # order_form = IOrderForm(request.POST, request.FILES, instance=user)
                # fields = ('order_id', 'user_customer', 'delivery_charges')
        order_data = {}
        # order_data["order_id"] = "3343322"
        # order_form.user_customer = user
        order_data["delivery_charges"] = 20
        # order_data["user_customer"] = user

        order_form = IOrderForm(order_data)
        # order_form.order_id = "3343322"

        # order_form.delivery_charges = 20

        if order_form.is_valid():
            order = order_form.save(commit=False)
            order.user_customer = user_profile
            order.order_id = unique_order_id_generator(order)
            order.save()


            for item in item_list:

                # "product_id":24, "uom_id":7,"quantity":5
                        # fields = ('order_item_id', 'product' 'item_name', 'item_quantity', 'order', 'measurement_unit')
                order_item_data = {}

                print("cameotem")
                print(item)
                order_item_data["item_name"] = "test"
                order_item_data["item_quantity"] = item['quantity']

                order_item_form = IOrderItemForm(order_item_data)

                if order_item_form.is_valid():


                    order_item = order_item_form.save(commit=False)
                    order_item.order = order
                    order_item.order_item_id = unique_order_item_id_generator(order_item)
                    order_item.product = Product.objects.get(id = item['product_id'])
                    print("eachit")
                    # print(item['uom_id'])
                    print(order_item.product.measurement_unit)
                    # order_item.measurement_unit = ItemMeasuementUnit.objects.get(id = item['uom_id'])
                    order_item.measurement_unit = order_item.product.measurement_unit
                    order_item.save()

                    # fields = ('status', 'order_item')
                    order_item_log_data = {}
                    order_item_log_data["status"] = dbconstants.O_ITEM_PLACED

                    order_item_log_form = OrderItemLogForm(order_item_log_data)

                    if order_item_log_form.is_valid():
                        order_item_log = order_item_log_form.save(commit=False)
                        order_item_log.order_item = order_item
                        order_item_log.save()






                else:
                    return HttpResponse(json.dumps({"SUCCESS":False, "RESPONSE_MESSAGE":"Error", "ERROR":order_item_form.errors}),
                        content_type="application/json")


            order_log_data = {}
            order_log_data["status"] = dbconstants.ORDER_PLACED

            order_log_form = OrderLogForm(order_log_data)

            if order_log_form.is_valid():
                order_log = order_log_form.save(commit=False)
                order_log.order = order
                order_log.save()


                # print(item)

        else:
            return HttpResponse(json.dumps({"SUCCESS":False, "RESPONSE_MESSAGE":"Error", "ERROR":order_form.errors}),
                content_type="application/json")



# unique_order_id_generator

            # order = CMN_CommunicationPhysicalModel.objects.get(slug=CMN_CommunicationPhysicalModel_data["slug"])
            # serializer_communication_physical = CMN_CommunicationPhysicalModelSerializer(instance = order_obj, data=CMN_CommunicationPhysicalModel_data, partial=True)






    # return HttpResponse(json.dumps({"SUCCESS":True, "RESPONSE_MESSAGE":"Status updated"}),
    #     content_type="application/json")


@csrf_exempt
def change_product_status(request):


    print(request.POST)

    product_id = request.POST['product_id']
    status = request.POST['status']
    product = Product.objects.get(id=product_id)

    print("camerr")

    user_status = True

    if status == "ENABLE":
        print("useractive")
        user_status = True
    else:
        user_status = False
        print("userinactive")
    product.is_available = user_status
    product.save()

    return HttpResponse(json.dumps({"SUCCESS":True, "RESPONSE_MESSAGE":"Status updated"}),
    content_type="application/json")


@csrf_exempt
def validate_user(request):

    if request.method == "POST":

        received_json_data=json.loads(request.body)

        print("recdd")
        print(received_json_data)
        phone = received_json_data["phone"]


        user_profile1 = UserProfileInfo.objects.filter(phone_primary=phone)



        if not user_profile1:
            return HttpResponse(json.dumps({"SUCCESS":False, "RESPONSE_MESSAGE":"User Not Exist"}), content_type="application/json")
        else:
            user_profile = UserProfileInfo.objects.get(phone_primary=phone)
            lang = received_json_data["user_lang"]
            user_profile.user_language = lang
            user_profile.save()

            print("rec_un")
            user_name = str(user_profile.user)
            print(user_name)
            user = User.objects.get(username = user_name)
            user_data = {}
            user_data["name"] = user.first_name
            user_data["location_latitude"] = user_profile.location_latitude
            user_data["location_longitude"] = user_profile.location_latitude

            return HttpResponse(json.dumps({"SUCCESS":True, "data": user_data, "RESPONSE_MESSAGE":"User Exist"}), content_type="application/json")


@csrf_exempt
def change_order_status(request):

    print("camemee")

    orderid = request.POST['order_id']
    orderstatus = request.POST['order_status']

    order_obj = Order.objects.get(order_id=orderid)
    updated_order_sataus=""
    for key, value in dbconstants.ORDER_STATUS:
        if value == orderstatus:
            updated_order_sataus= key
    order_obj.status = updated_order_sataus
    order_obj.save()

    return HttpResponse(json.dumps({"SUCCESS":True, "RESPONSE_MESSAGE":"Order status updated"}),
    content_type="application/json")



@csrf_exempt
def register_user(request):

    if request.method == "POST":

        received_json_data=json.loads(request.body)

        phone = received_json_data["phone"]
        name = received_json_data["name"]


        user = UserProfileInfo.objects.filter(phone_primary=phone)

        if not user:
            user_name_t = name.replace(" ", "_")
            user_name = createUserName(user_name_t)

            print("user_name")
            print(received_json_data)

            user_data = {}
            user_data["first_name"] = name
            user_data["username"] = user_name
            user_data["email"] = user_data["username"]+"@mycity.com"
            user_data["password"] = user_data["username"]+"@123"
            user_data["phone_primary"] = phone
            user_data["phone_secondary"] = received_json_data["whatsapp"]

            if "user_language" in received_json_data:
                user_data["user_language"] = received_json_data["user_language"]

            user_data["location_area"] = received_json_data["location_area"]


            if "location_sublocality" in received_json_data:
                if received_json_data["location_sublocality"] != "":
                    user_data["location_sublocality"] = received_json_data["location_sublocality"]
                else:
                    user_data["location_sublocality"] = "NOT AVAILABLE"

            else:
                user_data["location_sublocality"] = "NOT AVAILABLE"


            if "location_locality" in received_json_data:
                if received_json_data["location_sublocality"] != "":
                    user_data["location_locality"] = received_json_data["location_locality"]
                else:
                    user_data["location_locality"] = "NOT AVAILABLE"
            else:
                user_data["location_locality"] = "NONE"


            if "location_city" in received_json_data:
                user_data["location_city"] = received_json_data["location_city"]
            else:
                user_data["location_city"] = "NONE"

            user_data["location_state"] = received_json_data["location_state"]

            user_data["location_pincode"] = received_json_data["pincode"]

            user_data["location_latitude"] = received_json_data["location_latitude"]
            user_data["location_longitude"] = received_json_data["location_longitude"]


            user_data["age"] = received_json_data["age"]
            user_data["gender"] = received_json_data["gender"][0]

            # print("serrrddaa")
            # print(user_data)

            user_form = UserFormCustomer(user_data)
            profile_form = UserProfileInfoForm(data=user_data)

            if user_form.is_valid() and profile_form.is_valid() :

                user = user_form.save()
                user.set_password(user.password)
                user = user_form.save()
                user.save()

                profile = profile_form.save(commit=False)
                # profile.ref_id = unique_ref_id_generator(profile)
                profile.user = user

                profile.save()
            else:
                print("errorsa")
                print(user_form.errors)
                print(profile_form.errors)
                return HttpResponse(json.dumps({"SUCCESS":False, "RESPONSE_MESSAGE":"Error", "ERROR":profile_form.errors} ), content_type="application/json")

            return HttpResponse(json.dumps({"SUCCESS":True, "RESPONSE_MESSAGE":"User Created SUccessfully"}), content_type="application/json")
        else:
            return HttpResponse(json.dumps({"SUCCESS":False, "RESPONSE_MESSAGE":"User2 already Exist"}), content_type="application/json")
    else:
        return HttpResponse(json.dumps({"SUCCESS":False, "RESPONSE_MESSAGE":"User3 already Exist"}), content_type="application/json")


def unique_order_item_id_generator(instance, new_ref_id=None):
    """
    This is for a Django project and it assumes your instance
    has a model with a slug field and a title character (char) field.
    """
    if new_ref_id is not None:
        ref_id = new_ref_id
    else:
        ref_id = "ODR"+random_string_generator(size=5)

    Klass = instance.__class__
    qs_exists = Klass.objects.filter(order_item_id=ref_id).exists()
    if qs_exists:
        new_ref_id = constants.REF_ID_PREF_DELIVERY_AGENT+random_string_generator(size=5)
        # "{ref_id}-{randstr}".format(
        #             ref_id=ref_id,
        #             randstr=random_string_generator(size=8, chars=string.ascii_uppercase)
        #         )
        return unique_order_item_id_generator(instance, order_item_id=new_ref_id)
    return ref_id


def unique_order_id_generator(instance, new_ref_id=None):
    """
    This is for a Django project and it assumes your instance
    has a model with a slug field and a title character (char) field.
    """
    if new_ref_id is not None:
        ref_id = new_ref_id
    else:
        ref_id = "ODR"+random_string_generator(size=5)

    Klass = instance.__class__
    qs_exists = Klass.objects.filter(order_id=ref_id).exists()
    if qs_exists:
        new_ref_id = constants.REF_ID_PREF_DELIVERY_AGENT+random_string_generator(size=5)
        # "{ref_id}-{randstr}".format(
        #             ref_id=ref_id,
        #             randstr=random_string_generator(size=8, chars=string.ascii_uppercase)
        #         )
        return unique_order_id_generator(instance, order_id=new_ref_id)
    return ref_id


def unique_ref_id_generator(instance, new_ref_id=None):
    """
    This is for a Django project and it assumes your instance
    has a model with a slug field and a title character (char) field.
    """
    if new_ref_id is not None:
        ref_id = new_ref_id
    else:
        ref_id = "USER_"+random_string_generator(size=5)

    Klass = instance.__class__
    qs_exists = Klass.objects.filter(ref_id=ref_id).exists()
    if qs_exists:
        new_ref_id = constants.REF_ID_PREF_DELIVERY_AGENT+random_string_generator(size=5)
        # "{ref_id}-{randstr}".format(
        #             ref_id=ref_id,
        #             randstr=random_string_generator(size=8, chars=string.ascii_uppercase)
        #         )
        return unique_ref_id_generator(instance, new_ref_id=new_ref_id)
    return ref_id


def createUserName(username):
    username_f = username
    user_check = User.objects.filter(username=username)
    count = 1

    while user_check.count() != 0:
        username_f = username+str(count)
        user_check = User.objects.filter(username=username_f)
        count = count+1
    return username_f



class SymptomSet(APIView):

    # def get(self,request):


    def get(self,request):

        category =  C19SymptomSet.objects.filter(is_available=True)
        serializer_cat = C19SymptomSetSerializer(category, many=True)

        base_data = {}


        base_data["symptomset"] = serializer_cat.data

        return Response(base_data)



# @csrf_exempt
# def getSymptomSet(request):
#
#     symptoms = C19SymptomSet.objects.filter(is_available=True)
#     #
#     # serializer = C19SymptomSetSerializer(symptoms, many=True)
#     #
#     # # return Response(serializer)
#     # # serialized_obj = serializers.serialize('json', [ serializer])
#
#     return HttpResponse(json.dumps({"SUCCESS":True, "Data":symptoms}),
#         content_type="application/json")
#

class ProductList(APIView):

    def get(self,request):
        print(":cameggg");

        category = ProductCategory.objects.filter(is_available=True)
        serializer_cat = ProductCategorySerializer(category, many=True)

        product = Product.objects.filter(is_available=True).order_by('-priority')



        serializer_pro = ProductSerializer(product, context={"language":"ta"},  many=True)

        product_base = ProductBase.objects.filter(is_available=True)
        serializer_pro_base = ProductBaseSerializer(product_base, many=True)


        itemMeasuementUnit_base = ItemMeasuementUnit.objects.filter(is_available=True)
        serialiser_itemMeasuementUnit_base = ItemMeasuementUnitSerializer(itemMeasuementUnit_base, many=True)

        base_data = {}

        base_data["uom"] = serialiser_itemMeasuementUnit_base.data
        base_data["category"] = serializer_cat.data
        base_data["product"] = serializer_pro.data
        base_data["product_base"] = serializer_pro_base.data

        return Response(base_data)


        #
        # # product = Product.objects.filter(is_available=True)
        #
        # serializer = ProductCategorySerializer(category, many=True)
        # # serializer = ProductSerializer(product, many=True)
        # # return Response(serializer.data)
        # return serializer

        # orders = ProductCategory.objects.filter(is_available=True)
        #
        # serializer = ProductCategorySerializer(orders, many=True)
        # return Response(serializer.data)

    def post(self,request):
        received_json_data = json.loads(request.body)
        #
        phone = received_json_data["user_phone"]
        print(":cameggg");

        print(received_json_data);

        category = ProductCategory.objects.filter(is_available=True)
        serializer_cat = ProductCategorySerializer(category, many=True)

        product = Product.objects.filter(is_available=True).order_by('-priority')

        user = UserProfileInfo.objects.get(phone_primary=phone)

        serializer_pro = ProductSerializer(product, context={"language":user.user_language},   many=True)

        product_base = ProductBase.objects.filter(is_available=True)
        serializer_pro_base = ProductBaseSerializer(product_base, many=True)


        itemMeasuementUnit_base = ItemMeasuementUnit.objects.filter(is_available=True)
        serialiser_itemMeasuementUnit_base = ItemMeasuementUnitSerializer(itemMeasuementUnit_base, many=True)

        base_data = {}

        base_data["uom"] = serialiser_itemMeasuementUnit_base.data
        base_data["category"] = serializer_cat.data
        base_data["product"] = serializer_pro.data
        base_data["product_base"] = serializer_pro_base.data

        return Response(base_data)

# # {"category_filter":"All"}
#         received_json_data=json.loads(request.body)
#         #
#         category_filter = received_json_data["category_filter"]
#
#         # category_filter = "All"
#
#         if category_filter == "All":
#              product = Product.objects.filter(is_available=True).order_by('-priority')
#              serializer_pro = ProductSerializer(product, many=True)
#
#
#              category = ProductCategory.objects.filter(is_available=True)
#              serializer_cat = ProductCategorySerializer(category, many=True)
#
#
#              product_base = ProductBase.objects.filter(is_available=True)
#              serializer_pro_base = ProductBaseSerializer(product_base, many=True)
#
#
#              itemMeasuementUnit_base = ItemMeasuementUnit.objects.filter(is_available=True)
#              serialiser_itemMeasuementUnit_base = ItemMeasuementUnitSerializer(itemMeasuementUnit_base, many=True)
#
#         else:
#
#             product = Product.objects.filter(is_available=True).order_by('-priority')
#             serializer_pro = ProductSerializer(product, many=True)
#
#             category = ProductCategory.objects.filter(is_available=True, id= category_filter)
#             serializer_cat = ProductCategorySerializer(category, many=True)
#
#             product_base = ProductBase.objects.filter(is_available=True, product_category = category)
#             serializer_pro_base = ProductBaseSerializer(product_base, many=True)
#
#             itemMeasuementUnit_base = ItemMeasuementUnit.objects.filter(is_available=True)
#             serialiser_itemMeasuementUnit_base = ItemMeasuementUnitSerializer(itemMeasuementUnit_base, many=True)
#
#         base_data = {}
#
#         base_data["uom"] = serialiser_itemMeasuementUnit_base.data
#         base_data["category"] = serializer_cat.data
#         base_data["product"] = serializer_pro.data
#         base_data["product_base"] = serializer_pro_base.data
#
#         return Response(base_data)

        #
        # serializer = CMN_CommunicationPhysicalModelSerializer(data=request.data)
        #
        # data={}
        # if serializer.is_valid():
        #     serializer.save()
        #     return Response(serializer.data, status=status.HTTP_200_OK)
        # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# def get_products(request):

def customer_heatmap(request):

# data =     [
# {
# position: new google.maps.LatLng(-33.91721, 151.22630),
# type: 'info'
# }]


    user_list = UserProfileInfo.objects.prefetch_related('user').filter(user_m_status = dbconstants.M_STATUS_POSITIVE).order_by('-created_at')


    user_l_positive = []
    for user_p in user_list:
        arr = {}
        arr["lat"] = user_p.location_latitude
        arr["lon"] = user_p.location_longitude
        user_l_positive.append(arr)
            # user_l_positive.append(user_p.location_latitude+", "+user_p.location_longitude)

    print("tesssss")
    print(user_l_positive)

    return render(request, 'GEN/heatmaps.html',  {"user_positive":user_l_positive})


def customer_list(request):

    user_list = UserProfileInfo.objects.prefetch_related('user').filter(user_type = dbconstants.USER_TYPE_CONSUMER).order_by('-created_at')
    # user_list = User.objects.all().select_related('user_profile_info')

    # user_profile_list.

    user_list_final = []



    c_status = {}


# M_STATUS_POSITIVE = 'PTV'
# M_STATUS_NEGATIVE = 'NTV'
# M_STATUS_TEST_IN_PROGRESS = 'TIP'
# M_STATUS_NOT_TESTED = "NTD"
#
# M_STATUS_TYPES = [
#         (M_STATUS_POSITIVE, 'M_STATUS_POSITIVE'),
#         (M_STATUS_NEGATIVE, 'M_STATUS_NEGATIVE'),
#         (M_STATUS_TEST_IN_PROGRESS, 'M_STATUS_TEST_IN_PROGRESS'),
#         (M_STATUS_NOT_TESTED, 'M_STATUS_NOT_TESTED'),
#      ]

    c_status["PTV"] = "TESTED_POSITIVE"
    c_status["NTV"] = "TESTED_NEGATIVE"
    c_status["TIP"] = "TEST_IN_PROGRESS"
    c_status["NTD"] = "NOT_TESTED"





    for user_temp in user_list:
        # print("caddd")
        user_meta_raw = User.objects.get(username=user_temp.user)
        # print(user_meta_raw.username)
        user_meta = {}
        user_meta['username'] = user_meta_raw.username
        user_meta['fullname'] = user_meta_raw.first_name
        user_meta['c_status'] =c_status[user_temp.user_m_status]

        #
        #
        # user_temp['profile_pic_absolute'] =  appendServerPath(user_temp['profile_pic'])
        # user_temp.profile_pic("aa","aa")
        # pic = user_temp.profile_pic
        # print(pic)
        user_parent_set = {}
        # user_parent_set['profile_pic'] = appendServerPath(user_temp.profile_pic)
        user_parent_set['user_meta'] = user_meta
        user_parent_set['user_profile'] = user_temp
        #
        user_list_final.append(user_parent_set)

    serialized_obj = serializers.serialize('json', user_list)

    print("sizeb:"+ str(user_list.count()))

    page = request.GET.get('page', 1)

    paginator = Paginator(user_list_final, 10)
    try:
        users = paginator.page(page)
    except PageNotAnInteger:
        users = paginator.page(1)
    except EmptyPage:
        users = paginator.page(paginator.num_pages)
    return render(request, 'GEN/customers.html',  {'state_list':dbconstants.STATE_LIST_DICT, 'users': users})



# @login_required
def orders_list(request):


    # order_list = Order.objects.prefetch_related('user_customer').prefetch_related('user_delivery_agent').all().order_by('-updated_at')
    order_list = Order.objects.prefetch_related('user_customer').all().order_by('-updated_at')
    order_list_final = []

    for order_temp in order_list:
        # print("caddd")
        # print("cadddw"+str(order_temp.user_customer))
        user_customer_m =User.objects.get(username = order_temp.user_customer)
        user_customer = UserProfileInfo.objects.get(user = user_customer_m)
        #
        # user_delivery_agent_m =User.objects.get(username = order_temp.user_delivery_agent)
        # user_delivery_agent = UserProfileInfo.objects.get(user=user_delivery_agent_m)

        user_customer.user_location_display = user_customer.location_area +','+user_customer.location_sublocality+","+user_customer.location_city+","+user_customer.location_pincode


        # getting order item

        order_items = OrderItem.objects.filter(order = order_temp)
        # print("sizeaaa:"+ str(order_items.count()))

        item_name =""

        for order_item in order_items:

            if item_name != '':
                item_name += ", "+str(order_item.item_name)+" : " +str(order_item.item_quantity) + " " +str(order_item.measurement_unit)
            else:
                item_name += str(order_item.item_name) +" : " +str(order_item.item_quantity) + " " +str(order_item.measurement_unit) 

        order_temp.order_items = item_name

        # getting status text
        order_temp.status = dbconstants.ORDER_STATUS_DIC[order_temp.status]




        # print(user_meta_raw.username)
        order_foreign = {}
        order_foreign['user_customer'] = user_customer
        # order_foreign['user_delivery_agent'] = user_delivery_agent

        #
        #
        order_parent_set = {}
        order_parent_set['order_meta'] = order_temp
        order_parent_set['order_foreign'] = order_foreign
        #
        order_list_final.append(order_parent_set)
        # print("sizeb:"+ JsonResponse(json.loads(order_list_final)))
        # serialized_obja = serializers.serialize('json', order_parent_set)
        # # # filter(user__username ='azr')
        # # # user_list = User.objects.filter(username ='azr')
        # dataa = {"aSomeModel_json": serialized_obja}
        # ("atitaa")
        # print(dataa)
        #
        #




    # fetching prerequistis data for screen

    state_list  = dbconstants.STATE_LIST_DICT
    measurements_list = ItemMeasuementUnit.objects.all()
    # delivery_agents_list = UserProfileInfo.objects.prefetch_related('user').filter(user_type = dbconstants.USER_TYPE_DELIVERY_AGENT)
    order_status_list = dbconstants.ORDER_STATUS_DIC
    # for meas in measurements_list:
    #     print("came print m"+meas.name)
    #

    page = request.GET.get('page', 1)

    paginator = Paginator(order_list_final, 9)
    try:
        orders = paginator.page(page)
    except PageNotAnInteger:
        orders = paginator.page(1)
    except EmptyPage:
        orders = paginator.page(paginator.num_pages)
    # print("test1")
    return render(request, 'GEN/orders_list.html',  { 'orders': orders,  'measurements_list':measurements_list, 'state_list':state_list , 'order_status_list':order_status_list })


# @login_required
def product_list(request):

    product_list = Product.objects.all()

    product_list_final = []

    for product_i in product_list:

        each_obj = {}
        each_obj["id"] = str(product_i.id)+""
        each_obj["name"] = product_i.name+""
        each_obj["is_available"] = product_i.is_available

        each_obj["pic"] = appendServerPath(product_i.pic)
        each_obj["measurement_unit"] = str(product_i.measurement_unit)+""

        product_list_final.append(each_obj)

        # print(product_i.measurement_unit)

    # field_dic = dict_01()

    uom = ItemMeasuementUnit.objects.all()
    page = request.GET.get('page', 1)

    paginator = Paginator(product_list, 9)
    try:
        orders = paginator.page(page)
    except PageNotAnInteger:
        orders = paginator.page(1)
    except EmptyPage:
        orders = paginator.page(paginator.num_pages)
    # print("test1")
    return render(request, 'GEN/product_list.html',  { 'products': product_list_final, "uoms": uom })


@login_required
def place_order(request):
    auth_logout(request)
    return HttpResponseRedirect(reverse('GEN:index'))

@login_required
def user_logout(request):
    auth_logout(request)
    return HttpResponseRedirect(reverse('GEN:index'))

def appendServerPath(relative_path):
    a = str(relative_path)
    return GEN_Constants.SERVER_PREFIX+"media/"+a

def user_login2(request):
    return HttpResponse(json.dumps({"SUCCESS":False, "RESPONSE_MESSAGE":"INVALID DATA", "ERRORS": {}}),
    content_type="application/json")

def user_login(request):
    # return HttpResponse("Hi came view")

    if request.method == "POST":

        username = request.POST['username']
        password = request.POST['password']

        print(username+"+==="+password)

        user = authenticate(request, username = username, password = password)

        if user:
            if user.is_active:
                print('active')
                auth_login(request,user)
                return HttpResponse(json.dumps({"SUCCESS":True, "RESPONSE_MESSAGE":"Login successful"}),
                content_type="application/json")


                # return HttpResponseRedirect(reverse('base_app:index'))
            else:
                errors_dict = {"DATA":"Not a valid data"}
                return HttpResponse(json.dumps({"SUCCESS":False, "RESPONSE_MESSAGE":"2INVALID DATA", "ERRORS": errors_dict}),
                content_type="application/json")

        else:
            errors_dict = {"DATA":"Not a valid data"}
            return HttpResponse(json.dumps({"SUCCESS":False, "RESPONSE_MESSAGE":"INVALID DATA", "ERRORS": errors_dict}),
            content_type="application/json")

    else:
        print('jdkada')
        return render(request, 'GEN/login.html', {})

    # return render(request, 'GEN/login.html', {})
#
#
# class EnterPriseForm(APIView):
#
#     def get(self,request):
#         orders = CMN_CommunicationPhysicalModel.objects.all()
#         serializer = CMN_CommunicationPhysicalModelSerializer(orders, many=True)
#         return Response(serializer.data)
#
#     def post(self,request):
#          # "CMN_CommunicationPhysicalModel__slug":"ssssaaee",
#         # CMN_CommunicationPhysicalModel__
#         # "CMN_CommunicationVirtualModel__slug":"TEST",
#         # "CMN_CommunicationVirtualModel__id":"TEST",
#         # "CMN_CommunicationPhysicalModel__slug": "Y6OVJRZ3",
#         form_data = { "CMN_CommunicationVirtualModel__communication_channel_value": '["Channel v"]', "CMN_CommunicationPhysicalModel__address_line_01": "address_line_01", "CMN_CommunicationPhysicalModel__address_line_02":"address_line_02", "CMN_CommunicationPhysicalModel__city":"city", "CMN_CommunicationPhysicalModel__district":"district", "CMN_CommunicationPhysicalModel__country":"country", "CMN_CommunicationPhysicalModel__pincode":"008877", "CMN_CommunicationPhysicalModel__state":"state"}
#         # "CMN_CommunicationPhysicalModel__state":"state",
#         # "CMN_CommunicationPhysicalModel__country":"country",
#         # serializer = CMN_CommunicationPhysicalModelSerializer(data=request.data)
#         clean_serializer_data = getSerializerCleanData(form_data)
#
#
#         CMN_CommunicationPhysicalModel_data = clean_serializer_data["CMN_CommunicationPhysicalModel"]
#         CMN_CommunicationVirtualModel_data = clean_serializer_data["CMN_CommunicationVirtualModel"]
#         #
#         # print("came tesss")
#         # print(CMN_CommunicationPhysicalModel_data)
#         data={}
#
#         if 'slug' in CMN_CommunicationPhysicalModel_data:
#             order_obj = CMN_CommunicationPhysicalModel.objects.get(slug=CMN_CommunicationPhysicalModel_data["slug"])
#             serializer_communication_physical = CMN_CommunicationPhysicalModelSerializer(instance = order_obj, data=CMN_CommunicationPhysicalModel_data, partial=True)
#         else:
#             slug = unique_slug_generator(CMN_CommunicationPhysicalModel)
#             CMN_CommunicationPhysicalModel_data.add("slug",slug)
#             serializer_communication_physical = CMN_CommunicationPhysicalModelSerializer(data=CMN_CommunicationPhysicalModel_data, partial=True)
#
#         if 'slug' in CMN_CommunicationVirtualModel_data:
#             order_obj = CMN_CommunicationVirtualModel.objects.get(slug=CMN_CommunicationVirtualModel_data["slug"])
#             serializer_communication_virtual = CMN_CommunicationVirtualModelSerializer(instance = order_obj, data=CMN_CommunicationVirtualModel_data, partial=True)
#         else:
#             slug = unique_slug_generator(CMN_CommunicationVirtualModel)
#             CMN_CommunicationVirtualModel_data.add("slug",slug)
#             serializer_communication_virtual = CMN_CommunicationVirtualModelSerializer(data=CMN_CommunicationVirtualModel_data, partial=True)
#
#         # return Response(CMN_CommunicationPhysicalModel_data, status=status.HTTP_400_BAD_REQUEST)
#         # serializer = CMN_CommunicationPhysicalModelSerializer(data=request.data)
#
#         # CMN_CommunicationPhysicalModel_data.add("id",8)
#
#         if serializer_communication_physical.is_valid():
#             # serializer_communication_physical.save()
#             if serializer_communication_virtual.is_valid():
#                 cm_p = serializer_communication_physical.save()
#                 cm_v = serializer_communication_virtual.save()
#
#                 print("vm success")
#
#             else:
#                 return Response(serializer_communication_virtual.errors, status=status.HTTP_400_BAD_REQUEST)
#             return Response(serializer_communication_physical.data, status=status.HTTP_200_OK)
#         else:
#             return Response(serializer_communication_physical.errors, status=status.HTTP_400_BAD_REQUEST)
#             # return Response(serializer_communication_physical.data, status=status.HTTP_200_OK)
#
#
#             # return Response(serializer_communication_virtual.data, status=status.HTTP_200_OK)
#
#         return Response(serializer_communication_physical.errors, status=status.HTTP_400_BAD_REQUEST)
#
#


def MergeDict(dict1, dict2):
    (dict2.update(dict1))
    return dict2


# @csrf_exempt
def add_enterprise_s(request):
    usera = authenticate(request, username = "azr", password = "q1w2e3r41")
    # form_data  = dict_01()
    # # form_data = {"CMN_CommunicationVirtualModel__slug":"TEST","CMN_CommunicationVirtualModel__id":"TEST",  "CMN_CommunicationPhysicalModel__pincode":"601201", "CMN_CommunicationPhysicalModel__slug":"601201"}
    # if request.method == "POST":
    #     for key, value in request.POST.items():
    #         print(key,value)
    #         form_data.add(key,value)
    #     print("aaat")
    #     print(form_data)
    # else:
    #     print("GET")
    #
    # # print request.POST
    #
    # print(form_data)


    # od = collections.OrderedDict(sorted(form_data.items()))
    # clean_serializer_data = getSerializerCleanData(form_data)
    # slug - unique_slug_generator
    # CMN_CommunicationPhysicalModel__
    # data_m = {"CMN_CommunicationPhysicalModel__slug":"ssssaaee", "CMN_CommunicationPhysicalModel__address_line_01": "address_line_01", "CMN_CommunicationPhysicalModel__address_line_02":"address_line_02", "CMN_CommunicationPhysicalModel__city":"city", "CMN_CommunicationPhysicalModel__district":"district","CMN_CommunicationPhysicalModel__state":"state","CMN_CommunicationPhysicalModel__country":"country", "CMN_CommunicationPhysicalModel__pincode":"pincod"}
    data_m = {"slug":"ssssaaee", "address_line_01": "address_line_01", "address_line_02":"address_line_02", "city":"city", "district":"district","state":"state","country":"country", "pincode":"pincod"}
# , 'city':'city', 'country':'country', 'address_line_02': 'DSDW', 'address_line_01': 'WEWRSD','state': 'SDSD', 'district': 'FSDFDSF', 'pincode': '000000'}
    serializer = CMN_CommunicationPhysicalModelSerializer(data=data_m)

    # CMN_CommunicationPhysicalModel

    if serializer.is_valid():
        # serializer.save(user=usera, date=timezone.now(), status='sent')
        serializer.save(user=usera)

    # field_arr = ["HAHAH"]
    return JsonResponse({'sucees':serializer.errors}, safe=False)

# def posta(request):
#         serializer = CMN_CommunicationPhysicalModelSerializer(data=request.data)
#         data={}
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def user_logind(request):
    user = authenticate(request, username = "azr", password = "q1w2e3r41")

    # # return HttpResponse("Hi came view")
    #
    # if request.method == "POST":
    #
    #     username = request.POST['username']
    #     password = request.POST['password']
    #
    #     print(username+"+==="+password)
    #
    #     user = authenticate(request, username = username, password = password)
    #
    #     if user:
    #         if user.is_active:
    #             print('active')
    #             auth_login(request,user)
    #             return HttpResponse(json.dumps({"SUCCESS":True, "RESPONSE_MESSAGE":"Login successful"}),
    #             content_type="application/json")
    #
    #
    #             # return HttpResponseRedirect(reverse('GEN:index'))
    #         else:
    #             errors_dict = {"DATA":"Not a valid data"}
    #             return HttpResponse(json.dumps({"SUCCESS":False, "RESPONSE_MESSAGE":"2INVALID DATA", "ERRORS": errors_dict}),
    #             content_type="application/json")
    #
    #     else:
    #         errors_dict = {"DATA":"Not a valid data"}
    #         return HttpResponse(json.dumps({"SUCCESS":False, "RESPONSE_MESSAGE":"INVALID DATA", "ERRORS": errors_dict}),
    #         content_type="application/json")
    #
    # else:
    #     print('jdkada')
    #     return render(request, 'GEN/login.html', {})


def index(request):
    # enterpriseform_s
    # print("came changestat")

    # if request.method == 'GET':
    #     orders = Order.objects.all()
    #     serializer = OrderSerializer(orders, many=True)
    #     return JsonResponse(serializer.data, safe=False)
    #
    # elif request.method == 'POST':
    #     data = JSONParser.parse(request)
    #     serializer =OrderSerializer(data=data)
    #
    #     if(serializer.is_valid()):
    #         serializer.save()
    #         return JsonResponse(serializer.data, status=201)
    #     return JsonResponse(serializer.errors, status=400)

    # username = request.POST['username']
    # user_status = request.POST['user_status']
    #
    # user_obj = User.objects.get(username=username)
    # user_profile = UserProfileInfo.objects.get(user=user_obj)
    #
    # # user_profile = UserProfileInfo.objects.get(username=username)
    #
    # if user_status == "AT":
    #     print("useractive")
    #     user_status = dbconstants.USER_STATUS_DISABLED
    # else:
    #     user_status = dbconstants.USER_STATUS_ACTIVE
    #     print("userinactive")
    # user_profile.user_status = user_status
    # user_profile.save()
    # return render(request, 'GEN/base.html',  {})
    # return HttpResponse(json.dumps({"SUCCESS":True, "RESPONSE_MESSAGE":"Status updated"}),
    # content_type="application/json")
    # form_f = [{"fn": "company_name", "dt": "Text_100", "rq": true, "ph": "Enterprise Name"},{"fn": "company_mail", "dt": "Email", "rq": true, "ph": "Enterprise Email"}]
     # return HttpResponse(json.dumps({"SUCCESS":True, "RESPONSE_MESSAGE":"Status updated"})


     # CMN_CommunicationVirtualModelSerializer

     # [{"fn": "company_name", "dt": "Text_100", "rq": true, "ph": "Enterprise Name"},{"fn": "company_mail", "dt": "Email", "rq": true, "ph": "Enterprise Email"}]

    # return render(request, 'GEN/base.html',  {})
    # orders = CMN_CommunicationVirtualModel.objects.all()
    # serializer = CMN_CommunicationVirtualModelSerializer(orders, many=True)
    # return JsonResponse(serializer.data, safe=False)

    field_arr = []

    form_fields = ["CMN_CommunicationVirtualModel__slug", "CMN_CommunicationVirtualModel__communication_type", "CMN_CommunicationVirtualModel__communication_channel_key", "CMN_CommunicationVirtualModel__communication_channel_value", "CMN_CommunicationPhysicalModel__communication_type", "CMN_CommunicationPhysicalModel__address_line_01", "CMN_CommunicationPhysicalModel__address_line_02", "CMN_CommunicationPhysicalModel__city", "CMN_CommunicationPhysicalModel__district", "CMN_CommunicationPhysicalModel__state", "CMN_CommunicationPhysicalModel__pincode"]
    serializer = EnterPriseForm()

    field_arr =getSerilalierField(serializer,field_arr, "Parent", form_fields)
    return JsonResponse(field_arr, safe=False)

def add_enterprise(request):

    field_arr = []

    form_fields = ["CMN_CommunicationVirtualModel__slug", "CMN_CommunicationVirtualModel__communication_type", "CMN_CommunicationVirtualModel__communication_channel_key", "CMN_CommunicationVirtualModel__communication_channel_value", "CMN_CommunicationPhysicalModel__communication_type", "CMN_CommunicationPhysicalModel__address_line_01", "CMN_CommunicationPhysicalModel__address_line_02", "CMN_CommunicationPhysicalModel__city", "CMN_CommunicationPhysicalModel__district", "CMN_CommunicationPhysicalModel__state", "CMN_CommunicationPhysicalModel__pincode"]

    serializer = EnterPriseForm()

    field_arr =getSerilalierField(serializer,field_arr, "Parent", form_fields)
    return JsonResponse(field_arr, safe=False)



class dict_01(dict):

    # __init__ function
    def __init__(self):
        self = dict()

    # Function to add key:value
    def add(self, key, value):
        self[key] = value

def getSerializerCleanData(form_data):

    model_dic = dict_01()

    model_name = "NONE"
    field_dic = dict_01()
    field_set = []

    for key in form_data:

        print(key)
        split = key.split("__");
        model_name_c = split[0]

        if model_name != model_name_c:
            if model_name != "NONE":
                model_dic.add(model_name, field_dic)
            model_name = model_name_c
            field_dic = dict_01()


        field_name = split[1]
        field_dic.add(field_name, form_data[key])

    model_dic.add(model_name, field_dic)
    print(model_dic)
        # if(last)
        # model_dic.add(model_name, field_dic)

    return model_dic;

def getSerilalierField(serializer_obj,field_arr, model ,form_fields ):
    for field_name, field_obj in serializer_obj.get_fields().items():

        if 'Serializer' in field_obj.__class__.__name__ and field_obj.__class__.__name__ != 'SerializerMethodField':
            field_arr=getSerilalierField(field_obj, field_arr, field_obj.__class__.__name__, form_fields)
        else:
            name_final = model.replace("ModelSerializer", "Model")+"__"+field_name
            # name_final = name_final.replace("SerializerModel__", "Model__")
            if name_final in form_fields:
                each_obj ={}
                # each_obj['model'] = model
                each_obj['cn'] = name_final
                each_obj['dt'] = field_obj.help_text
                each_obj['dt_r'] = field_obj.__class__.__name__
                each_obj['required'] = field_obj.required
                if hasattr(field_obj, 'verbose_name'):
                    each_obj['lb'] = field_obj.verbose_name
                else:
                    v_name = field_name.replace("_"," ")
                    each_obj['lb'] = v_name

                if hasattr(field_obj, 'choices'):
                   each_obj['choices'] = field_obj.choices
                   # each_obj['dt'] = 'MOD_DT_CHOICES'
                # if hasattr(field_obj, 'label'):
                #    each_obj['lb'] = field_obj.label
                field_arr.append(each_obj)
    return field_arr;



def unique_slug_generator(Klass, new_slug=None):
    if new_slug is not None:
        slug = new_slug
    else:
        slug = random_string_generator(size=8)

    # Klass = instance.__class__
    qs_exists = Klass.objects.filter(slug= slug).exists()
    if qs_exists:
        new_slug = random_string_generator(size=8)
        return unique_slug_generator(Klass, new_slug= new_slug)
    return slug;

def unique_slug_generator_i(instance, new_slug=None):
    if new_slug is not None:
        slug = new_slug
    else:
        slug = random_string_generator(size=8)

    Klass = instance.__class__
    qs_exists = Klass.objects.filter(slug= slug).exists()
    if qs_exists:
        new_slug = random_string_generator(size=8)
        return unique_slug_generator(instance, new_slug= new_slug)
    return slug;


def random_string_generator(size=8, chars=string.ascii_uppercase +string.digits):
    return ''.join(random.choice(chars) for _ in range(size))
