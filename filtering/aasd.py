# Raw data as it is expected in text file.
# Contains
#   MGCP transid's numeric data with 9 digits.
#   CSTA callid's
#   SIP CallIds

raw_data = ''.replace(',', ' ')
if not raw_data:
    print("\nNo data to create Wireshark Filter. Exit...\n")

raw_data_list = raw_data.split()
sip_ids, csta_ids, csta_ids_2nd, mgcp_ids = [], [], [], []
wireshark_filter = []


def transform_sip(sip_ids):
    transformed_sip_ids = []
    for sip_id in sip_ids:
        a, b = '(sip.Call-ID == "', '")'
        transformed_sip_ids.append(a + sip_id + b)
    return transformed_sip_ids


def transform_csta(csta_ids):
    transformed_csta_ids = []

    for csta_id in csta_ids:
        a, b = '(xml.cdata == "FF0', '")'
        csta_id = a + csta_id[:-3] + b
        transformed_csta_ids.append(csta_id)
    return transformed_csta_ids


def transform_csta_2nd(csta_ids_2nd):
    transformed_csta_ids_2nd = []
    for csta_id in csta_ids_2nd:
        a, b = '(xml.cdata == "FF', '")'
        csta_id = a + csta_id[2:] + b
        transformed_csta_ids_2nd.append(csta_id)
    return transformed_csta_ids_2nd


def transform_mgcp_ids(mgcp_ids):
    transformed_mgcp_ids = []
    for mgcp_id in mgcp_ids:
        a, b = '(mgcp.transid == "', '")'
        transformed_mgcp_ids.append(a + mgcp_id + b)
    return transformed_mgcp_ids


for element in raw_data_list:
    if element.isnumeric() and len(element) == 7:
        mgcp_ids.append(element)
    elif element.endswith('-FF') and '000000000' in element:
        csta_ids.append(element)
    elif '000000000' in element and element.startswith('0'):
        csta_ids_2nd.append(element)
    else:
        sip_ids.append(element)

wireshark_filter = ' or '.join(transform_sip(sip_ids) + transform_csta(csta_ids) +
                               transform_csta_2nd(csta_ids_2nd) + transform_mgcp_ids(mgcp_ids))
print(f'\n\nWireshark Filter:\n{wireshark_filter}\n')