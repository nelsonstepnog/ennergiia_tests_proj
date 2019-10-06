#!/usr/bin/env python
# -*- coding: utf-8 -*-

from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from tests.features.directories_page.wishlist_page.wishlist_page import WishListPage
from tests.features.directories_page.women_skirts_page.women_skirts_page import WomenSkirtsPage
from tests.features.helper.helper import *
from tests.features.directories_page.main_page.main_page import *
from tests.features.directories_page.women_shoes_page.women_shoes_page import *


def step_woman_shoes_see_on_page():
    driver.get(WomenShoesPage.url_women_shoes)
    close_reg_form()


@given(u'страница с листингом товаров')
def step_impl(context):
    step_woman_shoes_see_on_page()


def step_woman_shoes_sort():
    Helper.wait_for_element(By.XPATH, "//*[@class='filter-trigger-name'][text()='Сортировать']")
    driver.find_element_by_xpath(WomenShoesPage.women_shoes_sort)


@given(u'тип сортировки По скидке')
def step_impl(context):
    step_woman_shoes_sort()


def step_woman_shoes_open_page():
    driver.get(WomenShoesPage.url_women_shoes)
    current_url = driver.current_url
    assert current_url == WomenShoesPage.url_women_shoes, 'url страницы не соответствует ожидаемому'
    driver.find_element_by_xpath(WomenShoesPage.women_shoes_title)
    Helper.wait_for_element(By.XPATH, "//*[@class='filter-trigger-name'][text()='Сортировать']")


@when(u'открыть заданную страницу')
def step_impl(context):
    step_woman_shoes_open_page()


def step_woman_shoes_sort_items_by_discount():
    driver.find_element_by_xpath(WomenShoesPage.women_shoes_sort).click()
    Helper.wait_for_element(By.XPATH, WomenShoesPage.women_shoes_discount)
    driver.find_element_by_xpath(WomenShoesPage.women_shoes_discount).click()


@when(u'выбрать упорядочить по По скидке')
def step_impl(context):
    step_woman_shoes_sort_items_by_discount()


def step_woman_shoes_sort_correct_by_discount():
    Helper.wait_for_element(By.XPATH, "//*[@class='filter-trigger-name'][text()='Сортировать']")
    driver.find_element_by_xpath(WomenShoesPage.women_shoes_sort).click()
    driver.find_element_by_xpath(WomenShoesPage.women_shoes_discount_active)


@then(u'результат поисковой выдачи соответствует заданной сортировке По скидке')
def step_impl(context):
    step_woman_shoes_sort_correct_by_discount()


def step_woman_shoes_brand_name():
    Helper.wait_for_element(By.XPATH, WomenShoesPage.women_shoes_brand_name)
    driver.find_element_by_xpath(WomenShoesPage.women_shoes_brand_name).click()
    driver.find_element_by_xpath("//*[text()='" + WomenShoesPage.name_of_brand + "']")


@given(u'имя бренда Baldinini')
def step_impl(context):
    step_woman_shoes_brand_name()


def step_woman_shoes_brand_name_choice():
    Helper.wait_for_element(By.XPATH, WomenShoesPage.women_shoes_brand_name)
    driver.find_element_by_xpath(WomenShoesPage.women_shoes_brand_name).click()
    driver.execute_script("window.scrollTo(0, 400)")
    driver.find_element_by_xpath(WomenShoesPage.women_shoes_brand_name_baldinini).click()
    driver.find_element_by_xpath(WomenShoesPage.women_shoes_title)
    driver.execute_script("window.scrollTo(0, 400)")
    driver.find_element_by_xpath(WomenShoesPage.women_shoes_brand_name_apply_btn).click()
    driver.implicitly_wait(1)


@when(u'выбрать фильтр по имени бренда')
def step_impl(context):
    step_woman_shoes_brand_name_choice()


def step_woman_shoes_brand_name_correct():
    brand_name = "baldinini"
    driver.find_element_by_xpath(WomenShoesPage.women_shoes_title)
    driver.find_element_by_xpath("//*[text()='" + WomenShoesPage.name_of_brand + "']")
    count_items_expected = 40
    elem_count_first_check = driver.find_elements_by_xpath(
        "//*[@class='product-preview__brand'][text()='" + WomenShoesPage.name_of_brand + "']")
    count_items_real_first = len(elem_count_first_check)
    driver.execute_script("window.scrollTo(0, 6000)")
    elem_count_second_check = driver.find_elements_by_xpath(
        "//*[@class='product-preview__brand'][text()='" + WomenShoesPage.name_of_brand + "']")
    count_items_real_second = len(elem_count_second_check)
    count_real = count_items_real_first + count_items_real_second
    print("    - Берем на проверку на странице - " + str(count_real) + " товаров, ожидаем из них " +
          str(count_items_expected) + " бренда " + brand_name)
    if count_real == count_items_expected:
        print("    Passed: все товары " + str(count_real) + " результатов являются брендом " + brand_name)
    else:
        print("    Fail: Фактическое количество товаров бренда " + brand_name + " на странице - " + str(count_real) +
              ", не соответствует ожидаемому количеству товаров -  " + str(count_items_expected))


@then(u'результат выдачи должен содержать только товары бренда Baldinini')
def step_impl(context):
    step_woman_shoes_brand_name_correct()


def step_item_search_word():
    search_items = "Блузка"
    return search_items


@given(u'фраза для поиска товара')
def step_impl(context):
    step_item_search_word()


def step_item_search_open_main_page():
    driver.get(url_main_page)


@when(u'открыть главную страницу')
def step_impl(context):
    step_item_search_open_main_page()


def step_item_search_click():
    driver.find_element_by_xpath(MainPage.search_icon_main_page).click()


@when(u'нажать кнопку поиск')
def step_impl(context):
    step_item_search_click()


def step_item_search_fill_field():
    driver.find_element_by_xpath(MainPage.search_field_main_page).send_keys("'" + step_item_search_word() + "'")
    driver.find_element_by_xpath(MainPage.search_field_main_page).send_keys(Keys.ENTER)


@when(u'ввести заданную фразу в поле поиска')
def step_impl(context):
    step_item_search_fill_field()


def step_item_search_check_count():
    Helper.wait_for_element(By.XPATH, "//*[text()='" + step_item_search_word() + "']")
    driver.find_element_by_xpath("//*[text()='" + step_item_search_word() + "']")
    lst_count_search = driver.find_elements_by_xpath("//*[text()='" + step_item_search_word() + "']")
    count_items_expected = 2
    count_items_real = len(lst_count_search)
    # assert len(lst_Count) == count_items_expected
    print("    - Фактическое кол-во товаров на странице по запросу:  '" + str(step_item_search_word()) + "' - " +
          str(count_items_real) + ", ожидаем не менее " + str(count_items_expected))
    if len(lst_count_search) >= count_items_expected:
        print("    Passed: найденные товары - " + str(count_items_real) + " результатов являются блузками")
    else:
        print("    Fail: Фактическое количество товаров на странице по запросу:  '" + str(step_item_search_word()) +
              ", ожидаем не менее " + str(count_items_expected))


@then(u'результат поисковой выдачи содержит как минимум 2 любых товара(ов) из строки блузка')
def step_impl(context):
    step_item_search_check_count()


def step_wishlist_join():
    Helper.wait_for_element(By.XPATH, MainPage.wishlist_icon_main_page)
    driver.find_element_by_xpath(MainPage.wishlist_icon_main_page).click()
    Helper.wait_for_element(By.XPATH, WishListPage.wishlist_page_text_check)
    driver.find_element_by_xpath(WishListPage.wishlist_page_text_check)


@when(u'перейти в wishlist когда он пуст')
def step_impl(context):
    step_wishlist_join()


def step_wishlist_go_to_women_skirts():
    driver.get(WomenSkirtsPage.url_women_skirts)
    Helper.wait_for_element(By.XPATH, WomenSkirtsPage.women_skirts_title)
    driver.find_element_by_xpath(WomenSkirtsPage.women_skirts_title)


@when(u'открыть заданную страницу юбок')
def step_impl(context):
    step_wishlist_go_to_women_skirts()


def step_wishlist_add_item_in_wishlist():
    global different_item_name
    driver.execute_script("window.scrollTo(0, 600)")
    for element in driver.find_elements_by_xpath(
            WomenSkirtsPage.women_skirts_sec_item + "//*[@class='product-preview__brand']"):
        different_item_name = element.text
    print("    Название бренда вещи в выбранном блоке " + str(different_item_name))
    driver.find_elements_by_xpath(WomenSkirtsPage.women_skirts_sec_item + "//*[text()='" + different_item_name + "']")
    driver.find_element_by_xpath(WomenSkirtsPage.women_skirts_sec_item + "//*[@data-test='add_to_wishlist']").click()


@when(u'случайно выбрать карточку товара и добавить в wishlist')
def step_impl(context):
    step_wishlist_add_item_in_wishlist()


def step_wishlist_go_to_wishlist():
    driver.execute_script("window.scrollTo(0, 0)")
    Helper.wait_for_element(By.XPATH, MainPage.wishlist_icon_main_page)
    driver.find_element_by_xpath(MainPage.wishlist_icon_main_page).click()


@when(u'перейти в wishlist когда добавлен товар')
def step_impl(context):
    step_wishlist_go_to_wishlist()


def step_wishlist_see_item():
    driver.find_element_by_xpath("//*[@class='product-preview__brand'][text()='" + different_item_name + "']")


@then(u'в wishlist отображается товар')
def step_impl(context):
    step_wishlist_see_item()
