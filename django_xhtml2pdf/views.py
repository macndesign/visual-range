#! /usr/bin/python
# -*- encoding: utf-8 -*-

from django import http
from django.conf import settings
from django.contrib.sites.models import Site
from django.shortcuts import render
from django.template.loader import get_template
from django.template import Context
import xhtml2pdf.pisa as pisa
import cStringIO as StringIO
import cgi

def index(request):
    return render(request, 'django_xhtml2pdf/index.html')


def download(request):
    if request.POST:
        result = StringIO.StringIO()
        pdf = pisa.CreatePDF(
            StringIO.StringIO(request.POST["data"]),
            result
        )

        if not pdf.err:
            return http.HttpResponse(
                result.getvalue(),
                mimetype='application/pdf')

    return http.HttpResponse('We had some errors')


def render_to_pdf(template_src, context_dict):
    template = get_template(template_src)
    context = Context(context_dict)
    html  = template.render(context)
    result = StringIO.StringIO()
    pdf = pisa.pisaDocument(StringIO.StringIO(html.encode("ISO-8859-1")), result)

    if not pdf.err:
        return http.HttpResponse(result.getvalue(), mimetype='application/pdf')

    return http.HttpResponse('We had some errors<pre>%s</pre>' % cgi.escape(html))


def ezpdf_sample(request):
    blog_entries = []
    current_site = Site.objects.get_current()
    static_url = settings.STATIC_URL

    for i in range(1,10):
        blog_entries.append({
            'id': i,
            'title': 'Playing with pisa 3.0.16 and django Template Engine',
            'body': 'This is a simple example..'
        })

    return render_to_pdf('django_xhtml2pdf/entries.html',{
        'pagesize': 'A4',
        'title': 'My amazing blog',
        'blog_entries':blog_entries,
        'current_site': current_site.domain,
        'static_url': static_url,
    })
