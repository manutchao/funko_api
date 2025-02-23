#!/bin/bash
echo "Waiting for MongoDB to start..."
sleep 5

echo "Importing initial Funko Pop data into MongoDB..."
mongoimport --host mongo --db funko_db --collection funkos --file /db/database.json --jsonArray

echo "MongoDB data import complete!"