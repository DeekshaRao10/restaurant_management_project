from django.urls import path,inlcude
from rest_framework.routers import DefaultRouter
from .views import(
    MenuItemSearchViewSet,
    MenucategoryListView,
    MenuItemIngrediensView
)

router=DefaultRouter()
router.register(r"menu-item/serach",MenuItemSearchViewSet,basename="menu-item-serach")

urlpatterns=[
    path("",include(router.urls)),

    path('menu-categories/',MenuCategoryListView.as_view(),name='menu-categories'),
    path("menu-items/<int:pk>/ingredients/",MenuItemIngredientView.as_view,name="menu-item-ingredients"),
    
]