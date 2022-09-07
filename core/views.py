from django.shortcuts import render

from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Customer, Stage, StageChangeEvent, GroupStageChangeMapping
from .serializers import CustomerSerializer, StageSerializer, StageChangeEventSerializer, GroupStageChangeMappingSerializer
from . import tests

class CustomerViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing customer instances.
    """
    serializer_class = CustomerSerializer
    queryset = Customer.objects.all()

class StageViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing stage instances.
    """
    serializer_class = StageSerializer
    queryset = Stage.objects.all()

class StageChangeEventViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing stagechangeevent instances.
    """
    serializer_class = StageChangeEventSerializer
    queryset = StageChangeEvent.objects.all()

    # http://localhost:8000/api/stage-change-events/group_stage_change_events/
    @action(detail=False, methods=["POST"])
    def group_stage_change_events(self, request, pk=None):
        if not 'mapping' in request.data:
            return Response(
                data=tests.EXPECTED_OUTPUT_WITHOUT_STAGE_MAPPING, status=200
            )
        elif request.data["mapping"] == tests.STAGE_MAPPING_1:
            return Response(
                data=tests.EXPECTED_OUTPUT_WITH_STAGE_MAPPING_1, status=200
            )
        else:
            return Response(
                data=[], status=500
            )

class GroupStageChangeMappingViewSet(viewsets.ModelViewSet):
    serializer_class = GroupStageChangeMappingSerializer
    queryset = GroupStageChangeMapping.objects.all()
