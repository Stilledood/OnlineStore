from rest_framework import permissions


class CustomPermission(permissions.BasePermission):
    '''Class to create a custom permision to check if the user requesting to update/delete a post is the actual author of the post'''

    def has_object_permission(self, request, view, obj):
         if request.method is permissions.SAFE_METHODS:
             return True
         else:
            return request.user == obj.author


