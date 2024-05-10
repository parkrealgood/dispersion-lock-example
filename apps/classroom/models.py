from django.db import models
from django.db.models import F

from apps.core.distribute_lock import DistributedLock


class ClassRoom(models.Model):
    name: str = models.CharField(max_length=100, verbose_name='강의실 이름')
    total_capacity: int = models.PositiveIntegerField(verbose_name='최대 수용 인원')
    remaining_capacity: int = models.PositiveIntegerField(verbose_name='남은 수용 인원')

    class Meta:
        db_table = 'classroom'
        verbose_name = '강의실'
        verbose_name_plural = '강의실 목록'

    def __str__(self):
        return self.name
