import tkinter as tk
from tkinter import messagebox
import sqlite3


def submit_data():
    # Retrieve input values
    nama_mahasiswa = nama_entry.get()
    biologi = int(biologi_entry.get())
    fisika = int(fisika_entry.get())
    inggris = int(inggris_entry.get())

    # Determine the predicted major
    # + based on the highest score
    if biologi > fisika and biologi > inggris:
        prediksi_fakultas = "Kedokteran"
    elif fisika > biologi and fisika > inggris:
        prediksi_fakultas = "Teknik"
    else:
        prediksi_fakultas = "Bahasa"

    # Tabel
    conn = sqlite3.connect("multiP.db")
    cursor = conn.cursor()
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS nilai_mahasiswa (
            id INTEGER PRIMARY KEY,
            nama_mahasiswa TEXT,
            biologi INTEGER,
            fisika INTEGER,
            inggris INTEGER,
            prediksi_fakultas TEXT
        )
    """
    )
    # Update the result label
    result_label.config(text="Prodi: " + prediksi_fakultas)

    # Store the data in the SQLite database
    cursor.execute(
        """
        INSERT INTO nilai_mahasiswa (nama_mahasiswa, biologi, fisika, inggris, prediksi_fakultas) VALUES (?, ?, ?, ?, ?)
    """,
        (nama_mahasiswa, biologi, fisika, inggris, prediksi_fakultas),
    )
    conn.commit()
    conn.close()

    messagebox.showinfo("info", "Data berhasil disubmit!")


# create main window
root = tk.Tk()
root.title("Aplikasi Prediksi Prodi Pilihan")

# Create input fields
nama_label = tk.Label(root, text="Nama Siswa")
nama_label.grid(row=0, column=0, padx=10, pady=10)
nama_entry = tk.Entry(root)
nama_entry.grid(row=0, column=1, padx=10, pady=10)

biologi_label = tk.Label(root, text="Nilai Biologi")
biologi_label.grid(row=1, column=0, padx=10, pady=10)
biologi_entry = tk.Entry(root)
biologi_entry.grid(row=1, column=1, padx=10, pady=10)

fisika_label = tk.Label(root, text="Nilai Fisika")
fisika_label.grid(row=2, column=0, padx=10, pady=10)
fisika_entry = tk.Entry(root)
fisika_entry.grid(row=2, column=1, padx=10, pady=10)

inggris_label = tk.Label(root, text="Nilai Inggris")
inggris_label.grid(row=3, column=0, padx=10, pady=10)
inggris_entry = tk.Entry(root)
inggris_entry.grid(row=3, column=1, padx=10, pady=10)

# Create predict button
button_submit = tk.Button(root, text="Submit Nilai", command=submit_data)
button_submit.grid(row=4, column=0, columnspan=2, pady=10)

# Create result label
result_label = tk.Label(root, text="Prodi: ")
result_label.grid(row=5, columnspan=2)

root.mainloop()