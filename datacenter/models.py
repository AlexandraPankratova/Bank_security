import django
from django.db import models


class Passcard(models.Model):
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now=True)
    passcode = models.CharField(max_length=200, unique=True)
    owner_name = models.CharField(max_length=255)

    def __str__(self):
        if self.is_active:
            return self.owner_name
        return f'{self.owner_name} (inactive)'


class Visit(models.Model):
    created_at = models.DateTimeField(auto_now=True)
    passcard = models.ForeignKey(Passcard)
    entered_at = models.DateTimeField()
    leaved_at = models.DateTimeField(null=True)

    def __str__(self):
        return "{user} entered at {entered} {leaved}".format(
            user=self.passcard.owner_name,
            entered=self.entered_at,
            leaved="leaved at "+str(self.leaved_at) if self.leaved_at else "not leaved"
        )


def get_duration(entered_at, leaved_at):
    if leaved_at:
        visit_duration = leaved_at - entered_at
    else:
        current_time = django.utils.timezone.now()
        visit_duration = current_time - entered_at
    return visit_duration


def format_duration(visit_duration_in_seconds):
    visit_duration_hours = visit_duration_in_seconds // 3600
    visit_duration_minutes = (visit_duration_in_seconds - visit_duration_hours*3600) // 60
    visit_duration_seconds = visit_duration_in_seconds % 60
    visit_duration = '{:.0f}:{:.0f}:{:.0f}'.format(
        visit_duration_hours,
        visit_duration_minutes,
        visit_duration_seconds,
    )
    return visit_duration


def is_visit_long(visit_duration_in_seconds):
    if visit_duration_in_seconds > 3600:
        return 'True'
    else:
        return 'False'
