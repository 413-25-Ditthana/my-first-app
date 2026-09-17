import streamlit as st

st.title("แอพพลิเคชั่นคำนวณราคาสินค้ารวม")

price = st.number_input("กรอกราคาสินค้า (บาท):", value=0.0, step=100.0)

# คำนวณส่วนลดตามเงื่อนไข (ส่วนลด 10% เมื่อซื้อเกิน 5,000 บาท)
if price > 5000:
    discount = price * 0.10
else:
    discount = 0.0

net_price = price - discount

# แสดงผลลัพธ์
if discount > 0:
    st.write(f"• ส่วนลด (10%): **{discount:.2f}** บาท")

st.header(f"• ราคาสุทธิ: **{net_price:,.2f}** บาท")
st.divider()
