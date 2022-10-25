from web3.middleware import geth_poa_middleware
from web3 import Web3
import json

def getWeb3Client():
    networkRpc = "https://testnet.telos.net/evm"
    web3Client = Web3(Web3.HTTPProvider(networkRpc))
    web3Client.middleware_onion.inject(geth_poa_middleware, layer=0)
    return web3Client

def getConfig():
    with open("config.json") as configFile:
        config = json.load(configFile)
        configFile.close()   
    return config

getWeb3Client()