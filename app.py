from azure.identity import DefaultAzureCredential
from azure.keyvault.secrets import SecretClient

from flask import Flask
import os

app = Flask(__name__)
# added to get value from app setting configuration

app.debug = True

# To retieve secret from secret url

# Set your Key Vault URI
key_vault_uri = "https://testkeyvault7hills.vault.azure.net"

# Authenticate using DefaultAzureCredential
credential = DefaultAzureCredential()

# Create a SecretClient
client = SecretClient(vault_url=key_vault_uri, credential=credential)

# Retrieve a secret
secret_name = "myname"
retrieved_secret = client.get_secret(secret_name)

# Access the secret value
print(retrieved_secret.value)

### end of secret 



@app.route("/home")
def home1():
    data = [os.getenv('Environment_Name')]
    configvalue=data[0]
    return "<h2>Hello!</h2> <p>Environment name : " +configvalue+"</p>"

@app.route("/secret")
def secretval():
    myname = [os.getenv('MyName')]
    secretvalue=myname[0]
    return "<h2>Hello Secret Name</h2> <p>Secret Name : " +retrieved_secret.value+"</p>"


@app.route("/")
def index():

    return "<h2>Hello!</h2> <p> Azure app settings configurations</p>"
    


if __name__ == '__main__':
    app.run()
