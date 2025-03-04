from neo4j import GraphDatabase
import time

# Connect to Neo4j Aura database
uri = "neo4j+s://7572f1b9.databases.neo4j.io"
username = "neo4j"
password = "7Bv-NQUOzvs_HFUpfoilpwdLBuICIP_joqkl7O7RxFY"

driver = GraphDatabase.driver(uri, auth=(username, password))

# Fetch updated product data from Neo4j
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

# Example usage
if __name__ == "__main__":
    # Set the initial sync timestamp, could be dynamically updated
    last_sync_time = "2025-02-25T12:00:00"  # Replace with your actual last sync time

    updated_data = fetch_updated_data(last_sync_time)
    if updated_data:
        print("Fetched updated products:")
        for product in updated_data:
            print(product)
    else:
        print("No updates found.")
