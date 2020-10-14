# Return values for a specific key from a nested dictionnary
# Arguments:
#   nestedDict: a nested dictionary
#   searchedKey: searched Key Name, if not set will return all values
# 
# How to use it:
#   {{ myDictionary | getValuesNestedDict('myKey') }}

from jinja2 import TemplateError

class FilterModule(object):

    def getValuesNestedDict(self, nestedDict, searchedKey=None):

        valueList = []

        def extract(nestedDict, searchedKey, valueList):
            if isinstance(nestedDict, dict):
                for id, item in nestedDict.items():
                    if isinstance(item, dict):
                        extract(item, searchedKey, valueList)
                    elif id == searchedKey or not searchedKey:
                        valueList.append(item)
            return valueList
        
        values = extract(nestedDict, searchedKey, valueList)
        return values
    
    def filters(self):
        return { 'getValuesNestedDict': self.getValuesNestedDict }