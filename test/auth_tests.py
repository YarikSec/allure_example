import allure
import pytest

@allure.id('37638')
@allure.tag('web', 'smoke')
@allure.title("Auth via Google")
@allure.feature("Auth")
def test_google_auth():
    with allure.step("Открываем главную страницу"):
        pass
    with allure.step("Выбираем способ авторизации через Google"):
        pass
    with allure.step("Авторизуемся как Mr Random"):
        with allure.step("Expected Result"):
            with allure.step("Водим логин random@gmail.com"):
                pass
            with allure.step("Вводим пароль random_password"):
                pass
            with allure.step("Нажимаем кнопку Войти"):
                pass
    with allure.step("Проверяем что авторизовались успешно"):
        pass
    with allure.step("Проверяем что данные обновились из Гугл"):
        with allure.step("Expected Result"):
            with allure.step("Имя Mr Random"):
                pass
            with allure.step("email: random@gmail.com"):
                pass