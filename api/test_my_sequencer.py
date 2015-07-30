# -*- coding: utf-8 -*-

"""Tests my_sequencer app

A different sequencer is used for each test as the readings are not idempotent.
"""

import pytest

import my_sequencer
import json
from threading import Thread

@pytest.fixture
def client(request):
    my_sequencer.app.config['TESTING'] = True
    test_client = my_sequencer.app.test_client()
    return test_client


def test_set(client):
    new_values = {
        "key": "lazy_number",
        "value": 3333
    }
    set_response = client.post("/value/lazy_number",
                               data=json.dumps(new_values),
                               headers={"content-type":"application/json"})
    set_value = json.loads(set_response.data)["value"]
    assert(set_value == 3333)


def test_set_and_retrieve(client):
    new_values = {
        "key": "po_number",
        "value": 1000
    }
    set_response = client.post("/value/po_number",
                               data=json.dumps(new_values),
                               headers={"content-type":"application/json"})
    set_value = json.loads(set_response.data)["value"]
    assert(set_value == 1000)

    get_response = client.get("/value/po_number")
    get_value = json.loads(get_response.data)["value"]
    assert(get_value == 1001)


def retrieve(client):
    get_response = client.get("/value/mt_number")


# this test is used to ensure the document level transaction is working
def test_multi_thread(client):
    threads = []

    # reset the counter to 5000
    new_values = {
        "key": "mt_number",
        "value": 5000
    }
    set_response = client.post("/value/mt_number",
                               data=json.dumps(new_values),
                               headers={"content-type":"application/json"})
    set_value = json.loads(set_response.data)["value"]
    assert(set_value == 5000)

    iterations = 20
    for i in range(iterations):
        t = Thread(target=retrieve, args=(client,))
        threads.append(t)

    for v in threads:
        v.start()

    for l in threads:
        l.join()

    get_response = client.get('/value/mt_number')
    get_value = json.loads(get_response.data)["value"]
    assert(get_value == (5000 + iterations + 1))