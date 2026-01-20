from rest_framework.generics import ListAPIView
from .models import MenuCategory
from .serializers import MenuCategorySerializer
class MenuCategoryListView(ListAPIView):
    queryset=MenuCategory.objects.all()
    serializer_class=MenuCategorySerializer
    def retrieve(Self,request,*args,**kwargs):
        menu_item=self.get_object()
        ingredientts=menu_item.ingrediants.all()
        serializer=IngredientSerializer(ingredients,many=True)
        return Response(serializer.dat,status=status.HTTP_200_0K)
