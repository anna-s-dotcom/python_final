# Lies zwei Zahlen ein und berechne die Fläche,
# wenn man sie als Seiten eines Rechtecks betrachtet.
# Gib die Fläche aus.

a = input("Gib Seite A ein: ")
a = float(a)

b = float(input("Gib Seite B ein: "))

area = a*b
# {x:.2f} x wird als float mit zwei nachkommastellen angezeigt
print(f"Fläche ist {area:.2f}qcm.")
