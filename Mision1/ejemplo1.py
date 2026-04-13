import pandas as pd
# crear  datos (simulacion estudiantes)
datos={
    "nombre":["Ana","Luis","Carlos","Sofia","Pedro"],
    "Edad":[39,70,48,10,69],
    "nota":[4.6,2.3,5.0,4.2,1.3],
}
df = pd.DataFrame(datos)
print(df)
# Promedio de notas
print("Promedio Notas:",df["nota"].mean())
# Promedio de Edad
print("Promedio Edad:",df["Edad"].mean())