# 🏛️ Advanced Personal Wealth & Market Analytics

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white)
![Plotly](https://img.shields.io/badge/Plotly-3F4F75?style=for-the-badge&logo=plotly&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

**FinSight** adalah platform dashboard berbasis web yang dirancang untuk mengintegrasikan manajemen portofolio multi-aset dengan analisis pasar modal secara real-time. Aplikasi ini membantu investor memantau performa aset, melakukan analisis teknikal, dan mengambil keputusan manajemen risiko secara matematis.

## 🚀 Fitur Utama

- **📊 Real-Time Market Integration:** Mengambil data harga saham langsung dari bursa melalui Yahoo Finance API.
- **📈 Interactive Candlestick Analysis:** Visualisasi pergerakan harga saham dengan grafik candlestick interaktif (90 hari terakhir) untuk analisis tren.
- **🧮 Smart Average Down Calculator:** Kalkulator simulasi untuk menentukan harga rata-rata baru saat melakukan akumulasi aset di harga bawah.
- **📋 Multi-Asset Tracking:** Monitoring komprehensif untuk berbagai kelas aset: Saham, Reksadana, SBN (Surat Berharga Negara), hingga Cash.
- **📉 Automated Profit/Loss & ROI:** Perhitungan otomatis nilai portofolio, keuntungan/kerugian (unrealized P/L), serta persentase ROI secara instan.

## 🏭 Implementasi & Relevansi Industri

Dashboard ini tidak hanya sekadar alat bantu pribadi, tetapi merepresentasikan solusi yang digunakan dalam industri **FinTech** dan **Wealth Management**:

1. **Portfolio Management System (PMS):** Logika yang digunakan identik dengan sistem perbankan untuk memantau nilai aset nasabah secara _mark-to-market_.
2. **Decision Support System (DSS):** Fitur _Average Down Calculator_ merupakan implementasi dari sistem pendukung keputusan yang membantu manajer investasi memitigasi risiko kerugian.
3. **Data Visualization & Analytics:** Penggunaan grafik interaktif menunjukkan kemampuan dalam menyajikan data kompleks (High-Low-Open-Close) menjadi informasi yang mudah dipahami (insightful) bagi pemangku kepentingan.
4. **Automated Reporting:** Menggantikan proses pelaporan manual (spreadsheet) dengan sistem otomatis yang minim risiko _human error_.

## 🛠️ Tech Stack

- **Framework:** [Streamlit](https://streamlit.io/) (Web Interface)
- **Data Source:** [yfinance](https://github.com/ranaroussi/yfinance) (Market Data API)
- **Visualization:** [Plotly](https://plotly.com/) (Interactive Charts) & [Matplotlib](https://matplotlib.org/)
- **Data Manipulation:** [Pandas](https://pandas.pydata.org/) (Dataframes & Analytics)

## 💻 Cara Menjalankan

1. Pastikan Anda sudah menginstal Python 3.x
2. Clone repository ini:
   ```bash
   git clone [https://github.com/Haidar-009/Personal-Wealth-Analytics.git](https://github.com/Haidar-009/Personal-Wealth-Analytics.git)
   ```

3.Instal dependensi:

```bash
pip install streamlit pandas yfinance plotly matplotlib
```

4.Jalankan aplikasi:

```Bash
streamlit run app.py
```
