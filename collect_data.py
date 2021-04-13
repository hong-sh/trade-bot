import pyupbit
import time
import pandas as pd
import csv

ticker_list = pyupbit.get_tickers()
prev_price_dict = {}

if __name__ == "__main__":
    while True:
        start_time = time.time()
        for ticker in ticker_list:
            
            current_price = pyupbit.get_current_price(ticker)

            if ticker not in prev_price_dict:
                prev_price_dict[ticker] = current_price

            min1_info = pyupbit.get_ohlcv(ticker, count=10, interval="minute1")
            min3_info = pyupbit.get_ohlcv(ticker, count=3, interval="minute3", to=min1_info.index[0])
            min5_info = pyupbit.get_ohlcv(ticker, count=2, interval="minute5", to=min3_info.index[0])
            min_info = pd.concat([min1_info, min3_info, min5_info]).sort_index(ascending=False)
            
            orderbook = pyupbit.get_orderbook(tickers=ticker)[0]
            bid_price_dict = {}
            ask_price_dict = {}
            for orderbook_unit in orderbook["orderbook_units"]:
                bid_price_dict[orderbook_unit["bid_size"]] = orderbook_unit["bid_price"]
                ask_price_dict[orderbook_unit["ask_size"]] = orderbook_unit["ask_price"]

            bid_price_dict = sorted(bid_price_dict.items(), reverse=True)
            bid_price_first, bid_price_second = bid_price_dict[0], bid_price_dict[1]

            ask_price_dict = sorted(ask_price_dict.items(), reverse=True)
            ask_price_first, ask_price_second = ask_price_dict[0], ask_price_dict[1]

            
            data = [ticker, time.time(), prev_price_dict[ticker]]
            for i in range(len(min_info)):
                data.append(min_info['open'][i])
                data.append(min_info['high'][i])
                data.append(min_info['low'][i])
                data.append(min_info['close'][i])
                data.append(min_info['volume'][i])

            data.append(bid_price_first[0])
            data.append(bid_price_first[1])
            data.append(bid_price_second[0])
            data.append(bid_price_second[1])
            data.append(ask_price_first[0])
            data.append(ask_price_first[1])
            data.append(ask_price_second[0])
            data.append(ask_price_second[1])
            data.append(current_price)

            prev_price_dict[ticker] = current_price

            f = open('data/'+ticker+'.csv', 'a', newline='')
            wr = csv.writer(f)
            wr.writerow(data)
            f.close()

            time.sleep(0.2)
        end_time = time.time()
        spand_time = end_time - start_time
        if spand_time < 60:
            time.sleep(60 - spand_time)
