from django.shortcuts import render
from datacenter.models import Visit
from datacenter.helpers import format_duration, is_visit_long, get_duration


def storage_information_view(request):
    not_closed_visits = []

    for visit in Visit.objects.filter(leaved_at=None):
        duration = get_duration(visit)

        not_closed_visits.append({
            'who_entered': visit.passcard.owner_name,
            'entered_at': visit.entered_at,
            'duration': format_duration(duration),
            'is_strange': is_visit_long(duration)
        })

    context = {
        'non_closed_visits': not_closed_visits,
    }
    return render(request, 'storage_information.html', context)
