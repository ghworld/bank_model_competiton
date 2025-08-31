#coding=utf-8

import pandas as pd


train_path='train.csv'
train_tx_path='train_bank_statement.csv'

test_path='testaa.csv'
test_tx_path='testaa_bank_statement.csv'

# def tx_stat():
#     a = 1

def process_base_data(file_input):
  df = pd.read_csv(file_input)
  df.head()

def main():
  process_base_data(train_path)



if __name__ == '__main__':
    main()
    





