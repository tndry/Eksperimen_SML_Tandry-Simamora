# Nama file: automate_Nama-Anda.py

import pandas as pd
import numpy as np
import os

def preprocess(raw_data_path, output_dir):
    # Pastikan direktori output ada, jika tidak, buat direktori tersebut.
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        print(f"Direktori dibuat: {output_dir}")

    # 1. Memuat dataset
    df = pd.read_csv("../heart_attack_raw/Heart Attack.csv")
    print("Dataset mentah berhasil dimuat.")

    # Membuat salinan untuk menghindari modifikasi dataframe asli secara tidak sengaja
    df_cleaned = df.copy()

    # 2. Penanganan Outliers
    numerical_features = ['age', 'impluse', 'pressurehight', 'pressurelow', 'glucose', 'kcm', 'troponin']
    print("Memulai proses penanganan outliers...")
    for col in numerical_features:
        Q1 = df_cleaned[col].quantile(0.25)
        Q3 = df_cleaned[col].quantile(0.75)
        IQR = Q3 - Q1
        lower_bound = Q1 - 1.5 * IQR
        upper_bound = Q3 + 1.5 * IQR
        
    # Menggunakan .loc untuk memastikan modifikasi dilakukan pada dataframe yang tepat
    df_cleaned.loc[:, col] = np.clip(df_cleaned[col], lower_bound, upper_bound)
    print("Penanganan outliers selesai.")

    # 3. Encoding Variabel Target
    df_cleaned.loc[:, 'class'] = df_cleaned['class'].map({'positive': 1, 'negative': 0})
    print("Variabel target 'class' telah di-encode.")

    # 4. Menyimpan data yang sudah bersih
    output_filename = 'heart_attack_preprocessed.csv'
    output_path = os.path.join(output_dir, output_filename)
    df_cleaned.to_csv(output_path, index=False)
    
    print(f"\n✅ Preprocessing selesai. Data bersih disimpan di: {output_path}")

if __name__ == '__main__':
    # Blok ini akan dieksekusi jika skrip dijalankan secara langsung
    
    # Tentukan path input (data mentah) dan direktori output (data bersih)
    # Path ini relatif terhadap lokasi file automate_Nama-Anda.py di dalam folder 'preprocessing'
    raw_path = '../heart_attack_raw/Heart Attack.csv'
    output_directory = './namadataset_preprocessing'
    
    # Panggil fungsi preprocessing
    preprocess(raw_data_path=raw_path, output_dir=output_directory)