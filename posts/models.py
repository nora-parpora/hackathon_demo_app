from django.db import models

from accounts.models import Employer
from posts.enums import EmploymentType


class JobSector(models.Model):
    NAME_MAX_LENGTH = 50
    name = models.CharField(max_length=NAME_MAX_LENGTH)


class JobAdvert(models.Model):
    POSITION_MAX_LENGTH = 50
    CITY_MAX_LENGTH = 50
    DESCR_MAX_LENGTH = 1000
    position = models.CharField(max_length=POSITION_MAX_LENGTH)
    # ToDo Implement 'city' as a separate model and use OneToMany rel
    city = models.CharField(max_length=CITY_MAX_LENGTH)
    sector = models.ForeignKey(JobSector, blank=True, null=True, on_delete=models.SET_NULL)
    employment_type = models.CharField(max_length=30, choices=[(t.name, t.value) for t in EmploymentType])
    description = models.TextField(max_length=DESCR_MAX_LENGTH)
    employer = models.ForeignKey(Employer, on_delete=models.CASCADE)
