#!/usr/bin/env python
import uvicorn
from fastapi import FastAPI


app = FastAPI()

def main():
    uvicorn.run("main:app")


if __name__ == "__main__":
    main()
