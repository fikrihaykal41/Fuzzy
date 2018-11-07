import pandas as p

data = p.read_csv('DataTugas2.csv')

i = 0
#Fuzzification Income
#High Income
print("Fuzzification:")
scoreHighIncome = list()
for i in range(0,100):
    if data.loc[i].values[1] <= 1.25:
        scoreHighIncome.insert(i, 0)
    elif data.loc[i].values[1] > 1.5:
        scoreHighIncome.insert(i, 1)
    else:
        score = round((data.loc[i].values[1]-1.25)/(1.5-1.25),4)
        scoreHighIncome.insert(i, score)
print("High Income\n",scoreHighIncome)
print("==============================================================================================================="
      "================================================================")
#Low Income
scoreLowIncome = list()
for i in range(0,100):
    if data.loc[i].values[1] > 0.75:
        scoreLowIncome.insert(i, 0)
    elif data.loc[i].values[1] <= 0.5:
        scoreLowIncome.insert(i, 1)
    else:
        score = round((data.loc[i].values[1]-0.5)/(0.75-0.5),4)
        scoreLowIncome.insert(i, score)
print("Low Income\n",scoreLowIncome)
print("==============================================================================================================="
      "================================================================")
#Average Income
scoreAvgIncome = list()
for i in range(0,100):
    if data.loc[i].values[1] <= 0.5 or data.loc[i].values[1] > 1.5:
        scoreAvgIncome.insert(i, 0)
    elif 0.5 < data.loc[i].values[1] and data.loc[i].values[1] <= 0.75:
        score = round((data.loc[i].values[1]-0.5)/(0.75-0.5),4)
        scoreAvgIncome.insert(i, score)
    elif 0.75 < data.loc[i].values[1] and data.loc[i].values[1] <= 1.25:
        scoreAvgIncome.insert(i, 1)
    else:
        score = round((1.5-data.loc[i].values[1])/(1.5-1.25),4)
        scoreAvgIncome.insert(i, score)
print("Average Income\n",scoreAvgIncome)
print("==============================================================================================================="
      "================================================================")
#Fuzzification Debt
#High Debt
scoreHighDebt = list()
for i in range(0,100):
    if data.loc[i].values[2] <= 75:
        scoreHighDebt.insert(i, 0)
    elif data.loc[i].values[2] > 80:
        scoreHighDebt.insert(i, 1)
    else:
        score = round((data.loc[i].values[2]-75)/(80-75),4)
        scoreHighDebt.insert(i, score)
print("High Debt\n",scoreHighDebt)
print("==============================================================================================================="
      "================================================================")
#Low Debt
scoreLowDebt = list()
for i in range(0,100):
    if data.loc[i].values[2] > 65:
        scoreLowDebt.insert(i, 0)
    elif data.loc[i].values[2] <= 60:
        scoreLowDebt.insert(i, 1)
    else:
        score = round((data.loc[i].values[2]-60)/(65-60),4)
        scoreLowDebt.insert(i, score)
print("Low Debt\n",scoreLowDebt)
print("==============================================================================================================="
      "================================================================")
#Average Debt
scoreAvgDebt = list()
for i in range(0,100):
    if data.loc[i].values[2] <= 60 or data.loc[i].values[2] > 80:
        scoreAvgDebt.insert(i, 0)
    elif 60 < data.loc[i].values[2] and data.loc[i].values[2] <= 65:
        score = round((data.loc[i].values[2]-60)/(65-60),4)
        scoreAvgDebt.insert(i, score)
    elif 65 < data.loc[i].values[2] and data.loc[i].values[2] <= 75:
        scoreAvgDebt.insert(i, 1)
    else:
        score = round((80-data.loc[i].values[2])/(80-75),4)
        scoreAvgDebt.insert(i, score)
print("Average Debt\n",scoreAvgDebt)
print("==============================================================================================================="
      "================================================================")
#Inference
print("Inference:")
scoreDecision = list()
count1 = 0
count2 = 0
count3 = 0
for i in range(0,100):
    if (scoreLowIncome[i] > scoreHighDebt[i]) or (scoreLowIncome[i] > scoreAvgDebt[i]):
        scoreDecision.insert(i, "Accepted")
        count1 += 1
        print(scoreDecision[i],":",scoreLowIncome[i])
    elif (scoreAvgIncome[i] > scoreHighDebt[i]) or (scoreAvgIncome[i] > scoreAvgDebt[i]) or\
            (scoreLowIncome[i] > scoreLowDebt[i]):
        scoreDecision.insert(i, "Considered")
        count2 += 1
        print(scoreDecision[i],":",scoreAvgIncome[i])
    else:
        scoreDecision.insert(i,"Rejected")
        count3 += 1
        print(scoreDecision[i],":", scoreHighIncome[i])
print("\nAccepted:",count1)
print("Considered:",count2)
print("Rejected:",count3)
print("==============================================================================================================="
      "================================================================")
#Defuzzification Sugeno-Style
print("Deffuzification Sugeno-Style:")
count4 = 0
count5 = 0
count6 = 0
result = list()
for i in range(0,100):
    if scoreDecision[i] == "Accepted":
        count4 += 1
    elif scoreDecision[i] == "Considered":
        count5 += 1
    else:
        count6 += 1
    score = ((scoreLowIncome[i]*100)+(scoreAvgIncome[i]*50)+(scoreHighIncome[i]*30))\
                 /(scoreHighIncome[i]+scoreAvgIncome[i]+scoreLowIncome[i])
    result.insert(i,score)
    print(scoreDecision[i],round(data.loc[i].values[1],4),round(data.loc[i].values[2],4),scoreLowIncome[i],scoreAvgIncome[i],scoreHighIncome[i],"Result:",round(result[i],4))
print("\nAccepted:",count4)
print("Considered:",count5)
print("Rejected:",count6)
print("==============================================================================================================="
      "================================================================")
j = 0
temp = list()
temp2 = list()
temp3 = list()
temp4 = list()
temp5 = list()
temp6 = list()
for i in range(0,20):
    for j in range(0,100):
        if scoreDecision[j] == "Accepted":
            temp5.append(data.loc[j].values[0])
            temp.append(scoreDecision[j])
            temp2.append(round(data.loc[j].values[1],4))
            temp3.append(round(data.loc[j].values[2],4))
            temp4.append(round(result[j],4))
            if result[j] == 100.0:
                temp6.append("Sangat Layak")
            else:
                temp6.append("Layak")
    print("No:",temp5[i],"|",temp[i],"|",temp2[i],"|",temp3[i],"Result:",temp4[i],"|",temp6[i])
# raw_data = {'no': temp5,
#             'pendapatan': temp2,
#             'hutang': temp3,
#             'nilai keputusan': temp4,
#             'keputusan': temp6}
# hasil = p.DataFrame(raw_data, columns = ['no', 'pendapatan', 'hutang', 'nilai keputusan', 'keputusan'])
# hasil.to_csv('TebakanTugas2.csv', index=False, mode='a')