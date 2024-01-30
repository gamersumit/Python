from rest_framework import permissions

class IsStaffEditorPermission(permissions.DjangoModelPermissions):

    perms_map = {
       # 'GET': [],   // original
        'GET': ['%(app_label)s.view_%(model_name)s'],
        'OPTIONS': [],
        'HEAD': [],
        'POST': ['%(app_label)s.add_%(model_name)s'],
        'PUT': ['%(app_label)s.change_%(model_name)s'],
        'PATCH': ['%(app_label)s.change_%(model_name)s'],
        'DELETE': ['%(app_label)s.delete_%(model_name)s'],
    }

    # def has_permission(self, request, view):
    #     if not request.user.is_staff:
    #         return False

    #     return super().has_permission(request, view)
 


    # EXAMPLE : JUST FOR UNDERSTANDING CUSTOM PERMISSIONS
    # def has_permission(self, request, view):
    #     user = request.user
    #     print(user.get_all_permissions())
    #     if user.is_staff:
    #         if user.has_perm("product.change_product") : # change/update
    #             print("update failed")
    #             return True
    #         if user.has_perm("product.add_product") : # add/ create  "class.action_model" (all small letters)
    #             print("add checked")
    #             return False
    #         if user.has_perm("product.delete_product") : # delete
    #             return True
    #         if user.has_perm("product.view_product") :  # view/get
    #             return True
    #         return False
    #     return False