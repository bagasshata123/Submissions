import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

sns.set(style='dark')

# Set tema Streamlit
st.set_page_config(
    page_title="E-Commerce Dashboard",
    page_icon="🛍️",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Membaca data CSV dari GitHub
alldata_df = pd.read_csv("https://raw.githubusercontent.com/bagasshata123/Submissions/main/all_data_ecommerce.csv")

# Header Streamlit dengan judul menarik
st.title('E-Commerce Dashboard')

# Menambahkan deskripsi untuk memberikan konteks
st.markdown(
    "Selamat datang di Dashboard E-Commerce! Pada Dashboard ini akan diberikan informasi terkait Hubungan harga dan biaya ongkir, dan 10 produk teratas."
)

# Membuat tab untuk subheader
selected_tab = st.sidebar.radio("Pilih Menu", ["Hubungan", "Produk Teratas"])

if selected_tab == "Hubungan":
    st.subheader("Hubungan")

    # Melihat hubungan antara price dan review_score
    fig, ax = plt.subplots(nrows=1, ncols=1, figsize=(24, 6))  # buat canvas terlebih dahulu
    colors = ["#72BCD4", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3"]

    sns.regplot(x=alldata_df['price'], y=alldata_df['freight_value'], ax=ax)
    st.pyplot(fig)  # Menampilkan plot dengan st.pyplot()

    selected_columns = alldata_df[['price', 'freight_value']]
    selected_columns.head(15)
    correlation_mat = selected_columns.corr()
    sns.heatmap(correlation_mat, annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.5, ax=ax)
    st.pyplot(fig)  # Menampilkan plot dengan st.pyplot()

# Tab "Produk Teratas"
elif selected_tab == "Produk Teratas":
    st.subheader("Produk Teratas")

    # Menentukan banyaknya produk yang terjual
    sum_order_items_df = alldata_df.groupby("product_category_name_english").order_id.count().sort_values(ascending=False).reset_index()
    sum_order_items_df.head(15)

    # Mengambil 10 kategori teratas berdasarkan jumlah produk yang terjual
    top_10_categories = sum_order_items_df.head(10)

    # Membuat diagram batang untuk 10 kategori teratas
    fig, ax = plt.subplots(figsize=(10, 5))
    sns.barplot(
        y="order_id",
        x="product_category_name_english",
        data=top_10_categories,
        ax=ax
    )
    plt.title("Banyaknya Produk Terjual per Kategori (10 Teratas)", loc="center", fontsize=15)
    plt.ylabel("Jumlah Produk Terjual")
    plt.xlabel("Kategori Produk")
    plt.xticks(rotation=45, ha='right')
    st.pyplot(fig)  # Menampilkan plot dengan st.pyplot()

st.caption("Copyright by BagasShata")
