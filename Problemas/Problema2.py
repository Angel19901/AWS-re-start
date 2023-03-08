print("Calculadora de descuento.");
Precio = float(input("Ingrese el precio del articulo:"));

if Precio >= 0:
    print(f"EL articulo con descuento del 15% es: {Precio * (1.0 - 0.15)}");
else:
    print("El precio debe ser mayor a 0.");