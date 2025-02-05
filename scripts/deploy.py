from brownie import network, config, accounts, FundMe, MockV3Aggregator
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

        if network.show_active() != "development":
            price_feed_address = config["network"][network.show_active()][
                "eth_usd_price_feed"
                ]
        else:
            print(f"active network = {network.show_active()}")
            print(f"Deploying mock...")
            mock_aggregator = MockV3Aggregator.deploy(18,2000000000000000000000, {"from": account})
            price_feed_address = mock_aggregator.address
            print("Mock deployed")
            
        #pass pricefeed address to our fundme contract        
        fund_me = FundMe.deploy(
            price_feed_address,
            {"from": account}, publish_source=config["networks"][network.show_active()].get("verify"))
        print(f"Contract deployed to {fund_me.address}")
    except Exception as e:
        print(f"Error during deployment: {str(e)}")
def main():
    # try:
    #     deploy_fund_me()
    # except Exception as e:
    #     print(f"An error occurred: {str(e)}")
        deploy_fund_me()
