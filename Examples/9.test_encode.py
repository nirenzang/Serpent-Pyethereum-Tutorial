import serpent
from ethereum.tools import tester
from ethereum import utils

serpent_code='''
def sha3check(choice, nonce):
    return(sha3([msg.sender, choice, nonce], items=3))
'''

s = tester.Chain()
c = s.contract(serpent_code, language='serpent')

choice1 = 1048576
nonce1 = 3628800

print('the sha3 result computed by serpent:')
print(c.sha3check(choice1, nonce1, sender=tester.k0))

ch1 = bytearray(utils.int_to_32bytearray(choice1))
no1 = bytearray(utils.int_to_32bytearray(nonce1))
tohash = bytearray().join([bytearray(12), tester.a0, ch1, no1])
print('the sha3 result computed by pyethereum')
print(utils.coerce_to_int(utils.sha3(bytes(tohash))))
