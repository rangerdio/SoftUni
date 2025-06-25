from flask import Flask, render_template, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


def transform_sip(sip_ids):
    return ['(sip.Call-ID == "{}")'.format(sip_id) for sip_id in sip_ids]


def transform_csta(csta_ids):
    return ['(xml.cdata == "FF0{}")'.format(csta_id[:-3]) for csta_id in csta_ids]


def transform_csta_2nd(csta_ids_2nd):
    return ['(xml.cdata == "FF{}")'.format(csta_id[2:]) for csta_id in csta_ids_2nd]


def transform_csta_extra_sst(csta_extra_sst):
    return ['(xml.cdata == "{}")'.format(csta_id) for csta_id in csta_extra_sst]


def transform_mgcp_ids(mgcp_ids):
    return ['(mgcp.transid == "{}")'.format(mgcp_id) for mgcp_id in mgcp_ids]


def wireshark_filtering(raw_data):
    if not raw_data:
        return "No valid IDs found to create Wireshark Filter."

    raw_data_list = raw_data.replace(',', ' ').split()
    sip_ids, csta_ids, csta_ids_2nd, csta_extra_sst, mgcp_ids = [], [], [], [], []

    for element in raw_data_list:
        if element.isdigit() and len(element) in (7, 8):
            mgcp_ids.append(element)
        elif '000000000' in element:
            # capture every csta for direct xml.cdata filter due to SingleStepTransfer usage
            csta_extra_sst.append(element)
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
        if csta_extra_sst:
            filter_parts.extend(transform_csta_extra_sst(csta_extra_sst))
    if mgcp_ids:
        filter_parts.extend(transform_mgcp_ids(mgcp_ids))

    return ' or '.join(filter_parts)  # Output without "Wireshark Filter:"


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/generate_filter', methods=['POST'])
def generate_filter():
    data = request.json.get("raw_data", "")
    result = wireshark_filtering(data)
    return jsonify({"filter": result})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

