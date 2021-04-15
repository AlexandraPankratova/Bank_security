import django
from django.shortcuts import render

from datacenter.models import Visit

from .models import format_duration, get_duration, is_visit_long


def storage_information_view(request):

    non_closed_visits = []

    for visitor in Visit.objects.filter(leaved_at=None):

        current_time = django.utils.timezone.now()

        visit_duration = get_duration(visitor.entered_at, current_time)

        non_closed_visits.append(
            {
                'visitor_name': visitor.passcard.owner_name,
                'entered_at': visitor.entered_at,
                'visit_duration': format_duration(
                    visit_duration.total_seconds(),
                ),
                'is_visit_long': is_visit_long(visit_duration.total_seconds()),
            }
        )

    context = {
        'non_closed_visits': non_closed_visits,
    }

    return render(request, 'storage_information.html', context)
