def transform_sip(sip_ids):
    return ['(sip.Call-ID == "{}")'.format(sip_id) for sip_id in sip_ids]


def transform_csta(csta_ids):
    return ['(xml.cdata == "FF0{}")'.format(csta_id[:-3]) for csta_id in csta_ids]


def transform_csta_2nd(csta_ids_2nd):
    return ['(xml.cdata == "FF{}")'.format(csta_id[2:]) for csta_id in csta_ids_2nd]


def transform_mgcp_ids(mgcp_ids):
    return ['(mgcp.transid == "{}")'.format(mgcp_id) for mgcp_id in mgcp_ids]


def wireshark_filtering(raw_data):
    wireshark_filter = '\n\n'

    if not raw_data:
        return "No valid IDs found to create Wireshark Filter."

    raw_data_list = raw_data.replace(',', ' ').split()
    sip_ids, csta_ids, csta_ids_2nd, mgcp_ids = [], [], [], []

    for element in raw_data_list:
        if element.isdigit() and len(element) == 7:
            mgcp_ids.append(element)
        elif '000000000' in element:
            if element.endswith('-FF'):
                csta_ids.append(element)
            elif element.startswith('0'):
                csta_ids_2nd.append(element)
        else:
            sip_ids.append(element)

    filter_parts = []
    if sip_ids:
        filter_parts.extend(transform_sip(sip_ids))
    if csta_ids:
        filter_parts.extend(transform_csta(csta_ids))
    if csta_ids_2nd:
        filter_parts.extend(transform_csta_2nd(csta_ids_2nd))
    if mgcp_ids:
        filter_parts.extend(transform_mgcp_ids(mgcp_ids))

    wireshark_filter += "Wireshark Filter:\n" + ' or '.join(filter_parts)
    return wireshark_filter


editor.appendText(wireshark_filtering(editor.getText()))
