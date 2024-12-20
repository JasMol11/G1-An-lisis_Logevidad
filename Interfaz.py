import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

def graficar_esperanza_vida_SV(input_file):
    """Genera la gráfica de esperanza de vida mujeres en El Salvador."""
    try:
        df = pd.read_csv(input_file, sep=';', encoding='utf-8', engine='python')
        df_melted = df.melt(
            id_vars=['Country Name', 'Country Code', 'Indicator Name', 'Indicator Code'], 
            var_name='Year', 
            value_name='Value'
        )
        df_melted['Year'] = pd.to_numeric(df_melted['Year'], errors='coerce')
        df_melted = df_melted.dropna(subset=['Year', 'Value']).sort_values('Year')

        plt.figure(figsize=(12, 6))
        sns.set_style("whitegrid")
        plt.plot(df_melted['Year'], df_melted['Value'], marker='o', linestyle='-', linewidth=2, markersize=5, color='blue')
        plt.title(f"Evolución de {df_melted['Indicator Name'].iloc[0]} en El Salvador", fontsize=15, fontweight='bold')
        plt.xlabel('Año', fontsize=12)
        plt.ylabel(df_melted['Indicator Name'].iloc[0], fontsize=12)
        plt.xticks(rotation=45)
        plt.grid(True, linestyle='--', alpha=0.7)
        plt.tight_layout()
        plt.show()
    except Exception as e:
        tk.messagebox.showerror("Error", f"Error al graficar: {e}")

def graficar_esperanza_vida_guatemala(input_file):
    """Genera la gráfica de esperanza de vida mujeres en Guatemala."""
    df = pd.read_csv(input_file, sep=';', encoding='utf-8', engine='python')
    df_melted = df.melt(id_vars=['Country Name', 'Country Code', 'Indicator Name', 'Indicator Code'], 
                        var_name='Year', 
                        value_name='Value')
    df_melted['Year'] = pd.to_numeric(df_melted['Year'], errors='coerce')
    df_melted = df_melted.dropna(subset=['Year', 'Value']).sort_values('Year')

    plt.figure(figsize=(12, 6))
    sns.set_style("whitegrid")
    plt.plot(df_melted['Year'], df_melted['Value'], marker='o', linestyle='-', linewidth=2, markersize=5, color='blue')
    plt.title(f"Evolución de {df_melted['Indicator Name'].iloc[0]} en Guatemala", fontsize=15, fontweight='bold')
    plt.xlabel('Año', fontsize=12)
    plt.ylabel(df_melted['Indicator Name'].iloc[0], fontsize=12)
    plt.xticks(rotation=45)
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.show()

def graficar_subalimentacion_guatemala(input_file):
    """Genera la gráfica de subalimentación en Guatemala."""
    df = pd.read_csv(input_file, sep=',', encoding='utf-8')
    df['Inicio_Periodo'] = df['Bianual'].apply(lambda x: x.split('-')[0])
    df = df.sort_values('Inicio_Periodo')

    plt.figure(figsize=(12, 6))
    sns.set_style("whitegrid")
    plt.plot(df['Inicio_Periodo'], df['value'], marker='o', linestyle='-', linewidth=2, markersize=5, color='#ff1e8a')
    plt.title("Número de personas en subalimentación en Guatemala (1999-2019)", fontsize=15, fontweight='bold')
    plt.xlabel('Año', fontsize=12)
    plt.ylabel('Número de personas en subalimentación (miles)', fontsize=12)
    plt.xticks(rotation=45)
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.show()


def graficar_pib_guatemala(input_file):
    """Genera la gráfica del Producto Interno Bruto (PIB) per cápita en Guatemala."""
    df = pd.read_csv(input_file, sep=",", encoding="utf-8")
    df = df[df["País__ESTANDAR"] == "Guatemala"]
    df = df.sort_values("Años__ESTANDAR")

    plt.figure(figsize=(12, 6))
    sns.set_style("whitegrid")
    plt.plot(df["Años__ESTANDAR"], df["value"], marker="o", linestyle="-", linewidth=2, markersize=5, color="#00bfff")
    plt.title("PIB per cápita en Guatemala (1990-2023)", fontsize=15, fontweight="bold")
    plt.xlabel("Año", fontsize=12)
    plt.ylabel("PIB per cápita (USD)", fontsize=12)
    plt.xticks(rotation=45)
    plt.grid(True, linestyle="--", alpha=0.7)
    plt.tight_layout()
    plt.show()

def graficar_pib_sv(input_file):
    """Genera la gráfica del Producto Interno Bruto (PIB) per cápita en El Salvador."""
    df = pd.read_csv(input_file, sep=",", encoding="utf-8")
    df = df[df["País__ESTANDAR"] == "El Salvador"]
    df = df.sort_values("Años__ESTANDAR")

    plt.figure(figsize=(12, 6))
    sns.set_style("whitegrid")
    plt.plot(df["Años__ESTANDAR"], df["value"], marker="o", linestyle="-", linewidth=2, markersize=5, color="#00bfff")
    plt.title("PIB per cápita en El Salvador (1990-2023)", fontsize=15, fontweight="bold")
    plt.xlabel("Año", fontsize=12)
    plt.ylabel("PIB per cápita (USD)", fontsize=12)
    plt.xticks(rotation=45)
    plt.grid(True, linestyle="--", alpha=0.7)
    plt.tight_layout()
    plt.show()

def graficar_temp_sv(input_file):
    """Genera la gráfica de la variación de temperatura en El Salvador."""
    df = pd.read_csv(input_file, sep=",", encoding="utf-8")
    df = df[df["País__ESTANDAR"] == "El Salvador"]
    df = df.sort_values("Años__ESTANDAR")

    plt.figure(figsize=(12, 6))
    sns.set_style("whitegrid")
    plt.plot(df["Años__ESTANDAR"], df["value"], marker="o", linestyle="-", linewidth=2, markersize=5, color="#00bfff")
    plt.title("Variación de le temperatura en El Salvador (1961-2022)", fontsize=15, fontweight="bold")
    plt.xlabel("Año", fontsize=12)
    plt.ylabel("Temperatura (°C)", fontsize=12)
    plt.xticks(rotation=45)
    plt.grid(True, linestyle="--", alpha=0.7)
    plt.tight_layout()
    plt.show()


def graficar_temp_G(input_file):
    """Genera la gráfica de la variación de temperatura en Guatemala."""
    df = pd.read_csv(input_file, sep=",", encoding="utf-8")
    df = df[df["País__ESTANDAR"] == "Guatemala"]
    df = df.sort_values("Años__ESTANDAR")

    plt.figure(figsize=(12, 6))
    sns.set_style("whitegrid")
    plt.plot(df["Años__ESTANDAR"], df["value"], marker="o", linestyle="-", linewidth=2, markersize=5, color="#00bfff")
    plt.title("Variación de le temperatura en Guatemala (1961-2022)", fontsize=15, fontweight="bold")
    plt.xlabel("Año", fontsize=12)
    plt.ylabel("Temperatura (°C)", fontsize=12)
    plt.xticks(rotation=45)
    plt.grid(True, linestyle="--", alpha=0.7)
    plt.tight_layout()
    plt.show()

def graficar_subalimentacion_sv(input_file):
    """Genera la gráfica de subalimentación en El Salvador."""
    df = pd.read_csv(input_file, sep=',', encoding='utf-8')
    df['Inicio_Periodo'] = df['Bianual'].apply(lambda x: x.split('-')[0])
    df = df.sort_values('Inicio_Periodo')

    plt.figure(figsize=(12, 6))
    sns.set_style("whitegrid")
    plt.plot(df['Inicio_Periodo'], df['value'], marker='o', linestyle='-', linewidth=2, markersize=5, color='#ff1e8a')
    plt.title("Número de personas en subalimentación en El Salvador (1999-2019)", fontsize=15, fontweight='bold')
    plt.xlabel('Año', fontsize=12)
    plt.ylabel('Número de personas en subalimentación (miles)', fontsize=12)
    plt.xticks(rotation=45)
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.show()

###########################################################################################################

def mostrar_menu_pais(pais, ventana_principal):
    """Muestra el menú específico para el país seleccionado."""
    ventana_principal.withdraw()

    ventana_pais = tk.Toplevel()
    ventana_pais.title(f"Menú - {pais}")
    ventana_pais.configure(bg="#212121")

    def regresar_menu_principal():
        ventana_pais.destroy()
        ventana_principal.deiconify()


    ventana_pais.geometry("430x404")

    tk.Label(
        ventana_pais, 
        text=f"Opciones para {pais}", 
        font=("Arial", 16, "bold"),
        bg="#212121",
        fg="white"
        
    ).pack(pady=10,)

    
    estilo_botones = {
        "font": ("Arial", 14),
        "bg": "#1061a9",
        "fg": "white",
        "activebackground": "white",
        "activeforeground": "#1061a9",
        "relief": "flat",
        "bd": 0,
        "highlightthickness": 0,
        "width": 25,
        "height": 2
    }


    if pais == "El Salvador":
        input_file_esperanza = 'CSV_LIMPIOS/El_Salvador_Supervivencia_Limpio.csv'
        input_file_subalimentacion = 'CSV_LIMPIOS/Subalimentacion_El_Salvador.csv'
        input_filePIBSV = 'CSV_LIMPIOS/PIB_El_Salvador.csv'
        input_fileTempsv = 'CSV_LIMPIOS/Temperatura_El_Salvador.csv'

        tk.Button(
            ventana_pais, 
            text="Esperanza de vida mujeres", 
            command=lambda: graficar_esperanza_vida_SV(input_file_esperanza),
            **estilo_botones
        ).pack(pady=5)

        tk.Button(
            ventana_pais, 
            text="Subalimentación", 
            command=lambda: graficar_subalimentacion_sv(input_file_subalimentacion),
            **estilo_botones
        ).pack(pady=5)

        tk.Button(
            ventana_pais, 
            text="Producto Interno Bruto", 
            command=lambda: graficar_pib_sv(input_filePIBSV),
            **estilo_botones
        ).pack(pady=5)

        tk.Button(
            ventana_pais, 
            text="Variación de la temperatura", 
            command=lambda: graficar_temp_sv(input_fileTempsv),
            **estilo_botones
        ).pack(pady=5)

    elif pais == "Guatemala":
        input_file_esperanza = 'CSV_LIMPIOS/Guatemala_Supervivencia_Limpio.csv'
        input_file_subalimentacion = 'CSV_LIMPIOS/Subalimentacion_Guatemala.csv'
        input_file_PibGM = 'CSV_LIMPIOS/PIB_Guatemala.csv'
        input_file_tempG = 'CSV_LIMPIOS/Temperatura_Guatemala.csv'

        tk.Button(
            ventana_pais, 
            text="Esperanza de vida mujeres", 
            command=lambda: graficar_esperanza_vida_guatemala(input_file_esperanza),
            **estilo_botones
        ).pack(pady=5)

        tk.Button(
            ventana_pais, 
            text="Producto Interno Bruto", 
            command=lambda: graficar_pib_guatemala(input_file_PibGM),
            **estilo_botones
        ).pack(pady=5)

        tk.Button(
            ventana_pais, 
            text="Subalimentación", 
            command=lambda: graficar_subalimentacion_guatemala(input_file_subalimentacion),
            **estilo_botones
        ).pack(pady=5)

        tk.Button(
            ventana_pais, 
            text="Variación de temperatura", 
            command=lambda: graficar_temp_G(input_file_tempG),
            **estilo_botones
        ).pack(pady=5)

    tk.Button(
        ventana_pais, 
        text="Regresar al menú principal", 
        command=regresar_menu_principal,
        **estilo_botones
    ).pack(pady=20)

def mostrar_menu_principal():
    """Muestra el menú principal."""
    ventana_menu = tk.Tk()
    ventana_menu.title("Menú Principal")
    ventana_menu.configure(bg="#212121")

    # Estilo para los botones
    estilo_botones = {
        "font": ("Arial", 14),
        "bg": "#1061a9",
        "fg": "white",
        "activebackground": "white",
        "activeforeground": "#1061a9",
        "relief": "flat",
        "bd": 0,
        "highlightthickness": 0,
        "padx": 10,
        "pady": 10,
    }

    # Logo principal
    logo_image = Image.open("IMAGENES/SIC.png").resize((151, 151))
    logo = ImageTk.PhotoImage(logo_image)
    etiqueta_logo = tk.Label(ventana_menu, image=logo, bg="#212121")
    etiqueta_logo.image = logo  # Evita que Python elimine la referencia
    etiqueta_logo.pack(pady=10)

    ventana_menu.geometry("535x435")

    tk.Label(
        ventana_menu, 
        text="Selecciona un país para ver la gráfica", 
        font=("Arial", 16, "bold"),
        bg="#212121", 
        fg="white"
    ).pack(pady=10)

    # Bandera de El Salvador
    bandera_sv_image = Image.open("IMAGENES/el_salvador.png").resize((50, 30))
    bandera_sv = ImageTk.PhotoImage(bandera_sv_image)
    boton_el_salvador = tk.Button(
        ventana_menu, 
        text="El Salvador", 
        image=bandera_sv,
        compound=tk.LEFT,
        width=200,
        height=50,
        command=lambda: mostrar_menu_pais("El Salvador", ventana_menu),
        **estilo_botones
    )
    boton_el_salvador.image = bandera_sv
    boton_el_salvador.pack(pady=10)

    # Bandera de Guatemala
    bandera_gt_image = Image.open("IMAGENES/guatemala.png").resize((50, 30))
    bandera_gt = ImageTk.PhotoImage(bandera_gt_image)
    boton_guatemala = tk.Button(
        ventana_menu, 
        text="Guatemala", 
        image=bandera_gt,
        compound=tk.LEFT,
        width=200,
        height=50,
        command=lambda: mostrar_menu_pais("Guatemala", ventana_menu),
        **estilo_botones
    )
    boton_guatemala.image = bandera_gt
    boton_guatemala.pack(pady=10)

    ventana_menu.mainloop()
    

if __name__ == "__main__":
    mostrar_menu_principal()
