from brownie import network, config, accounts, MockV3Aggregator # type: ignore
from web3 import Web3 # type: ignore

LOCAL_BLOCKCHAIN_ENVIRONMENTS = ["development", "ganache-local"]

DECIMALS = 18
STARTING_PRICE = 2000
def get_account():
    if network.show_active() == "development":
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["from_key"])

def deploy_mocks():
        print(f"active network = {network.show_active()}")
        print(f"Deploying mock...")
        if len(MockV3Aggregator) <= 0:
            MockV3Aggregator.deploy(
                DECIMALS, Web3.to_wei(STARTING_PRICE, "ether"), {"from": get_account()})
        print("Mock deployed")