from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "面试机器人后端已启动"}


@app.get("/question")
def get_question():
    return {"question": "请做一下自我介绍。"}