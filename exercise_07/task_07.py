# Написать функцию расчета аннуитетного платежа. Написать функцию расчета ежимесячного платежа.
# Рассчитать размер платежа при ипотеке 15 млн на 25 лет под 14% годовых.
# Мат. часть: http://biznes-kredit.info/malyj/raschet-annuitetnyh-platezhej-formula-excel.html


PERIOD = 25  # Срок кредита в годах
YEAR_INTEREST = 14  # Годовая ставка
CREDIT = 15000000  # Сумма кредита


def get_annuity_rate():
    """Функция возвращает коэффициент аннуитета"""
    period_months = PERIOD * 12
    month_interest = YEAR_INTEREST / 12 / 100
    complex_year_interest = (1 + month_interest) ** period_months
    return (month_interest * complex_year_interest) / (complex_year_interest - 1)


def get_annuity_amount():
    """Функция возвращает размер аннуитетного платежа по кредиту"""
    return get_annuity_rate() * CREDIT


# print(get_annuity_rate())
print("Ежемесячно нужно платить: {:.2f} руб.".format(get_annuity_amount()))
