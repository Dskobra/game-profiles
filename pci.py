def configure_mangohud_config():
    oldFile = "MangoHud.conf"
    newFile = "MangoHud.conf"

    # Read in the file
    with open(oldFile, 'r') as file:
        filedata = file.read()

    # Replace 'user' text with username
    filedata = filedata.replace('INSERT_PCI_DEVICE', pci_device)

    # Write the new file
    with open(newFile, 'w') as file:
      file.write(filedata)

def configure_diablo_config():
    oldFile = "wine-Diablo IV.conf"
    newFile = "wine-Diablo IV.conf"

    # Read in the file
    with open(oldFile, 'r') as file:
        filedata = file.read()

    # Replace 'user' text with username
    filedata = filedata.replace('INSERT_PCI_DEVICE', pci_device)

    # Write the new file
    with open(newFile, 'w') as file:
      file.write(filedata)

def configure_ffxiv_config():
    oldFile = "wine-ffxiv_dx11.conf"
    newFile = "wine-ffxiv_dx11.conf"

    # Read in the file
    with open(oldFile, 'r') as file:
        filedata = file.read()

    # Replace 'user' text with username
    filedata = filedata.replace('INSERT_PCI_DEVICE', pci_device)

    # Write the new file
    with open(newFile, 'w') as file:
      file.write(filedata)


def configure_gw2_config():
    oldFile = "wine-Gw2-64.conf"
    newFile = "wine-Gw2-64.conf"

    # Read in the file
    with open(oldFile, 'r') as file:
        filedata = file.read()

    # Replace 'user' text with username
    filedata = filedata.replace('INSERT_PCI_DEVICE', pci_device)

    # Write the new file
    with open(newFile, 'w') as file:
      file.write(filedata)

def configure_newworld_config():
    oldFile = "wine-NewWorld.conf"
    newFile = "wine-NewWorld.conf"

    # Read in the file
    with open(oldFile, 'r') as file:
        filedata = file.read()

    # Replace 'user' text with username
    filedata = filedata.replace('INSERT_PCI_DEVICE', pci_device)

    # Write the new file
    with open(newFile, 'w') as file:
      file.write(filedata)  

def configure_runescape_config():
    oldFile = "wine-RuneScape.conf"
    newFile = "wine-RuneScape.conf"

    # Read in the file
    with open(oldFile, 'r') as file:
        filedata = file.read()

    # Replace 'user' text with username
    filedata = filedata.replace('INSERT_PCI_DEVICE', pci_device)

    # Write the new file
    with open(newFile, 'w') as file:
      file.write(filedata) 


def configure_stardewvalley_config():
    oldFile = "wine-Stardew Valley.conf"
    newFile = "wine-Stardew Valley.conf"

    # Read in the file
    with open(oldFile, 'r') as file:
        filedata = file.read()

    # Replace 'user' text with username
    filedata = filedata.replace('INSERT_PCI_DEVICE', pci_device)

    # Write the new file
    with open(newFile, 'w') as file:
      file.write(filedata) 

def configure_worldoftanks_config():
    oldFile = "wine-WorldOfTanks.conf"
    newFile = "wine-WorldOfTanks.conf"

    # Read in the file
    with open(oldFile, 'r') as file:
        filedata = file.read()

    # Replace 'user' text with username
    filedata = filedata.replace('INSERT_PCI_DEVICE', pci_device)

    # Write the new file
    with open(newFile, 'w') as file:
      file.write(filedata)

def configure_wow_config():
    oldFile = "wine-WoW.conf"
    newFile = "wine-WoW.conf"

    # Read in the file
    with open(oldFile, 'r') as file:
        filedata = file.read()

    # Replace 'user' text with username
    filedata = filedata.replace('INSERT_PCI_DEVICE', pci_device)

    # Write the new file
    with open(newFile, 'w') as file:
      file.write(filedata)


pci_device = input("Enter pci device name: ") 
configure_mangohud_config()
configure_diablo_config()
configure_ffxiv_config()
configure_gw2_config()
configure_newworld_config()
configure_runescape_config()
configure_stardewvalley_config()
configure_worldoftanks_config()
configure_wow_config()