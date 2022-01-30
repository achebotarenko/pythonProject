def currency_rates(currency):

    """
    get the rate of currency by code from www.cbr.ru for RUB
    :param currency:
    :return: rate
    """

    from requests import get
    response = get('http://www.cbr.ru/scripts/XML_daily.asp').text
    charcode = [el_charcode.split('</CharCode>')[0] for el_charcode in response.split('<CharCode>')[1:]]
    nominal = [el_nominal.split('</Nominal>')[0] for el_nominal in response.split('<Nominal>')[1:]]
    value = [el_value.split('</Value>')[0] for el_value in response.split('<Value>')[1:]]
    dict_rate = dict(zip(charcode, zip(nominal, value)))
    rate = dict_rate.get(currency.upper())
    if dict is None:
        print('Указанная валюта отсутствует')
    else:
        print(f'Курс RUB за {rate[0]} {currency.upper()}: {rate[1]}')


currency_rates(input("Ведите код валюты (ХХХ): "))
