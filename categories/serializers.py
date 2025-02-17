from rest_framework import serializers

class CategorySerializer(serializers.Serializer):

    pk = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=True)
    kind = serializers.CharField()
    created_at = serializers.DateTimeField(read_only=True)

    def create(self, validated_data):
        return Category.objects.create(**validated_data)

    def update(self, instance, validate_data):
        instance.name = validated_data.get('name', instance.name)
        instance.kind = validated_data.get('kind', instance.kind)
        instance.save()
        return instance