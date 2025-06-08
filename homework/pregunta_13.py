"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en los archivos `tbl0.tsv`, `tbl1.tsv` y 
`tbl2.tsv`. En este laboratorio solo puede utilizar las funciones y 
librerias de pandas para resolver las preguntas.
"""

from homework.load_input import load_input 
import pandas as pd

def pregunta_13():
    """
    Si la columna `c0` es la clave en los archivos `tbl0.tsv` y `tbl2.tsv`,
    compute la suma de `tbl2.c5b` por cada valor en `tbl0.c1`.

    Rta/
    c1
    A    146
    B    134
    C     81
    D    112
    E    275
    Name: c5b, dtype: int64
    """
    sequence_0 = load_input("files/input",0)
    sequence_2 = load_input("files/input",2)

    tabla2 = sequence_2.groupby("c0")["c5b"].sum()

    sequence = pd.merge(sequence_0,tabla2, on="c0")
    result = sequence.groupby("c1")["c5b"].sum()
    print(result)
    return result

if __name__ == "__main__":
    pregunta_13()