from rest_framework import generics
from .serializers import *
from rest_framework.parsers import MultiPartParser 
from django.contrib.auth.models import Group
from rest_framework.response import Response
from knox.models import AuthToken
from rest_framework.permissions import IsAuthenticated
from .models import *
from knox.auth import AuthToken

class UserRegister(generics.GenericAPIView):
    serializer_class = RegisterSerializer
    parser_classes = [MultiPartParser]

    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            try:
                user = serializer.save()
                Claim_Assure_Admin = Group.objects.get(
                    name='Claim_Assure_Admin')
             
                Support_Staff = Group.objects.get(name="Support_Staff")
                Document_Manager = Group.objects.get(name='Document_Manager')
          
                if user.is_claimAssure_admin:
                    user.groups.add(Claim_Assure_Admin)

                elif user.is_support_staff == True:
                    user.groups.add(Support_Staff)

                elif user.is_document_manager == True:
                    user.groups.add(Document_Manager)

                return Response({'status': 'success',
                                'Message': 'Registration Successfull'}, status=200)
            except:
                return Response({'Message': 'Please select any one group',
                                 'status' : 'error'}, status=400)
        else:
          
            key, value = list(serializer.errors.items())[0]
            error_message = key+" , "+value[0]
            return Response({'Message': error_message, 
                            'status' : 'error'}, status=400)


class LoginView(generics.GenericAPIView):
    serializer_class = LoginSerializer
    parser_classes = [MultiPartParser]

    def post(self, request):
        try:
            serializer = LoginSerializer(data=request.data)
            if serializer.is_valid():
                user_data = serializer.validated_data
                print(user_data)
                user = RegisterSerializer(user_data).data
                if serializer is not None:
                    # Check if a token already exists for this user
                    try:
                        token = AuthToken.objects.filter(user=serializer.validated_data)
                        # If a token already exists, invalidate it
                        token.delete()
                    except AuthToken.DoesNotExist:
                        pass
                    
                    # Create a new token for the current user and device
                    _, token = AuthToken.objects.create(serializer.validated_data)
                    return Response({
                        'Message': 'Login successfull',
                        'Token': token,
                        'status': 'success',
                        'user': user_data.email,
                        'username': user_data.username,
                        'Group': user_data.groups.values_list("name", flat=True)[0]
                    }, status=200)
            else:
                print(serializer.errors)
                key, value = list(serializer.errors.items())[0]
                error_message = key+" , "+value[0]
                return Response({'Message': error_message, 
                                'status' : 'error'}, status=400)

        except:
            return Response({
                'Message': 'Email or Password is Invalid',
                'status': 'failed'
            }, status=400)


class ChangePasswordView(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ChangePasswordSerializer
    parser_classes = [MultiPartParser]

    def post(self, request, format=None):
        serializer = ChangePasswordSerializer(
            data=request.data, context={'user': request.user})
        serializer.is_valid(raise_exception=True)
        return Response({'Message': 'password change successfully',
                         'status': 'success'})

