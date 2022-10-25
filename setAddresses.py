import helper 
from dotenv import load_dotenv
import os    
import abis

contracts = helper.getConfig()
w3 = helper.getWeb3Client()

load_dotenv()
PRIVATE_KEY = os.getenv('PRIVATE_KEY')
PUBLIC_KEY = w3.toChecksumAddress(os.getenv('PUBLIC_KEY'))

def setActivePool():
    try:
        ActivePoolContract = w3.eth.contract(address=contracts["ActivePool"], abi=abis.ActivePool())
        
        tx = ActivePoolContract.functions.setAddresses(
            contracts["BorrowerOperations"], 
            contracts["TroveManager"],
            contracts["StabilityPool"],
            contracts["DefaultPool"],
            contracts["CommunityIssuance"],
            contracts["BorrowerRewards"],
            contracts["DevAddress"]
            ).buildTransaction({
                "gasPrice": w3.eth.gas_price,
                'from': PUBLIC_KEY, 
                'nonce': w3.eth.getTransactionCount(PUBLIC_KEY)
                })
        
        signed_tx = w3.eth.account.signTransaction(tx, PRIVATE_KEY)
        tx_hash = w3.eth.sendRawTransaction(signed_tx.rawTransaction)
        print("ActivePool Complete : tx_hash", w3.toHex(tx_hash))
        return w3.toHex(tx_hash)
    except:
        print("Set ActivePool Failed")


def setBorrowerOperations():
    try:
        BorrowerOperationsContract = w3.eth.contract(address=contracts["BorrowerOperations"], abi=abis.BorrowerOperations())
        
        tx = BorrowerOperationsContract.functions.setAddresses(
            contracts["TroveManager"], 
            contracts["ActivePool"],
            contracts["DefaultPool"],
            contracts["StabilityPool"],
            contracts["GasPool"],   
            contracts["CollSurplusPool"], 
            contracts["PriceFeedTestnet"],
            contracts["SortedTroves"],
            contracts["LUSDToken"],
            contracts["LQTYStaking"],
            contracts["BorrowerAccountingToken"],
            contracts["BorrowerRewards"]
            ).buildTransaction({
                "gasPrice": w3.eth.gas_price,
                'from': PUBLIC_KEY, 
                'nonce': w3.eth.getTransactionCount(PUBLIC_KEY)
                })
        
        signed_tx = w3.eth.account.signTransaction(tx, PRIVATE_KEY)
        tx_hash = w3.eth.sendRawTransaction(signed_tx.rawTransaction)
        print("BorrowerOperations Complete : tx_hash", w3.toHex(tx_hash))
        return w3.toHex(tx_hash)
    except:
        print("Set Borrower Operations Failed")


def setTroveManager():
    try:
        TroveManagerContract = w3.eth.contract(address=contracts["TroveManager"], abi=abis.TroveManager())
        
        tx = TroveManagerContract.functions.setAddresses(
            contracts["BorrowerOperations"], 
            contracts["ActivePool"],
            contracts["DefaultPool"],
            contracts["StabilityPool"],
            contracts["GasPool"],   
            contracts["CollSurplusPool"], 
            contracts["PriceFeedTestnet"],
            contracts["LUSDToken"],
            contracts["SortedTroves"],
            contracts["LQTYToken"],
            contracts["LQTYStaking"],
            ).buildTransaction({
                "gasPrice": w3.eth.gas_price,
                'from': PUBLIC_KEY, 
                'nonce': w3.eth.getTransactionCount(PUBLIC_KEY)
                })
        
        signed_tx = w3.eth.account.signTransaction(tx, PRIVATE_KEY)
        tx_hash = w3.eth.sendRawTransaction(signed_tx.rawTransaction)
        print("TroveManager Complete : tx_hash", w3.toHex(tx_hash))
    except:
        print("Set Trove Manager Failed")


def setStabilityPool():
    try:
        StabilityPoolContract = w3.eth.contract(address=contracts["StabilityPool"], abi=abis.StabilityPool())
        
        tx = StabilityPoolContract.functions.setAddresses(
            contracts["BorrowerOperations"], 
            contracts["TroveManager"],
            contracts["ActivePool"],
            contracts["LUSDToken"],
            contracts["SortedTroves"],
            contracts["PriceFeedTestnet"],
            contracts["CommunityIssuance"],
            ).buildTransaction({
                "gasPrice": w3.eth.gas_price,
                'from': PUBLIC_KEY, 
                'nonce': w3.eth.getTransactionCount(PUBLIC_KEY)
                })
        
        signed_tx = w3.eth.account.signTransaction(tx, PRIVATE_KEY)
        tx_hash = w3.eth.sendRawTransaction(signed_tx.rawTransaction)
        print("StabilityPool Complete : tx_hash", w3.toHex(tx_hash))
        return w3.toHex(tx_hash)
    except:
        print("Set Stability Pool Failed")


def setDefaultPool():
    try:
        DefaultPoolContract = w3.eth.contract(address=contracts["DefaultPool"], abi=abis.DefaultPool())
        
        tx = DefaultPoolContract.functions.setAddresses(
            contracts["TroveManager"],
            contracts["ActivePool"],
            ).buildTransaction({
                "gasPrice": w3.eth.gas_price,
                'from': PUBLIC_KEY, 
                'nonce': w3.eth.getTransactionCount(PUBLIC_KEY)
                })
        
        signed_tx = w3.eth.account.signTransaction(tx, PRIVATE_KEY)
        tx_hash = w3.eth.sendRawTransaction(signed_tx.rawTransaction)
        print("DefaultPool Complete : tx_hash", w3.toHex(tx_hash))
        return w3.toHex(tx_hash)
    except:
        print("Set Default Pool Failed")


def setCollSurplusPool():
    try:
        CollSurplusPoolContract = w3.eth.contract(address=contracts["CollSurplusPool"], abi=abis.CollSurplusPool())
        
        tx = CollSurplusPoolContract.functions.setAddresses(
            contracts["BorrowerOperations"], 
            contracts["TroveManager"],
            contracts["ActivePool"],
            ).buildTransaction({
                "gasPrice": w3.eth.gas_price,
                'from': PUBLIC_KEY, 
                'nonce': w3.eth.getTransactionCount(PUBLIC_KEY)
                })
        
        signed_tx = w3.eth.account.signTransaction(tx, PRIVATE_KEY)
        tx_hash = w3.eth.sendRawTransaction(signed_tx.rawTransaction)
        print("CollSurplusPool Complete : tx_hash", w3.toHex(tx_hash))
        return w3.toHex(tx_hash)
    except:
        print("Set CollSurplusPool Failed")


def setHintHelpers():
    try:
        HintHelpersContract = w3.eth.contract(address=contracts["HintHelpers"], abi=abis.HintHelpers())
        
        tx = HintHelpersContract.functions.setAddresses(
            contracts["SortedTroves"],
            contracts["TroveManager"],
            ).buildTransaction({
                "gasPrice": w3.eth.gas_price,
                'from': PUBLIC_KEY, 
                'nonce': w3.eth.getTransactionCount(PUBLIC_KEY)
                
                })
        
        signed_tx = w3.eth.account.signTransaction(tx, PRIVATE_KEY)
        tx_hash = w3.eth.sendRawTransaction(signed_tx.rawTransaction)
        print("HintHelpers Complete : tx_hash", w3.toHex(tx_hash))
        return w3.toHex(tx_hash)
    except:
        print("Set HintHelpers Failed")


def setLQTYStaking():
    try:      
        LQTYStakingContract = w3.eth.contract(address=contracts["LQTYStaking"], abi=abis.LQTYStaking())
        
        tx = LQTYStakingContract.functions.setAddresses(
            contracts["LQTYToken"],
            contracts["LUSDToken"], 
            contracts["TroveManager"],
            contracts["BorrowerOperations"],
            contracts["ActivePool"],
            ).buildTransaction({
                "gasPrice": w3.eth.gas_price,
                'from': PUBLIC_KEY, 
                'nonce': w3.eth.getTransactionCount(PUBLIC_KEY)
                })
        
        signed_tx = w3.eth.account.signTransaction(tx, PRIVATE_KEY)
        tx_hash = w3.eth.sendRawTransaction(signed_tx.rawTransaction)
        print("LQTYStaking Complete : tx_hash", w3.toHex(tx_hash))
        return w3.toHex(tx_hash)
    except:
        print("Set LQTYStaking Failed")


def setCommunityIssuance():
    try:
        CommunityIssuanceContract = w3.eth.contract(address=contracts["CommunityIssuance"], abi=abis.CommunityIssuance())
        
        tx = CommunityIssuanceContract.functions.setAddresses(
            contracts["stlosToken"],
            contracts["StabilityPool"], 
            ).buildTransaction({
                "gasPrice": w3.eth.gas_price,
                'from': PUBLIC_KEY, 
                'nonce': w3.eth.getTransactionCount(PUBLIC_KEY)
                })
        
        signed_tx = w3.eth.account.signTransaction(tx, PRIVATE_KEY)
        tx_hash = w3.eth.sendRawTransaction(signed_tx.rawTransaction)
        print("CommunityIssuance Complete : tx_hash", w3.toHex(tx_hash))
        return w3.toHex(tx_hash)
    except:
        print("Set Community Issuance Failed")
        
def setBorrowerRewards():
    try:
        CommunityIssuanceContract = w3.eth.contract(address=contracts["BorrowerRewards"], abi=abis.BorrowerRewards())
        
        tx = CommunityIssuanceContract.functions.setAddresses(
            contracts["BorrowerAccountingToken"],
            contracts["STLOSToken"], 
            contracts["TroveManager"],
            contracts["BorrowerOperations"],
            contracts["ActivePool"],
            ).buildTransaction({
                "gasPrice": w3.eth.gas_price,
                'from': PUBLIC_KEY, 
                'nonce': w3.eth.getTransactionCount(PUBLIC_KEY)
                })
        
        signed_tx = w3.eth.account.signTransaction(tx, PRIVATE_KEY)
        tx_hash = w3.eth.sendRawTransaction(signed_tx.rawTransaction)
        print("BorrowerRewards Complete : tx_hash", w3.toHex(tx_hash))
        return w3.toHex(tx_hash)
    except:
        print("Set BorrowerRewards Failed")


def setAllContracts():
    setActivePool()
    setBorrowerOperations()
    setTroveManager()
    setStabilityPool()
    setDefaultPool()
    setCollSurplusPool()
    setHintHelpers()
    setLQTYStaking()
    setCommunityIssuance()
    setBorrowerRewards()
setAllContracts()