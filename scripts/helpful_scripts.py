from brownie import network, config, accounts, MockV3Aggregator
from web3 import Web3

LOCAL_BLOCKCHAIN_ENVIRONMENTS = ["development", "ganache-local"]
FORKED_LOCAL_ENVIRONMENTS = ["mainnet-fork"]

DECIMALS = 8
STARTING_PRICE = 200000000000

def get_account():
    if network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS or network.show_active() in FORKED_LOCAL_ENVIRONMENTS:
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["from_key"])

def deploy_mocks():
        print(f"active network = {network.show_active()}")
        print(f"Deploying Mock...")
        if len(MockV3Aggregator) <= 0:
            MockV3Aggregator.deploy(
                DECIMALS,STARTING_PRICE, {"from": get_account(),"gas_price": Web3.to_wei(10, "gwei"), "gas_limit": 3000000})
        print("Mock Deployed!")