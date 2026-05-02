import streamlit as st
import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt
import plotly.graph_objects as go
from datetime import datetime, timedelta

# 1. KONFIGURASI HALAMAN
st.set_page_config(page_title="InvestTrack Pro - Haidar", layout="wide")

# 2. FUNGSI AMBIL HARGA
def get_live_price(ticker):
    try:
        return yf.Ticker(ticker).fast_info['last_price']
    except:
        return 0

# 3. HEADER
st.set_page_config(page_title="FinSight - Wealth Dashboard", layout="wide")
st.title("🏛️ FinSight: Personal Wealth Analytics")
st.markdown("""
    *Dashboard ini adalah alat bantu pengambilan keputusan investasi yang mengintegrasikan data pasar real-time 
    dengan strategi manajemen risiko seperti Average Down Calculator.*
""")

# 4. SIDEBAR (Gabungan Update Manual & Average Down)
st.sidebar.header("⚙️ Update Data Harian")
cuan_danamas = st.sidebar.number_input("Untung Danamas (%)", value=0.15, step=0.01)
cuan_majoris = st.sidebar.number_input("Untung Majoris (%)", value=0.08, step=0.01)
kupon_sbr = st.sidebar.number_input("Kupon SBR Cair (Rp)", value=100000)

st.sidebar.markdown("---")
st.sidebar.header("🧮 Average Down Calculator")
# Ambil data BBRI sebagai default buat simulasi
avg_harga_beli_skrg = 4300
avg_lot_skrg = 6 # 600 lembar
plan_harga_baru = st.sidebar.number_input("Rencana Harga Beli Baru", value=3000)
plan_lot_tambah = st.sidebar.number_input("Rencana Tambah (Lot)", value=2)

# Logika Average Down
total_lembar_lama = avg_lot_skrg * 100
total_lembar_baru = plan_lot_tambah * 100
new_avg = ((total_lembar_lama * avg_harga_beli_skrg) + (total_lembar_baru * plan_harga_baru)) / (total_lembar_lama + total_lembar_baru)
st.sidebar.success(f"Harga Rata-rata Baru: **Rp {new_avg:,.0f}**")

# 5. DATABASE ASSET

portfolio_data = [
    {'Aset': 'BBRI', 'Kategori': 'Saham', 'Ticker': 'BBRI.JK', 'Jumlah': 5000, 'Harga_Beli': 4600}, 
    {'Aset': 'TLKM', 'Kategori': 'Saham', 'Ticker': 'TLKM.JK', 'Jumlah': 3000, 'Harga_Beli': 3100},
    {'Aset': 'ASII', 'Kategori': 'Saham', 'Ticker': 'ASII.JK', 'Jumlah': 2000, 'Harga_Beli': 5000},
    {'Aset': 'Danamas Pasti', 'Kategori': 'RDPT', 'Ticker': None, 'Jumlah': 20000, 'Harga_Beli': 5283},
    {'Aset': 'SBR013', 'Kategori': 'SBN', 'Ticker': None, 'Jumlah': 50, 'Harga_Beli': 1000000}, # 50 Juta
]

df = pd.DataFrame(portfolio_data)

# 6. LOGIKA UPDATE
def update_logic(row):
    if row['Aset'] == 'BBRI': return get_live_price("BBRI.JK")
    if row['Aset'] == 'WBSA': 
        p = get_live_price("WBSA.JK")
        return p if p > 0 else 1330
    if row['Aset'] == 'Danamas Pasti': return row['Harga_Beli'] * (1 + cuan_danamas/100)
    if row['Aset'] == 'Majoris Syariah': return row['Harga_Beli'] * (1 + cuan_majoris/100)
    if row['Aset'] == 'SBR013': return row['Harga_Beli'] + kupon_sbr
    return row['Harga_Beli']

df['Harga_Sekarang'] = df.apply(update_logic, axis=1)
df['Modal'] = df['Jumlah'] * df['Harga_Beli']
df['Nilai_Sekarang'] = df['Jumlah'] * df['Harga_Sekarang']
df['Profit_Loss'] = df['Nilai_Sekarang'] - df['Modal']
df['ROI_%'] = (df['Profit_Loss'] / df['Modal']) * 100

# 7. TAMPILAN METRICS
col1, col2, col3 = st.columns(3)
total_nilai = df['Nilai_Sekarang'].sum()
total_modal = df['Modal'].sum()
total_pl = total_nilai - total_modal

col1.metric("Total Asset Value", f"Rp {total_nilai:,.0f}")
col2.metric("Total Profit/Loss", f"Rp {total_pl:,.0f}", f"{(total_pl/total_modal)*100:.2f}%")
col3.metric("Potensi Dividen BBRI", "Rp 189,000")

# 8. FITUR BARU: CANDLESTICK CHART
st.subheader("📊 Analisis Teknikal (90 Hari Terakhir)")
target_ticker = st.selectbox("Pilih Saham untuk Dilihat Grafiknya:", ["BBRI.JK", "WBSA.JK"])

with st.spinner('Sedang mengambil data market...'):
    # Menambahkan auto_adjust=True agar formatnya lebih konsisten
    hist_data = yf.download(target_ticker, start=datetime.now() - timedelta(days=90), auto_adjust=True)

if not hist_data.empty:
    # --- BARIS SAKTI UNTUK PERBAIKAN GRAFIK ---
    # Jika kolomnya bertumpuk (Multi-index), kita ambil level paling atas saja
    if isinstance(hist_data.columns, pd.MultiIndex):
        hist_data.columns = hist_data.columns.get_level_values(0)
    
    hist_data = hist_data.reset_index()
    # ------------------------------------------

    fig_candle = go.Figure(data=[go.Candlestick(
        x=hist_data['Date'],
        open=hist_data['Open'],
        high=hist_data['High'],
        low=hist_data['Low'],
        close=hist_data['Close'],
        increasing_line_color='#2ecc71',
        decreasing_line_color='#e74c3c'
    )])
    
    fig_candle.update_layout(
        template='plotly_dark', 
        xaxis_rangeslider_visible=False, 
        height=450,
        margin=dict(l=20, r=20, t=20, b=20)
    )
    st.plotly_chart(fig_candle, use_container_width=True)
else:
    st.warning(f"Data untuk {target_ticker} tidak ditemukan.")

# 9. GRAFIK PERFORMA (LAMA)
st.subheader("📊 Komposisi & Performa")
fig_bar, ax = plt.subplots(figsize=(10, 3))
colors = ['#2ecc71' if x > 0 else '#e74c3c' for x in df['Profit_Loss']]
ax.bar(df['Aset'], df['Nilai_Sekarang'], color=colors)
st.pyplot(fig_bar)

# 10. TABEL RINCIAN
st.subheader("📋 Rincian Portofolio Lengkap")
st.dataframe(df.drop(columns=['Ticker']).style.format({
    'Harga_Beli': '{:,.2f}', 
    'Harga_Sekarang': '{:,.2f}', 
    'Modal': '{:,.0f}', 
    'Nilai_Sekarang': '{:,.0f}', 
    'Profit_Loss': '{:,.0f}',
    'ROI_%': '{:.2f}%'
}), use_container_width=True)

if st.button("Simpan Data ke CSV"):
    df.to_csv("InvestTrack_Final.csv", index=False)
    st.success("Data Tersimpan!")