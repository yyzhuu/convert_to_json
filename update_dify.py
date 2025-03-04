from neo4j import GraphDatabase
import requests
import time
import schedule

# Neo4j connection details
uri = "neo4j+s://<your_database_id>.databases.neo4j.io"
username = "<your_username>"
password = "<your_password>"

# Dify API details
dify_api_url = "https://api.dify.ai/v1"  # Replace with the actual Dify API endpoint
dify_api_key = "app-zxIfu7c1XtYaoNzn45025usQ"  # Replace with your Dify API key

# Initialize Neo4j driver
driver = GraphDatabase.driver(uri, auth=(username, password))

# Fetch updated data from Neo4j
def fetch_updated_data(last_sync_time):
    with driver.session() as session:
        query = f"""
        MATCH (p:Product)
        WHERE p.last_modified > '{last_sync_time}'
        RETURN p.name AS name, p.overview AS overview, p.features AS features, p.last_modified AS last_modified
        """
        result = session.run(query)
        data = []
        for record in result:
            data.append({
                "name": record["name"],
                "overview": record["overview"],
                "features": record["features"],
                "last_modified": record["last_modified"]
            })
        return data

# Upload updated data to Dify
def upload_to_dify(data):
    headers = {
        "Authorization": f"Bearer {dify_api_key}",
        "Content-Type": "application/json"
    }
    response = requests.post(dify_api_url, headers=headers, json=data)
    if response.status_code == 200:
        print("Data uploaded successfully!")
    else:
        print(f"Failed to upload data: {response.status_code}, {response.text}")

# Sync function that will be called periodically
def sync_data():
    # Track the last sync time, for example, in a file or database
    last_sync_time = "2025-02-25T12:00:00"  # Example of the last sync timestamp
    
    # Fetch updated data from Neo4j
    updated_data = fetch_updated_data(last_sync_time)
    
    # Update Dify with the fetched data
    upload_to_dify(updated_data)
    
    # Update the last sync timestamp (you should store the actual latest timestamp)
    if updated_data:
        last_sync_time = updated_data[-1]['last_modified']  # Update the last sync time to the most recent record

# Schedule the sync to run every 5 minutes
schedule.every(5).minutes.do(sync_data)

# Run the scheduler in an infinite loop
while True:
    schedule.run_pending()
    time.sleep(1)
