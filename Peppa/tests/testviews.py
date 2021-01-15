from fastapi import FastAPI, APIRouter
import uvicorn


class testviews():
    @FastAPI.get("/test1", summary="测试1")
    def Test2():
        return {"data": "1", "Person": "周杰伦"}


app = FastAPI()
test = testviews(app)


@app.get("/test", summary="测试")
def Test():
    return {"data": "1", "Person": "周杰伦"}


if __name__ == "__main__":

    uvicorn.run(app='testviews:app',
                host="127.0.0.1",
                port=3333,
                reload=True,
                debug=True)
