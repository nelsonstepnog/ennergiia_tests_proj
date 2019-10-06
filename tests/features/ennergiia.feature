# -- FILE: tests/features/ennergiia.feature

Feature: веб-сайт ennergiia.com

  @test_tag_sort
  Scenario Outline: Сортировать товар по скидке
    Given страница с листингом товаров
    And тип сортировки По скидке
    When открыть заданную страницу
    And выбрать упорядочить по По скидке
    Then результат поисковой выдачи соответствует заданной сортировке По скидке

    Examples: Vertical
      | url  | https://www.ennergiia.com/catalog/zhenschiny/obuv |
      | sort | По скидке                                         |

  @test_tag_filter
  Scenario Outline: Фильтровать товар по одному бренду
    Given страница с листингом товаров
    And имя бренда Baldinini
    When открыть заданную страницу
    And выбрать фильтр по имени бренда
    Then результат выдачи должен содержать только товары бренда Baldinini

    Examples: Vertical
      | url        | https://www.ennergiia.com/catalog/zhenschiny/obuv |
      | brand_name | Baldinini                                         |

  @test_tag_search
  Scenario Outline: Искать товар по фразе
    Given фраза для поиска товара
    When открыть главную страницу
    And нажать кнопку поиск
    And ввести заданную фразу в поле поиска
    Then результат поисковой выдачи содержит как минимум 2 любых товара(ов) из строки блузка

    Examples: Vertical
      | string | count | result         |
      | блузка | > 2   | блузка;рубашка |

  @test_tag_add
  Scenario Outline: Добавить товары в wishlist
    Given страница с листингом товаров
    When перейти в wishlist когда он пуст
    And открыть заданную страницу юбок
    And случайно выбрать карточку товара и добавить в wishlist
    And перейти в wishlist когда добавлен товар
    Then в wishlist отображается товар

    Examples: Vertical
      | url | https://www.ennergiia.com/catalog/zhenschiny/odezhda/jubki |
      | url | https://www.ennergiia.com/wishlist                         |
