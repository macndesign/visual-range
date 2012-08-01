# coding=utf-8
try:
    from PIL import Image, ImageOps
except ImportError:
    import Image
    import ImageOps

from django.db import models

class Uf(models.Model):
    abreviatura = models.CharField(max_length=2)
    descricao = models.CharField(max_length=255, verbose_name='Descrição')

    class Meta:
        verbose_name = 'Uf'
        ordering = ['abreviatura']
        unique_together = ('abreviatura', 'descricao')

    @property
    def cidades(self):
        cidades = self.cidade_set.all()
        clist = []

        for cidade in cidades:
            clist.append(
                    {'pk': cidade.pk, 'nome': cidade.descricao}
            )

        return clist

    def __unicode__(self):
        return self.abreviatura

    def as_dict(self):
        return {
            'pk': self.pk,
            'sigla': self.abreviatura,
            'cidades': list(self.cidades),
            }


class Cidade(models.Model):
    descricao = models.CharField(max_length=255, verbose_name='Descrição')
    uf = models.ForeignKey('Uf')

    class Meta:
        ordering = ['descricao']
        unique_together = ('descricao', 'uf')

    @property
    def bairros(self):
        bairros = self.bairro_set.all()
        blist = []

        for bairro in bairros:
            blist.append(
                    {'pk': bairro.pk, 'nome': bairro.descricao}
            )

        return blist

    def __unicode__(self):
        return u'{0} - {1}'.format(self.descricao, self.uf)

    def as_dict(self):
        return {
            'pk': self.pk,
            'nome': self.descricao,
            'uf_pk': self.uf.pk,
            'bairros': list(self.bairros),
            }


class Bairro(models.Model):
    descricao = models.CharField(max_length=255, verbose_name='Descrição')
    cidade = models.ForeignKey('Cidade')

    class Meta:
        ordering = ['descricao']
        unique_together = ('descricao', 'cidade')

    def __unicode__(self):
        return u'{0} - {1}'.format(self.descricao, self.cidade)

    def as_dict(self):
        return {
            'pk': self.pk,
            'nome': self.descricao,
            'cidade_pk': self.cidade.pk,
            }


def resize_or_crop(file, size, quality=75, crop=False):
    image = Image.open(file)
    if image.mode not in ('L', 'RGB'):
        image = image.convert('RGB')

    if crop:
        image = ImageOps.fit(image, size, Image.ANTIALIAS)
    else:
        image.thumbnail(size, Image.ANTIALIAS)

    image.save(file, 'JPEG', quality=quality)


class PhotoImage(models.Model):
    name = models.CharField(max_length=75)
    photo = models.ImageField(upload_to='images')
    width = models.PositiveIntegerField(default=300)
    height = models.PositiveIntegerField(default=200)
    quality = models.PositiveIntegerField(default=75)
    crop = models.BooleanField()

    def save(self, *args, **kwargs):
        super(PhotoImage, self).save(*args, **kwargs)

        resize_or_crop(
            file = self.photo.path,
            size = (self.width, self.height),
            quality = self.quality,
            crop = self.crop,
        )

    def __unicode__(self):
        return self.name
