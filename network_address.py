# network_address.py

import ipaddress

def calc_network_address(ip, netmask):
    # IPアドレスとネットマスクを結合
    network = ipaddress.IPv4Network(f"{ip}/{netmask}", strict=False)

    # ネットワークアドレスを返す
    return str(network.network_address)


# 実行例
ip = input("IPアドレスを入力してください: ")
netmask = input("ネットマスクを入力してください: ")

network_address = calc_network_address(ip, netmask)

print("ネットワークアドレス:", network_address)
