from django.urls import path
from GEN import views
# from .views import EnterPriseForm

app_name = 'GEN'

urlpatterns =[
path('',views.user_login, name = "index"),
path('user_login/',views.user_login, name = "user_login"),
path('index/',views.index, name = "index"),
path('orders_list/', views.orders_list, name = "orders_list"),
path('change_product_status/', views.change_product_status, name = "change_product_status"),
# path('EnterPriseForm/', views.EnterPriseForm.as_view(), name = "EnterPriseForm"),
path('orders_list/',views.orders_list, name = "orders_list1"),
path('order_create/',views.order_create, name = "order_create"),
# path('getSymptomSet/',views.getSymptomSet, name = "getSymptomSet"),

path('login/',views.user_login, name = "login"),
path('logout/',views.user_logout, name = "logout"),
path('validate_user/',views.validate_user, name = "validate_user"),
path('register_user/',views.register_user, name = "register_user"),
path('ProductList/', views.ProductList.as_view(), name = "ProductList"),
path('SymptomSet/', views.SymptomSet.as_view(), name = "SymptomSet"),
path('CustomerOrder/', views.CustomerOrder.as_view(), name = "CustomerOrder"),

path('product_list/', views.product_list, name = "product_list"),
path('change_order_status/', views.change_order_status, name = "change_order_status"),
path('alter_order_item/', views.alter_order_item, name = "alter_order_item"),
path('alter_order/', views.alter_order_item, name = "alter_order"),
path('order_details/', views.order_details, name = "order_details"),
path('order_list_user/', views.order_list_user, name = "order_list_user"),
path('order_create_m/', views.order_create_m, name = "order_create_m"),

path('customer_heatmap/', views.customer_heatmap, name = "customer_heatmap"),

path('validate_app/',views.validate_app, name = "validate_app"),
path('product_list_suggestion/',views.product_list_suggestion, name = "product_list_suggestion"),
path('get_user_suggestion_list/',views.get_user_suggestion_list, name = "get_user_suggestion_list"),
path('get_user_details/',views.get_user_details, name = "get_user_details"),
path('feed_contact/',views.feed_contact, name = "feed_contact"),
path('feed_news/',views.feed_news, name = "feed_news"),
path('submit_symptoms/',views.submit_symptoms, name = "submit_symptoms"),
path('customer_list/',views.customer_list, name = "customer_list"),
path('change_user_status/',views.change_user_status, name = "change_user_status"),


# path('posta/',views.posta, name = "posta"),
# posta
 ]
