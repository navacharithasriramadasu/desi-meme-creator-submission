import streamlit as st
from PIL import Image, ImageDraw, ImageFont
import os
import pandas as pd
from datetime import datetime
from googletrans import Translator

TEMPLATE_DIR = "assets/templates/"
CORPUS_FILE = "data/corpus.csv"

translator = Translator()
LANG_CODES = {
    "English": "en", "Hindi": "hi", "Telugu": "te", "Tamil": "ta",
    "Kannada": "kn", "Malayalam": "ml", "Gujarati": "gu",
    "Bengali": "bn", "Marathi": "mr", "Punjabi": "pa"
}
FONT_FILES = {
    "English": "assets/fonts/NotoSans-Regular.ttf",
    "Hindi": "assets/fonts/NotoSansDevanagari-Regular.ttf",
    "Telugu": "assets/fonts/NotoSansTelugu-Regular.ttf",
    "Tamil": "assets/fonts/NotoSansTamil-Regular.ttf",
    "Kannada": "assets/fonts/NotoSansKannada-Regular.ttf",
    "Malayalam": "assets/fonts/NotoSansMalayalam-Regular.ttf",
    "Gujarati": "assets/fonts/NotoSansGujarati-Regular.ttf",
    "Bengali": "assets/fonts/NotoSansBengali-Regular.ttf",
    "Marathi": "assets/fonts/NotoSansDevanagari-Regular.ttf",
    "Punjabi": "assets/fonts/NotoSansGurmukhi-Regular.ttf",
}
def translate_caption(caption, target_lang):
    if target_lang == "English": return caption
    try: return translator.translate(caption, dest=LANG_CODES[target_lang]).text
    except Exception: return caption
def generate_meme(template_path, caption, language):
    img = Image.open(template_path).convert("RGB")
    draw = ImageDraw.Draw(img)
    font_path = FONT_FILES.get(language, FONT_FILES["English"])
    
    if not os.path.exists(font_path):
        st.error(f"Font file not found: {font_path}")
        return img

    font = ImageFont.truetype(font_path, 40)
    W, H = img.size
    bbox = draw.textbbox((0, 0), caption, font=font)
    w, h = bbox[2] - bbox[0], bbox[3] - bbox[1]
    draw.text(((W - w) / 2, H - h - 20), caption, fill="white", font=font,
              stroke_width=2, stroke_fill="black")
    return img


def save_to_corpus(caption, language, template):
    new_row = pd.DataFrame([{"timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                             "caption": caption, "language": language, "template": template}])
    os.makedirs(os.path.dirname(CORPUS_FILE), exist_ok=True)
    if os.path.exists(CORPUS_FILE): new_row.to_csv(CORPUS_FILE, mode="a", header=False, index=False)
    else: new_row.to_csv(CORPUS_FILE, mode="w", header=True, index=False)
st.set_page_config(page_title="🎭 Desi Meme Creator", layout="wide")
st.title("🎭 Desi Meme Creator (Multilingual)")
st.markdown("Create memes in any Indian language! Type caption in English, select language, choose template, generate meme.")
caption = st.text_input("Enter your caption in English")
language = st.selectbox("Choose language", list(LANG_CODES.keys()))
template_files = os.listdir(TEMPLATE_DIR)
template_choice = st.selectbox("Choose a template", template_files)
if st.button("Generate Meme"):
    if caption:
        final_caption = translate_caption(caption, language)
        template_path = os.path.join(TEMPLATE_DIR, template_choice)
        meme = generate_meme(template_path, final_caption, language)
        st.image(meme, caption=f"Meme in {language}", use_column_width=True)
        save_to_corpus(final_caption, language, template_choice)
        st.success("Meme generated and caption saved to corpus!")
    else: st.warning("Please enter a caption first!")