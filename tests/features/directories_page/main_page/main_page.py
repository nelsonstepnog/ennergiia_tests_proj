#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" Класс паттерна PageObject с элементами для проверки главной страницы """


class MainPage(object):
    """ Иконка закрытия попапа регистрации на главной странице """
    reg_popup_close_main_page = "//*[@class='modal-close']"

    """ Иконка поиска по товарам на главной странице """
    search_icon_main_page = "//*[@class='search_menu']"

    """ Поле поиска по товарам на главной странице """
    search_field_main_page = "//*[@class='search_dropdown_input']//input"

    """ Иконка wishlist на главной странице """
    wishlist_icon_main_page = "//*[@data-unit='wishlist_item_list']"
