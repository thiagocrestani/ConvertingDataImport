import json
f = open('source_file_2.json')
data = json.load(f)
f.close()
managers = {}
watchers = {}

def sortSecond(val): 
    return val[1]

for item in data:
    for manager in item['managers']:
        if manager not in managers:
            managers[manager] = []
        managers[manager].append((item['name'],item['priority']))
    
    for watcher in item['watchers']:
        if watcher not in watchers:
            watchers[watcher] = []
        watchers[watcher].append((item['name'],item['priority']))


for manager in managers:  
    managers[watcher].sort(key = sortSecond)
    for i in range(0, len(managers[manager])):
        managers[manager][i] = managers[manager][i][0]
    
for watcher in watchers:  
    watchers[watcher].sort(key = sortSecond)
    for i in range(0, len(watchers[watcher])):
        watchers[watcher][i] = watchers[watcher][i][0]
   
with open('manager.json', 'w') as outfile:
    json.dump(managers, outfile, indent=4)

with open('watchers.json', 'w') as outfile:
    json.dump(watchers, outfile, indent=4)
