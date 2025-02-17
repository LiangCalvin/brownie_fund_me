from brownie import network, config, accounts, FundMe, MockV3Aggregator # type: ignore
from scripts.helpful_scripts import get_account, deploy_mocks
from dotenv import load_dotenv # type: ignore
import os
from web3 import Web3 # type: ignore

load_dotenv()

def deploy_fund_me():
    try:
        account = get_account()
        if network.show_active() != "development":
            price_feed_address = config["networks"][network.show_active()][
                "eth_usd_price_feed"
                ]
        else:
            deploy_mocks()
            price_feed_address = MockV3Aggregator[-1].address

        fund_me = FundMe.deploy(
            price_feed_address,
            {"from": account, "gas_price": Web3.to_wei(30, "gwei"), "gas_limit": 5000000}, 
            publish_source=config["networks"][network.show_active()].get("verify"))
        print(f"Contract deployed to {fund_me.address}")
    except Exception as e:
        print(f"Error during deployment: {str(e)}")
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
