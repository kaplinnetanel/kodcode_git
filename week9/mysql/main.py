from fastapi import FastAPI,HTTPException,Query
import queries
import uvicorn
import db 

app = FastAPI()


@app.get("/soldiers/units")
def get_by_units():
    return {"units":queries.get_distinct_units()}

@app.get("/soldiers/search")
def get_soldiers_by_search(name:str):
    return queries.search_by_name(name)


@app.get("/soldiers")
def get_soldiers_private(rank :str | None = Query(default= None),
                         sort : str |None = Query(default= None) , 
                         unit: str | None = Query(default= None) ):
    if rank:
        return {"soldiers": queries.get_by_rank(rank)}
    
    elif sort:
        return {"soldiers": queries.get_active_sorted(sort)}
    
    elif unit:
        return {"soldiers": queries.get_by_unit(unit)}
    
    else:
        return {"soldiers": db.get_all() }



@app.get("/soldiers/{soldier_id}") 
def get_soldier(soldier_id: int): 
    soldier = db.get_by_id(soldier_id) 
    if soldier is None: 
        raise HTTPException(status_code=404, detail="Soldier not found") 
    return soldier

@app.post("/soldiers", status_code=201) 
def add_soldier(body: dict): 
    new_id = db.create(body["name"], body["rank"], body["unit"]) 
    return {"id": new_id, "message": "Soldier created"}


@app.put("/soldiers/{soldier_id}")
def edit_soldier(soldier_id: int, body: dict):
    data = body.model_dump(exclude_none=True)
    if not data:
        raise HTTPException(status_code=400, detail="No data provided for update")
        
    success = db.update(soldier_id, data)
    if not success:
        raise HTTPException(status_code=404, detail="Soldier not found")
    return {"message": "Updated"}

@app.delete("/soldiers/{soldier_id}")
def remove_soldier(soldier_id: int):
    success = db.delete(soldier_id)
    if not success:
        raise HTTPException(status_code=404, detail="Soldier not found")
    return {"message": "Deleted"}