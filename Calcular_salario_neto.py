salario = 8000
renta = (8000 * 0.10)
seguro = (8000 * 0.05)
pensiones = (8000 * 0.03)
sum_total = (renta + seguro + pensiones)
rest = (salario - sum_total)
SalarioNeto = rest
print(f"El salario bruto es: {salario}")
print(f"Las deducciones totales son : {sum_total}")
print(f"El salario neto es: {rest}")
