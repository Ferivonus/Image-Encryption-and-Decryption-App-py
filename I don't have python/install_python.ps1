# Python 3.10 sürümü indirilecek ve yüklenecek
$pythonUrl = "https://www.python.org/ftp/python/3.10.0/python-3.10.0-amd64.exe"
$pythonExe = "C:\python-3.10.0-amd64.exe"
Invoke-WebRequest $pythonUrl -OutFile $pythonExe

# Yükleme için varsayılan seçenekleri kullanarak Python kurulumunu başlat
Start-Process -FilePath $pythonExe -ArgumentList "/quiet InstallAllUsers=1 PrependPath=1 TargetDir=C:\Python310" -Wait

# Kurulum sonrası Python klasörünün yolunu ortama ekleyin
$pythonInstallPath = "C:\Python310"
[Environment]::SetEnvironmentVariable("Path", "$($Env:Path);$pythonInstallPath", "Machine")
