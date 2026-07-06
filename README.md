# 🤖 Kawan AI - Chatbot Pintar

Aplikasi chatbot interaktif berbasis Streamlit yang menggunakan OpenAI API (GPT-4o-mini) untuk memberikan respons yang cerdas dan kontekstual.

## ✨ Fitur

- 💬 Chat interaktif dengan AI
- 🧠 Mempertahankan konteks percakapan
- ⚡ Menggunakan model GPT-4o-mini (cepat & hemat biaya)
- 🎨 Interface yang user-friendly dengan Streamlit
- 🔐 Input API Key yang aman

## 🚀 Cara Memulai

### 1. Clone Repository
```bash
git clone https://github.com/fitridafa727-ai/my-first-project.git
cd my-first-project
```

### 2. Buat Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# atau
venv\Scripts\activate  # Windows
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Jalankan Aplikasi
```bash
streamlit run app.py
```

Aplikasi akan membuka di browser pada `http://localhost:8501`

## 🔑 Konfigurasi API Key

Ada 2 cara untuk menggunakan API Key:

### Cara 1: Input Manual (Sementara)
- Masukkan OpenAI API Key Anda di sidebar saat aplikasi berjalan
- Cocok untuk testing dan development

### Cara 2: Menggunakan Streamlit Secrets (Permanent)
1. Buat folder `.streamlit` di root project
2. Buat file `secrets.toml` di dalam folder tersebut:
```toml
OPENAI_API_KEY = "sk-your-api-key-here"
```
3. Ubah kode `app.py` untuk menggunakan secrets:
```python
openai_api_key = st.secrets.get("OPENAI_API_KEY", "")
```

## 📋 Requirements

- Python 3.8+
- OpenAI API Key (dapatkan dari [platform.openai.com](https://platform.openai.com))

## 📦 Dependencies

- `streamlit` - Framework untuk membuat web app
- `openai` - Library resmi OpenAI Python

## 🛠️ Troubleshooting

### Error: "Invalid API Key"
- Pastikan API Key Anda benar dan memiliki akses ke model GPT-4o-mini
- Cek saldo/quota di dashboard OpenAI

### Error: "Model not available"
- Pastikan akun OpenAI Anda memiliki akses ke model `gpt-4o-mini`
- Model ini mungkin tidak tersedia di semua region

### Error: "Rate limit exceeded"
- Tunggu beberapa saat sebelum mengirim pesan baru
- Pertimbangkan upgrade plan OpenAI untuk rate limit lebih tinggi

## 📝 Lisensi

MIT License - Silakan gunakan dan modifikasi sesuai kebutuhan

## 👥 Kontribusi

Pull requests sangat diterima! Untuk perubahan besar, silakan buka issue terlebih dahulu untuk mendiskusikan perubahan yang ingin dilakukan.

---

**Dibuat dengan ❤️ menggunakan Streamlit & OpenAI**
