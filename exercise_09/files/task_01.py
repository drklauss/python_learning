# Вводится имя файла. Требуется проверить, что его расширение входит в список допустимых (png, jpg, jpeg, gif, svg')


def is_extension_valid(ext: str) -> bool:
    """Входит ли расширение в список разрешенных"""
    is_valid = False
    for extension in ("png", "jpg", "jpeg", "gif", "svg"):
        if extension in ext:
            is_valid = True
            break
    return is_valid


fileName = input("Введите название файла:")
if is_extension_valid(fileName):
    print("valid")
else:
    print("not valid")
