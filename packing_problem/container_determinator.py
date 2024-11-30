from collections import Counter
from itertools import combinations_with_replacement

def determinate_containers(selected_products, containers):
    # Calculate the total volume of the selected products.
    products_total_volume = sum(total_volume for _, _, total_volume in selected_products)

    # Early return when all the products fit in one container.
    if fitting_container := _find_fitting_container(products_total_volume, containers):
        _show_individual_container(fitting_container)
        return [fitting_container]

    # The best 3 options of containers
    possible_containers = []

    # Number of elements per combination.
    r = 2

    # Possible combinations of containers.
    while len(possible_containers) < 5:
        combinations = [
            (combination, sum(container.volume for container in combination))
            for combination in combinations_with_replacement(containers, r)
        ]

        for combination in sorted(combinations, key=lambda c: c[-1]):
            if combination[-1] >= products_total_volume:
                possible_containers.append(combination)

                if len(possible_containers) >= 3:
                    break

        # Security validation to avoid infinity loops.
        if r > len(containers) * 5:
            raise ValueError("No se encontraron suficientes combinaciones adecuadas.")

        r += 1

    possible_containers = sorted(possible_containers, key=lambda container: container[-1])

    _show_possible_containers(possible_containers)

    return possible_containers

def _find_fitting_container(products_total_volume, containers):
    for container in containers:
        if container.can_package_products(products_total_volume):
            return container
    return None

def _show_individual_container(container):
    print("\033[32m\n=== El mejor resultado ===\n\033[0m")
    print(f"{container.name} (Volumen Total: {container.volume}):")

def _show_possible_containers(possible_containers):
    print("\033[32m\n=== Mejores opcines ===\n\033[0m")

    for combination, count in Counter(tuple(combo for combo, _ in possible_containers)).items():
        total_volume = sum(container.volume for container in combination)
        container_names = ", ".join(container.name for container in combination)
        print(f"Combinación: [{container_names}] -> Volumen total: {total_volume} -> Cantidad: {count}")
