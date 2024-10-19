from django.shortcuts import render

# Create your views here.
from rest_framework.viewsets import ModelViewSet
from .models import *
from .serializers import *
from rest_framework.permissions import IsAuthenticated,AllowAny
from utils.APIResponse import APIResponse
from rest_framework.decorators import api_view,permission_classes
from rest_framework import status
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate,login,logout
from rest_framework.decorators import action
from django.db import transaction




class RoleViewSet(ModelViewSet):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer
    permission_classes = [IsAuthenticated]


class UserViewSet(ModelViewSet):
    queryset = User.objects.filter(is_superuser=False)
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        search_term = self.request.query_params.get('search', '')
        return self.queryset.filter(first_name__icontains=search_term) | self.queryset.filter(last_name__icontains=search_term)
 

    @action(detail=False, methods=['put'], permission_classes=[IsAuthenticated])
    def bulk_update(self, request):
        """
        Dynamically update multiple users. If 'user_ids' is provided, update only those users.
        If 'user_ids' is not provided, update all users in the table.
        Only fields present in the request will be updated.
        """
        user_ids = request.data.get('user_ids', None)
        update_data = {key: value for key, value in request.data.items() if key != 'user_ids'}

        # Ensure that there is something to update
        if not update_data:
            return APIResponse(
            {},
            status=status.HTTP_400_BAD_REQUEST,
            notification=('msg', 'Email and password are required')
        )

        # If user_ids is provided, update only the specified users
        if user_ids:
            users = User.objects.filter(id__in=user_ids)
        else:
            # If no user_ids are provided, update all users
            users = User.objects.all()

        # Perform bulk update on the selected users
        users.update(**update_data)

        return APIResponse(
            data={},
            status=status.HTTP_200_OK,
            notification=('msg', 'Update data Successfully!')
        )

    @action(detail=False, methods=['put'], permission_classes=[IsAuthenticated])
    def user_update(self, request):
        """
        Dynamically update multiple users. If 'user_ids' is provided, update only those users.
        If 'user_ids' is not provided, update all users in the table.
        Only fields present in the request will be updated.
        """
        update_data = request.data.get('update_data', None)
        if update_data:
            users_to_update = []
            
            for data in update_data:
                user_id = data.pop('id', None)
                if user_id:
                    user = User.objects.get(id=user_id)
                    for key, value in data.items():
                        setattr(user, key, value)
                    users_to_update.append(user)
            
            with transaction.atomic():
                User.objects.bulk_update(users_to_update, fields=[*data.keys()])

        return APIResponse(
            data={},
            status=status.HTTP_200_OK,
            notification=('msg', 'Update data Successfully!')
        )
    
    @action(detail=False, methods=['GET'], permission_classes=[IsAuthenticated])
    def check_access(self, request):
        access_module = list(request.user.role.accessModules.keys())
        user_check_module = request.query_params.get('module')
        if user_check_module in access_module:
            return APIResponse(
            data={"user_check_module":user_check_module},
            status=status.HTTP_200_OK,
            notification=('msg', 'User have a permission to access!')
        )
        return APIResponse(
            data={"user_check_module":user_check_module},
            status=status.HTTP_200_OK,
            notification=('msg', "User don't have a permission to access!")
        )


@permission_classes([AllowAny])
@api_view(['POST'])
def signup_API(request):
    first_name = request.data.get('first_name')
    last_name = request.data.get('last_name')
    email = request.data.get('email')
    password = request.data.get('password')
    role = Role.objects.get(id=request.data.get('role_id'))
    user = User.objects.create_user(email=email, first_name=first_name, last_name=last_name, password=password)
    user.role = role
    user.save()
    return APIResponse(
            {
                'email': user.email
            },
            status=status.HTTP_201_CREATED,
            notification=('msg', 'User created successfully!!!!!'))


@permission_classes([AllowAny])
@api_view(['POST'])
def LoginAPI(request):
    email = request.data.get('email')
    password = request.data.get('password')

    if not email or not password:
        return APIResponse(
            {},
            status=status.HTTP_400_BAD_REQUEST,
            notification=('msg', 'Email and password are required')
        )

    try:
        # Authenticate the user
        user = authenticate(request, email=email, password=password)
        if user is None:
            return APIResponse(
                {},
                status=status.HTTP_401_UNAUTHORIZED,
                notification=('msg', 'Invalid email or password')
            )

        login(request, user)
        token, _ = Token.objects.get_or_create(user=user)
        data = {
            "email": user.email,
            "token": token.key,
            "role":user.role.roleName,
            "access_module":user.role.accessModules,
            "is_register": user.is_register
        }

        return APIResponse(
            data=data,
            status=status.HTTP_200_OK,
            notification=('msg', 'Login Successfully!')
        )

    except User.DoesNotExist:
        return APIResponse(
            {},
            status=status.HTTP_404_NOT_FOUND,
            notification=('msg', 'User not found')
        )

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def LogoutAPI(request):
    request.user.auth_token.delete()
    logout(request)
    return APIResponse(
        {},
            status=status.HTTP_200_OK,
            notification=('msg', 'logout successfuly !!!'))