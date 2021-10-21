# Домашняя работа

Примеры создания рекурсивной функции и работы с Pillow можно найти в этой директории.

## Рекурсия

1. Дописать функцию вывода элементов списка через рекурсию.
```python
def recursive_print_list(l: list):
    """
    Печатает все элементы списка при помощи рекурсии. Пользоваться циклами
    запрещено. Для реализации можно пользоваться срезами.
    """
    pass
```

## Pillow

2. Написать программу, которая:
   * Считывает jpg/png изображение
   * На основе считанного изображения создает инвертированное, формула:
    ```python
    r = 255 - r0
    g = 255 - g0
    b = 255 - b0
    ```
   * При помощи модуля [ImageFilter](https://pillow.readthedocs.io/en/stable/reference/ImageFilter.html) накладывает на полученное изображение [фильтр размытия](https://pillow.readthedocs.io/en/stable/reference/ImageFilter.html#PIL.ImageFilter.GaussianBlur) с радиусом 10
   * [Сохраняет](https://pillow.readthedocs.io/en/stable/reference/Image.html#PIL.Image.Image.save) итоговый результат в новый файл
