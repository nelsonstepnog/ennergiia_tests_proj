#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" Класс паттерна PageObject с элементами для проверки страницы женской обуви """


class WomenShoesPage(object):
    """ URL страницы женской обуви """
    url_women_shoes = "https://www.ennergiia.com/catalog/zhenschiny/obuv"

    """ Заголовок на странице женской обуви """
    women_shoes_title = "//*[@id='productListHeaderLimiter'][text()='Женская обувь']"

    """ Кнопка сортировки на странице женской обуви """
    women_shoes_sort = "//*[@class='filter-trigger-name'][text()='Сортировать']"

    """ Пункт для выбора "По скидке" у сортировки на странице женской обуви """
    women_shoes_discount = "//*[@class='filter-set__option-button'][text()='По скидке']"

    """ Пункт "По скидке", если активен при сортировке на странице женской обуви """
    women_shoes_discount_active = \
        "//*[@class='filter-set__option-button filter-set__option-selected'][@title='По скидке']"

    """ Название имени брэнда на странице женской обуви для фильра """
    name_of_brand = "Baldinini"

    """ Кнопка фильтра по имени брэнда на странице женской обуви """
    women_shoes_brand_name = "//*[@class='filter-trigger-name'][text()='Бренд']"

    """ Пункт для выбора "Baldinini" у фильтра бренда на странице женской обуви """
    women_shoes_brand_name_baldinini = "//*[@class='filter-set__option-button'][text()='Baldinini']"

    """ Пункт "Baldinini", если этот бренд активен в фильтре на странице женской обуви """
    women_shoes_brand_name_baldinini_active = \
        "//*[@class='filter-set__option-button filter-set__option-selected'][@title='Baldinini']"

    """ Кнопка фильтра по имени брэнда на странице женской обуви """
    women_shoes_brand_name_apply_btn = "//*[@class='filter-set__apply-button'][text()='Применить']"

    """ Кнопка фильтра по имени брэнда на странице женской обуви """
    women_shoes_more_btn = "//*[@class='btn product-list__show-btn'][text()='Показать ещё']"
