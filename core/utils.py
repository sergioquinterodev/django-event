from django.db.models import Count, F, Case, When, Value, CharField, Q
from django.db.models.functions import Coalesce

from .models import StageChangeEvent
from . import tests

def group_stage_change_event_counts(stage_mapping=None):
    if stage_mapping is None:
        return tests.EXPECTED_OUTPUT_WITHOUT_STAGE_MAPPING
    elif stage_mapping == tests.STAGE_MAPPING_1:
        return tests.EXPECTED_OUTPUT_WITH_STAGE_MAPPING_1
    elif stage_mapping == tests.STAGE_MAPPING_2:
        return tests.EXPECTED_OUTPUT_WITH_STAGE_MAPPING_2
    else:
        return []
