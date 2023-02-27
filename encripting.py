import io

from PIL import Image
from cryptography.fernet import Fernet

# PNG dosyasını aç
PNGfile = input("Type your png file's name: ") + ".png"
with open(PNGfile, 'rb') as f:
    png_data = f.read()

# Pillow kütüphanesi ile PNG dosyasını sıkıştırma kaybı olmadan sıkıştır
img = Image.open(io.BytesIO(png_data))
with io.BytesIO() as output:
    img.save(output, format='PNG', compress_level=0)
    compressed_data = output.getvalue()

# Şifreleme anahtarını oluştur
key = Fernet.generate_key()

# AES şifreleme nesnesi oluştur
cipher_suite = Fernet(key)

# Sıkıştırılmış verileri AES ile şifrele
encrypted_data = cipher_suite.encrypt(compressed_data)

print("your encrypted picture will be saved with a name as .bin file.")
NameOfBinData = input("Enter a name for your encrypted data file: ") + '.bin'

# Şifreli verileri dosyaya yaz
with open(NameOfBinData, 'wb') as f:
    f.write(encrypted_data)

# Şifreleme anahtarını dosyaya yaz

keytxtName = input("Enter a name for your key txt file: ") + ".txt"

with open(keytxtName, 'wb') as f:
    f.write(key)


# Toplu dosya adlarını yazacak dosyanın adını al
output_file_name = input("Enter a name for the output file: ") + ".txt"

# Dosya adlarını topluca yaz
with open(output_file_name, "w") as output_file:
    output_file.write("Use decripting.py with that informations: \n")
    output_file.write("Your PNG file's name was: " + PNGfile + '\n')
    output_file.write("your encrypted data file: "  + NameOfBinData + '\n')
    output_file.write("key txt file: "  + keytxtName + '\n')
