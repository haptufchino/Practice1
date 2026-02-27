import json

a = open("/storage/emulated/0/Download/sample-data.json", "r")
b = json.loads("".join(a.readlines()))
print("Interface Status")
print("================================================================================")
print("DN                                                 Description           Speed    MTU")
print("-------------------------------------------------- --------------------  ------  ------")
k = 0
for i in b["imdata"]:
  if k == 3:
  	break
  print(i["l1PhysIf"]["attributes"]["dn"], " " * 28, i["l1PhysIf"]["attributes"]["speed"], " ", i["l1PhysIf"]["attributes"]["mtu"])
  k += 1