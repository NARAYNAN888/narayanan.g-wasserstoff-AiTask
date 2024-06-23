from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from rag_cot import process_query_with_chain_of_thought

app = FastAPI()

@app.post("/query")
async def process_query(request: Request):
    data = await request.json()
    user_query = data['query']
    response = process_query_with_chain_of_thought(user_query)
    return JSONResponse(content={"response": response})

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
