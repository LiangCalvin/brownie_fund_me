# from brownie import network, config, accounts, FundMe
# from scripts.helpful_scripts import get_account

# import requests

# def publish_source(deployed_contract):
#     url = "https://api-sepolia.etherscan.io/api"

#     # Prepare the data for the API request
#     data = {
#         "module": "contract",
#         "action": "verify",
#         "apikey": config["networks"][network.show_active()]["etherscan_token"],
#         "contractAddress": deployed_contract.address,
#         # "sourceCode": deployed_contract.get_sourcecode(),  # This method retrieves the source code
#         "sourceCode": deployed_contract.get_source(),  # Use get_verification_source() for the source code

#         "codeformat": "solidity-single-file",
#         "contractName": deployed_contract.__class__.__name__,  # Use the class name of the contract
#         "constructorArguments": '',  # Update this if you have constructor arguments
#     }

#     # Send the request
#     response = requests.post(url, data=data)

#     # Print the raw response to see what's being returned
#     print("Response from Etherscan:", response.text)

#     # Handle the response
#     try:
#         response.raise_for_status()  # Raise an error for bad responses
#         return response.json()  # Return the JSON response
#     except ValueError:  # Catch JSON decode errors
#         print(f"Error decoding JSON: {response.text}")
#         return None  # Handle the error as needed

# def deploy_fund_me():
#     account = get_account()
#     fund_me = FundMe.deploy({"from": account}, publish_source=False)  # Set to False for manual publishing
#     print(f"Contract deployed to {fund_me.address}")

#     # Now, call the publish_source function
#     try:
#         publish_response = publish_source(fund_me)  # Publish the source code
#         print(f"Publish response: {publish_response}")  # Print the response from the publish
#     except Exception as e:
#         print(f"An error occurred during source publishing: {str(e)}")


# # def deploy_fund_me():
# #     account = get_account()
# #     fund_me = FundMe.deploy({"from": account}, publish_source=True)
# #     print(f"Contract deployed to {fund_me.address}")

# def main():
#     # deploy_fund_me()
#         try:
#             deploy_fund_me()
#         except Exception as e:
#             print(f"An error occurred: {str(e)}")
from brownie import network, config, accounts, FundMe
from scripts.helpful_scripts import get_account
import requests

def publish_source(deployed_contract):
    url = "https://api-sepolia.etherscan.io/api"

    # Set chain ID for Sepolia
    chain_id = 11155111  # Chain ID for Sepolia

    # Prepare the data for the API request
    data = {
        "module": "contract",
        "action": "verifysourcecode",  # Correct action name for verification
        "apikey": config["networks"][network.show_active()]["etherscan_token"],
        "contractaddress": deployed_contract.address,
        "sourceCode": deployed_contract.get_verification_source(),  # Correct method to get the source code
        "contractname": "contracts/FundMe.sol:FundMe",  # Correct format for contract name
        "compilerVersion": "v0.6.6+commit.6c089d02",  # Replace with the correct compiler version
        "codeformat": "solidity-single-file",  # Format for the source code
        "constructorArguments": '',  # Include if your contract uses constructor arguments in ABI encoded format
        "optimizationUsed": 1,  # Set to 1 if optimization was used, otherwise set to 0
        "chainId": chain_id  # Add the chain ID
    }

    # Print the data being sent for better debugging
    print("Request Data:", data)

    # Send the request
    response = requests.post(url, data=data)

    # Print the raw response to see what's being returned
    print("Raw response from Etherscan:", response.text)

    # Handle the response
    try:
        response.raise_for_status()  # Raise an error for bad responses
        return response.json()  # Return the JSON response
    except ValueError:  # Catch JSON decode errors
        print(f"Error decoding JSON: {response.text}")
        return None  # Handle the error as needed


def deploy_fund_me():
    account = get_account()
    fund_me = FundMe.deploy({"from": account}, publish_source=True)  # Set to False for manual publishing
    print(f"Contract deployed to {fund_me.address}")

    # Now, call the publish_source function
    try:
        publish_response = publish_source(fund_me)  # Publish the source code
        print(f"Publish response: {publish_response}")  # Print the response from the publish
    except Exception as e:
        print(f"An error occurred during source publishing: {str(e)}")

def main():
    try:
        deploy_fund_me()
    except Exception as e:
        print(f"An error occurred: {str(e)}")
