from brownie import network, config, accounts, FundMe
from scripts.helpful_scripts import get_account
from dotenv import load_dotenv
import os

load_dotenv()

# Print out the token to verify
print(f"ETHERSCAN_TOKEN: {os.getenv('ETHERSCAN_TOKEN')}")

def deploy_fund_me():
    try:
        account = get_account()
        print(f"Deploying from account: {account}")
        fund_me = FundMe.deploy({"from": account}, publish_source=True)
        print(f"Contract deployed to {fund_me.address}")
    except Exception as e:
        print(f"Error during deployment: {str(e)}")
def main():
    # try:
    #     deploy_fund_me()
    # except Exception as e:
    #     print(f"An error occurred: {str(e)}")
        deploy_fund_me()
