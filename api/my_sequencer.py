# -*- coding: utf-8 -*-

from flask import Flask, jsonify , request
from flask.ext.pymongo import PyMongo


app = Flask(__name__)
# config files are used just to flip between prod and test
app.config.from_envvar('CONFIG')

mongo = PyMongo(app)


@app.route('/value/<sequencer>', methods=['GET'])
def get_sequence(sequencer):
    # find_and_modify is used to ensure document level transaction
    result = mongo.db.sequencers.find_and_modify(
        query={"key": sequencer},
        update={"$inc": {"value": 1}},
        upsert=True,
        new=True)

    return jsonify(value=result['value'])


@app.route('/value/<sequencer>', methods=['POST'])
def set_sequence(sequencer):

    reset_info = request.get_json()

    # reset_info also has the key, but it is redundant
    # find_and_modify is used to ensure document level transaction
    result = mongo.db.sequencers.find_and_modify(
        query={"key": sequencer},
        update= {"value": reset_info['value'],
                 "key": sequencer},
        upsert=True,
        new=True)

    return jsonify(value=result['value'], status_code=201)

if __name__ == '__main__':
    app.run()
