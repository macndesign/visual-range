# coding=utf-8
from PIL import Image, ImageChops, ImageOps
from django.db import models
from django.core.files.storage import default_storage

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


class PhotoImage(models.Model):
    name = models.CharField(max_length=75)
    photo = models.ImageField(upload_to='images')

    def save(self, *args, **kwargs):
        super(PhotoImage, self).save(*args, **kwargs)

        file = self.photo.path
        size = (300, 100)

        try:
            im = Image.open(file)
            im_width = im.size[0]
            im_height = im.size[1]

            little = im_width if im_width < im_height else im_height
            im.thumbnail((little, little), Image.ANTIALIAS)

            im.thumbnail(size, Image.ANTIALIAS)
            im.save(file, "JPEG")
        except IOError:
            return "Cannot create thumbnail for", file

        """
        size = (self.photo_width, self.photo_height)
        image = Image.open(self.photo.path)
        image.thumbnail(size, Image.ANTIALIAS)
        image_size = image.size

        if self.pad:
            thumb = image.crop((0, 0, size[0], size[1]))
            offset_x = max((size[0] - image_size[0]) / 2, 0)
            offset_y = max((size[1] - image_size[1]) / 2, 0)

            thumb = ImageChops.offset(thumb, offset_x, offset_y)
            thumb.save(self.photo.path)

        else:
            thumb = ImageOps.fit(image, size, Image.ANTIALIAS, (0.5, 0.5))
            thumb.save(self.photo.path)
        """


    def delete(self, using=None):
        default_storage.delete(self.photo.path)
        super(PhotoImage, self).delete(using)

    def __unicode__(self):
        return self.name
