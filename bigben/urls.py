from django.urls import path
from .import views

urlpatterns=[
   path('home',views.index,name='home'),
   path('about',views.bath,name='about'),
   path('work',views.document,name='work'),
   path('new',views.other,name='new'),
   path('card',views.smart,name='card'),
   path('js',views.java,name='js'),
   path('condition',views.condition,name='condition'),
   path('bootstrap',views.bootstrap,name='bootstrap'),
   path('array',views.array,name='array'),
   path('dom',views.docu,name='dom'),
   path('dom2',views.doc,name='dom2'),
   path('calculator',views.calcu,name='calculator')
   
]