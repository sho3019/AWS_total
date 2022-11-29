import json 
import calc

json_open = open('../sample.json', 'r')
json_load = json.load(json_open)


json_load["calc"] = calc.ans

json_result = open('output.json', 'w')
json.dump(json_load, json_result, indent = 4)

