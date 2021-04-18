import csv
import pandas

import os


if __name__ == "__main__":
    path = "./data"
    file_list = os.listdir(path)
    csv_file_list = [file for file in file_list if file.endswith(".csv")]
    total_data_frame = pandas.DataFrame()
    for csv_file in csv_file_list:
        if csv_file.startswith("KRW"):
            # print(csv_file)
            pd = pandas.read_csv('data/'+csv_file, names=["ticker", "time", "prev_price", \
                "min1_open",  "min1_high", "min1_low", "min1_close", "min1_volume", \
                    "min2_open",  "min2_high", "min2_low", "min2_close", "min2_volume", \
                        "min3_open",  "min3_high", "min3_low", "min3_close", "min3_volume", \
                            "min4_open",  "min4_high", "min4_low", "min4_close", "min4_volume", \
                                "min5_open",  "min5_high", "min5_low", "min5_close", "min5_volume", \
                                    "min6_open",  "min6_high", "min6_low", "min6_close", "min6_volume", \
                                        "min7_open",  "min7_high", "min7_low", "min7_close", "min7_volume", \
                                            "min8_open",  "min8_high", "min8_low", "min8_close", "min8_volume",\
                                                "min9_open",  "min9_high", "min9_low", "min9_close", "min9_volume",\
                                                    "min10_open",  "min10_high", "min10_low", "min10_close", "min10_volume",\
                                                        "min13_open",  "min13_high", "min13_low", "min13_close", "min13_volume",\
                                                            "min16_open",  "min16_high", "min16_low", "min16_close", "min16_volume",\
                                                                "min19_open",  "min19_high", "min19_low", "min19_close", "min19_volume",\
                                                                    "min25_open",  "min25_high", "min25_low", "min25_close", "min25_volume",\
                                                                        "min30_open",  "min30_high", "min30_low", "min30_close", "min30_volume",\
                                                "bid_size_first", "bid_price_first", "bid_size_second", "bid_price_second", "ask_size_first", "ask_price_first", "ask_size_second", "ask_price_second", "current_price"])
            df = pandas.DataFrame(pd)
            next_price = pd['current_price']
            next_price = next_price.to_list()
            next_price.insert(0,0.0)
            next_price.pop()
            df['next_price'] = next_price
            df = df.drop(0,axis=0)

            df['prev_price'] = df['prev_price'] / df['current_price']
            df['min1_open'] = df['min1_open'] / df['current_price']
            df['min1_high'] = df['min1_high'] / df['current_price']
            df['min1_low'] = df['min1_low'] / df['current_price']
            df['min1_close'] = df['min1_close'] / df['current_price']
            df['min1_volume'] = df['min1_volume'] / df['min1_volume'].mean()

            df['min2_open'] = df['min2_open'] / df['current_price']
            df['min2_high'] = df['min2_high'] / df['current_price']
            df['min2_low'] = df['min2_low'] / df['current_price']
            df['min2_close'] = df['min2_close'] / df['current_price']
            df['min2_volume'] = df['min2_volume'] / df['min2_volume'].mean()

            df['min3_open'] = df['min3_open'] / df['current_price']
            df['min3_high'] = df['min3_high'] / df['current_price']
            df['min3_low'] = df['min3_low'] / df['current_price']
            df['min3_close'] = df['min3_close'] / df['current_price']
            df['min3_volume'] = df['min3_volume'] / df['min3_volume'].mean()

            df['min4_open'] = df['min4_open'] / df['current_price']
            df['min4_high'] = df['min4_high'] / df['current_price']
            df['min4_low'] = df['min4_low'] / df['current_price']
            df['min4_close'] = df['min4_close'] / df['current_price']
            df['min4_volume'] = df['min4_volume'] / df['min4_volume'].mean()

            df['min5_open'] = df['min5_open'] / df['current_price']
            df['min5_high'] = df['min5_high'] / df['current_price']
            df['min5_low'] = df['min5_low'] / df['current_price']
            df['min5_close'] = df['min5_close'] / df['current_price']
            df['min5_volume'] = df['min5_volume'] / df['min5_volume'].mean()

            df['min6_open'] = df['min6_open'] / df['current_price']
            df['min6_high'] = df['min6_high'] / df['current_price']
            df['min6_low'] = df['min6_low'] / df['current_price']
            df['min6_close'] = df['min6_close'] / df['current_price']
            df['min6_volume'] = df['min6_volume'] / df['min6_volume'].mean()

            df['min7_open'] = df['min7_open'] / df['current_price']
            df['min7_high'] = df['min7_high'] / df['current_price']
            df['min7_low'] = df['min7_low'] / df['current_price']
            df['min7_close'] = df['min7_close'] / df['current_price']
            df['min7_volume'] = df['min7_volume'] / df['min7_volume'].mean()

            df['min8_open'] = df['min8_open'] / df['current_price']
            df['min8_high'] = df['min8_high'] / df['current_price']
            df['min8_low'] = df['min8_low'] / df['current_price']
            df['min8_close'] = df['min8_close'] / df['current_price']
            df['min8_volume'] = df['min8_volume'] / df['min8_volume'].mean()

            df['min9_open'] = df['min9_open'] / df['current_price']
            df['min9_high'] = df['min9_high'] / df['current_price']
            df['min9_low'] = df['min9_low'] / df['current_price']
            df['min9_close'] = df['min9_close'] / df['current_price']
            df['min9_volume'] = df['min9_volume'] / df['min9_volume'].mean()

            df['min10_open'] = df['min10_open'] / df['current_price']
            df['min10_high'] = df['min10_high'] / df['current_price']
            df['min10_low'] = df['min10_low'] / df['current_price']
            df['min10_close'] = df['min10_close'] / df['current_price']
            df['min10_volume'] = df['min10_volume'] / df['min10_volume'].mean()

            df['min13_open'] = df['min13_open'] / df['current_price']
            df['min13_high'] = df['min13_high'] / df['current_price']
            df['min13_low'] = df['min13_low'] / df['current_price']
            df['min13_close'] = df['min13_close'] / df['current_price']
            df['min13_volume'] = df['min13_volume'] / df['min13_volume'].mean()

            df['min16_open'] = df['min16_open'] / df['current_price']
            df['min16_high'] = df['min16_high'] / df['current_price']
            df['min16_low'] = df['min16_low'] / df['current_price']
            df['min16_close'] = df['min16_close'] / df['current_price']
            df['min16_volume'] = df['min16_volume'] / df['min16_volume'].mean()

            df['min19_open'] = df['min19_open'] / df['current_price']
            df['min19_high'] = df['min19_high'] / df['current_price']
            df['min19_low'] = df['min19_low'] / df['current_price']
            df['min19_close'] = df['min19_close'] / df['current_price']
            df['min19_volume'] = df['min19_volume'] / df['min19_volume'].mean()

            df['min25_open'] = df['min25_open'] / df['current_price']
            df['min25_high'] = df['min25_high'] / df['current_price']
            df['min25_low'] = df['min25_low'] / df['current_price']
            df['min25_close'] = df['min25_close'] / df['current_price']
            df['min25_volume'] = df['min25_volume'] / df['min25_volume'].mean()

            df['min30_open'] = df['min30_open'] / df['current_price']
            df['min30_high'] = df['min30_high'] / df['current_price']
            df['min30_low'] = df['min30_low'] / df['current_price']
            df['min30_close'] = df['min30_close'] / df['current_price']
            df['min30_volume'] = df['min30_volume'] / df['min30_volume'].mean()

            df['bid_price_first'] = df['bid_price_first'] / df['current_price']
            df['bid_size_first'] = df['bid_size_first'] / df['bid_size_first'].mean()

            df['bid_price_second'] = df['bid_price_second'] / df['current_price']
            df['bid_size_second'] = df['bid_size_second'] / df['bid_size_second'].mean()

            df['ask_price_first'] = df['ask_price_first'] / df['current_price']
            df['ask_size_first'] = df['ask_size_first'] / df['ask_size_first'].mean()

            df['ask_price_second'] = df['ask_price_second'] / df['current_price']
            df['ask_size_second'] = df['ask_size_second'] / df['ask_size_second'].mean()
            df['next_price'] = df['next_price'] / df['current_price']


            # print(df)  
            total_data_frame = total_data_frame.append(df)
            # print(total_data_frame)

        del total_data_frame['ticker']
        del total_data_frame['time']    


X = total_data_frame.iloc[:,:-1].to_numpy()
Y = total_data_frame.iloc[:,-1].to_numpy()
