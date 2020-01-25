import matplotlib.pyplot as plt
import numpy as np
import csv

# with open('Dead.csv') as csvFile:
#     readCSV = csv.reader(csvFile, delimiter=',')
#
#     years = []
#     data = {
#         "Brazil": [],
#         "China": [],
#         "India": [],
#         "Japan": [],
#         "Nigeria": [],
#         "Arab Emirates": [],
#         "United Kingdom": [],
#         "United States": []
#     }
#
#     for row in readCSV:
#         years.append(row[0])
#         data["Brazil"].append(row[1])
#         data["China"].append(row[2])
#         data["India"].append(row[3])
#         data["Japan"].append(row[4])
#         data["Nigeria"].append(row[5])
#         data["Arab Emirates"].append(row[6])
#         data["United Kingdom"].append(row[7])
#         data["United States"].append(row[8])
#
#     dataSum = []
#     for i in data:
#         dataSum.append((sum(list(map(int, data[i])))))
#     total = (sum(list(map(int, data[i]))))
#     avg = []
#     numbers = list(map(int, dataSum))
#     for i in numbers:
#         k = round(i / total * 100, 2)
#         avg.append(k)
#
#     labels = ('Brazil', 'China', 'India', 'Japan', 'Nigeria', 'UAE', 'UK', 'USA')
#     plt.title('Mortality Due to Air Pollution')
#
#     y_pos = np.arange(len(labels))
#
#     plt.bar(y_pos, avg)
#     plt.xticks(y_pos, labels)
#     plt.ylabel('Mortality')
#     plt.show()

with open('AirQuality.csv') as csvFile:
    readCSV = csv.reader(csvFile, delimiter=',')

    years = []
    data = {
        "Brazil": [],
        "China": [],
        "India": [],
        "Nigeria": [],
        "Arab Emirates": [],
        "United Kingdom": [],
        "United States": []
    }

    for row in readCSV:
        years.append(row[0])
        data["Brazil"].append(row[1])
        data["China"].append(row[2])
        data["India"].append(row[3])
        data["Nigeria"].append(row[4])
        data["Arab Emirates"].append(row[5])
        data["United Kingdom"].append(row[6])
        data["United States"].append(row[7])

    print(data['Nigeria'])

    plt.plot(years, data["Brazil"], label="Brazil", color='blue')
    plt.plot(years, data["China"], label="China", color='yellow')
    plt.plot(years, data["India"], label="India", color='black')
    plt.plot(years, data["Nigeria"], label="Nigeria", color='red')
    plt.plot(years, data["Arab Emirates"], label="Arab Emirates", color='pink')
    plt.plot(years, data["United Kingdom"], label="United Kingdom", color='green')
    plt.plot(years, data["United States"], label="United States", color='purple')

    plt.title('Air Quality')
    plt.xlabel("Years")
    plt.ylabel("Average Annual Pollution - Weighted PM2.5")

    plt.yscale('linear')
    plt.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc='lower left', ncol=2, mode="expand", borderaxespad=0.)
    plt.show()

# with open('Airpolution.csv') as csvFile:
#     readCSV = csv.reader(csvFile, delimiter=',')
#
#     years = []
#     data = {
#         "Brazil": [],
#         "China": [],
#         "India": [],
#         "Nigeria": [],
#         "Arab Emirates": [],
#         "United Kingdom": [],
#         "United States": []
#     }
#
#     for row in readCSV:
#         years.append(row[0])
#         data["Brazil"].append(row[1])
#         data["China"].append(row[2])
#         data["India"].append(row[3])
#         data["Nigeria"].append(row[4])
#         data["Arab Emirates"].append(row[5])
#         data["United Kingdom"].append(row[6])
#         data["United States"].append(row[7])
#
#     sizes = []
#     for i in data:
#         percent = (sum(list(map(int, data[i])))) / len(data[i])
#         sizes.append(percent)
#
#     explode = (0.0, 0.1, 0.1, 0.0, 0.0, 0.0, 0.0)
#     labels = 'Brazil', 'China', 'India', 'Nigeria', 'Arab Emirates', 'United Kingdom', 'United States'
#     colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue', 'pink', 'beige', 'orange']
#     plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%0.1f%%', shadow=True, startangle=140)
#     plt.title('Air Pollution')
#     plt.axis('equal')
#     plt.show()
