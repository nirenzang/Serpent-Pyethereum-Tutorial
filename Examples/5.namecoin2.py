import serpent
from ethereum.tools import tester
from ethereum import utils

serpent_code = '''
data registry[](owner, value)
    
def register(key):
    # Key not yet claimed
    if not self.registry[key].owner:
        self.registry[key].owner = msg.sender
    
def transfer_ownership(key, new_owner):
    if self.registry[key].owner == msg.sender:
        self.registry[key].owner = new_owner
    
def set_value(key, new_value):
    if self.registry[key].owner == msg.sender:
        self.registry[key].value = new_value
    
def ask(key):
    return([self.registry[key].owner, self.registry[key].value], items=2)
'''

c = tester.Chain()
x = c.contract(serpent_code, language='serpent')
x.register('a', sender=tester.k0)
print("Key \"a\" registered by user 0.")
x.set_value('a', 3, sender=tester.k0)
print("Value \"3\" set by user 0.")
o = x.ask('a', outsz=2)
if o[0] == utils.coerce_to_int(utils.privtoaddr(tester.k0)):
    print("Checked: key \"a\" is registered under user 0")
else:
    print("Error: key \"a\" is not registered under user 0")
print("The value registered under \"a\" is " + str(o[1]))
