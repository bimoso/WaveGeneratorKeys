
[English](https://github.com/bimoso/WaveGeneratorKeys/blob/main/README-US.md)
# 🔑 Wave Key Generator

Un generador automatizado de claves para Wave utilizando Python y Selenium.

## 📋 Requisitos Previos

- [Python 3.10.11](https://www.python.org/downloads/release/python-31011/)
- Google Chrome o Chromium
- [ChromeDriver](https://googlechromelabs.github.io/chrome-for-testing/) compatible con tu versión de Chrome

## ⚙️ Configuración del Entorno

### 1. Instalación de Python

1. Descarga [Python 3.10.11](https://www.python.org/downloads/release/python-31011/)
2. Durante la instalación:
   - ✅ Marca "Add Python to PATH"
   - Sigue el asistente de instalación

### 2. Instalación del ChromeDriver
Es necesario colocar el ChromeDriver en tu carpeta de usuario:

1. Descarga el ChromeDriver compatible con tu versión de Chrome
2. Crea la carpeta: `C:\Users\TU_USUARIO\chromedriver-win64`
3. Descomprime el archivo descargado en esta carpeta
4. Verifica que el archivo `chromedriver.exe` esté en: C:\Users\TU_USUARIO\chromedriver-win64\chromedriver.exe
   
> ⚠️ **Importante**: Reemplaza `TU_USUARIO` con tu nombre de usuario de Windows

### 3. Variable de Entorno PATH
1. Abre las Variables de entorno del sistema
2. En "Variables de usuario", haz clic en "Nueva"
3. Nombre: `PATH`
4. Valor: `C:\Users\TU_USUARIO\chromedriver-win64`
5. Haz clic en "Aceptar" para guardar

> ⚠️ **Importante**: Reemplaza `TU_USUARIO` con tu nombre de usuario de Windows

### 4. Instalación de Dependencias

```bash
pip install -r requirements.txt
```

## 🚀 Uso

1. Verifica tu conexión a Internet
2. Ejecuta el script:
```bash
python WaveGenerateKey.py
```

## 📁 Estructura del Proyecto

```
wave-key-generator/
│
├── WaveGenerateKey.py    # Script principal
├── requirements.txt      # Dependencias
├── chromedriver-win64.zip   # Driver comprimido v130
├── keys.txt             # Archivo de claves generadas
└── README.md            # Documentación
```

## 🌐 Versiones Compatibles de ChromeDriver

| Versión de Chrome | ChromeDriver       | Enlace de Descarga                                                                 |
|-------------------|--------------------|------------------------------------------------------------------------------------|
| Chrome 130       | v130.0.6723.91     | [Descargar](https://edgedl.me.gvt1.com/edgedl/chrome/chrome-for-testing/130.0.6723.91/win64/chromedriver-win64.zip) |
| Chrome 129       | v129.0.6668.89     | [Descargar](https://edgedl.me.gvt1.com/edgedl/chrome/chrome-for-testing/129.0.6668.89/win64/chromedriver-win64.zip) |
| **Otros**        | -                  | [Enlace a todas las versiones](https://googlechromelabs.github.io/chrome-for-testing/) |

### 🔍 Verificar tu Versión de Chrome

1. Abre Google Chrome
2. En la barra de direcciones, escribe: `chrome://version`
3. Descarga el ChromeDriver correspondiente a tu versión

## 🔧 Solución de Problemas

Si encuentras errores de compatibilidad con ChromeDriver:

1. Verifica tu versión de Chrome (`chrome://version`)
2. Descarga el ChromeDriver correspondiente
3. Reemplaza el archivo existente en la carpeta `chromedriver-win64`

## 💡 Consejos

- Utiliza una VPN para evitar limitaciones de uso
- Las claves generadas se guardan automáticamente en `keys.txt`
- Mantén actualizado tanto Chrome como ChromeDriver