#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" Класс паттерна PageObject с элементами для проверки страницы женских юбок """


class WomenSkirtsPage(object):
    """ URL страницы женских юбок """
    url_women_skirts = "https://www.ennergiia.com/catalog/zhenschiny/odezhda/jubki"

    """ Заголовок на странице женских юбок """
    women_skirts_title = "//*[@id='productListHeaderLimiter'][text()='Женские юбки']"

    """ Название имени брэнда на странице женских юбок берем из этого блока, последний div можно поменять  """
    women_skirts_sec_item = "//div[3]/div[2]/div/div/div[2]"
