# Voice_assistant_salutspeach
voice assistant for salut speach

# Installation
1. Создать .env файл
```
AUTH_DATA="<auth_data строка из аккаунта разработчика сбер id>"
ACCESS_TOKEN="Bearer токен, можно получить из файлов ...example_no_file.py. Необходим для ручного тестирования файлов ..._example.py"
SYNTHESIS_HOST="smartspeech.sber.ru"
RECOGNIZE_HOST="smartspeech.sber.ru"
```
   
3. Установить сертификаты безопастности Минцифры, инструкция есть в документации сбера и Госуслугах. Сами сертификаты также можно скачать с госуслуг.
4. Поместить файлы russian_trusted_root_ca.cer и russian_trusted_sub_ca.cer в папку salut_speach_example если они отсутствуют.

# Usage recognition
## Рабочие файлы:
1. recognize_example.py - Ручной запуск с заранее известынм ACCESS_TOKEN.
   Пример запуска: $ python recognize_example.py --file "<file_name>"
   
2. recognize_example_no_file.py - Запуск распознавания речи с использованием микрофона. Для запуска необходим AUTH_DATA.

# Usage synthesis
## Рабочие файлы
1. synthesis_example.py - Ручной запуск с заранее известынм ACCESS_TOKEN.
   Пример запуска: $ python synthesis_example.py --text "<text_data>" --file "<file_name>"
   
2. synthesis_example_no_file.py - Синтез речи с использованием колонок минуя файлы. Для запуска необходим AUTH_DATA. 
   Текст для синтеза можно изменить в коде.


