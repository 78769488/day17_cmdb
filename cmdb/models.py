from django.db import models


# Create your models here.
class User(models.Model):
    username = models.CharField(verbose_name="用户名", max_length=32)
    password = models.CharField(verbose_name="密码", max_length=32)
    email = models.EmailField(verbose_name="邮箱")
    business = models.ForeignKey(verbose_name="业务线ID", to="Business", to_field="id")

    def __str__(self):
        return "%s - %s - %s" % (self.username, self.password, self.email)

    class Meta:
        verbose_name = "用户信息"
        verbose_name_plural = "用户信息"


class Business(models.Model):
    """业务线"""
    caption = models.CharField(verbose_name="名称", max_length=32)
    code = models.CharField(verbose_name="标识", max_length=32)

    def __str__(self):
        return "%s - %s " % (self.caption, self.code)

    class Meta:
        verbose_name = "业务线"
        verbose_name_plural = "业务线"


class Host(models.Model):
    """主机信息"""
    hostname = models.CharField(verbose_name="主机名称", max_length=32, db_index=True)
    ip = models.GenericIPAddressField(verbose_name="IP", db_index=True)
    port = models.IntegerField(verbose_name="Port")
    business = models.ForeignKey(verbose_name="业务线ID", to="Business", to_field="id")

    def __str__(self):
        return "%s - %s - %s " % (self.hostname, self.ip, self.port)

    class Meta:
        verbose_name = "主机信息"
        verbose_name_plural = "主机信息"


class Application(models.Model):
    """应用"""
    name = models.CharField(verbose_name="名称", max_length=32)
    code = models.CharField(verbose_name="标识", max_length=32)
    app2host = models.ManyToManyField(to="Host")

    def __str__(self):
        return "%s - %s " % (self.name, self.code)

    class Meta:
        verbose_name = "应用"
        verbose_name_plural = "应用"

