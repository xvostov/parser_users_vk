# This script checks VK users

from functions import *


def main():
    init(autoreset=True)
    print_greeting()
    urls_list = read_url_file()
    # print(urls_list)
    parse_urls(urls_list)


if __name__ == '__main__':
    main()
