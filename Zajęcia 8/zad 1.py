import streamlit as st
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt


# --- Funkcje do bazy danych ---

def init_db():
    conn = sqlite3.connect('sales.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS sales (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            produkt TEXT,
            ilosc INTEGER,
            cena REAL,
            data TEXT,
            latitude REAL,
            longitude REAL
        )
    ''')
    conn.commit()
    return conn


def get_data(conn):
    df = pd.read_sql_query("SELECT * FROM sales", conn)
    return df


def add_record(conn, produkt, ilosc, cena, data, lat, lon):
    c = conn.cursor()
    c.execute("INSERT INTO sales (produkt, ilosc, cena, data, latitude, longitude) VALUES (?, ?, ?, ?, ?, ?)",
              (produkt, ilosc, cena, data, lat, lon))
    conn.commit()


# --- Inicjalizacja bazy ---
conn = init_db()

# --- UI aplikacji ---
st.title("Aplikacja sprzedażowa")

# 1. Wyświetlenie danych z tabeli sales
df = get_data(conn)

# 3. Filtr po produkcie
produkty = df['produkt'].unique().tolist()
produkty.insert(0, "Wszystkie")
wybrany_produkt = st.selectbox("Filtruj po produkcie:", produkty)

if wybrany_produkt != "Wszystkie":
    df_filtered = df[df['produkt'] == wybrany_produkt]
else:
    df_filtered = df

st.subheader("Dane sprzedaży")
st.dataframe(df_filtered)

# 2. Dodawanie nowego rekordu
st.subheader("Dodaj nowy rekord sprzedaży")

with st.form("form_dodaj"):
    produkt = st.text_input("Produkt:")
    ilosc = st.number_input("Ilość:", min_value=1, step=1)
    cena = st.number_input("Cena za jednostkę:", min_value=0.01, format="%.2f")
    data = st.date_input("Data sprzedaży")

    # 6. Wybór lokalizacji - gotowe miasta
    miasta = {
        "Warszawa": (52.2297, 21.0122),
        "Kraków": (50.0647, 19.9450),
        "Wrocław": (51.1079, 17.0385),
        "Gdańsk": (54.3520, 18.6466),
        "Poznań": (52.4064, 16.9252)
    }
    miasto = st.selectbox("Wybierz lokalizację sklepu:", ["--wybierz--"] + list(miasta.keys()))

    lat, lon = None, None
    if miasto != "--wybierz--":
        lat, lon = miasta[miasto]

    submitted = st.form_submit_button("Dodaj rekord")
    if submitted:
        if not produkt:
            st.error("Podaj nazwę produktu.")
        elif miasto == "--wybierz--":
            st.error("Wybierz lokalizację sklepu.")
        else:
            add_record(conn, produkt, ilosc, cena, data.strftime("%Y-%m-%d"), lat, lon)
            st.success("Rekord dodany!")
            st.balloons()

            # Odświeżenie danych po dodaniu
            df = get_data(conn)
            if wybrany_produkt != "Wszystkie":
                df_filtered = df[df['produkt'] == wybrany_produkt]
            else:
                df_filtered = df

# 4a. Wykres sprzedaży dziennej (ilość × cena)
st.subheader("Sprzedaż dzienna")
df_filtered['wartosc'] = df_filtered['ilosc'] * df_filtered['cena']
df_daily = df_filtered.groupby('data')['wartosc'].sum().reset_index()
df_daily['data'] = pd.to_datetime(df_daily['data'])

fig1, ax1 = plt.subplots()
ax1.plot(df_daily['data'], df_daily['wartosc'], marker='o')
ax1.set_xlabel("Data")
ax1.set_ylabel("Wartość sprzedaży")
ax1.set_title("Sprzedaż dzienna")
ax1.grid(True)
st.pyplot(fig1)

# 4b. Suma sprzedanych produktów wg typu
st.subheader("Suma sprzedanych produktów wg typu")
df_prod_sum = df_filtered.groupby('produkt')['ilosc'].sum().reset_index()

fig2, ax2 = plt.subplots()
ax2.bar(df_prod_sum['produkt'], df_prod_sum['ilosc'])
ax2.set_xlabel("Produkt")
ax2.set_ylabel("Ilość sprzedanych")
ax2.set_title("Sprzedane produkty wg typu")
plt.xticks(rotation=45)
st.pyplot(fig2)

# 7. Mapa z lokalizacjami sprzedaży
st.subheader("Mapa lokalizacji sprzedaży")

# Filtrowanie mapy
filter_date = st.checkbox("Filtruj po dacie")
if filter_date:
    data_od = st.date_input("Data od", value=pd.to_datetime(df['data']).min())
    data_do = st.date_input("Data do", value=pd.to_datetime(df['data']).max())
    df_map = df_filtered[
        (pd.to_datetime(df_filtered['data']) >= pd.to_datetime(data_od)) &
        (pd.to_datetime(df_filtered['data']) <= pd.to_datetime(data_do))
        ]
else:
    df_map = df_filtered

filter_map_prod = st.checkbox("Filtruj po produkcie na mapie")
if filter_map_prod:
    produkt_map = st.selectbox("Wybierz produkt do filtrowania na mapie", ["Wszystkie"] + list(df['produkt'].unique()))
    if produkt_map != "Wszystkie":
        df_map = df_map[df_map['produkt'] == produkt_map]

if not df_map.empty and df_map[['latitude', 'longitude']].notnull().all(axis=1).any():
    st.map(df_map[['latitude', 'longitude']])
else:
    st.write("Brak danych do wyświetlenia na mapie.")

