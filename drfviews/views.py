from django.shortcuts import render
from app1.models import  Product
from .models import  Laptop
from  .serialzers import ProductSerializer, LaptopSerializer
from  rest_framework.views import  APIView
from rest_framework.response import  Response
from  rest_framework.viewsets import  ModelViewSet
from  rest_framework.decorators import action

# Create your views here.
class ProductView(APIView):
    def get(self, request, pk):

        if pk:
            data = Product.objects.filter(id=pk).values()
        else:
            data = Product.objects.all().values()
        return  Response(data)

    def post(self,request):
        data = request.data
        Product.objects.create(
            name = data["name"],
            price=int(data["price"]),
            desc=data["desc"],
            rating=data["rating"],
            org_email=data["org_email"],
            org_website=data["org_website"],
            pro_image=data["pro_image"],
        )
        return  Response("data has been populated")
    def put(self,request,pk):
        data = request.data

        instance = Product.objects.get(id=pk)
        instance.name = data.get("name", instance.name)
        instance.price = data.get("price", instance.price)
        instance.desc = data.get("desc", instance.desc)
        instance.rating = data.get("rating", instance.rating)
        instance.org_email = data.get("org_email", instance.org_email)
        instance.org_website = data.get("org_website", instance.org_website)
        instance.pro_image = data.get("pro_image", instance.pro_image)
        instance.save()
        return Response("data updated successfully")

    def delete(self, request, pk):
        instance = Product.objects.get(id=pk)
        instance.delete()
        return Response("data has been deleted")

class ProViewset(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    @action(methods=["get"], detail=True, url_path="branded")
    def get_branded(self, request, *args, **kwargs):
        data = self.get_object()
        print(data)
        result = Product.objects.filter(price__gte = 100000).values()
        return Response(result)


class LapView(ModelViewSet):
    queryset = Laptop.objects.all()
    serializer_class = LaptopSerializer