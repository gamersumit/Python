from rest_framework import permissions

class CalorieChartPermissions(permissions.DjangoModelPermissions):
    permission_queryset = None

    perms_map = {
       # 'GET': [],   // original
        'OPTIONS': [],
        'HEAD': [],
        'GET': ['%(app_label)s.view_%(model_name)s'],
        'POST': ['%(app_label)s.add_%(model_name)s'],
        'PUT': ['%(app_label)s.change_%(model_name)s'],
        'PATCH': ['%(app_label)s.change_%(model_name)s'],
        'DELETE': ['%(app_label)s.delete_%(model_name)s'],
    }

    def has_permission(self, request, view):
        # Check if the user can perform the action based on DjangoModelPermissions
        has_model_permissions = super().has_permission(request, view)
        print(request.method)

        if request.method == 'DELETE' : 
            return request.user.is_master_user
        
        if request.method != 'GET' and (request.user.is_master_user or request.user.is_mode_user):
            return True

        if request.method == 'GET' :
            return True   

        return has_model_permissions    