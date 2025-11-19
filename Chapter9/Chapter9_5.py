def process_teams(data):
    teams_raw = data.split("/")
    teams = []
    for t in teams_raw:
        name, wins, loss, draws, scored, conceded = t.split(",")
        wins, loss, draws, scored, conceded = map(int, [wins, loss, draws, scored, conceded])
        
        points = 3 * wins + draws
        gd = scored - conceded
        
        teams.append({
            "name": name.strip(),
            "points": points,
            "gd": gd
        })
    
    n = len(teams)
    for i in range(n-1):
        for j in range(n-1-i):
            a, b = teams[j], teams[j+1]
            if (a["points"] < b["points"]) or \
               (a["points"] == b["points"] and a["gd"] < b["gd"]):
                teams[j], teams[j+1] = teams[j+1], teams[j]
    
    results = []
    for t in teams:
        results.append([t["name"], {"points": t["points"]}, {"gd": t["gd"]}])
    
    return results


inp = input("Enter Input : ")
print("== results ==")
for r in process_teams(inp):
    print(r)
