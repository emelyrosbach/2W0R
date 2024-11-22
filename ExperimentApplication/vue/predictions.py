class AIPredictions():
    def getAIPredictions():
        AIpredictions = {
            "10": "22",
            "11": "50",
            "12": "40",
            "13": "76",
            "14": "70",
            "15": "64",
            "16": "37",
            "17": "90",
            "18": "90",
            "19": "91",
            "20": "27",
            "21": "28",
            "22": "56",
            "23": "59",
            "24": "95",
            "25": "20",
            "26": "61",
            "27": "30",
            "28": "83",
            "29": "86",
        } 
        return AIpredictions
    
    def getAITumorCellCount():
        AIpredictions = {
            "10": "20",
            "11": "690",
            "12": "661",
            "13": "1129",
            "14": "100",
            "15": "51",
            "16": "39",
            "17": "87",
            "18": "320",
            "19": "279",
            "20": "384",
            "21": "416",
            "22": "68",
            "23": "860",
            "24": "134",
            "25": "17",
            "26": "56",
            "27": "449",
            "28": "297",
            "29": "244",
        } 
        return AIpredictions
    
    def getAITotalCellCount():
        AIpredictions = {
            "10": "91",
            "11": "1381",
            "12": "1633",
            "13": "1482",
            "14": "142",
            "15": "80",
            "16": "106",
            "17": "97",
            "18": "355",
            "19": "308",
            "20": "1449",
            "21": "1480",
            "22": "121",
            "23": "1448",
            "24": "141",
            "25": "86",
            "26": "92",
            "27": "1513",
            "28": "358",
            "29": "283",
        } 
        return AIpredictions
    
class TrainingAIPredictions():
    def getTrainingAIPredictions():
        TrainingAIpredictions = {
            0: "53",
            1: "56",
            2: "87",
        } 
        return TrainingAIpredictions
    
    def getTrainingAITumorCellCount():
        TrainingAIpredictions = {
            0: "72",
            1: "780",
            2: "222",
        } 
        return TrainingAIpredictions
    
    def getTrainingAITotalCellCount():
        TrainingAIpredictions = {
            0: "137",
            1: "1382",
            2: "255",
        } 
        return TrainingAIpredictions 
    
class GroundTruth():
    def getGroundTruth(key):
        GT = {
            "10": 30,
            "11": 44,
            "12": 63,
            "13": 72,
            "14": 19,
            "15": 15,
            "16": 61,
            "17": 88,
            "18": 86,
            "19": 90,
            "20": 28,
            "21": 49,
            "22": 60,
            "23": 71,
            "24": 14,
            "25": 11,
            "26": 55,
            "27": 22,
            "28": 82,
            "29": 91,
        } 
        return GT.get(key)
