from django.contrib import admin
from core.models import Uf, Cidade, Bairro, PhotoImage

class UfAdmin(admin.ModelAdmin):
    class Media:
        js = ('ajax-submit.js',)

admin.site.register(Uf, UfAdmin)
admin.site.register(Cidade)
admin.site.register(Bairro)
admin.site.register(PhotoImage)
