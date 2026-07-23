import streamlit as st
st.title("แอพพลิเคชั่นคำนาณราคาสินค้ารวมvat7%")
price = st.number_input("กรอกราคาสินค้า(บาท):",value=0.0)
vat = price * 0.07
net.price = price - value
st.header(f"•ภาษีมูลค่า(vat=7%):**{vat:.2f}**บาท")
st.header(f"•ราคาสุทธิ:{net_price:.2f}บาท")
st.divider()
st.write("นาย ดิฐธนา สุระธนาจิต เลขที่ 25  ม.4/13")
