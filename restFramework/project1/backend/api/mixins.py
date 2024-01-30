from rest_framework import permissions
from .permissions import IsStaffEditorPermission


class StaffEditorPermissionMixin(IsStaffEditorPermission):
    permission_classes = [
        permissions.IsAdminUser,
        IsStaffEditorPermission,
        ]

