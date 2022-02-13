# Не используя библиотеки для парсинга, распарсить (получить определённые данные)
# файл логов web-сервера nginx_logs.txt
# (https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs)
# — получить список кортежей вида: (<remote_addr>, <request_type>, <requested_resource>). Например:
# [
#    ...
#    ('141.138.90.60', 'GET', '/downloads/product_2'),
#    ('141.138.90.60', 'GET', '/downloads/product_2'),
#    ('173.255.199.22', 'GET', '/downloads/product_2'),
#    ...
# ]


with open('nginx_logs.txt', 'r', encoding='utf-8') as f:
    parsed_result = []
    for line in f:
        parsed_result.append((
            line.replace('"', '').split()[0],
            line.replace('"', '').split()[5],
            line.replace('"', '').split()[6]))
print(parsed_result)
