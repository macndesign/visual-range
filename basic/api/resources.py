from django.contrib.auth.models import User
from tastypie import fields
from tastypie.resources import ModelResource
from tastypie.authorization import Authorization
from basic.models import Note, AnnotatedNote, SlugBasedNote


# json indent
from django.core.serializers import json
from django.utils import simplejson
from tastypie.serializers import Serializer


class PrettyJSONSerializer(Serializer):
    json_indent = 4


    def to_json(self, data, options=None):
        options = options or {}
        data = self.to_simple(data, options)
        return simplejson.dumps(data, cls=json.DjangoJSONEncoder,
            sort_keys=True, ensure_ascii=False, indent=self.json_indent)


class UserResource(ModelResource):
    class Meta:
        resource_name = 'users'
        queryset = User.objects.all()
        authorization = Authorization()


class CachedUserResource(ModelResource):
    class Meta:
        allowed_methods = ('get', )
        queryset = User.objects.all()
        resource_name = 'cached_users'

    def create_response(self, *args, **kwargs):
        resp = super(CachedUserResource, self).create_response(*args, **kwargs)
        resp['Cache-Control'] = "max-age=3600"
        return resp


class NoteResource(ModelResource):
    user = fields.ForeignKey(UserResource, 'user')

    def create_response(self, *args, **kwargs):
        resp = super(NoteResource, self).create_response(*args, **kwargs)
        resp['Access-Control-Allow-Origin'] = '*'
        resp['Access-Control-Allow-Headers'] = 'X-Requested-With'
        return resp

    class Meta:
        resource_name = 'notes'
        include_resource_uri = False
        limit = 10
        default_format = 'application/json'
        allowed_methods = ('get', 'post')
        queryset = Note.objects.all()
        authorization = Authorization()
        serializer = PrettyJSONSerializer()


class BustedResource(ModelResource):
    class Meta:
        queryset = AnnotatedNote.objects.all()
        resource_name = 'busted'

    def get_list(self, *args, **kwargs):
        raise Exception("It's broke.")


class SlugBasedNoteResource(ModelResource):
    class Meta:
        queryset = SlugBasedNote.objects.all()
        resource_name = 'slugbased'
        detail_uri_name = 'slug'
