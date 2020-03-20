#!/bin/bash


echo "Start to download series data"

curl https://github.com/CSSEGISandData/COVID-19/blob/master/csse_covid_19_data/csse_covid_19_time_series/time_series_19-covid-Recovered.csv >data/csse_covid_19_time_series/time_series_19-covid-Recovered.csv

curl https://github.com/CSSEGISandData/COVID-19/blob/master/csse_covid_19_data/csse_covid_19_time_series/time_series_19-covid-Deaths.csv >data/csse_covid_19_time_series/time_series_19-covid-Deaths.csv

curl https://github.com/CSSEGISandData/COVID-19/blob/master/csse_covid_19_data/csse_covid_19_time_series/time_series_19-covid-Confirmed.csv >data/csse_covid_19_time_series/time_series_19-covid-Confirmed.csv


echo "All done"
