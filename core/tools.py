# """
#     pass
# """
#
# import requests
# import json
# import base64  # переопределяется (зацикливание)
# import urllib.parse  # переопределяется (зацикливание)
# from datetime import datetime  # переопределяется (зацикливание)
# import os
# import requests
#
# __BASE_HEADERS = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)',
#     'Accept': 'application/json',
#     'Accept-Encoding': 'gzip, deflate, br, zstd',
#     'Referer': 'https://www.mvideo.ru/',
#     # todo добавить возможность добавлять значения . определить состав для дефолтных настроек.
#     'Origin': 'https://www.mvideo.ru',
# }
#
#
# def get_response(url: str, headers: dict=None, params: dict=None, cookies: dict=None, session=None,
#                  json_type=True) -> object:
#     """
#     Универсальная функция для запросов с передаваемыми параметрами.
#     :param url:
#     :type url:
#     :param headers:
#     :type headers:
#     :param params:
#     :type params:
#     :param cookies:
#     :type cookies:
#     :param session:
#     :type session:
#     :return:
#     :rtype:
#     """
#
#
#     # Устанавливаем куки в сессии
#     if session and cookies:
#         session.cookies.update(cookies)
#
#     # Обычный запрос или сессия:
#     if session:
#         response = session.get(url, headers=headers, params=params)
#
#     else:
#         response = requests.get(url, headers=headers, params=params, cookies=cookies)
#
#
#     # Выполнение запроса:
#     if response.status_code == 200:
#
#         if json_type:
#             # Если ответ нужен в json:
#             data = response.json()
#
#         elif not json_type:
#             # Если ответ нужен в html:
#             data = response.text
#             # print(f'{data}')
#
#     else:
#         data = None
#         print(f"Ошибка: {response.status_code} - {response.text}")
#
#     return data
#
#
# class Tools
#
#     def __init__(self):
#
#         # self.__base_headers = self._get_headers()
#         pass
#
#
#     def _get_response_json(self, url: str = None, params: dict = None, cookies: dict = None) -> object:
#         """Функция для запросов с мутабельными параметрами. """
#
#         # Устанавливаем куки в сессии (если были переданы):
#         if cookies:
#             self.__session.cookies.update(cookies)
#
#         try:
#             # Выполнение запроса с сессией
#             response = self.__session.get(url=url, headers=self.__base_headers, params=params)
#             # Проверка кода ответа
#             if response.status_code == 200:
#                 data = response.json()  # Ответ в формате JSON
#
#             else:
#                 # Обработка некорректных HTTP ответов
#                 raise requests.exceptions.HTTPError(f"Ошибка HTTP: {response.status_code} - {response.text}")
#
#         # Перехватываем любые ошибки, включая сетевые и прочие исключения
#         except Exception as error_connect:
#             raise  # Передача исключения на верхний уровень для обработки
#         return data
#
#
#
#     #
#     # def _set_timeout(self, new_timeout_param: int):
#     #     """Передача нового значения промежутка времени между повторными подключениями, в случае сбоев."""
#     #     self.__TIMEOUT = self._validation_params(new_timeout_param, int, '_set_timeout')
#     #
#     #
#     # @staticmethod
#     # def _base64_decoded(url_param_string):
#     #     """
#     #         Расшифровка параметров URL.
#     #
#     #         :param url_param_string: (base64_string)
#     #         :type url_param_string:
#     #         :return:
#     #         :rtype:
#     #     """
#     #     try:
#     #         # Шаг 1: URL-декодирование
#     #         url_param_string_decoded = urllib.parse.unquote(url_param_string)
#     #         # Шаг 2: Base64-декодирование
#     #         base64_decoded_string = base64.b64decode(url_param_string_decoded).decode('utf-8')
#     #         return base64_decoded_string
#     #     except Exception as e:
#     #         print(f'Ошибка декодирования: {e}')
#     #         return None
#     #
#     # def param_encoded(self, param_string: str | int | float):  # todo добавить валидацию. сделать возможно статик методом
#     #     """Базовый метод кодирования в base64."""
#     #     param_string = str(param_string)  # Приводим к str принудительно.
#     #     bytes_string = param_string.encode('utf-8')  # Преобразуем строку в байтовый объект (bytes), utf-8:
#     #     base64_encoded = base64.b64encode(bytes_string).decode('utf-8')  # Base64-кодирование
#     #     result_encoded = urllib.parse.quote(base64_encoded)  # URL-кодирование
#     #     return result_encoded
#     #
#     # def encoded_param_string(self, key: str, value: str) -> str:
#     #     """Mетод кодирования одиночного параметра (ключ: значение) в base64."""
#     #     value_encoded = self.param_encoded(value)
#     #     return f'&{key}={value_encoded}'
#     #
#     #
#     #
#     #
#     #
#     #
#     #
#     # def values_validation(self, value: any) -> any:
#     #     """Валидация данных.
#     #     Пропускаются только стандартные типы данных. На верхнем уровне, будут приведены в str."""
#     #     if not isinstance(value, (str, int, float, dict, list, tuple, bool)):
#     #         raise ValueError(f"Неподдерживаемый тип данных: {type(value)} для объекта {value}. "
#     #                          f"Допустимые типы даннных: str, int, float, dict, list, tuple, bool.")
#     #     return value
#     #
#     # def args_validation(self,  # todo пересмотреть может исправить (упростить)
#     #                     key: str,
#     #                     value: Union[str, int, float, tuple[Union[str, int, float]], list[Union[str, int, float]]]
#     #                     ) -> str:
#     #     """На вход элемент картежа (for in *args)"""
#     #     tmp_params_list = []
#     #     param_string = None
#     #
#     #     # Если на вход обычные (str, int, float) - просто кодируем:
#     #     if isinstance(value, (str, int, float)):
#     #         param_string = self.encoded_param_string(key, value)
#     #
#     #     # Если на вход (tuple, list), - перебираем по элементам и кодируем:
#     #     elif isinstance(value, (tuple, list)):
#     #         for v in value:
#     #             # if not isinstance(v, (str, int, float)):
#     #             #     raise ValueError(f"Неподдерживаемый тип данных: {type(v)} в итерируемом объекте {value}. "
#     #             #                      f"Элементы должны быть str, int или float.")
#     #
#     #             param_string_tmp = self.encoded_param_string(key, v)
#     #             tmp_params_list.append(param_string_tmp)
#     #         param_string = ''.join(tmp_params_list)
#     #
#     #     # Не пропускаем другие типы данных:
#     #     else:
#     #         raise ValueError(f"Неподдерживаемый тип данных для входного значения: {type(value)}. "
#     #                          f"Ожидались str, int, float, tuple или list.")
#     #     return param_string
#     # # __________________________________________________________________
#     # # __________________________________________________________________ encoded_params_methods
#     # def encoded_params_list(self, key: str, *values: str | int | float) -> list[tuple]:
#     #     """
#     #     Формирователь закодированных (в base64) параметров 1.0.
#     #     В случаях, когда требуется передать в URL-строку параметры типа: одинаковые ключи - разные значения
#     #
#     #                 # Пример в URL-строке:
#     #                 '&filterParams=value_1&filterParams=value_2&filterParams=value_3',
#     #
#     #     тогда формируем список картежей всех переданных параметров, повторяя ключ:
#     #
#     #                 # Пример выходных параметров (для наглядности не в закодированном виде).
#     #                 filter_params = [
#     #                     ('filterParams', encoded_value_1),
#     #                     ('filterParams', encoded_value_2),
#     #                 ].
#     #                 На верхнем уровне, далее,- передача в request.
#     #
#     #     Однако, стоит учитывать, что не все сервисы корректно принимают параметры с одинаковыми ключами. Хотя requests
#     #     корректно формирует URL с повторяющимися параметрами, сервер может их неправильно обрабатывать.
#     #     """
#     #     result_params_list = []
#     #     for value in values:  # Перебираем все значения в *values
#     #         validation_value_encoded = self.args_validation(key, value)  # url_encoded(value) parser_01_vers_(procedural_func)
#     #         param_string = (validation_value_encoded)  # param_string = (key, value_encoded) parser_01_vers_(procedural_func)
#     #         result_params_list.append(param_string)
#     #     return result_params_list
#     #
#     # def encoded_params_monostring(self, key: str, *values: str | int | float) -> str:
#     #     """
#     #     Формирователь закодированных (в base64) параметров 1.1.
#     #     В случаях, когда требуется передать в URL-строку параметры типа: одинаковые ключи - разные значения
#     #
#     #                 # Пример в URL-строке:
#     #                 '&filterParams=value_1&filterParams=value_2&filterParams=value_3',
#     #
#     #     тогда формируем строку с конкатенацией всех переданных параметров, повторяя ключ:
#     #
#     #                 # Пример выходных параметров (для наглядности не в закодированном виде).
#     #                 filter_params = '&filterParams=value_1&filterParams=value_2&filterParams=value_3',
#     #                 На верхнем уровне, далее, - передача в в формируемую строку (full_url = f'{url_base}{ilter_params}.
#     #
#     #     Этот метод служит только для передачи параметров запроса с одинаковыми ключами непосредственно
#     #     в формируемую строку (full_url = f'{url_base}{ilter_params}, передача такой строки через метод param в requests
#     #     вызовет ошибку.
#     #     """
#     #     temp_params_list = []
#     #     # Перебираем все значения в *values
#     #     for value in values:
#     #         param_string = self.args_validation(key, value)  # f'&{key}={self._encoded(value)}' parser_01_vers_(procedural_func)
#     #         temp_params_list.append(param_string)
#     #     result_params = ''.join(temp_params_list)
#     #     return result_params
#     #
#     # def encoded_params_dict(self, no_encoded_params_dict: dict[str, str]) -> dict[str, str]:
#     #     """
#     #     Формирователь закодированных (в base64) параметров 2.0.
#     #     В случаях, когда требуется передать в URL-строку параметры типа: уникальные ключи - значения
#     #
#     #                 # Пример в URL-строке:
#     #                 '&filterParams_1=value_1&filterParams_2=value_2&filterParams_3=value_3',
#     #
#     #     тогда на основе переданного в метод словаря формируем новый, но уже с закодированными параметрами
#     #     (предварительно проводится валидация данных):
#     #
#     #                 # Пример выходных параметров (для наглядности не в закодированном виде).
#     #                 filter_params = {
#     #                     filterParams_1: encoded_value_1
#     #                     filterParams_2: encoded_value_2
#     #                     filterParams_3: encoded_value_3
#     #                     }.
#     #                 На верхнем уровне, далее, - передача в request.
#     #     """
#     #     return {key: self.param_encoded(value) for key, value in no_encoded_params_dict.items()
#     #             if self.values_validation(key) and self.values_validation(value)}