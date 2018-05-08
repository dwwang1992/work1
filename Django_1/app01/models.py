from django.db import models

# Create your models here.


class Asset(models.Model):
    host_name = models.CharField(max_length=64, db_column='hostname')
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)


# class UserType(models.Model):
#     typename = models.CharField(max_length=32)
#
#
# class UserInfo(models.Model):
#     username = models.CharField(max_length=16)
#     email = models.CharField(max_length=32)
#
#     type = models.ForeignKey(UserType, on_delete='CASCADE')
#
#
# class Group(models.Model):
#     groupname = models.CharField(max_length=16)
#
#
# class User(models.Model):
#     username = models.CharField(max_length=16)
#     email = models.CharField(max_length=32)
#
#     group_relation = models.OneToOneField(Group, on_delete='CASCADE')


class UserType(models.Model):
    typename = models.CharField(max_length=32)


class UserGroup(models.Model):
    groupname = models.CharField(max_length=16)


class UserInfo(models.Model):
    username = models.CharField(max_length=16)
    password = models.CharField(max_length=16)
    email = models.CharField(max_length=32)

    type = models.ForeignKey(UserType, on_delete='CASCADE')
    group_relation = models.ManyToManyField(UserGroup)














