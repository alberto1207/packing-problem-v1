import os
import pandas as pd

from container import Container
from product import Product


def get_data():
    containers_path, products_path = _get_file_paths()

    return (sorted(_create_instance(Container, containers_path), key=lambda c: c.volume),
            _create_instance(Product, products_path))

def _get_file_paths():
    # Determinate the project base route.
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    # Build and return absolute routes for the files.
    return (os.path.join(base_dir, "data", "containers.xlsx"),
            os.path.join(base_dir, "data", "products.xlsx"))

def _create_instance(box_class, path):
    return [
        box_class(
            name=row['nombre'],
            large=row['largo'],
            width=row['ancho'],
            height=row['altura']
        )
        for row in pd.read_excel(path).to_dict(orient='records')
    ]
