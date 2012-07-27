# coding=utf-8
from django.db import models

class Uf(models.Model):
    abreviatura = models.CharField(max_length=2)
    descricao = models.CharField(max_length=255, verbose_name='Descrição')

    class Meta:
        verbose_name = 'Uf'
        ordering = ['descricao']

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
        return self.descricao

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
        return self.descricao

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

    def __unicode__(self):
        return self.descricao

    def as_dict(self):
        return {
            'pk': self.pk,
            'nome': self.descricao,
            'cidade_pk': self.cidade.pk,
            }
