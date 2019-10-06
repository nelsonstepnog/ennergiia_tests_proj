#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" Класс паттерна PageObject с элементами для проверки страницы списка желаний """


class WishListPage(object):
    """ Текст в wishlist, когда товаров нет на странице """
    wishlist_page_text_check = "//*[text()='Список желаемого пуст']"
