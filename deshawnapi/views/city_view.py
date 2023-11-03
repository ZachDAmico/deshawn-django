
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from deshawnapi.models import City


class CityView(ViewSet):

# retrieve() method is for single
    def retrieve(self, request, pk=None):
        # Step 1: Get a single city based on the primary key in the request URL
        city = City.objects.get(pk=pk)

        # Step 2: Serialize/convert the city record as/into JSON
        serialized = CitySerializer(city, many=False)

        # Step 3: Send JSON response to client with 200 status code
        return Response(serialized.data, status=status.HTTP_200_OK)

# list() method is for all
    def list(self, request):
        # Step 1: Get all city data from the database
        cities = City.objects.all()

        # Step 2: Convert the data to JSON format
        serialized = CitySerializer(cities, many=True)

        # Step 3: Respond to the client with the JSON data and 200 status code
        return Response(serialized.data, status=status.HTTP_200_OK)


class CitySerializer(serializers.ModelSerializer):

# Meta is subclass
# specify what database model to use
# specify which fields in model should be in final JSON string
    class Meta:
        model = City
        fields = ('id', 'name',)

# can now use serializer in view to generate JSON from class instances - pass it two arguments
# 1 data structure to be serialized into JSON
# 2 set many to true if serializing a list, set to false if serializing single instance