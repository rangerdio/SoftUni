
def transform_sip(sip_ids_):
    transformed_sip_ids = []
    for sip_id in sip_ids_:
        a, b = '(sip.Call-ID == "', '")'
        transformed_sip_ids.append(a + sip_id + b)
    return transformed_sip_ids


def transform_csta(csta_ids_):
    transformed_csta_ids = []

    for csta_id in csta_ids_:
        a, b = '(xml.cdata == "FF0', '")'
        csta_id = a + csta_id[:-3] + b
        transformed_csta_ids.append(csta_id)
    return transformed_csta_ids


def transform_csta_2nd(csta_ids_2nd_):
    transformed_csta_ids_2nd = []
    for csta_id in csta_ids_2nd_:
        a, b = '(xml.cdata == "FF', '")'
        csta_id = a + csta_id[2:] + b
        transformed_csta_ids_2nd.append(csta_id)
    return transformed_csta_ids_2nd


def transform_mgcp_ids(mgcp_ids_):
    transformed_mgcp_ids = []
    for mgcp_id in mgcp_ids_:
        a, b = '(mgcp.transid == "', '")'
        transformed_mgcp_ids.append(a + mgcp_id + b)
    return transformed_mgcp_ids


# Raw data as it is expected in text file.
# Contains
#   MGCP transid's numeric data with 9 digits.
#   CSTA callid's
#   SIP CallIds
raw_data = editor.getText()

# raw_data = '5381418 5388189 5384189 5814190 5384190 8814188 5388141 5388141 5388141 \
# 538814191 SEC11-610d397-710d397-1-yrDCLnlcNUIW c1d574cae7024e38 SEC11-610d397-710d397-1-4nK96z2x5fFZ \
# c55fa32041bc4314 SEC11-610d397-710d397-1-DZxse1RlD08g c5b796bceac7993a SEC11-610d397-710d397-1-F39y1y5R3x0a \
# c71047a099ac8e93 SEC11-610d397-710d397-1-BJF1dSVPXGCX c855ef523e1603c4 SEC11-610d397-710d397-1-kbb3qkZ053zx \
# cba40c793566499f SDb0gk602--SCP-vm-cdf-onenet-pbxip01-P-1726750859287-cafa118c_bq0 0010000000000E720EC664A5E0000-FF \
# 0010000000000E120EC66495E0000-FF 0010000000000E720EC664A5E0000-FF 0300010000000000F920EC664F5E0000 \
# 0300010000000000F920EC664FGE0000'.replace(',', ' ')
result = ''

if not raw_data:
    result = "\nNo data to create Wireshark Filter. Exit...\n"

else:
    raw_data_list = raw_data.split()
    sip_ids, csta_ids, csta_ids_2nd, mgcp_ids = [], [], [], []
    wireshark_filter = []
    element = ''
    for el in raw_data_list:
        element == str(el)
        if element.isnumeric() and len(element) == 7:
            mgcp_ids.append(element)
        elif element.endswith('-FF') and '000000000' in element:
            csta_ids.append(element)
        elif '000000000' in element and element.startswith('0'):
            csta_ids_2nd.append(element)
        else:
            sip_ids.append(element)

    wireshark_filter_list = (transform_sip(sip_ids) + transform_csta(csta_ids) +
                             transform_csta_2nd(csta_ids_2nd) + transform_mgcp_ids(mgcp_ids))
    wireshark_filter = ' or '.join(wireshark_filter_list)

    result = wireshark_filter
editor.appendText(result)
