import streamlit as st
import os
def xor_encrypt_decrypt(data, key):
    data_bytes = data.encode('utf-8')
    key_bytes = key.encode('utf-8')
    decrypted_bytes = bytearray()
    for i in range(len(data_bytes)):
        decrypted_byte = data_bytes[i] ^ key_bytes[i % len(key_bytes)]
        decrypted_bytes.append(decrypted_byte)
    return decrypted_bytes.decode('utf-8', errors='ignore')
def main():
    texts_folder = 'texts_folder'
    text_files = os.listdir(texts_folder)
    if not text_files:
        st.error("Нет текстовых документов в указанной папке.")
        return
    if 'current_file_index' not in st.session_state:
        st.session_state.current_file_index = 0
    current_file_index = st.session_state.current_file_index
    if current_file_index < len(text_files):
        current_text_file = os.path.join(texts_folder, text_files[current_file_index])
        with open(current_text_file, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            question = lines[0].strip()
            encrypted_text = ''.join(lines[1:]).strip()
        st.header(f"Вопрос: {question}")
        # Пользователь вводит ответ (ключ для дешифрования)
        answer = st.text_input("Введите ответ на вопрос (как ключ для дешифрования):", key=f"answer_{current_file_index}")
        if st.button("Дешифровать текст"):
            if answer:
                decrypted_text = xor_encrypt_decrypt(encrypted_text, answer)
                st.success("Дешифрованный текст:")
                st.text_area("Текст", value=decrypted_text)
            else:
                st.warning("Введите ответ на вопрос.")
        if st.button("Следующий вопрос"):
            # Переходим к следующему вопросу
            st.session_state.current_file_index += 1
            st.experimental_rerun()
    else:
        st.write("Вопросы закончились.")
if __name__ == "__main__":
    main()
