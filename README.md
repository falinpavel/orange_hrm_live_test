# OrangeHRM Automated Testing

Этот проект содержит автотесты для веб-приложения [OrangeHRM Demo](https://opensource-demo.orangehrmlive.com/web/index.php/auth/login). Тесты написаны для автоматизации проверки функциональности приложения.

## 📋 Описание

Автотесты предназначены для проверки работы следующих компонентов OrangeHRM:

- Авторизация пользователей
- Навигация по страницам
- Проверка функциональности панели управления
- Управление пользователями и записями

## 🧪 Покрытие тестов
| Функциональность                | Статус    | Примечания |
|---------------------------------|-----------|-----------|
| Авторизация и logout            | ✅        | Complete  |
| Боковая панель меню (навигация) | ✅        | Complete  |
| Страница "Admin"                | ✅        | In progress   |
| Страница "PIM"                  | ⬜        | Backlog   |
| Страница "Leave"                | ⬜        | Backlog   |
| Страница "Time"                 | ⬜        | Backlog   |
| Страница "Recruitment"          | ⬜        | Backlog   |
| Страница "My Info"              | ✅        | In progress |
| Страница "Performance"          | ⬜        | Backlog   |
| Страница "Dashboard"            | ⬜        | Backlog   |
| Страница "Directory"            | ⬜        | Backlog   |
| Страница "Maintenance"          | ⬜        | Backlog   |
| Страница "Claim"                | ⬜        | Backlog   |
| Страница "Buzz"                 | ⬜        | Backlog   |
| Отчеты                          | ⬜        | Backlog   |

## 🛠️ Используемые технологии

- **Язык программирования:** Python
- **Фреймворк для тестирования:** pytest
- **Инструменты для автоматизации:** Selenium WebDriver
- **Менеджер зависимостей:** pip
- **Подходы к тестированию:** Page Object Model (POM)

## 📂 Структура проекта

```plaintext
├── base/                   # base_page и base_test (Базовые страницы и тесты)
├── pages/                  # Модели страниц (Page Object)
├── tests/                  # Тестовые сценарии
├── config/                 # Конфигурация и ссылки
├── .env                    # Креды для тестовых сценариев
├── conftest.txt            # Инициализация драйвера, фикстуры
├── requirements.txt        # Список зависимостей
└── README.md               # Описание проекта
```

## 🚀 Запуск тестов
Шаг 1. Клонируйте репозиторий
git clone <ссылка-на-репозиторий>
cd <имя-проекта>
Шаг 2. Установите зависимости
Убедитесь, что Python версии 3.8+ установлен на вашем компьютере.

pip install -r requirements.txt

Шаг 3. Запустите тесты
pytest -s -v

## 📑 Пример теста

```python
    def change_first_name(self, new_first_name):
        with allure.step(f"Change first name on {new_first_name}"):
            """Изменение имя сотрудника"""
            first_name_field = self.wait.until(EC.element_to_be_clickable(
                self.EMPLOYEE_FIRST_NAME_FIELD)
            )
            first_name_field.click()
            first_name_field.clear()
            first_name_field.send_keys(new_first_name)
            self.name = new_first_name

    def change_middle_name(self, new_middle_name):
        with allure.step(f"Change middle name on {new_middle_name}"):
            middle_name = self.wait.until(EC.element_to_be_clickable(
                self.EMPLOYEE_MIDDLE_NAME_FIELD)
            )
            middle_name.click()
            middle_name.clear()
            middle_name.send_keys(new_middle_name)
            self.name = new_middle_name

    def change_second_name(self, new_second_name):
        with allure.step(f"Change second name on {new_second_name}"):
            second_name = self.wait.until(EC.element_to_be_clickable(
                self.EMPLOYEE_SECOND_NAME_FIELD)
            )
            second_name.click()
            second_name.clear()
            second_name.send_keys(new_second_name)
            self.name = new_second_name
```

## 🛠️ Настройка окружения
Создайте файл .env в корне проекта и укажите следующие параметры:

BASE_URL=https://opensource-demo.orangehrmlive.com
USERNAME=Admin
PASSWORD=admin123
