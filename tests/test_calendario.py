from datetime import date

import pytest

from calendario import calcular_idade, dias_ate


@pytest.mark.parametrize(
    ("nascimento", "hoje", "esperado"),
    [
        (date(2000, 6, 15), date(2026, 6, 15), 26),
        (date(2000, 6, 16), date(2026, 6, 15), 25),
        (date(2000, 1, 1), date(2026, 12, 31), 26),
    ],
)
def test_calcular_idade(nascimento, hoje, esperado):
    assert calcular_idade(nascimento, hoje) == esperado


def test_calcular_idade_rejeita_nascimento_futuro():
    with pytest.raises(ValueError):
        calcular_idade(date(2026, 6, 16), date(2026, 6, 15))


def test_dias_ate_data_futura():
    assert dias_ate(date(2026, 6, 20), date(2026, 6, 15)) == 5


def test_dias_ate_hoje():
    assert dias_ate(date(2026, 6, 15), date(2026, 6, 15)) == 0


def test_dias_ate_rejeita_data_passada():
    with pytest.raises(ValueError):
        dias_ate(date(2026, 6, 14), date(2026, 6, 15))


def test_dias_desde_data_passada():
    from calendario import dias_desde

    assert dias_desde(date(2026, 6, 10), date(2026, 6, 15)) == 5


def test_dias_desde_hoje():
    from calendario import dias_desde

    assert dias_desde(date(2026, 6, 15), date(2026, 6, 15)) == 0


def test_dias_desde_rejeita_data_futura():
    from calendario import dias_desde

    with pytest.raises(ValueError):
        dias_desde(date(2026, 6, 16), date(2026, 6, 15))
