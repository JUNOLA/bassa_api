# 🚀 French ↔ Bassa Translation API

## 📌 Overview

This project provides a REST API powered by **FastAPI** for translating text between **French** and **Bassa** (a Bantu language spoken in Cameroon). The translation model is a custom-trained **MarianMT** model hosted on **Google Drive** and loaded dynamically at runtime.

It can be integrated into **Flutter mobile** and **web** apps via HTTP requests.

---

## 🧱 System Architecture

```
Flutter App (mobile/web)
        ↓
  [ HTTP POST Request ]
        ↓
┌──────────────────────┐
│     FastAPI Server    │
└──────────────────────┘
        ↓
 [ Load MarianMT model ]
        ↓
   [ Tokenizer + Inference ]
        ↓
 [ JSON Response with Translation ]
```

---

## 🧱 System Architecture

```mermaid
flowchart TD
    A[Flutter App\n(mobile/web)]
    B[HTTP POST Request]
    C[FastAPI Server]
    D[Load MarianMT Model]
    E[Tokenizer + Inference]
    F[JSON Response with Translation]
    
    A -->|Sends text and\ndirection| B
    B -->|Routes to\n/translate endpoint| C
    C -->|Checks if model\nis loaded| D
    D -->|Initializes tokenizer\nand model| E
    E -->|Generates translation\nusing transformer| F
    F -->|Returns translated text\nin JSON format| A
```

---

## ⚙️ Local Development Setup

```bash
git clone https://github.com/your-user/bassa_translate_api.git
cd bassa_translate_api
pip install -r requirements.txt
uvicorn main:app --reload
```

API available at: `http://127.0.0.1:8000/docs`

---

## 🔁 API Endpoints

### `POST /translate`

**Description:** Translates text from French ↔ Bassa.

**Request (JSON):**

```json
{
  "text": "Bonjour, comment vas-tu ?",
  "direction": "Fr → Bs"
}
```

**Response (JSON):**

```json
{
  "translation": "Mbɔtɔ, wa kɛ?"
}
```

**Valid `direction` values:**

* `"Fr → Bs"` (French to Bassa)
* `"Bs → Fr"` (Bassa to French)

---

## 📱 Flutter Integration (Mobile & Web)

### Add `http` package

```yaml
dependencies:
  http: ^0.13.5
```

### Sample Code

```dart
import 'dart:convert';
import 'package:http/http.dart' as http;

Future<String> translateText(String text, String direction) async {
  final url = Uri.parse("https://your-api-url.onrender.com/translate");

  final response = await http.post(
    url,
    headers: {"Content-Type": "application/json"},
    body: jsonEncode({"text": text, "direction": direction}),
  );

  if (response.statusCode == 200) {
    return jsonDecode(response.body)['translation'];
  } else {
    throw Exception("Failed to translate text");
  }
}
```

### Example Usage in UI

```dart
String result = await translateText("Bonjour", "Fr → Bs");
print(result);
```

---

## 🚀 Deployment on Render (Free Hosting)

1. Push your project to a public GitHub repo
2. Go to [https://render.com](https://render.com)
3. Create a new Web Service:

   * Environment: Python
   * Build command: `pip install -r requirements.txt`
   * Start command: `bash start.sh`
   * Port: `10000`

Render will provide you a public URL (e.g., `https://your-api-url.onrender.com`)

---

## 🔐 Optional Features

* API key authentication (`X-API-KEY` header)
* Rate limiting (e.g., max 50 requests/min/user)
* Logging & Monitoring (e.g., with Sentry, Prometheus)

---

## 🧠 Future Features

* [ ] English ↔ Bassa (En ↔ Bs)
* [ ] German ↔ Bassa (De ↔ Bs)
* [ ] Admin dashboard to upload new models
* [ ] Real-time translation via WebSockets

---

## 📄 License & Credits

* MarianMT Model trained by you
* Based on Hugging Face Transformers
* Hosted via Render or Hugging Face Spaces

---

For support or contributions, contact: `your-email@example.com`
