import serpent
from ethereum.tools import tester
from ethereum import abi
serpent_code = '''
def triple(a):
    return(a*3)
    
def multiply(a, b):
    return(a*b)
'''

s = tester.Chain()
x = s.contract(serpent_code, language='serpent')
translator = abi.ContractTranslator(serpent.mk_full_signature(serpent_code))
data = translator.encode('triple', [20])
result = translator.decode('triple', s.tx(tester.k0, x.address, 0, data))
print(result)
data = translator.encode('multiply', [20, 4])
result = translator.decode('triple', s.tx(tester.k0, x.address, 0, data))
print(result)
