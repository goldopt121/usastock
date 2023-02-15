from  django.urls import path
from . import views

# ALL PATHS

urlpatterns=[
    path('', views.index),
    path('update/', views.uploads),
    path('about/', views.about),
    path('signup/', views.signup),
    path('login/', views.login),
    path('account/', views.account),
    path('deposit/', views.deposit),
    path('wallet/', views.wallet),
    path('withdraw/', views.withdraw),
    path('bank/', views.bank),
    path('livetrade/', views.livetrade),
    path('setup/', views.setup),
    path('card/', views.card),
    path('upgrade/', views.cardv),
    path('history/', views.history),
    path('list/', views.list),
    path('admin/', views.admin),
    path('edit/', views.edit),
    path('market/', views.market),
    path('order/', views.order),
    path('site/', views.site),
    path('logout/', views.logout),

]