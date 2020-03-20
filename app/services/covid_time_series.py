import numpy as np
import pandas as pd

from config import Config

base_path = Config.DATA_BASE_PATH


class COVIDTimeSeriesData:
    def __init__(self):
        self.confirmed_file_name = f'{base_path}/data/csse_covid_19_time_series/time_series_19-covid-Confirmed.csv'
        self.death_file_name = f'{base_path}/data/csse_covid_19_time_series/time_series_19-covid-Deaths.csv'
        self.recovered_file_name = f'{base_path}/data/csse_covid_19_time_series/time_series_19-covid-Recovered.csv'
        self.death_df = None
        self.confirmed_df = None
        self.recovered_df = None

    def get_confirmed_data(self):
        if self.confirmed_df is None:
            df = pd.read_csv(self.confirmed_file_name)
            df = df[df['Country/Region'] == 'Australia']
            self.confirmed_df = self.date_series(df)
        return self.confirmed_df

    def get_death_data(self):
        if self.death_df is None:
            df = pd.read_csv(self.death_file_name)
            df = df[df['Country/Region'] == 'Australia']
            self.death_df = self.date_series(df)

        return self.death_df

    def get_recover_data(self):
        if self.recovered_df is None:
            df = pd.read_csv(self.recovered_file_name)
            df = df[df['Country/Region'] == 'Australia']
            self.recovered_df = self.date_series(df)

        return self.recovered_df

    def date_series(self, df):
        dates = df.columns[4:]
        columns = df['Province/State']
        # print(columns)
        data_array = []
        # print(dates)

        date_index = pd.DatetimeIndex(dates.to_list(), dtype='datetime64[ns]', freq='D')
        # print(date_index)
        for d in dates:
            rows = df[d].to_list()
            data_array.append(rows)

        new_df = pd.DataFrame(data_array, index=date_index, columns=columns.to_list())

        return new_df


def test2():
    ts = COVIDTimeSeriesData()
    df = ts.get_confirmed_data()
    print(df.head())
    print(df.columns)
    # print(df.index.to_list())
    # print(df['New South Wales'])


if __name__ == "__main__":
    test2()
