import pygal
import lxml
import requests


api_key = "65210ZZ38CVFIWM4"
#api docs https://www.alphavantage.co/documentation/
print("Stock Data Visualizer\n======================")

symbol = input("\nEnter the stock symbol are looking for: ")
#check and see if symbol exist > error handling


print("\nChart Types\n==================\n1. Bar\n2. Line")
chart_type = input("Enter the chart type you want (1 , 2):")
#make sure it's 1 or 2, while loop > error handling
if (chart_type == 1):
    #implement function to get bar chart > API integration
    print("1")
if (chart_type == 2):
    #implement function to get line chart > API inegration
    print("2")

print("\nSelect the Time Series of chart you want to Generate\n=================================================================")
print("\n1. Interday\n2. Daily\n3. Weekly\n4. Monthly")
time_series = input("Enter the time series option (1, 2, 3, 4): ")
# error check option picked > error handling
start_date = input("Enter the start Date (YYYY-MM-DD):")
# error handling > check valid date in YYYY-MM-DD
end_date = input("Enter the end Date (YYYY-MM-DD):")
# error hadling > check valid date in YYYY-MM-DD and that it is after the start date

#create lmxl file 

#send lxml to http and open file
