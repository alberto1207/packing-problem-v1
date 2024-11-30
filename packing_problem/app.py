from container_determinator import determinate_containers
from data_utils import get_data
from user_input import select_products

if __name__ == '__main__':
    containers, products = get_data()

    selected_products = select_products(containers, products)

    selected_containers = determinate_containers(selected_products, containers)
