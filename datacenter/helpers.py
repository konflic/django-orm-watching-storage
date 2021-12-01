from django.utils.timezone import localtime


def get_duration(visit):
    return (visit.leaved_at - visit.entered_at).total_seconds()


def format_duration(duration):
    hours = duration // (60 * 60)
    duration %= (60 * 60)
    minutes = duration // 60
    duration %= 60
    return "%02i:%02i:%02i" % (hours, minutes, duration)


def is_visit_long(visit, minutes=60):
    if not visit.leaved_at:
        duration = (visit.leaved_at - visit.entered_at)
    else:
        duration = (localtime() - visit.entered_at)
    return duration.total_seconds() > 60 * minutes
