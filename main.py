from fastapi import FastAPI

from pydantic import BaseModel

app = FastAPI()

app.counter = -1


class PatientRequest(BaseModel):
	name: str
	surename: str


class PatientResponse(BaseModel):
	id: int
	patient: PatientRequest


class HelloResp(BaseModel):
    msg: str


@app.get('/')
def hello_world() ->str:
    return {'message': 'Hello World during the coronavirus pandemic!'}

@app.get("/hello/{name}", response_model=HelloResp)
async def read_item(name: str) -> str:
    return HelloResp(msg=f"Hello {name}")

@app.post('/method')
def post_f() ->str:
	return {"method": "POST"}

@app.get('/method')
def get_f() ->str:
	return {"method": "GET"}

@app.put('/method')
def put_f() ->str:
	return {"method": "PUT"}

@app.delete('/method')
def del_f() ->str:
	return {"method": "DELETE"}

@app.post('/patient', response_model=PatientResponse)
def receive_pat(request: PatientRequest):
	app.counter += 1
	return PatientResponse(id=app.counter, patient=request)


