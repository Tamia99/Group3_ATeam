import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics.pairwise import cosine_similarity
import database

def recommendationSysAlgorithm(userList):
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
    print(userList)
    print(data)
    userinfo = []
    for i in range(0, len(userList)):
        if userList[i] != -1 and userList[i] != '':
            headers2.append(headers1[i + 1])
            userinfo.append(userList[i])
    print(userinfo)
    print(headers2)
    user = pd.DataFrame([userinfo],columns = headers2)
    data = data[headers2].copy()
    print(user)
    print(data)
    data = pd.concat([user, data])
    # One-hot encoding
    data = pd.get_dummies(data)
    # Data normalization
    scaler = MinMaxScaler()
    data = pd.DataFrame(scaler.fit_transform(data), columns=data.columns, index=data.index)
    user = data.iloc[0]
    data = data.iloc[1:]
    similarity = []
    for i in range(0, len(data)):
        sim = CalculateSimilarity(user, data.iloc[i])
        similarity.append(sim[0][0])
    similar = pd.DataFrame({'similarity': similarity})
    data = pd.concat([data_id, data, similar], axis=1)
    data = data.reindex(data['similarity'].abs().sort_values(ascending=False).index)
    recommendation_id = np.array(data.head(10)['Id']).tolist()
    print(recommendation_id)
    return recommendation_id

def CalculateSimilarity(user, data):
    result = cosine_similarity(user.values.reshape(1, -1), data.values.reshape(1, -1))
    return result


