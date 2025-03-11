import re
pin=input("enter the pin -->")
if len(pin)==4:
    match=re.fullmatch(r"[0-9][0-9][0-9][0-9]",pin)
    if match==None:
        print(f"False entry: {pin}\npin did not contain alphabet or symbol")
    else:
        print(f"True entry: {pin}")

elif len(pin)==6:
    match=re.fullmatch(r"[0-9][0-9][0-9][0-9][0-9][0-9]",pin)
    if match==None:
        print(f"False entry: {pin}\npin did not contain alphabet or symbol")
    else:
        print(f"True entry: {pin}")
else:
    print(f"False entry: {pin} \nATM machines only allow 4 or 6 digit PIN codes, your enter {len(pin)} PIN codes")
