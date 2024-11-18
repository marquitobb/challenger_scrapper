"""
1. Genera un script en Python que obtenga y de formato a las siguientes
propiedades de un archivo JSON:
    ● allergens
    ● sku
    ● vegan,
    ● kosher,
    ● organic,
    ● vegetarian,
    ● gluten_free,
    ● lactose_free,
    ● package_quantity,
    ● Unit_size,
    ● net_weight

Las propiedades se encuentran en un nodo llamado “custom_attributes”.
Archivo json:
storage.googleapis.com/resources-prod-shelftia/scrapers-prueba/product.json

Salida esperada CSV: https://storage.googleapis.com/resources-prod-shelftia/scrapers-
prueba/output-product.csv
"""


import requests
import json
import pandas as pd

class JSONProcessor:
    def __init__(self, url):
        self.url = url
        self.propierties_values = {}

    def download_json(self):
        response = requests.get(self.url)
        return response.json()

    def extract_custom_attributes(self, data):
        if "allVariants" in data and len(data["allVariants"]) > 0:
            attributesRaw = data["allVariants"][0].get("attributesRaw")
            for item in attributesRaw:
                if item.get("name") == "custom_attributes":
                    self.propierties_values = item.get("value")
                    break
        else:
            print("No existen variantes en el archivo JSON")

    def format_data(self):
        extracted_data = []
        for key, value in self.propierties_values.items():
            data_value = json.loads(value)
            extracted_data.append({
                "allergens": [data_value.get("allergens").get("value")[0].get("name")],
                "sku": int(data_value.get("sku").get("value")),
                "vegan": data_value.get("vegan").get("value"),
                "kosher": data_value.get("kosher").get("value"),
                "organic": data_value.get("organic").get("value"),
                "vegetarian": data_value.get("vegetarian").get("value"),
                "gluten_free": data_value.get("gluten_free").get("value"),
                "lactose_free": data_value.get("lactose_free").get("value"),
                "package_quantity": float(data_value.get("package_quantity").get("value")),
                "Unit_size": float(data_value.get("unit_size").get("value")),
                "net_weight": float(data_value.get("net_weight").get("value"))
            })
        return extracted_data

    def save_to_csv(self, data, output_path):
        attributes_to_extract = [
            "allergens", "sku", "vegan", "kosher", "organic",
            "vegetarian", "gluten_free", "lactose_free",
            "package_quantity", "Unit_size", "net_weight"
        ]
        df = pd.DataFrame(data, columns=attributes_to_extract)
        df.to_csv(output_path, index=False)

if __name__ == "__main__":
    url = "https://storage.googleapis.com/resources-prod-shelftia/scrapers-prueba/product.json"
    output_path = "./output-product.csv"

    processor = JSONProcessor(url)
    data = processor.download_json()
    processor.extract_custom_attributes(data)
    formatted_data = processor.format_data()
    processor.save_to_csv(formatted_data, output_path)