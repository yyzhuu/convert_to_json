import requests
import json
import os

# Fetch the product list
product_list_url = 'https://sg.creative.com/search'
response = requests.get(product_list_url)
product_list = response.json()  # Assuming the response is in JSON format

# Define a function to fetch price using MasterProductID
def fetch_price(product_id):
    price_list_url = f'https://sg.creative.com/productpriceapi/getproductjson/?MasterProductID={product_id}'
    response = requests.get(price_list_url)
    price_data = response.json()
    return price_data

# Initialize a list to hold the results
final_product_data = []

# Iterate through each product and map the product ID to the price
for product in product_list['Products']:  # Assuming 'products' is the key in the JSON response
    product_id = product.get('M')  # Assuming 'm' is the key for product ID
    if product_id:
        price_data = fetch_price(product_id)
        
        # Assuming price data contains 'price' and 'name'
        if 'price' in price_data and 'name' in price_data:
            product_info = {
                'name': price_data['name'],
                'price': price_data['price']
            }
            final_product_data.append(product_info)

# Convert to JSON format
json_data = json.dumps(final_product_data, indent=4)

# Specify the output directory
output_dir = "./"  # Change this to your desired directory path

# Ensure the directory exists, if not, create it
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Define the output file path
output_file = os.path.join(output_dir, "products_data.json")

# Save the JSON data to a file
with open(output_file, "w", encoding='utf-8') as output_f:
    output_f.write(json_data)

# Count the number of products
count = len(final_product_data)

# Print the results
print(f"Data successfully saved to {output_file}")
print("Count: ", count)
