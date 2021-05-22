# coding=utf-8
import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics.pairwise import cosine_similarity
import database
import math

def recommendationSysAlgorithm(userList):
    print("re:",userList)
    # User information
    #userList = recommend()
    #userList = ['', 5000, 'Lvl', '', 'NAmes', '1Story', 2004, '', 'None', '', 200, 'GasA', 0, 'SBrkr', 1700, '', -1, 3, 2, 6, 0, -1, 0, 0, 100000]
    recommendation = database.getAllRecommendations()
    headers1 = ["Id", "MSZoning", "LotArea", "LandContour", "Utilities", "Neighborhood",
              "HouseStyle", "YearBuilt", "RoofStyle", "MasVnrType", "Foundation",
              "TotalBsmtSF", "Heating", "CentralAir", "Electrical", "GrLivArea",
              "TotalFullBath", "TotalHalfBath", "BedroomAbvGr", "KitchenAbvGr",
              "TotRmsAbvGrd", "Fireplaces", "GarageCars", "WoodDeckSF","Pool", "SalePrice"]
    headers2 = []
    data = pd.DataFrame(list(recommendation), columns = headers1)
    data_id = pd.DataFrame(data["Id"])
    data.drop("Id", axis=1, inplace=True)
    # Add the user information to the first line
    # print("re:",userList)
    print("re:",data)
    userinfo = []
    for i in range(0, len(userList)):
        if userList[i] != -1 and userList[i] != '':
            headers2.append(headers1[i + 1])
            userinfo.append(userList[i])
    print("re:",userinfo)
    print("re:",headers2)
    user = pd.DataFrame([userinfo],columns = headers2)
    data = data[headers2].copy()
    print("re:",user)
    print("re:",data)
    data = pd.concat([user, data])
    print("join:",data)
    # One-hot encoding
    data = pd.get_dummies(data)
    print("onehot:",data)
    # Data normalization
    scaler = MinMaxScaler()
    data = pd.DataFrame(scaler.fit_transform(data), columns=data.columns, index=data.index)
    print("minmax:",data,type(data))
    user = data[0:1].values
    dataArray = data[1:].values
    data = data[1:]
    print("user:",user,type(user))
    print("data:",data,type(data))
    # print("array:",data.values)
    similarity = CalculateSimilarity(user,dataArray)
    # print("sim:",similarity)
    # for i in range(1, len(data)):
    #     sim = CalculateSimilarity(user, data[i:i+1])
    #     print(data[i:i+1])
    #     similarity.append(sim[0][0])
    similar = pd.DataFrame({"similarity": similarity})
    print(similar)
    data = pd.concat([data_id, data, similar], axis=1)
    print("sim:",data)
    data = data.reindex(data['similarity'].abs().sort_values(ascending=True).index)
    print("re:",data)
    recommendation_id = np.array(data.head(12)['Id']).tolist()
    print("re:",recommendation_id)
    return recommendation_id

def CalculateSimilarity(user,data):
    # result = cosine_similarity(user.values.reshape(1, -1), data.values.reshape(1, -1))
    result = []
    for item in data:
        sim = 0
        x = 0
        for i in item:
            count = (user[0][x] - i) * (user[0][x] - i)
            sim += count
            x += 1
        sim = math.sqrt(sim)
        result.append(sim)
    # result = cosine_similarity(user,data)
    return result


