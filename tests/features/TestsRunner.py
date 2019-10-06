#!/usr/bin/python
# -*- coding: utf-8 -*-


"""  С этого файла запускаются все тесты, написанные на Python + Behave + BDD """
import sys
from behave import __main__ as runner_with_options

if __name__ == '__main__':
    sys.stdout.flush()
    # Расскоментировать строку ниже если вы под windows:
    # featureFilePath = ' features/ennergiia.feature '

    # Расскоментировать строку ниже если вы под linux:
    # featureFilePath = ' ../features/ennergiia.feature '

    commonRunnerOptions = ' --no-capture --no-capture-stderr -f plain '
    fullRunnerOptions = featureFilePath + commonRunnerOptions
    runner_with_options.main(fullRunnerOptions)

    # Для linux:
    # Команды для запуска конкретных тестов выполняются в корне проекта из консоли
    # По имени сценария:$ behave tests/features/ennergiia.feature --name="Фильтровать товар по одному бренду"
    # По тегу сценария:$ behave tests/features/ennergiia.feature --tags="@test_tag_filter"
    # Запустить всю пачку:$ behave tests/features

    # Для windows:
    # Команды для запуска конкретных тестов выполняются в корне проекта из консоли
    # Но при таком запуске могут возникать ошибки "ERROR:data_channel.cc" на функционал тестов не влияют.
    # По имени сценария:$ behave tests\features\ennergiia.feature --name="Фильтровать товар по одному бренду"
    # По тегу сценария:$ behave tests\features\ennergiia.feature --tags="@test_tag_filter"
    # Запустить всю пачку:$ behave tests\features
