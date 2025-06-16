from fastapi import FastAPI
from pydantic import BaseModel
from transformers import MarianMTModel, MarianTokenizer
import torch
from utils import download_model_from_drive

# ID de ton dossier Drive
FOLDER_ID = "1jDdj95HR70OeK-gohnx05nFBMhF9iux0"

# Télécharger le modèle
download_model_from_drive(FOLDER_ID)

# Charger le modèle
model_path = "./model/checkpoint-3295"
tokenizer = MarianTokenizer.from_pretrained(model_path)
model = MarianMTModel.from_pretrained(model_path)

# API
app = FastAPI()

class TranslationInput(BaseModel):
    text: str
    direction: str  # "Fr → Bs" ou "Bs → Fr"

@app.post("/translate")
def translate_text(input: TranslationInput):
    if input.direction == "Fr → Bs":
        src, tgt = "fr", "bs"
    else:
        src, tgt = "bs", "fr"

    tokens = tokenizer(input.text, return_tensors="pt", padding=True)
    ids = model.generate(**tokens, max_length=128)
    output = tokenizer.decode(ids[0], skip_special_tokens=True)
    return {"translation": output}
