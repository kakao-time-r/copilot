import pandas as pd

file_path = "/Users/time/Desktop/VSCODE/python/copilot/"

# Sample data
data = {
    'Type': ['100G Single LC to LC', '100G Single LC to LC', '100G Single LC to LC'],
    'use' : ['ADR-GDR', 'ADR-GDR', 'ADR-GDR'],
    'label' : ['AS1-ADR0301_Eth1/19<->AS1-GDR0401_Eth1/36', 'AS1-ADR0302_Eth1/19<->AS1-GDR0401_Eth2/36', 'AS1-ADR0303_Eth1/19<->AS1-GDR0401_Eth3/36'],
    'HOST-F': ['AS1-ADR0301', 'AS1-ADR0302', 'AS1-ADR0303'],
    'Rack-F': ['AS1-031-10-03-03', 'AS1-031-10-04-03', 'AS1-031-10-05-03'],
    'PORT-F': ['Eth1/19', 'Eth1/19', 'Eth1/19'],
    'HOST-T': ['AS1-GDR0401', 'AS1-GDR0401', 'AS1-GDR0401'],
    'Rack-T': ['AS1-041-10-06-03', 'AS1-041-10-06-03', 'AS1-041-10-06-03'],
    'PORT-T': ['Eth1/36', 'Eth2/36', 'Eth3/36']
}

# Create a DataFrame
df = pd.DataFrame(data)

df.index += 1

# Save DataFrame to Excel
df.to_excel(f'{file_path}file.xlsx', index=True)
