Feature: Ввод данные для регистраци трансопртных средств

  Как Оперетор
  Я хочу зарегистрировать транспортное средство
  Для этого я

  Scenario: Открытие страницы регистрации трансопртных средств
    Given Адрес веб страницы
    When Оператор открывает страницу
    Then Тогда видеть титульник

  Scenario Outline:  Оператор вводит данные по машине и водителю
    Given Оператор на странице ввода
    When Опертор ввел данные маршрута с водителем <drivers>
    Then На странице появляется таблица с данными маршрута c водителем <drivers_on_page>

  Examples: Список водителей
       | drivers        | drivers_on_page |
       | Driver A       | Driver A        |
       | Driver B       | Driver B        |
