def func(a: object, b: object, c: object) -> object:
    return a, b, c


func(1, 2, c=3, **{"c": 4})  # [repeated-keyword]
func(1, 2, **{"c": 3}, **{"c": 4})  # [repeated-keyword]
