'''
returns a dict with keys: names values: [datapoints]
'''
def splitDatasetByNames(dataSet):
    names=[]
    out = {}
    for i,dp in enumerate(dataSet):
        if dp[1] not in names:
            names.append[dp[1]]
            out[dp[1]] = [dp]
        else:
            out[dp[1]].append(dp)
    return out
    