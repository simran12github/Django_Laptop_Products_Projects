from  rest_framework.serializers import ModelSerializer, SerializerMethodField
from app1.models import Product
from .models import Laptop, LapImage

class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"

class LaptopSerializer(ModelSerializer):
    images = SerializerMethodField()

    def get_images(self,obj):
        image_data = LapImage.objects.filter(laptop__id = obj.id).values("id","image_name", "image")

        return image_data

    class Meta:
        model = Laptop
        fields = ["id","brand_name", "price", "configurations","rating", "images"]

    def create(self, validated_data):
        image_list = self.context.get("view").request.FILES
        #populating the data
        instance = Laptop.objects.create(
            brand_name = validated_data["brand_name"],
            price=validated_data["price"],
            configurations=validated_data["configurations"],
            rating=validated_data["rating"],
        )
        for img in image_list.getlist("image"):
            name = img.name
            LapImage.objects.create(image = img, laptop = instance, image_name = name )

        return instance

    def update(self, instance, validated_data):
        image_list = self.context.get("view").request.FILES
        delete_image_ids = self.context["request"].data.get("delete_img_id", None)
        delete_image_ids = eval(delete_image_ids)
        #print(type(delete_image_ids))
        instance.brand_name = validated_data.get("brand_name", instance.brand_name)
        instance.configurations = validated_data.get("configurations", instance.configurations)
        instance.price = validated_data.get("price", instance.price)
        instance.rating = validated_data.get("rating", instance.rating)

        #while updating laptop record if the user wanted delete existing laptop record connected images and add new images
        existing_image_instances = LapImage.objects.filter(id__in=delete_image_ids, laptop = instance).delete()

        for img in image_list.getlist("image"):
            name = img.name
            LapImage.objects.create(image = img, laptop = instance, image_name = name )


        return  instance

