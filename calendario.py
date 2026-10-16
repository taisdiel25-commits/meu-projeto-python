"""Funções para cálculos de idade e intervalos entre datas."""

from datetime import date


def calcular_idade(data_nascimento: date, hoje: date | None = None) -> int:
    """Retorna a idade em anos completos na data ``hoje`` (ou na data atual)."""
    hoje = hoje or date.today()
    if data_nascimento > hoje:
        raise ValueError("A data de nascimento não pode estar no futuro.")

    idade = hoje.year - data_nascimento.year
    aniversario_ja_ocorreu = (hoje.month, hoje.day) >= (
        data_nascimento.month,
        data_nascimento.day,
    )
    return idade if aniversario_ja_ocorreu else idade - 1


def dias_ate(data_futura: date, hoje: date | None = None) -> int:
    """Retorna quantos dias faltam até uma data futura (hoje retorna zero)."""
    hoje = hoje or date.today()
    if data_futura < hoje:
        raise ValueError("A data informada deve ser hoje ou uma data futura.")
    return (data_futura - hoje).days
