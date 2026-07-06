import streamlit as st
from openai import OpenAI

# 1. Konfigurasi Halaman Streamlit
st.set_page_config(page_title="Chatbot Keren", page_icon="🤖")
st.title("🤖 Chatbot Pintar")
st.write("Halo! Ada yang bisa saya bantu hari ini?")

# 2. Inisialisasi API Key (Ganti dengan API key Anda atau gunakan Secrets)
openai_api_key = st.sidebar.text_input("Masukkan OpenAI API Key Anda:", type="password")

# 3. Inisialisasi Riwayat Obrolan (Session State)
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Halo! Saya adalah AI asistenmu. Silakan tanya apa saja."}
    ]

# 4. Menampilkan Pesan dari Riwayat Obrolan
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# 5. Menangani Input Pengguna
if prompt := st.chat_input("Ketik pesan Anda di sini..."):
    
    # Validasi jika API key belum diisi
    if not openai_api_key:
        st.info("Silakan masukkan OpenAI API Key Anda di sidebar untuk memulai.")
        st.stop()

    # Tampilkan pesan pengguna di layar
    with st.chat_message("user"):
        st.write(prompt)
    
    # Simpan pesan pengguna ke dalam riwayat
    st.session_state.messages.append({"role": "user", "content": prompt})

    # 6. Mengirim Permintaan ke OpenAI API dan Menampilkan Respon
    try:
        client = OpenAI(api_key=openai_api_key)
        
        with st.chat_message("assistant"):
            with st.spinner("Sedang berpikir..."):
                # Memanggil API dengan membawa seluruh riwayat percakapan agar bot ingat konteks
                response = client.chat.completions.create(
                    model="gpt-4o-mini", # Menggunakan model gpt-4o-mini yang cepat dan hemat biaya
                    messages=[
                        {"role": m["role"], "content": m["content"]}
                        for m in st.session_state.messages
                    ]
                )
                output_text = response.choices[0].message.content
                st.write(output_text)
                
        # Simpan respon bot ke dalam riwayat
        st.session_state.messages.append({"role": "assistant", "content": output_text})
        
    except Exception as e:
        st.error(f"Terjadi kesalahan: {e}")
