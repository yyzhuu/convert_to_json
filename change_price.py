import json

# Define the JSON structure
product_data = {
    "StoreID": 1,
    "CountryID": 65,
    "MasterProductID": 23272,
    "MasterProductName": "Creative SXFI AMP",
    "IsSingleProduct": True,
    "IsComingSoon": False,
    "SelectedID": 23322,
    "SelectedFreeItem": None,
    "Products": [
        {
            "ProductID": 23322,
            "ProductName": "Creative SXFI AMP",
            "InStock": True,
            "FreeShipping": True,
            "ShippingCost": "$0.00",
            "Available": "In Stock",
            "Message": None,
            "FreeItems": [],
            "IsComingSoon": False,
            "MinQrdQtyList": [],
            "Price": 99.99,  # Your new price
            "PriceFormat": "$99.99",
            "ListPrice": 219.00,
            "ListPriceFormat": "$219.00",
            "MemberPrice": 0,
            "MemberPriceFormat": None,
            "TradeIn": False
        }
    ],
    "ProductAttributes": [],
    "NewMasterProductID": 0,
    "BundleContent": None,
    "Gallery": [],
    "Favourited": False,
    "Description": "",
    "Image": "//d287ku8w5owj51.cloudfront.net/images/products/large/pdt_23272.png?width=450&height=350",
    "FriendlyURL": "/p/amplifiers/creative-sxfi-amp",
    "FriendlyBuyURL": "/p/amplifiers/creative-sxfi-amp/buy"
}

# Save JSON file to the current directory ("./")
file_path = "./product_data.json"

with open(file_path, "w") as file:
    json.dump(product_data, file, indent=4)

print(f"JSON file created at: {file_path}")

