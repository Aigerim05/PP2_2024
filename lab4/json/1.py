import json

with open("sample_data.json") as f:
    sample = json.load(f)

head = '''
Interface Status
================================================================================
DN                                                 Description           Speed    MTU  
-------------------------------------------------- --------------------  ------  ------
'''
print(head)
for i in sample["imdata"]:
    dn = i["l1PhysIf"]["attributes"]["dn"]
    descr = ' '*20
    speed = i["l1PhysIf"]["attributes"]["speed"]
    mtu = i["l1PhysIf"]["attributes"]["mtu"]
    print("{:<50} {:<20} {:<8} {:<6}".format(dn, descr, speed, mtu))


