from django.db import models


# ユーザーモデル (AbstractUserをコピペし編集)
class User(AbstractBaseUser, PermissionsMixin):
    """
    追加
    table - 参加しているテーブル
    """
    pass
