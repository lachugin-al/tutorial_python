d = {"key": "value"}

# Обработка исключения KeyError

try:

    d["super_key"]

except KeyError as e:
    print(e, "ты передал не тот ключ")
    raise KeyError(f"{e}") from e
