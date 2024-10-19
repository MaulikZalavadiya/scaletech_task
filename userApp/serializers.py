from rest_framework import serializers
from .models import User, Role


class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = ['id', 'roleName', 'accessModules', 'createdAt', 'active']


class UserSerializer(serializers.ModelSerializer):
    roleName = serializers.CharField(source='role.roleName', read_only=True)
    accessModules = serializers.ListField(source='role.accessModules', read_only=True)

    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'email', 'roleName', 'accessModules']
