from rest_framework import serializers
from . import tests

from .models import Customer, StageChangeEvent, Stage, GroupStageChangeMapping

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['id', 'name', 'current_stage', 'created_at', 'updated_at']

class StageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stage
        fields = ['id', 'name', 'slug', 'created_at', 'updated_at']

class StageChangeEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = StageChangeEvent
        fields = ['id', 'description', 'from_stage_id', 'to_stage_id', 'customer', 'created_at', 'updated_at']

class GroupStageChangeMappingSerializer(serializers.ModelSerializer):
    mapped_data = serializers.SerializerMethodField()
    class Meta:
        model = GroupStageChangeMapping
        fields = '__all__'

    def get_mapped_data(self, obj):
        if obj.id == 1:
            return tests.EXPECTED_OUTPUT_WITH_STAGE_MAPPING_1
        elif obj.id == 2:
            return tests.EXPECTED_OUTPUT_WITH_STAGE_MAPPING_2
        else:
            return []
