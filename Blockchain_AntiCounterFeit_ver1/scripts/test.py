#!/usr/bin/python3

from brownie import accounts
from brownie import Reports
import time
import qrcode
# import numpy as np
# 10 accounts by default

def main():
    print("There are %d accounts."%(len(accounts)))

    contracts = accounts[9].deploy(Reports)

    roles = ["manufacturer", "distributor", "retailer", "customer"]
    reviewers = ["A_manufacturer", "B_distributor", "C_retailer", "D_customer", "E_fake", "F_fake"]
    goods = "shoes"

    for i in [4, 5, 6, 7, 8]:
        contracts.blackUser(accounts[i])

    for i in range(len(roles)):
        contracts.addUser(accounts[i], reviewers[i], roles[i])

    for i in range(4, 5):
        contracts.addUser(accounts[i], reviewers[i], "retailer")
    
    contracts.addProduct(accounts[0], "0001", goods)
    contracts.addProduct(accounts[0], "0002", goods)
    contracts.addProduct(accounts[0], "0003", goods)

    tx = contracts.getItemById("0001")
    print(tx.return_value)
    tx = contracts.getItemById("0002")
    print(tx.return_value)
    tx = contracts.getItemById("0003")
    print(tx.return_value)

    contracts.transfer(accounts[1], "0001", "distributor")
    tx = contracts.getItemById("0001")
    print(tx.return_value)
    tx = contracts.checkFake("0001")
    if tx.return_value:
        print("fake")
    else:
        print("goods")
    contracts.transfer(accounts[2], "0001", "retailer")
    tx = contracts.getItemById("0001")
    print(tx.return_value)
    tx = contracts.checkFake("0001")
    if tx.return_value:
        print("fake")
    else:
        print("goods")
    contracts.transfer(accounts[3], "0001", "customer") # Buy it
    tx = contracts.getItemById("0001")
    print(tx.return_value)
    # print(tx)
    tx = contracts.checkFake("0001")
    if tx.return_value:
        print("fake")
    else:
        print("goods")

    
    if contracts.transfer(accounts[1], "0002", "retailer"):
        print("fail to tansfer")

    contracts.transfer(accounts[1], "0003", "distributor")
    tx = contracts.getItemById("0003")
    # print(tx.return_value)
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(str(tx.return_value))
    qr.make(fit=True)
    qr.print_ascii()
    tx = contracts.checkFake("0003")
    if tx.return_value:
        print("fake")
    else:
        print("goods")
    contracts.transfer(accounts[4], "0003", "retailer")
    tx = contracts.getItemById("0003")
    # print(tx.return_value)
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(str(tx.return_value))
    qr.make(fit=True)
    qr.print_ascii()
    tx = contracts.checkFake("0003")
    if tx.return_value:
        print("fake")
    else:
        print("goods")
    # This is fake, do not buy it

    time.sleep(3)

