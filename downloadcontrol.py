import os
import shutil
import time

# Ścieżka do folderu, który będzie monitorowany (np. folder Pobrane)
folder_to_track = r'C:\Users\zosia\Downloads'  # Zmień na właściwą ścieżkę

# Słownik mapujący rozszerzenia plików na ścieżki docelowych folderów
folder_destination = {
    '.pdf': r'C:\Users\zosia\Documents',  # Zmień na właściwą ścieżkę
    '.jpg': r'C:\Users\zosia\Pictures',     # Zmień na właściwą ścieżkę
    '.png': r'C:\Users\zosia\Videos'     # Zmień na właściwą ścieżkę
    # Tutaj można dodać więcej rozszerzeń i odpowiadających im folderów
}

# Funkcja do przenoszenia plików do odpowiednich folderów
def move_files():
    for filename in os.listdir(folder_to_track):
        src = os.path.join(folder_to_track, filename)
        extension = os.path.splitext(filename)[1]
        dest_folder = folder_destination.get(extension)

        if dest_folder:
            # Tworzenie folderu docelowego, jeśli nie istnieje
            if not os.path.exists(dest_folder):
                os.makedirs(dest_folder)

            dest = os.path.join(dest_folder, filename)
            shutil.move(src, dest)

# Pętla, która będzie regularnie sprawdzać folder i przenosić pliki
try:
    while True:
        move_files()
        time.sleep(10)  # Sprawdza folder co 10 sekund
except KeyboardInterrupt:
    print("Skrypt zatrzymany.")