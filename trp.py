#fake api response
data = {"total_audience":10000,
        "shows":[
            {"name":"news 9pm", "audience": 2500},
            {"name": "starplus", "audience": 5000},
            {"name": "disney", "audience":4000},
            {"name": "sony", "audience": 8000}
        ]}
total_audience =data["total_audience"]
print("total audience:", total_audience)
for show in data["shows"]:
    name= show["name"]
    audience = show["audience"]
    trp = (audience/total_audience)*100
    print("show name:", name)
    print("trp:", trp)
    print("audience:", audience)
    if trp>=50:
        print("super hit")
