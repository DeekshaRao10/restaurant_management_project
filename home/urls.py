from django.urls import path,inlcude
from rest_framework.routers import DefaultRouter
from .views import MenuItemSearchViewSet

router=DefaultRouter()
router.register(r"menu-item/serach",MenuItemSearchViewSet,basename="menu-item-serach")

urlpatterns=[
    path("",include(router.urls)),
]

urlpatterns = [
    path('menu-categories/',MenuCategoryListView.as_view(),name='menu-categories'),
    
]