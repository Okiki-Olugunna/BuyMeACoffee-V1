from brownie import BuyMeACoffee, accounts, config


def main():
    account = accounts.add(config["wallets"]["from_key"])

    print("Deploying contract...")
    contract = BuyMeACoffee.deploy({"from": account})
    print(f"Contract deployed to: {contract}")
