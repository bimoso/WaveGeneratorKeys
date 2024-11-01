# 🔑 Wave Key Generator

An automated key generator for Wave using Python and Selenium.

## 📋 Prerequisites

- [Python 3.10.11](https://www.python.org/downloads/release/python-31011/)
- Google Chrome or Chromium
- [ChromeDriver](https://googlechromelabs.github.io/chrome-for-testing/) compatible with your Chrome version

## ⚙️ Environment Setup

### 1. Python Installation

1. Download [Python 3.10.11](https://www.python.org/downloads/release/python-31011/)
2. During the installation:
   - ✅ Check "Add Python to PATH"
   - Follow the installation wizard

### 2. ChromeDriver Installation
You need to place ChromeDriver in your user folder:

1. Download the ChromeDriver compatible with your Chrome version
2. Create the folder: `C:\Users\YOUR_USERNAME\chromedriver-win64`
3. Extract the downloaded file into this folder
4. Make sure the `chromedriver.exe` file is located at: `C:\Users\YOUR_USERNAME\chromedriver-win64\chromedriver.exe`
   
> ⚠️ **Important**: Replace `YOUR_USERNAME` with your Windows username

### 3. PATH Environment Variable
1. Open System Environment Variables
2. Under "User variables," click "New"
3. Name: `PATH`
4. Value: `C:\Users\YOUR_USERNAME\chromedriver-win64`
5. Click "OK" to save

> ⚠️ **Important**: Replace `YOUR_USERNAME` with your Windows username

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

## 🚀 Usage

1. Ensure you have an active internet connection
2. Run the script:
```bash
python WaveGenerateKey.py
```

## 📁 Project Structure

```
wave-key-generator/
│
├── WaveGenerateKey.py       # Main script
├── requirements.txt         # Dependencies
├── chromedriver-win64.zip   # Driver zip v130
├── keys.txt                 # File with generated keys
└── README.md                # Documentation
```

## 🌐 Compatible ChromeDriver Versions

| Chrome Version   | ChromeDriver       | Download Link                                                                 |
|------------------|--------------------|-------------------------------------------------------------------------------|
| Chrome 130       | v130.0.6723.91     | [Download](https://edgedl.me.gvt1.com/edgedl/chrome/chrome-for-testing/130.0.6723.91/win64/chromedriver-win64.zip) |
| Chrome 129       | v129.0.6668.89     | [Download](https://edgedl.me.gvt1.com/edgedl/chrome/chrome-for-testing/129.0.6668.89/win64/chromedriver-win64.zip) |
| **Others**       | -                  | [All Versions](https://googlechromelabs.github.io/chrome-for-testing/) |

### 🔍 Check Your Chrome Version

1. Open Google Chrome
2. In the address bar, type: `chrome://version`
3. Download the ChromeDriver corresponding to your version

## 🔧 Troubleshooting

If you encounter compatibility errors with ChromeDriver:

1. Check your Chrome version (`chrome://version`)
2. Download the corresponding ChromeDriver
3. Replace the existing file in the `chromedriver-win64` folder

## 💡 Tips

- Use a VPN to avoid usage limitations
- Generated keys are automatically saved in `keys.txt`
- Keep both Chrome and ChromeDriver updated
