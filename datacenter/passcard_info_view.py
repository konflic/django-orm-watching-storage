from django.shortcuts import render

from datacenter.helpers import get_duration, format_duration, is_visit_long
from datacenter.models import Passcard
from datacenter.models import Visit


def passcard_info_view(request, passcode):
    passcard = Passcard.objects.filter(passcode=passcode)[0]

    this_passcard_visits = []
    for visit in Visit.objects.filter(passcard=passcard):
        visit_duration = get_duration(visit)

        this_passcard_visits.append(
            {
                'entered_at': visit.entered_at,
                'duration': format_duration(visit_duration),
                'is_strange': is_visit_long(visit_duration)
            },
        )

    context = {
        'passcard': passcard,
        'this_passcard_visits': this_passcard_visits
    }

    return render(request, 'passcard_info.html', context)
