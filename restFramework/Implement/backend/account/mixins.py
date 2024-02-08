from rest_framework import permissions
from .permissions import CalorieChartPermissions, NonVerifiedUserPermissions

class CalorieChartPermissionsMixin(CalorieChartPermissions):
    permission_classes = [
        permissions.IsAuthenticated,
        NonVerifiedUserPermissions,
        CalorieChartPermissions,
    ]

class NonVerifiedUserPermissionsMixin(NonVerifiedUserPermissions) :
     permission_classes = [
        NonVerifiedUserPermissions,
    ]