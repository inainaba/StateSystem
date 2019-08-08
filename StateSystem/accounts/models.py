from django.contrib.auth.models import AbstractUser, PermissionsMixin
from django.db import models

from stateapp.models import Table


# ユーザーモデル (AbstractUserをコピペし編集)
class User(AbstractUser, PermissionsMixin):
    """
    追加
    table - 参加しているテーブル
    """
    table = models.ForeignKey(
        Table, on_delete='CASCADE', null='true', blank='true')
