from django.shortcuts import render
from .models import Product, Person, Profile
from django.http import HttpResponse, JsonResponse
from  django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import  api_view
from  rest_framework.response import  Response
# Create your views here.
import json
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
from  rest_framework.authtoken.models import  Token
from django.views.generic import ListView, DetailView

@receiver(post_save, sender = User)
def create_auth_token(sender, instance = None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)

@api_view(["GET", "POST", "PUT", "DELETE"])
def type_req(request):
    if request.method == "GET":
        """
        using this get method we return all the datas from the product table
        """
        data = Product.objects.all().values()
        return  Response(data)

    elif request.method == "POST":
        payload = request.data

        Product.objects.create(
            name = payload["name"],
            price=payload["price"],
            desc=payload["desc"],
            rating=payload["rating"],
            org_email=payload["org_email"],
            org_website=payload["org_website"],
            pro_image=payload["pro_image"]
        )
        return  Response("data posted successfully")

    elif request.method == "PUT":
        """
        get() will fetch the specific data
        filter() will fetch all the matching
        we updated if the payload has the key with new values else we keep the old records only
        """
        payload = request.data

        instance = Product.objects.get(id = payload["id"])
        instance.name = payload.get("name", instance.name)
        instance.price = payload.get("price", instance.price)
        instance.desc = payload.get("desc", instance.desc)
        instance.rating = payload.get("rating", instance.rating)
        instance.org_email = payload.get("org_email", instance.org_email)
        instance.org_website = payload.get("org_website", instance.org_website)
        instance.pro_image = payload.get("pro_image", instance.pro_image)
        instance.save()

        return HttpResponse("data updated successfully")

    elif request.method == "DELETE":
        payload = request.data

        instance = Product.objects.get(id=payload["id"])
        instance.delete()
        return  HttpResponse("data removed succesfully")


class ProductView(ListView):
    model = Product

class ProfileDetailView(DetailView):
    model = Person

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["profile"] = Profile.objects.filter(person = self.object)
        return context