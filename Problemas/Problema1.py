print("Calculadora de consumo por kilometro.");
Kilometros = float(input("Ingrese la cantidad de kilometros recorridos: "));
Gasolina = float(input("Ingrese la cantidad de gasolina usada: "));

if Kilometros >= 0.0 and Gasolina >= 0.0:
    print(f"El consumo por kilometro es de: {Kilometros / Gasolina}");
else:
    print("Debe ingresar valores mayores a 0.");