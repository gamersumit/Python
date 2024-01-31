from rest_framework import permissions
from .permissions import IsStaffEditorPermission


class UserQuerySetMixin():
    user_field = 'user'
    print("################################################################")
    print('method userquery')
    def get_queryset(self, *args, **kwargs):
        lookup_data = {}
        lookup_data[self.user_field] = self.request.user
        qs = super().get_queryset(*args, **kwargs)
        user = self.request.user
        
        if user.is_superuser:
         IsStaffEditorPermission.permission_queryset = qs
         return qs
        
        
        IsStaffEditorPermission.permission_queryset = qs = qs.filter(**lookup_data)
        return qs




class StaffEditorPermissionMixin(IsStaffEditorPermission):
    print("################################################################")
    print('method staffuser')
    permission_classes = [
        permissions.IsAdminUser,
        IsStaffEditorPermission,
        ]
