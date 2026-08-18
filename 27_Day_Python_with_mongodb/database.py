from flask import Flask, render_template
import os # importing operating system module
MONGODB_URI = 'mongodb+srv://hamzasskour123_db_user:tKm4O7j1UJeN1JMQ@hcluster.8yvzizf.mongodb.net/?appName=HCluster'
client = pymongo.MongoClient(MONGODB_URI)
print(client.list_database_names())

app = Flask(__name__)
if __name__ == '__main__':
    # for deployment we use the environ
    # to make it work for both production and development
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)


