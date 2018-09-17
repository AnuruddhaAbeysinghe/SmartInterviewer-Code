#-----For check whether function is working

# from BackEnd.Controller import CreateReward
#
# facial = 15
# voice = 15
# answer = 20
#
# userid = "uid001"
# langName = "python"
# nodeid = "6"
# category = "easy"
#
# CreateReward.rewardForQuestion(facial,voice,answer,userid,langName,nodeid,category)

#----For Integrate with sarindi--------------------------

def getLanguageName(getLang):
    global langName
    langName = getLang
    return langName
    #langName = "python"


def getNodeID(getNode):
    global nodeid
    nodeid = getNode
    return nodeid
    #nodeid = "6"

def getCategoryName(getCategory):
    global category
    category = getCategory
    return category
    #category = "easy"







