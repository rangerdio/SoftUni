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


def wireshark_filtering(raw_data):
    wireshark_filter = '\n\n'

    # raw_data = '5381418 5388189 5384189 5814190 5384190 8814188 5388141 5388141 5388141 \
    # 538814191 SEC11-610d397-710d397-1-yrDCLnlcNUIW c1d574cae7024e38 SEC11-610d397-710d397-1-4nK96z2x5fFZ \
    # c55fa32041bc4314 SEC11-610d397-710d397-1-DZxse1RlD08g c5b796bceac7993a SEC11-610d397-710d397-1-F39y1y5R3x0a \
    # c71047a099ac8e93 SEC11-610d397-710d397-1-BJF1dSVPXGCX c855ef523e1603c4 SEC11-610d397-710d397-1-kbb3qkZ053zx \
    # cba40c793566499f SDb0gk602--SCP-vm-cdf-onenet-pbxip01-P-1726750859287-cafa118c_bq0 0010000000000E720EC664A5E0000-FF \
    # 0010000000000E120EC66495E0000-FF 0010000000000E720EC664A5E0000-FF 0300010000000000F920EC664F5E0000 \
    # 0300010000000000F920EC664FGE0000'.replace(',', ' ')
    if not raw_data:
        wireshark_filter += "No data to create Wireshark Filter. Exit..."
        return wireshark_filter
    raw_data_list = raw_data.replace(',', ' ').split()
    sip_ids, csta_ids, csta_ids_2nd, mgcp_ids = [], [], [], []

    for element in raw_data_list:
        if element.isdigit() and len(element) == 7:
            mgcp_ids.append(element)
        elif element.endswith('-FF') and '000000000' in element:
            csta_ids.append(element)
        elif '000000000' in element and element.startswith('0'):
            csta_ids_2nd.append(element)
        else:
            sip_ids.append(element)

    wireshark_filter = (wireshark_filter + "Wireshark Filter:" + "\n" +
                        ' or '.join(transform_sip(sip_ids) + transform_csta(csta_ids) +
                                    transform_csta_2nd(csta_ids_2nd) + transform_mgcp_ids(mgcp_ids)))
    return wireshark_filter


editor.appendText(wireshark_filtering(editor.getText()))
