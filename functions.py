from colorama import init, Fore

from config import *

import requests, time, csv


def print_greeting():
    print(f"""{Fore.BLUE}


██    ██ ██   ██     ██████   █████  ██████  ███████ ███████ ██████  
██    ██ ██  ██      ██   ██ ██   ██ ██   ██ ██      ██      ██   ██ 
██    ██ █████       ██████  ███████ ██████  ███████ █████   ██████  
 ██  ██  ██  ██      ██      ██   ██ ██   ██      ██ ██      ██   ██ 
  ████   ██   ██     ██      ██   ██ ██   ██ ███████ ███████ ██   ██ 

                                                            {Fore.RESET} by Xv0st0v""")


def read_url_file():
    """Читает файл с ссылками и генерирует список"""
    print(f"Чтение файла {path_urls_file} ...")
    try:
        urls_file = open(path_urls_file, "r")
    except FileNotFoundError:
        print(f"{Fore.RED}Файл urls.txt не найден")
        print("Завершение программы...")
        urls_file.close()
        raise

    urls = [url.strip() for url in urls_file]  # Генерируем список с адресами страниц
    urls_file.close()

    print(f"{Fore.GREEN}Файл {path_urls_file} успешно прочитан. \n\n")
    return urls


def parse_urls(urls_list):
    """Обходит все ссылки из списка"""
    file_valid = open(path_valid_file, "w", encoding="utf-8")
    file_bad = open(path_bad_file, "w", encoding="utf-8")
    for url in urls_list:
        if check_url(url) == "active":
            print(f"{Fore.GREEN}Страница Активна")
            file_valid.write(url + "\n")

        elif check_url(url) == "banned":
            print(f"{Fore.RED}Страница заблокирована")
            file_bad.write(url + "\n")
        time.sleep(0.3)
    file_valid.close()
    file_bad.close()


def check_url(url):
    """ Делает запрос к vk api и вызывает функцию parse_error_code, которая возвращает Active или Banned страница"""
    response = requests.get("https://api.vk.com/method/users.get", params={'user_ids': cut_url(url),
                                                                           'fields': 'deactivated',
                                                                           'access_token': token,
                                                                           'v': '5.131'})
    response = response.json()
    # print(response)
    return parse_error_code(response)


def parse_error_code(response):
    # print(response)
    # print(response["response"][0]["deactivated"])
    return response["response"][0].get("deactivated", "active")


def cut_url(url):
    """Обрезает url"""
    if "id" in url:
        """Обращаемся по id"""
        # print("id")
        # print(url[17:])
        user_id = url[17:]
    else:
        """Обращаемся по домену"""
        # print("Домен")
        # print(url[15:])
        user_id = url[15:]
    return user_id





