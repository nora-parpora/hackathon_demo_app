from django.urls import path
from .views import ProfileView, EmployerView, HouseOwnerView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


urlpatterns = [
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('profiles/', ProfileView.as_view(), name="profile_view"),
    path('employers/', EmployerView.as_view(), name="empl_view"),
    path('owners/', HouseOwnerView.as_view(), name="house_owners_view"),

]

