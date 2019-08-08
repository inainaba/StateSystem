from django.contrib.auth.models import AbstractUser, PermissionsMixin
from django.db import models

from stateapp.models import Table


# ユーザーモデル
class User(AbstractUser, PermissionsMixin):
    """
    必須(元User)
        username-30以下文字列
        password-ハッシュ
    追加
        table - 参加しているテーブル
        is_teacher - 教授か否か
    """
    table = models.ForeignKey(
        Table, on_delete='CASCADE', null='true', blank='true')
    is_teacher = models.BooleanField('教授か', default=False)
