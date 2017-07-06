import serpent
from ethereum.tools import tester
serpent_code = '''
def multiply(a):
    return(a*2)
'''

s = tester.Chain()
x = s.contract(serpent_code, language='serpent')
o = x.multiply(5)
print(str(o))
