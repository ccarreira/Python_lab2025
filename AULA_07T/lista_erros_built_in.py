Lista **curta, prática e focada** dos **erros built-in mais usados** no Python (os que realmente aparecem em código normal, jogos, scripts e exercícios).

---

# **1. Erros de valor/lógica**

| Exceção            | Quando usar / Quando aparece                                                   |
| ------------------ | ------------------------------------------------------------------------------ |
| **ValueError**     | Valor válido em tipo, mas inválido em lógica (ex: `int("abc")`, dano negativo) |
| **TypeError**      | Tipo errado (ex: somar string com inteiro)                                     |
| **AssertionError** | Falha de `assert`                                                              |
| **IndexError**     | Índice fora da lista/tuple                                                     |
| **KeyError**       | Key inexistente num dicionário                                                 |
| **AttributeError** | Atributo/método não existe                                                     |
| **NameError**      | Variável não definida                                                          |
| **RuntimeError**   | Erro genérico de execução sem categoria melhor                                 |

---

# **2. Erros matemáticos**

| Exceção                | Quando aparece                             |
| ---------------------- | ------------------------------------------ |
| **ZeroDivisionError**  | Dividir por zero                           |
| **OverflowError**      | Valor numérico demasiado grande            |
| **FloatingPointError** | Problemas com floats (raro sem configurar) |

---

# **3. Erros de ficheiros / IO**

| Exceção               | Quando aparece                         |
| --------------------- | -------------------------------------- |
| **FileNotFoundError** | Ficheiro não existe                    |
| **PermissionError**   | Sem permissoes para abrir/escrever     |
| **IsADirectoryError** | Tentaste abrir uma pasta como ficheiro |
| **IOError / OSError** | Problemas genéricos com input/output   |

---

# **4. Erros de conversão / parsing**

| Exceção                               | Quando aparece                     |
| ------------------------------------- | ---------------------------------- |
| **UnicodeDecodeError**                | Ler texto com encoding errado      |
| **UnicodeEncodeError**                | Escrever texto com encoding errado |
| **JSONDecodeError** *(vem de `json`)* | JSON mal formado                   |

---

# **5. Erros de iteração**

| Exceção                | Quando aparece                        |
| ---------------------- | ------------------------------------- |
| **StopIteration**      | Fim de iterador (normalmente interno) |
| **StopAsyncIteration** | Versão async                          |

---

# **6. Erros de módulo / importação**

| Exceção                 | Quando aparece                             |
| ----------------------- | ------------------------------------------ |
| **ModuleNotFoundError** | Módulo não existe                          |
| **ImportError**         | Problema ao importar algo dentro do módulo |

---

# **7. Erros de sistema**

| Exceção               | Quando aparece              |
| --------------------- | --------------------------- |
| **MemoryError**       | Sem memória                 |
| **RecursionError**    | Recursão demasiado profunda |
| **KeyboardInterrupt** | Ctrl + C                    |

---

# **8. Erros de sintaxe (não são apanhados com `try`)**

| Exceção              | Quando                                    |
| -------------------- | ----------------------------------------- |
| **SyntaxError**      | Erro na fase de parsing (antes de correr) |
| **IndentationError** | Identação errada                          |
| **TabError**         | Mistura de tabs e espaços                 |

*(Estes não podem ser apanhados com `except`, porque o código nem chega a correr.)*

---

# **A lista mínima que realmente usas no dia-a-dia**

Se fores pragmático:

```
ValueError
TypeError
KeyError
IndexError
AttributeError
NameError
FileNotFoundError
JSONDecodeError
ZeroDivisionError
RuntimeError
AssertionError
```

Esses 11 cobrem **95%** das situações reais.

---

Se quiseres, posso fazer uma versão da lista com:
✓ para que serve
✗ como NÃO usar

* exemplo de `try/except` curto para cada.


#**************************************

Aqui tens uma **versão ultra-prática**, com ✓ *quando usar*, ✗ *quando não usar*, e 1 exemplo curto por erro.
É a lista funcional que deves decorar.

---

# **1. ValueError**

✓ Valor errado, mas tipo certo
✗ Não usar para tipo errado (`TypeError` é melhor)

```python
def set_hp(hp):
    if hp < 0:
        raise ValueError("HP não pode ser negativo")
```

---

# **2. TypeError**

✓ Tipo errado
✗ Não usar para valores fora do intervalo

```python
def set_speed(s):
    if not isinstance(s, int):
        raise TypeError("speed deve ser int")
```

---

# **3. KeyError**

✓ Chave não existente num dicionário
✗ Não usar para índices de listas

```python
stats = {"hp": 100}
try:
    print(stats["atk"])
except KeyError:
    print("stat inexistente")
```

---

# **4. IndexError**

✓ Índice fora dos limites de lista/tuplo
✗ Não usar para dicionários

```python
nums = [10, 20]
try:
    print(nums[5])
except IndexError:
    print("fora da lista")
```

---

# **5. AttributeError**

✓ Objeto não tem atributo/método
✗ Não usar quando é um bug de lógica grave → aí usa assert

```python
class Hero: pass

h = Hero()
try:
    h.attack()
except AttributeError:
    print("Hero não tem attack()")
```

---

# **6. NameError**

✓ Variável não existe
✗ Praticamente nunca se “usa” — é sempre erro do programador

```python
try:
    print(x)
except NameError:
    print("x não definido")
```

---

# **7. FileNotFoundError**

✓ Ficheiro faltando
✗ Não usar para JSON inválido

```python
try:
    open("save.json")
except FileNotFoundError:
    print("save não existe")
```

---

# **8. JSONDecodeError**

✓ JSON mal formado
✗ Não usar para ficheiro vazio → isso é ValueError

```python
import json

try:
    json.loads("{bad}")
except json.JSONDecodeError:
    print("json inválido")
```

---

# **9. ZeroDivisionError**

✓ Divisão por zero
✗ Só para casos matemáticos

```python
try:
    1/0
except ZeroDivisionError:
    print("divisão zero")
```

---

# **10. AssertionError**

✓ Garantias internas (invariants)
✗ Nunca usar como validação de input do utilizador

```python
def update_hp(hp):
    assert hp >= 0, "HP ficou negativo → BUG"
```

---

# **11. RuntimeError**

✓ Erro genérico quando nada mais faz sentido
✗ Não usar sempre → só quando não há categoria específica

```python
if hero.state == "dead":
    raise RuntimeError("Hero não pode agir morto")
```
