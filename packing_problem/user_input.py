def select_products(containers, products):
    _show_data(containers, products)

    print("\nSeleccione productos indicando el número y la cantidad que desea.\n")

    selected_products = {}
    while True:
        try:
            product_idx = int(input("\033[34m*  ¿Qué producto quiere? (número): \033[0m").strip())
            if product_idx < 1 or product_idx > len(products):
                print("\033[33m-  Índice fuera de rango. Intente de nuevo.\033[0m")
                continue

            quantity = int(input(f"\033[35m+  ¿Cuántas unidades de \033[0m{products[product_idx - 1].name}\033[35m necesita?: \033[0m").strip())
            if quantity <= 0:
                print("\033[33m-  La cantidad debe ser mayor que 0. Intente de nuevo.\033[0m")
                continue

            selected_product = products[product_idx - 1]

            if selected_product in selected_products:
                selected_products[selected_product] += quantity
            else:
                selected_products[selected_product] = quantity
        except ValueError:
            print("\033[33m-  Entrada inválida. Por favor, introduzca números válidos.\033[0m")
            continue

        while True:
            add_another = input("¿Agregar otro producto? (y/n) [y]: ").strip().lower()
            if add_another == '':
                add_another = 'y'

            if add_another in ['y', 'n']:
                break
            else:
                print("\033[33m-  Entrada inválida. Por favor, responda con 'y' o 'n'.\033[0m")

        if add_another == 'n':
            break

    selected_products = sorted(
        [
            (product, quantity, product.determinate_total_volume(quantity))
            for product, quantity in selected_products.items()
        ],
        key=lambda sp: sp[-1],
        reverse=True
    )

    print("\033[32m\n===Productos seleccionados===\n\033[0m")

    for product, quantity, total_volume in selected_products:
        print(f"{quantity} x {product.name} (Volumen total: {total_volume})")

    products_total_volume = sum(total_volume for _, _, total_volume in selected_products)
    print(f"\033[35m\nVolumen total de todos los productos: {products_total_volume}\033[0m")

    return selected_products

def _show_data(containers, products):
    print("\033[32m==== Cajas disponibles ====\n\033[0m")
    for _, container in enumerate(containers):
        print(
            f"{container.name} (Dimensiones: {container.large}x{container.width}x{container.height}, "
            f"Volumen: {container.volume})")

    print("\033[32m\n==== Productos disponibles ====\n\033[0m")
    for idx, product in enumerate(products, start=1):
        print(f"{idx}. {product.name} (Dimensiones: {product.large}x{product.width}x{product.height}, "
              f"Volumen: {product.volume})")
