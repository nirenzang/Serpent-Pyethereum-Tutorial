import serpent
from ethereum.tools import tester
from ethereum import abi
serpent_code = '''
def multiply(a):
    return(a*3)
'''

s = tester.Chain()
x = s.contract(serpent_code, language='serpent')
translator = abi.ContractTranslator(serpent.mk_full_signature(serpent_code))
data = translator.encode('multiply', [20])
result = translator.decode('multiply', s.tx(tester.k0, x.address, 1000, data))
print(result)
