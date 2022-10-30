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
        activePoolContract = w3.eth.contract(address=contracts["activePool"], abi=abis.ActivePool())
        
        tx = activePoolContract.functions.setAddresses(
            contracts["borrowerOperations"], 
            contracts["troveManager"],
            contracts["stabilityPool"],
            contracts["defaultPool"],
            contracts["communityIssuance"],
            contracts["borrowerRewards"],
            contracts["devAddress"]
            ).buildTransaction({
                "gasPrice": w3.eth.gas_price,
                'from': PUBLIC_KEY, 
                'nonce': w3.eth.getTransactionCount(PUBLIC_KEY)
                })
        
        signed_tx = w3.eth.account.signTransaction(tx, PRIVATE_KEY)
        tx_hash = w3.eth.sendRawTransaction(signed_tx.rawTransaction)
        print("activePool Complete : tx_hash", w3.toHex(tx_hash))
        return w3.toHex(tx_hash)
    except:
        print("Set activePool Failed")


def setBorrowerOperations():
    try:
        borrowerOperationsContract = w3.eth.contract(address=contracts["borrowerOperations"], abi=abis.BorrowerOperations())
        
        tx = borrowerOperationsContract.functions.setAddresses(
            contracts["troveManager"], 
            contracts["activePool"],
            contracts["defaultPool"],
            contracts["stabilityPool"],
            contracts["gasPool"],   
            contracts["collSurplusPool"], 
            contracts["priceFeed"],
            contracts["sortedTroves"],
            contracts["lusdToken"],
            contracts["lqtyStaking"],
            contracts["borrowerAccountingToken"],
            contracts["borrowerRewards"]
            ).buildTransaction({
                "gasPrice": w3.eth.gas_price,
                'from': PUBLIC_KEY, 
                'nonce': w3.eth.getTransactionCount(PUBLIC_KEY)
                })
        
        signed_tx = w3.eth.account.signTransaction(tx, PRIVATE_KEY)
        tx_hash = w3.eth.sendRawTransaction(signed_tx.rawTransaction)
        print("borrowerOperations Complete : tx_hash", w3.toHex(tx_hash))
        return w3.toHex(tx_hash)
    except:
        print("Set Borrower Operations Failed")


def setTroveManager():
    try:
        troveManagerContract = w3.eth.contract(address=contracts["troveManager"], abi=abis.TroveManager())
        
        tx = troveManagerContract.functions.setAddresses(
            contracts["borrowerOperations"], 
            contracts["activePool"],
            contracts["defaultPool"],
            contracts["stabilityPool"],
            contracts["gasPool"],   
            contracts["collSurplusPool"], 
            contracts["priceFeed"],
            contracts["lusdToken"],
            contracts["sortedTroves"],
            contracts["lqtyToken"],
            contracts["lqtyStaking"],
            ).buildTransaction({
                "gasPrice": w3.eth.gas_price,
                'from': PUBLIC_KEY, 
                'nonce': w3.eth.getTransactionCount(PUBLIC_KEY)
                })
        
        signed_tx = w3.eth.account.signTransaction(tx, PRIVATE_KEY)
        tx_hash = w3.eth.sendRawTransaction(signed_tx.rawTransaction)
        print("troveManager Complete : tx_hash", w3.toHex(tx_hash))
    except:
        print("Set Trove Manager Failed")


def setStabilityPool():
    try:
        stabilityPoolContract = w3.eth.contract(address=contracts["stabilityPool"], abi=abis.StabilityPool())
        
        tx = stabilityPoolContract.functions.setAddresses(
            contracts["borrowerOperations"], 
            contracts["troveManager"],
            contracts["activePool"],
            contracts["lusdToken"],
            contracts["sortedTroves"],
            contracts["priceFeed"],
            contracts["communityIssuance"],
            ).buildTransaction({
                "gasPrice": w3.eth.gas_price,
                'from': PUBLIC_KEY, 
                'nonce': w3.eth.getTransactionCount(PUBLIC_KEY)
                })
        
        signed_tx = w3.eth.account.signTransaction(tx, PRIVATE_KEY)
        tx_hash = w3.eth.sendRawTransaction(signed_tx.rawTransaction)
        print("stabilityPool Complete : tx_hash", w3.toHex(tx_hash))
        return w3.toHex(tx_hash)
    except:
        print("Set Stability Pool Failed")


def setDefaultPool():
    try:
        defaultPoolContract = w3.eth.contract(address=contracts["defaultPool"], abi=abis.DefaultPool())
        
        tx = defaultPoolContract.functions.setAddresses(
            contracts["troveManager"],
            contracts["activePool"],
            ).buildTransaction({
                "gasPrice": w3.eth.gas_price,
                'from': PUBLIC_KEY, 
                'nonce': w3.eth.getTransactionCount(PUBLIC_KEY)
                })
        
        signed_tx = w3.eth.account.signTransaction(tx, PRIVATE_KEY)
        tx_hash = w3.eth.sendRawTransaction(signed_tx.rawTransaction)
        print("defaultPool Complete : tx_hash", w3.toHex(tx_hash))
        return w3.toHex(tx_hash)
    except:
        print("Set Default Pool Failed")


def setCollSurplusPool():
    try:
        collSurplusPoolContract = w3.eth.contract(address=contracts["collSurplusPool"], abi=abis.CollSurplusPool())
        
        tx = collSurplusPoolContract.functions.setAddresses(
            contracts["borrowerOperations"], 
            contracts["troveManager"],
            contracts["activePool"],
            ).buildTransaction({
                "gasPrice": w3.eth.gas_price,
                'from': PUBLIC_KEY, 
                'nonce': w3.eth.getTransactionCount(PUBLIC_KEY)
                })
        
        signed_tx = w3.eth.account.signTransaction(tx, PRIVATE_KEY)
        tx_hash = w3.eth.sendRawTransaction(signed_tx.rawTransaction)
        print("collSurplusPool Complete : tx_hash", w3.toHex(tx_hash))
        return w3.toHex(tx_hash)
    except:
        print("Set collSurplusPool Failed")


def setHintHelpers():
    try:
        hintHelpersContract = w3.eth.contract(address=contracts["hintHelpers"], abi=abis.HintHelpers())
        
        tx = hintHelpersContract.functions.setAddresses(
            contracts["sortedTroves"],
            contracts["troveManager"],
            ).buildTransaction({
                "gasPrice": w3.eth.gas_price,
                'from': PUBLIC_KEY, 
                'nonce': w3.eth.getTransactionCount(PUBLIC_KEY)
                
                })
        
        signed_tx = w3.eth.account.signTransaction(tx, PRIVATE_KEY)
        tx_hash = w3.eth.sendRawTransaction(signed_tx.rawTransaction)
        print("hintHelpers Complete : tx_hash", w3.toHex(tx_hash))
        return w3.toHex(tx_hash)
    except:
        print("Set hintHelpers Failed")


def setLQTYStaking():
    try:      
        lqtyStakingContract = w3.eth.contract(address=contracts["lqtyStaking"], abi=abis.LQTYStaking())
        
        tx = lqtyStakingContract.functions.setAddresses(
            contracts["lqtyToken"],
            contracts["lusdToken"], 
            contracts["troveManager"],
            contracts["borrowerOperations"],
            contracts["activePool"],
            ).buildTransaction({
                "gasPrice": w3.eth.gas_price,
                'from': PUBLIC_KEY, 
                'nonce': w3.eth.getTransactionCount(PUBLIC_KEY)
                })
        
        signed_tx = w3.eth.account.signTransaction(tx, PRIVATE_KEY)
        tx_hash = w3.eth.sendRawTransaction(signed_tx.rawTransaction)
        print("lqtyStaking Complete : tx_hash", w3.toHex(tx_hash))
        return w3.toHex(tx_hash)
    except:
        print("Set lqtyStaking Failed")


def setCommunityIssuance():
    try:
        communityIssuanceContract = w3.eth.contract(address=contracts["communityIssuance"], abi=abis.CommunityIssuance())
        
        tx = communityIssuanceContract.functions.setAddresses(
            contracts["stlosToken"],
            contracts["stabilityPool"], 
            ).buildTransaction({
                "gasPrice": w3.eth.gas_price,
                'from': PUBLIC_KEY, 
                'nonce': w3.eth.getTransactionCount(PUBLIC_KEY)
                })
        
        signed_tx = w3.eth.account.signTransaction(tx, PRIVATE_KEY)
        tx_hash = w3.eth.sendRawTransaction(signed_tx.rawTransaction)
        print("communityIssuance Complete : tx_hash", w3.toHex(tx_hash))
        return w3.toHex(tx_hash)
    except:
        print("Set Community Issuance Failed")
        
def setBorrowerRewards():
    try:
        communityIssuanceContract = w3.eth.contract(address=contracts["borrowerRewards"], abi=abis.BorrowerRewards())
        
        tx = communityIssuanceContract.functions.setAddresses(
            contracts["borrowerAccountingToken"],
            contracts["stlosToken"], 
            contracts["troveManager"],
            contracts["borrowerOperations"],
            contracts["activePool"],
            ).buildTransaction({
                "gasPrice": w3.eth.gas_price,
                'from': PUBLIC_KEY, 
                'nonce': w3.eth.getTransactionCount(PUBLIC_KEY)
                })
        
        signed_tx = w3.eth.account.signTransaction(tx, PRIVATE_KEY)
        tx_hash = w3.eth.sendRawTransaction(signed_tx.rawTransaction)
        print("borrowerRewards Complete : tx_hash", w3.toHex(tx_hash))
        return w3.toHex(tx_hash)
    except:
        print("Set borrowerRewards Failed")


def SetBorrowerAccountingToken():
    try:
        borrowerAccountingTokenContract = w3.eth.contract(address=contracts["borrowerAccountingToken"], abi=abis.BorrowerAccountingToken())
        
        tx = borrowerAccountingTokenContract.functions.transferOwnership(
            contracts["borrowerOperations"],

            ).buildTransaction({
                "gasPrice": w3.eth.gas_price,
                'from': PUBLIC_KEY, 
                'nonce': w3.eth.getTransactionCount(PUBLIC_KEY)
                })
        
        signed_tx = w3.eth.account.signTransaction(tx, PRIVATE_KEY)
        tx_hash = w3.eth.sendRawTransaction(signed_tx.rawTransaction)
        print("borrowerAccountingToken Complete : tx_hash", w3.toHex(tx_hash))
        return w3.toHex(tx_hash)
    except:
        print("Set borrowerAccountingToken Failed")
        

def SetSortedTroves():
    try:
        sortedTrovesContract = w3.eth.contract(address=contracts["sortedTroves"], abi=abis.SortedTroves())
        
        tx = sortedTrovesContract.functions.setParams(  
            1000000,
            contracts["troveManager"],
            contracts["borrowerOperations"],

            ).buildTransaction({
                "gasPrice": w3.eth.gas_price,
                'from': PUBLIC_KEY, 
                'nonce': w3.eth.getTransactionCount(PUBLIC_KEY)
                })
        
        signed_tx = w3.eth.account.signTransaction(tx, PRIVATE_KEY)
        tx_hash = w3.eth.sendRawTransaction(signed_tx.rawTransaction)
        print("sortedTroves Complete : tx_hash", w3.toHex(tx_hash))
        return w3.toHex(tx_hash)
    except:
        print("Set sortedTroves Failed")
    
    
def setAllContracts():
    setActivePool()
    setBorrowerOperations()
    setTroveManager()
    setStabilityPool()
    setDefaultPool()
    setCollSurplusPool()
    setHintHelpers()
    setCommunityIssuance()
    setBorrowerRewards()
    setLQTYStaking()
    SetBorrowerAccountingToken()
    SetSortedTroves()
setAllContracts()