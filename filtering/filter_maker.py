
# Raw data as it is expected in text file.
# Contains
#   MGCP transid's numeric data with 9 digits.
#   CSTA callid's
#   SIP CallIds

raw_data = '538814188,538814189 538814189 538814190 538814190 538814188 538814188 538814191 \
538814191 SEC11-610d397-710d397-1-yrDCLnlcNUIW c1d574cae7024e38 SEC11-610d397-710d397-1-4nK96z2x5fFZ \
c55fa32041bc4314 SEC11-610d397-710d397-1-DZxse1RlD08g c5b796bceac7993a SEC11-610d397-710d397-1-F39y1y5R3x0a \
c71047a099ac8e93 SEC11-610d397-710d397-1-BJF1dSVPXGCX c855ef523e1603c4 SEC11-610d397-710d397-1-kbb3qkZ053zx \
cba40c793566499f SDb0gk602--SCP-vm-cdf-onenet-pbxip01-P-1726750859287-cafa118c_bq0 0010000000000E720EC664A5E0000-FF \
0010000000000E120EC66495E0000-FF 0010000000000E720EC664A5E0000-FF 0300010000000000F920EC664F5E0000 \
0300010000000000F920EC664FGE0000'.replace(',', ' ')
# raw_data = raw_data.replace(',', ' ')
raw_data_list = raw_data.split()
print(raw_data_list)

sip_ids, csta_ids, mgcp_ids = []

for element in raw_data_list:
    if element.isnumeric() and len(element) == 7:

