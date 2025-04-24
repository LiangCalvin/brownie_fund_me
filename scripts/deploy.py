from brownie import network, config, accounts, FundMe, MockV3Aggregator
from scripts.helpful_scripts import get_account, deploy_mocks, LOCAL_BLOCKCHAIN_ENVIRONMENTS
from dotenv import load_dotenv
import os
from web3 import Web3

load_dotenv()

def deploy_fund_me():
    try:
        account = get_account()
        # pass the pricefeed address to our fundme contract

# if we are on a persistent network like rinkeby, use the associated address
        if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
            price_feed_address = config["networks"][network.show_active()][
                "eth_usd_price_feed"
                ]
# otherwise, deploy mocks
        else:
            print(f"The active network is {network.show_active()}")
            print(f"Deploying Mocks...")
            deploy_mocks()
            price_feed_address = MockV3Aggregator[-1].address

        fund_me = FundMe.deploy(
            price_feed_address,
            {"from": account, "gas_price": Web3.to_wei(30, "gwei"), "gas_limit": 5000000}, 
            publish_source=config["networks"][network.show_active()].get("verify"))
        print(f"Contract deployed to {fund_me.address}")
        return fund_me
    except Exception as e:
        print(f"Error during deployment: {str(e)}")
        
def main():
    # try:
    #     deploy_fund_me()
    # except Exception as e:
    #     print(f"An error occurred: {str(e)}")
    deploy_fund_me()
