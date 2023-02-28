from flask import Flask, jsonify
from data import df

app = Flask(__name__)

@app.route('/get_details_by_ifsc/<string:ifsc>')
def get_details_by_ifsc(req_ifsc):
    for i, ifsc in enumerate(df.ifsc, start=0):
        if ifsc == req_ifsc:
            return jsonify(df.loc[i].to_dict())
    return "Incorrect IFSC code."

@app.route('/get_details_by_bank_id_and_branch/<int:req_bank_id>/<string:branch>')
def get_details_by_branch(req_bank_id, branch):
    response = []
    for i, bank_id in enumerate(df.bank_id, start=0):
        if bank_id == req_bank_id and df.loc[i].branch == branch:
            response.append(df.loc[i].to_dict())
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
