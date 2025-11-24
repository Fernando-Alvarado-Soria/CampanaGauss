from math import erf, sqrt

def phi(z):
    """Función de distribución acumulada de la normal estándar."""
    return 0.5 * (1 + erf(z / sqrt(2)))

def z_score(x, mu, sigma):
    return (x - mu) / sigma

def prob_menor_que(x, mu, sigma):
    z = z_score(x, mu, sigma)
    prob = phi(z)
    return z, prob

def prob_mayor_que(x, mu, sigma):
    z = z_score(x, mu, sigma)
    prob = 1 - phi(z)
    return z, prob

def prob_entre(a, b, mu, sigma):
    z1 = z_score(a, mu, sigma)
    z2 = z_score(b, mu, sigma)
    prob = phi(z2) - phi(z1)
    return z1, z2, prob

def main():
    print("=== Campana de Gauss / Distribución Normal ===")

    mu = float(input("Ingresa la media (μ): "))
    sigma = float(input("Ingresa la desviación estándar (σ): "))

    if sigma <= 0:
        print("La desviación estándar debe ser mayor que 0.")
        return

    while True:
        print("\n¿Qué deseas calcular?")
        print("1) P(X ≤ x)")
        print("2) P(X ≥ x)")
        print("3) P(a ≤ X ≤ b)")
        print("0) Salir")
        opcion = input("Opción: ")

        if opcion == "0":
            break

        # P(X <= x)
        if opcion == "1":
            x = float(input("Ingresa el valor x: "))
            z, prob = prob_menor_que(x, mu, sigma)

            print("\n--- Paso a paso ---")
            print("1) Fórmula de conversión a Z:")
            print("   Z = (X - μ) / σ")
            print(f"2) Sustituyendo valores: Z = ({x} - {mu}) / {sigma}")
            print(f"3) Resultado de Z: Z = {z:.4f}")
            print("4) Buscamos la probabilidad acumulada Φ(Z) = P(X ≤ x)")
            print("\n--- Resultado ---")
            print(f"P(X ≤ {x}) = {prob:.4f}  →  {prob*100:.2f}%")
            if x > mu:
                print(f"Interpretación: hay un {prob*100:.2f}% de probabilidad de que X sea menor o igual a {x},")
                print("es decir, el área sombreada está a la izquierda de x, en la parte derecha de la media.")
            else:
                print(f"Interpretación: hay un {prob*100:.2f}% de probabilidad de que X sea menor o igual a {x},")
                print("el área sombreada está a la izquierda de x, principalmente en la parte izquierda de la media.")

        # P(X >= x)
        elif opcion == "2":
            x = float(input("Ingresa el valor x: "))
            z, prob = prob_mayor_que(x, mu, sigma)

            print("\n--- Paso a paso ---")
            print("1) Fórmula de conversión a Z:")
            print("   Z = (X - μ) / σ")
            print(f"2) Sustituyendo valores: Z = ({x} - {mu}) / {sigma}")
            print(f"3) Resultado de Z: Z = {z:.4f}")
            print("4) Primero obtenemos la probabilidad acumulada Φ(Z) = P(X ≤ x)")
            print("5) Como queremos P(X ≥ x), usamos:  P(X ≥ x) = 1 - Φ(Z)")
            print("\n--- Resultado ---")
            print(f"P(X ≥ {x}) = {prob:.4f}  →  {prob*100:.2f}%")

        # P(a <= X <= b)
        elif opcion == "3":
            a = float(input("Ingresa el valor a (límite inferior): "))
            b = float(input("Ingresa el valor b (límite superior): "))

            if a >= b:
                print("Error: se requiere que a < b.")
                continue

            z1, z2, prob = prob_entre(a, b, mu, sigma)
            phi_z1 = phi(z1)
            phi_z2 = phi(z2)

            print("\n--- Paso a paso ---")
            print("1) Convertimos ambos límites a valores Z:")
            print("   Z = (X - μ) / σ")
            print(f"   Para a: Z1 = ({a} - {mu}) / {sigma} = {z1:.4f}")
            print(f"   Para b: Z2 = ({b} - {mu}) / {sigma} = {z2:.4f}")
            print("2) Buscamos las probabilidades acumuladas:")
            print(f"   Φ(Z1) = P(X ≤ {a}) ≈ {phi_z1:.4f}")
            print(f"   Φ(Z2) = P(X ≤ {b}) ≈ {phi_z2:.4f}")
            print("3) Restamos para obtener el área entre a y b:")
            print("   P(a ≤ X ≤ b) = Φ(Z2) - Φ(Z1)")
            print(f"   P({a} ≤ X ≤ {b}) = {phi_z2:.4f} - {phi_z1:.4f} = {prob:.4f}")
            print("\n--- Resultado ---")
            print(f"P({a} ≤ X ≤ {b}) = {prob:.4f}  →  {prob*100:.2f}%")

        else:
            print("Opción no válida, intenta de nuevo.")

if __name__ == "__main__":
    main()