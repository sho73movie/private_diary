from django.contrib.auth.models import AbstractUser

# settings_common.pyのAUTH_USER_MODELに設定必要
class CustomUser(AbstractUser):
    # 拡張ユーザーモデル
    class Meta:
        verbose_name_plural = 'CustomUser'