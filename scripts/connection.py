from web3 import Web3
import os
from dotenv import load_dotenv

load_dotenv()

# Get the Alchemy API URL from environment variable
alchemy_url = f"https://eth-sepolia.g.alchemy.com/v2/{os.getenv('ALCHEMY_API_KEY')}"

# Connect to Alchemy via Web3
web3 = Web3(Web3.HTTPProvider(alchemy_url))

if web3.isConnected():
    print("Alchemy connection successful!")
else:
    print("Failed to connect to Alchemy.")
