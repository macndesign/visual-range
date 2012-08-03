# myapp/api/resources.py
from django.contrib.auth.models import User
from tastypie.authentication import ApiKeyAuthentication
from tastypie.authorization import Authorization
from tastypie import fields
from tastypie.resources import ModelResource, ALL, ALL_WITH_RELATIONS
from blog_rest.models import Entry


class UserResource(ModelResource):
    # Filter user data
    # def apply_authorization_limits(self, request, object_list):
    #    return object_list.filter(user=request.user)

    class Meta:
        queryset = User.objects.all()
        resource_name = 'user'
        # authorization = Authorization()
        # authentication = ApiKeyAuthentication()
        excludes = ['email', 'password', 'is_active', 'is_staff', 'is_superuser']
        filtering = {
            'username': ALL,
        }


class EntryResource(ModelResource):
    user = fields.ForeignKey(UserResource, 'user')

    class Meta:
        queryset = Entry.objects.all()
        resource_name = 'entry'
        # authorization = Authorization()
        # authentication = ApiKeyAuthentication()
        list_allowed_methods = ['get', 'post']
        detail_allowed_methods = ['get', 'post', 'put', 'delete']
        filtering = {
            'slug': ALL,
            'user': ALL_WITH_RELATIONS,
            'pub_date': ['exact', 'lt', 'lte', 'gte', 'gt', 'year', 'month', 'day'],
        }

# http://localhost:8000/api/v1/login/?username={{ request.user.username }}&api_key={{ apikey }}
