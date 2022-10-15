from django.urls import path
from .views import ProfileView, EmployerView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


urlpatterns = [
    path('api/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/profiles/', ProfileView.as_view(), name="profile_view"),
    path('api/employers/', EmployerView.as_view(), name="empl_view"),

    #path('api/profiles/', ProfileView.as_view(), name="sign_up"),
]

