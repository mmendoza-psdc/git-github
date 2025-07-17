import os
from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

@app.get("/familia")
def get_familia():
    rows = ["Amin", "Marce", "Miranda"]
    return rows

@app.get("/superheroesDC")
def get_superheroes():
    rows = ["Superman", "Batman", "Flash", "Linterna Verde", "Mujer maravilla", "Aquaman", "Shazam", "Cyborg"]
    return rows

@app.get("/superheroesMarvel")
def get_superheroes_marvel():
    rows = ["Spider-Man", "Iron Man", "Thor", "Hulk", "Black Widow", "Doctor Strange", "Black Panther", "Captain America"]
    return rows

@app.get("/warriorsLOTR")
def get_warriors_lotr():
    rows = ["Frodo", "Sam", "Gandalf", "Aragorn", "Legolas", "Gimli", "Boromir", "Gollum"]
    return rows

@app.get("/warriorsGOT")
def get_warriors_got():
    rows = ["Jon Snow", "Daenerys Targaryen", "Arya Stark", "Tyrion Lannister", "Cersei Lannister", "Jaime Lannister", "Bran Stark", "Sansa Stark"]
    return rows
