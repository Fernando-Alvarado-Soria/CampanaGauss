from math import erf, sqrt

def phi(z):
    """Función de distribución acumulada de la normal estándar."""
    return 0.5 * (1 + erf(z / sqrt(2)))

def z_score(x, mu, sigma):
    return (x - mu) / sigma

def prob_menor_que(x, mu, sigma):
    z = z_score(x, mu, sigma)
    return z, phi(z)

def prob_mayor_que(x, mu, sigma):
    z = z_score(x, mu, sigma)
    return z, 1 - phi(z)

def prob_entre(a, b, mu, sigma):
    z1 = z_score(a, mu, sigma)
    z2 = z_score(b, mu, sigma)
    return (z1, z2), phi(z2) - phi(z1)

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

        if opcion == "1":
            x = float(input("Ingresa el valor x: "))
            z, prob = prob_menor_que(x, mu, sigma)
            print(f"\nZ = {z:.2f}")
            print(f"P(X ≤ {x}) = {prob:.4f}  →  {prob*100:.2f}%")

        elif opcion == "2":
            x = float(input("Ingresa el valor x: "))
            z, prob = prob_mayor_que(x, mu, sigma)
            print(f"\nZ = {z:.2f}")
            print(f"P(X ≥ {x}) = {prob:.4f}  →  {prob*100:.2f}%")

        elif opcion == "3":
            a = float(input("Ingresa el valor a (límite inferior): "))
            b = float(input("Ingresa el valor b (límite superior): "))

            if a >= b:
                print("Error: se requiere que a < b.")
                continue

            (z1, z2), prob = prob_entre(a, b, mu, sigma)
            print(f"\nZ1 = {z1:.2f}, Z2 = {z2:.2f}")
            print(f"P({a} ≤ X ≤ {b}) = {prob:.4f}  →  {prob*100:.2f}%")

        else:
            print("Opción no válida, intenta de nuevo.")

if __name__ == "__main__":
    main()
