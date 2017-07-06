import serpent
from ethereum import utils
from ethereum.tools import tester

serpent_code_mul = '''
def multiply(a, b):
    return(a*b)
'''

c = tester.Chain()
xmul = c.contract(serpent_code_mul, language='serpent')

externMul_code = """
extern mul: [multiply:[int256,int256]:int256]

def externMul(muladdr, a, b):
    c = muladdr.multiply(a, b)
    return(c)
    
def externMul2(a, b):
    c = {}.multiply(a, b)
    return(c)
""".format(utils.coerce_to_int(xmul.address))

x2 = c.contract(externMul_code, language='serpent')
print(x2.externMul(xmul.address, 3, 5))
print(x2.externMul2(4, 6))
