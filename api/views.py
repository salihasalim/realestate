from django.shortcuts import render

from rest_framework.views import APIView

from api.models import Property

from api.serializers import PropertySerializer

from rest_framework.response import Response

class PropertyListcreateView(APIView):

    serializer_class=PropertySerializer

    def get(self,request,*args,**kwargs):

        qs=Property.objects.all()


        if "property_type" in request.query_params:

            filter_text=request.query_params.get("property_type")

            qs=qs.filter(property_type=filter_text)

        # serialization

        serializer_instance=self.serializer_class(qs,many=True)  #query set to python native type

        
        return Response(data=serializer_instance.data)

    def post(self,request,*args,**kwargs):

        serializer_instance=self.serializer_class(data=request.data)

        if serializer_instance.is_valid():

            serializer_instance.save()

            return Response(data=serializer_instance.data)
        return Response(data=serializer_instance.errors)


class PropertyUpdateDeleteView(APIView):

    serializer_class=PropertySerializer

    def get(self,request,*args,**kwargs):

        id=kwargs.get("pk")

        qs=Property.objects.get(id=id)

        serializer_instance=self.serializer_class(qs)

        return Response(data=serializer_instance.data)



    def delete(self,request,*args,**kwargs):

        
        id=kwargs.get("pk")

        qs=Property.objects.get(id=id).delete()

        return Response(data={"message":"item deleted"})


    def put(self,request,*args,**kwargs):

        id=kwargs.get("pk")

        property_object=Property.objects.get(id=id)

        serializer_instance=self.serializer_class(data=request.data,instance=property_object)

        if serializer_instance.is_valid():

            serializer_instance.save()

            return Response(data=serializer_instance.data)
        
        return Response(data=serializer_instance.errors)


class PropertyTypeView(APIView):

   
    def get(self,request,*args,**kwargs):

        
        property_type=[tp[0] for tp in Property.PROPERTY_CHOICES]

        return Response(data=property_type)





