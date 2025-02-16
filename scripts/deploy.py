from brownie import network, config, accounts, FundMe, MockV3Aggregator # type: ignore
from scripts.helpful_scripts import get_account
from dotenv import load_dotenv # type: ignore
import os
from web3 import Web3 # type: ignore

load_dotenv()

# Print out the token to verify
print(f"ETHERSCAN_TOKEN: {os.getenv('ETHERSCAN_TOKEN')}")

def deploy_fund_me():
    # try:
        account = get_account()
        print(f"Deploying from account: {account}")
        # pass the price feed address to our fundme contract

        # if we are on a persistent network like rinkeby, use the associated address
        # otherwise, deploy mocks
        if network.show_active() != "development":
            price_feed_address = config["networks"][network.show_active()][
                "eth_usd_price_feed"
                ]
        else:
            print(f"The active network is {network.show_active()}")
            print(f"Deploying Mocks...")
            mock_aggregator = MockV3Aggregator.deploy(
                18, 200000000000000000000000, {"from": account}
                )
            price_feed_address = mock_aggregator.address
            print("Mocks Deployed!")

        fund_me = FundMe.deploy(
            price_feed_address,
            {"from": account}, publish_source=config["networks"][network.show_active()].get("verify"))
        print(f"Contract deployed to {fund_me.address}")
        
        # if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        #     price_feed_address = config["networks"][network.show_active()][
        #         "eth_usd_price_feed"
        #         ]
        # else:
        #     deploy_mocks()
        #     price_feed_address = MockV3Aggregator[-1].address
            
        #pass pricefeed address to our fundme contract        
        # fund_me = FundMe.deploy(
        #     price_feed_address,
        #     {"from": account}, publish_source=config["networks"][network.show_active()].get("verify"))
        
    # except Exception as e:
    #     print(f"Error during deployment: {str(e)}")   
        
def main():
    # try:
    #     deploy_fund_me()
    # except Exception as e:
    #     print(f"An error occurred: {str(e)}")
    deploy_fund_me()
