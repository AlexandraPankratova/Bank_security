from django.shortcuts import render

from datacenter.models import Passcard, Visit

from .models import format_duration, get_duration, is_visit_long


def passcard_info_view(request, passcode):

    passcard = Passcard.objects.get(passcode=passcode)

    this_passcard_visits = []

    for visits in Visit.objects.filter(passcard=passcard):

        visit_duration = get_duration(visits.entered_at, visits.leaved_at)

        this_passcard_visits.append({
            'entered_at':
            visits.entered_at,
            'visit_duration':
            format_duration(visit_duration.total_seconds()),
            'is_visit_long':
            is_visit_long(visit_duration.total_seconds()),
        })

    context = {
        'passcard': passcard,
        'this_passcard_visits': this_passcard_visits,
    }

    return render(request, 'passcard_info.html', context)
