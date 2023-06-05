from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('faq',views.FAQ,name="faq"),
    path('addABook',views.add_a_book,name="AddABook"),
    path('addAMember',views.add_a_member,name="AddAMember"),
    path('checkOut',views.check_out,name="checkOut"),
    path('glossary',views.glossary,name="glossary"),
    path('searchCatalog',views.search_catalog,name="searchCatalog")
]