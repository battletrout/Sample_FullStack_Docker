#Create and deploy a simple docker frontend and backend

##From Nelson's Docker full stack tutorial: 
https://www.youtube.com/watch?v=Jx39roFmTNg

Backend in simple "Person" list in FastAPI, uses pydantic BaseModel. Front end is in React JS.

###Create a docker network 
docker network create foobar

###Build and deploy Backend:
cd /backend
docker build . -t backend
docker run --name backend --network foobar --rm -p 8000:8000 backend

###Build and deploy Frontend:
cd /frontend
docker build . -t frontend
docker run --rm --name frontend --network foobar -p 3000:3000 frontend