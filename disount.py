import streamlit as st
st.title("แอพพลิเคชั่นคำนาณราคาสินค้ารวม")
price = st.number_input("กรอกราคาสินค้า(บาท):",value=0.0)
if price > 5000:
  discount = price * 0.10
  net_price = price - discount
  st.header(f"•ส่วนลด(discount=7%):**{vat:.2f}**บาท")
st.header(f"•ราคาสุทธิ:{net_price:.2f}บาท")
st.divider()
