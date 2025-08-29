def maximum_units(boxTypes, truckSize):
    boxTypes = sorted(boxTypes, key=lambda x : x[1], reverse=True)
    index = 0
    number_of_units = 0
    while truckSize > 0:
        units = 0
        if boxTypes[index][0] <= truckSize:
            number_of_units += boxTypes[index][1] * boxTypes[index][0]
            truckSize -= boxTypes[index][0]
        else:
            number_of_units += truckSize * boxTypes[index][1]
            truckSize = 0

        index += 1

    return number_of_units

boxTypes = [[5,10],[2,5],[4,7],[3,9]]
truckSize = 10
result = maximum_units(boxTypes, truckSize)
print(result)