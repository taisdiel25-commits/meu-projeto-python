# Meu Projeto — calendário

Projeto Python com funções para calcular a idade em anos completos e os dias que faltam até uma data.

## Requisitos

Python 3.10 ou superior. Para executar os testes, instale pytest:

```bash
python -m pip install -e ".[test]"
python -m pytest
```

## Uso

```python
from datetime import date
from calendario import calcular_idade, dias_ate

idade = calcular_idade(date(1990, 8, 20))
dias_restantes = dias_ate(date(2030, 1, 1))
```

As funções aceitam opcionalmente `hoje`, o que facilita testes e uso com uma data de referência. `calcular_idade` rejeita nascimento futuro; `dias_ate` aceita hoje (zero dias), mas rejeita datas passadas.

Na branch `NovoCalculo` há também `dias_desde`, para contar dias transcorridos desde uma data passada.
