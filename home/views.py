from rest_Framework import viewsets,status
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser
from rest_framework.generics import ListAPIView
from .models import MenuCategory
from .serializers import MenuCategorySerializer

class MenuItemUpdateViewSet(viewsets.ViewSet):
    permission_classes=[IsAdminUser]

    def update(Self,request,pk=None):
        try:
            menu_item=MenuItem.objects.get(pk=pk)
        except MenuItem.DoesNotExist:
            return Response(
                {"error":"Menu item not found"},
                status=status.HTTP_404_NOT_FOUND
            )
        serializer=MenuItemSerializer(menu_item,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class MenuCategoryListView(ListAPIView):
    queryset=MenuCategory.objects.all()
    serializer_class=MenuCategorySerializer
    def retrieve(Self,request,*args,**kwargs):
        menu_item=self.get_object()
        ingredientts=menu_item.ingrediants.all()
        serializer=IngredientSerializer(ingredients,many=True)
        return Response(serializer.dat,status=status.HTTP_200_0K)
class MenuItemByCategoryView(APIView):
    def get(Self,request):
        category=request.query_params.get("category")
        if not category:
            return Response(
                {"error":"category query parameter is requeried"},
                status=status.HTTP_400_BAD_REQUEST
            )
        items=MenuItem.objects.filter(category__name__iexact=category)
        serializer=MenuItemSerializer(items,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
class TableDetailView(RetrieveAPIView):
    queryset=Table.objects.all()
    serializer_class=TableSerializer