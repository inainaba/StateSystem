from django.db import models


# ユーザーモデル (AbstractUserをコピペし編集)
class User(AbstractBaseUser, PermissionsMixin):
    """
    ID - auto 
    name - ユーザ名
    password - パスワード
    table - 参加しているテーブル
    """
    pass


# 状態モデル
class State(models.Model):
    """
    ID - auto
    state - 在室or離席or帰宅
          - 在室or離席or講義or出張or帰宅
    """
    state = models.CharField('状態', max_length=30)


# 出欠モデル
class Attendance(models.Model):
    """
    ID - auto
    user - 外部キー(User)
    state - 外部キー(State)
    """
    user = models.ForeignKey(User, on_delete='CASCADE')
    state = models.ForeignKey(State, on_delete='CASCADE')


# テーブルモデル
class Table(models.Model):
    """
    ID - auto
    name - テーブル名
    attendance - 外部キー(Attendance)
    seminar - ゼミ中かどうか(True or False)
    """
    name = models.CharField('テーブル名', max_length=200)
    Attendance = models.ForeignKey(Attendance, on_delete='CASCADE')
    seminar = models.BooleanField('ゼミ中か', default=False)
