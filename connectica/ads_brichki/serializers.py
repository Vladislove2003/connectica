from rest_framework import serializers


class Ad:
    def __init__(self, brand, model, generation, engine_type, boost_type,
        drive, body, mileage, price):

        self.brand = brand
        self.model = model
        self.generation = generation
        self.engine_type = engine_type
        self.boost_type = boost_type
        self.drive = drive
        self.body = body
        self.mileage = mileage
        self.price = price


class AdSerializer(serializers.Serializer):
    brand = serializers.CharField(max_length=100)
    model = serializers.CharField(max_length=100)
    generation = serializers.CharField(max_length=100)
    engine_type = serializers.CharField(max_length=100)
    boost_type = serializers.CharField(max_length=100)
    drive = serializers.CharField(max_length=100)
    body = serializers.CharField(max_length=100)
    mileage = serializers.IntegerField()
    price = serializers.IntegerField()

    def create(self, validated_data):
        return Ad(**validated_data)