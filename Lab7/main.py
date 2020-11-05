import numpy as np
import pandas as pd

# Sieć neuronowa z jednym neuronem na wejściu
## Implementacja bramki logicznej AND
X = np.vstack([(0, 0), (0, 1), (1, 0), (1, 1)])
datasetAND = pd.DataFrame(X, columns={"X1", "X2"})

andValues = []
functionValues = []
for i in X:
    wynik = i[0] and i[1]
    andValues.append(wynik)
    function_result = -1.5 + i[0] + i[1]
    functionValues.append(function_result)

datasetAND["AND"] = andValues
datasetAND["-1,5+X1+X2"] = functionValues
datasetAND["a"] = andValues
print(datasetAND, "\n")

## Implementacja bramki logicznej OR
datasetOR = pd.DataFrame(X, columns={"X1", "X2"})

orValues = []
function2Values = []
for i in X:
    result = i[0] or i[1]
    orValues.append(result)
    function_result = -0.5 + i[0] + i[1]
    function2Values.append(function_result)

datasetOR["OR"] = orValues
datasetOR["-0,5+X1+X2"] = function2Values
datasetOR["a"] = orValues
print(datasetOR, "\n")

## Implementacja bramki logicznej NOT
X = np.vstack([0, 1])
datasetNOT = pd.DataFrame(X, columns={"X1"})

notValues = []
function3Values = []
for i in X:
    result = not i
    notValues.append(int(result))
    function_result = int(1 - 2*i)
    function3Values.append(function_result)

datasetNOT["NOT"] = notValues
datasetNOT["1-2*X1"] = function3Values
datasetNOT["a"] = notValues
print(datasetNOT, "\n")

## Implementacja bramki logicznej XOR
X = np.vstack([(0, 0), (0, 1), (1, 0), (1, 1)])
datasetXOR = pd.DataFrame(X, columns={"X1", "X2"})

xorValues = []
function4Values = []
for i in X:
    result = i[0] or i[1]
    if i[0] and i[1] == 1:
        result = 0
        xorValues.append(result)
    else:
        xorValues.append(result)
    function_result = -0.5 + i[0] + i[1]
    function4Values.append(function_result)

datasetXOR["XOR"] = xorValues
datasetXOR["-0,5+X1+X2"] = function4Values
datasetXOR["a"] = xorValues
print(datasetXOR, "\n")

## Implementacja bramki logicznej XNOR
X = np.vstack([(0, 0), (0, 1), (1, 0), (1, 1)])
datasetXNOR = pd.DataFrame(X, columns={"X1", "X2"})

xnorValues = []
function5Values = []
for i in X:
    result = not(i[0] or i[1])
    if i[0] and i[1] == 1:
        result = 1
        xnorValues.append(int(result))
    else:
        xnorValues.append(int(result))
    function_result = -0.5 + i[0] + i[1]
    function5Values.append(function_result)

datasetXNOR["XNOR"] = xnorValues
datasetXNOR["-0,5+X1+X2"] = function5Values
datasetXNOR["a"] = xnorValues
print(datasetXNOR, "\n")

