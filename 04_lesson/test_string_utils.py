import pytest
from string_utils import StringUtils

utils = StringUtils()

# 1. ТЕСТЫ ДЛЯ capitalize (Первая буква заглавная)
def test_capitalize_positive():
    # Позитивный тест: обычное слово
    assert utils.capitalize("skypro") == "Skypro"

def test_capitalize_empty():
    # Негативный тест: пустая строка
    assert utils.capitalize("") == ""


# 2. ТЕСТЫ ДЛЯ trim (Удаление пробелов в начале)
def test_trim_with_spaces():
    # Позитивный тест: удаляем три пробела
    assert utils.trim("   skypro") == "skypro"

def test_trim_without_spaces():
    # Позитивный тест: если пробелов нет, возвращаем строку без изменений
    assert utils.trim("skypro") == "skypro"


# 3. ТЕСТЫ ДЛЯ contains (Проверка наличия символа)
def test_contains_true():
    # Позитивный тест: символ 'S' есть в строке
    assert utils.contains("SkyPro", "S") is True

def test_contains_false():
    # Позитивный тест: символа 'U' нет в строке
    assert utils.contains("SkyPro", "U") is False


# 4. ТЕСТЫ ДЛЯ delete_symbol (Удаление подстроки)
def test_delete_symbol_positive():
    # Позитивный тест: удаляем букву 'k'
    assert utils.delete_symbol("SkyPro", "k") == "SyPro"

def test_delete_symbol_not_found():
    # Негативный тест: удаляем символ, которого нет (строка не меняется)
    assert utils.delete_symbol("SkyPro", "z") == "SkyPro"
