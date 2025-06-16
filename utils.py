import os
import gdown

def download_model_from_drive(folder_id, dest_path="./model"):
    os.makedirs(dest_path, exist_ok=True)
    print("Téléchargement du modèle depuis Google Drive...")

    # URL pour télécharger tous les fichiers
    url = f"https://drive.google.com/drive/folders/{folder_id}"
    gdown.download_folder(url=url, output=dest_path, quiet=False, use_cookies=False)

    print("Modèle téléchargé.")

