import io

from PIL import Image
from cryptography.fernet import Fernet

# Şifreli verileri dosyadan oku
encrypted_file_name = input("Enter the name of the encrypted file: ") + ".bin"
with open(encrypted_file_name, 'rb') as f:
    encrypted_data = f.read()

# Şifreleme anahtarını dosyadan oku
key_file_name = input("Enter the name of the key file: ") + ".txt"
with open(key_file_name, 'rb') as f:
    key = f.read()

# AES şifreleme nesnesi oluştur
cipher_suite = Fernet(key)

# Şifreli verileri AES ile çöz
decrypted_data = cipher_suite.decrypt(encrypted_data)

# Sıkıştırma kaybı olmadan sıkıştırılmış verileri PNG dosyasına dönüştür
with io.BytesIO() as output:
    img = Image.open(io.BytesIO(decrypted_data))
    img.save(output, format='PNG')
    png_data = output.getvalue()

# Yeniden açılan PNG dosyasının adını al
png_file_name = input("Enter a name for the decrypted PNG file: ") + ".png"

# PNG dosyasını diske yaz
with open(png_file_name, 'wb') as f:
    f.write(png_data)
