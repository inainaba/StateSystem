from django.contrib.auth.models import AbstractUser, UserManager, PermissionsMixin
from django.db import models
from django.utils.translation import gettext_lazy as _


# ユーザーマネージャー
class UserManager(UserManager):
    def _create_user(self, email, password, **extra_fields):
        # メールアドレスでの登録
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        # is_staff(管理サイトにログインできるか)と、is_superuer(全ての権限)をFalseに
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        # スーパーユーザーは、is_staffとis_superuserをTrueに
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)


# ユーザーモデル
class User(AbstractUser):
    username = models.CharField(_('username'), max_length=150, blank=True)
    email = models.EmailField(_('email address'), unique=True)
    """
    追加
        is_teacher - 教授か否か
    """
    is_teacher = models.BooleanField('教授か', default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []


"""
学習したこと

error : is_superuser is clash
    AbstructUserとPermissionMixinは衝突する．
    AbstructUserにPermissionMixinがサブクラスとして含まれているから．
    AbstructBaseUserにはPermissionMixinは含まれていないため，こっちを使う場合は必要である．

"""
