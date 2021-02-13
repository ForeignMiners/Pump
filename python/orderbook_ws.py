#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re
import sys
import os
import argparse
#import pandas as pd
#import numpy as np
import json
import time
import math
import traceback
import dateparser
from datetime import datetime
from binance.client import Client
from binance.websockets import BinanceSocketManager
from binance.depthcache import DepthCacheManager

client = Client(api_key, api_secret)


def process_depth(msg):
    print("NEWmsg")

def get_candle(client,symbol):
    candle = {}
    kline = client.get_historical_klines(symbol=symbol,interval=client.KLINE_INTERVAL_1HOUR,start_str="4 days ago UTC",end_str="now UTC",limit = 500)
    return kline

			
if __name__ == '__main__':
#    asset = input("Insert Symbol")
    asset = "BTC"
    symbol = asset + "USDC"
    info = client.get_symbol_info(symbol)

    symbols = []
    all_prices = client.get_all_tickers()
    for p in all_prices:
        if p["symbol"].find(asset) != -1:
           symbols.append(p["symbol"])
#            symbols.append(p["symbol"].lower()+"@depth5@1000ms")
#        elif p["symbol"].find("XRP") != -1:
#            symbols.append(p["symbol"].lower()+"@depth5")
#        elif p["symbol"].find("ETH") != -1:
#            symbols.append(p["symbol"].lower()+"@depth5")
    print( "Numero di coppie con BTC: " + str(len(symbols)))
    print(symbols)
    bm = BinanceSocketManager(client)
    dcm = DepthCacheManager(client,"WTCBTC",callback=process_depth,bm=bm, refresh_interval=2)
    while True:
        depth_cache = dcm.get_depth_cache()
        if depth_cache is not None:
            print("symbol {}".format(depth_cache.symbol))
            print("top 5 asks")
            print(depth_cache.get_asks()[-2:-1])
            print("last update time {}".format(depth_cache.update_time))            
