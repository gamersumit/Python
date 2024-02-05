from rest_framework import permissions
from .permissions import CalorieChartPermissions

class CalorieChartPermissionsMixin(CalorieChartPermissions):
    permission_classes = [
        permissions.IsAuthenticated,
        CalorieChartPermissions,
    ]