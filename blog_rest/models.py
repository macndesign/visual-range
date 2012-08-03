from tastypie.utils import now
from tastypie.models import create_api_key
from django.contrib.auth.models import User
from django.db import models
from django.template.defaultfilters import slugify
from django.contrib import admin


class Entry(models.Model):
    user = models.ForeignKey(User)
    pub_date = models.DateTimeField(default=now)
    title = models.CharField(max_length=200)
    slug = models.SlugField()
    body = models.TextField()

    def __unicode__(self):
        return self.title

    def save(self, *args, **kwargs):
        # For automatic slug generation.
        if not self.slug:
            self.slug = slugify(self.title)[:50]

        return super(Entry, self).save(*args, **kwargs)


class EntryAdmin(admin.ModelAdmin):
    list_display = ('user', 'pub_date')


admin.site.register(Entry, EntryAdmin)
models.signals.post_save.connect(create_api_key, sender=User)
