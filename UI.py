import streamlit as st
import requests

# Set RTL CSS for Arabic text
st.markdown("""
    <style>
    body {
        direction: rtl;
        text-align: right;
        font-family: 'Arial', sans-serif;
    }
    .stTextArea, .stButton, .stAlert {
        direction: rtl;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("تحليل المراجعات")
st.write("أدخل رأيك هنا للحصول على التحليل (الكلام غير العربي سيتم تجاهله)")

review = st.text_area("الرأي")

if st.button("توقع المشاعر"):
    if review.strip() == "":
        st.warning("يرجى إدخال رأيك.")
    else:
        try:
            with st.spinner("جارٍ التحليل..."):
                response = requests.post(
                    "http://127.0.0.1:5000/predict",
                    json={"review": review}
                )

                if response.status_code == 200:
                    result = response.json()
                    sentiment = result["prediction"]
                    st.success(f"المشاعر: **{sentiment}**")
                else:
                    st.error("فشل في الحصول على استجابة")
        except requests.exceptions.RequestException as e:
            print(f"Error connecting to Flask server: {e}")