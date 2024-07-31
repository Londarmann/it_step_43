
from django.urls import path, include

from .views import RegistrationView
from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView

urlpatterns = [

    path('register/', RegistrationView.as_view(), name='register'),
    path('login/', include('rest_framework.urls')),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh')

]
