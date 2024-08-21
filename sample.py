from azure.identity import ManagedIdentityCredential
from azure.keyvault.secrets import SecretClient

# Replace with your Key Vault URL
VAULT_URL = "https://testkeyvault7hills.vault.azure.net/"

# Create a ManagedIdentityCredential instance
credential = ManagedIdentityCredential()

# Create a SecretClient instance
client = SecretClient(vault_url=VAULT_URL, credential=credential)

# Retrieve the secret
secret_name = "myname"
retrieved_secret = client.get_secret(secret_name)

print(f"Secret Value: {retrieved_secret.value}")
