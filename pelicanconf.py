#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Gustavo Furtado de Oliveira Alves'
SITENAME = u'Minicurso de Lógica de Programação'
SITEURL = 'http://localhost:9000'

PATH = 'content'

TIMEZONE = 'America/Sao_Paulo'

DEFAULT_LANG = u'pt_BR'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# Plugins
PLUGIN_PATHS = ['./pelican-plugins']
PLUGINS = ['sitemap']

# Sitemap
SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.5,
        'indexes': 0.5,
        'pages': 0.5
    },
    'changefreqs': {
        'articles': 'monthly',
        'indexes': 'monthly'
    }
}

ARTICLE_URL = '{slug}/'
ARTICLE_SAVE_AS = '{slug}/index.html'
PAGE_URL = '{slug}/'
PAGE_SAVE_AS = '{slug}/index.html'

# Theme
THEME = 'theme'
COURSE_DESCRIPTION = """Minicurso 100% GRÁTIS de Lógica de Programação.
São 10 lições super explicadas com a melhor didática para ensinar programação do ZERO para qualquer pessoa!
Agora aprender programação está acessível a qualquer um!"""
COURSE_AUTHOR = "Gustavo"
LP_LINK = "https://mclp.dicasdeprogramacao.com.br/"
OG_IMAGE = "/images/gustavo-furtado.jpg"
LP_IMAGE = "/images/Logo.png"
LP_TITLE = "Quer aprender lógica de programação GRÁTIS?"
LP_DESCRIPTION = "Coloque seu e-mail abaixo e receba GRATUITAMENTE o minicurso de lógica de programação."
LP_ACTION = "https://mautic.dicasdeprogramacao.com.br/form/submit?formId=2"
LP_EMAIL_FIELD = "mauticform[email]"
LP_HIDDEN_FIELDS = '<input type="hidden" name="mauticform[formId]" id="mauticform_mclpsignin_id" value="2"/><input type="hidden" name="mauticform[return]" id="mauticform_mclpsignin_return" value=""/><input type="hidden" name="mauticform[formName]" id="mauticform_mclpsignin_name" value="mclpsignin"/>'
TITLEBAR_TEXT = "Receba este minicurso de lógica de programação GRÁTIS!"
TOTAL_LESSONS = 10
SHARE_ON_TWITTER = "http://twitter.com/share?url=http://mclp.dicasdeprogramacao.com.br/&text=Estou fazendo o minicurso de lógica de programação TOTALMENTE GRÁTIS do @dicasprog."
SHARE_ON_FACEBOOK = "http://www.facebook.com/sharer.php?u=http://mclp.dicasdeprogramacao.com.br/"
SHARE_ON_GPLUS = "https://plus.google.com/share?url=http://mclp.dicasdeprogramacao.com.br/"
SHARE_ON_LINKEDIN = "https://www.linkedin.com/cws/share?url=http://mclp.dicasdeprogramacao.com.br/"
FOOTER_PSS = """
<p>Aqui você encontrará conteúdo simples, práticos e que vai te ensinar os conceitos básicos por trás da programação,
ao final você será capaz de criar pequenos programas e estará pronto para aprender qualquer linguagem de programação sem dificuldades.</p>
"""
