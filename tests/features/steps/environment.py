#!/usr/bin/env python
# -*- coding: utf-8 -*-


import sys
import locale

# hack for windows platform for setting valid locale encoding
# хак, устраняющий проблемы с кодировками на ОС Windows
if sys.platform in ['win32', 'cygwin']:
    def default_enc(*args, **kwargs):
        return "utf8"


    locale.getpreferredencoding = default_enc


def after_all(context):
    try:
        context.browser.close()
        context.browser.quit()
    except Exception:
        pass
