import requests

def test_product_catalog_api():
    response = requests.get("https://demo.opencart.com/index.php?route=api/product")
    assert response.status_code == 200
    data = response.json()
    assert "products" in data
