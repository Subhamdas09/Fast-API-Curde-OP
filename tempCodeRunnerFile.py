@app.post("/teas")  #add a new tea
def add_tea(tea: Tea):
    teas.append(tea)
    return tea