# parser users vk

Скрипт для проверки страниц пользователей на валидность, 
на выходе получается два файла valid.txt (с ссылками на валидные страницы) и bad.txt (с ссылками на заблокированные страницы)

## Как пользоваться?
1. Сначала нужно получить токен для VK api по этой ссылке
https://vkhost.github.io/

2. Далее полученный токен вставляем в config.py в поле token
должно получиться так: token = "ваш токен"

3. Следующим шагом нужно поместить ссылки на страницы пользователей ВК
ссылки могут иметь такой формат:
https://vk.com/id000000
https://vk.com/xxxxxxxx

4. Теперь можно запускать скрипт
