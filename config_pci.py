import sys
pciDevice = sys.argv[1:]
def config(fileNames, pciDevice):
    oldFile = fileNames
    newFile = fileNames

    # Read in the file
    with open(oldFile, 'r') as file:
        filedata = file.read()

    # Replace 'user' text with username
    filedata = filedata.replace('INSERT_PCI_DEVICE', pciDevice)

    # Write the new file
    with open(newFile, 'w') as file:
      file.write(filedata)

#pciDevice = input("Enter pci device name: ")
pciDeviceString = ''.join(pciDevice)
print(pciDeviceString)
fileNames = ["MangoHud.conf", "custom.conf", "wine-Diablo IV.conf", "wine-ffxiv_dx11.conf",
"wine-Gw2-64.conf", "wine-NewWorld.conf", "wine-Stardew Valley.conf", "wine-WorldOfTanks.conf", "wine-WoW.conf", "wine-Anno1800.conf"]
for fileNames in fileNames:
    config(fileNames, pciDeviceString)
