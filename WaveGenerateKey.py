"""
WaveGenerateKey module for bypassing tasks on getwave.gg.
"""

import os
import time
import threading
import warnings
import logging
import winsound
import urllib3
from urllib.parse import urlparse, parse_qs
import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.remote_connection import LOGGER
from urllib3.connectionpool import log as urllibLogger

server_vpn = input("¿En qué servidor VPN estás?: ")

def check_update():
    try:
        response = requests.get('https://raw.githubusercontent.com/bimoso/WaveGeneratorKeys/refs/heads/main/WaveGenerateKey.py')
        if response.status_code == 200:
            remote_code = response.text
            with open('WaveGenerateKey.py', 'r', encoding='utf-8') as f:
                local_code = f.read()
            
            if local_code != remote_code:
                print("Actualizando código...")
                with open('WaveGenerateKey.py', 'w', encoding='utf-8') as f:
                    f.write(remote_code)
                    print("Código actualizado exitosamente")
                    # Salir para reiniciar el script
                    exit()
        else:
            print("No se pudo verificar actualización")
    except Exception as e:
        print(f"Error verificando actualización: {e}")

check_update()

def suppress_all_logs():
    """
    Suppress all logs and warnings from various libraries.
    """
    # Suprimir advertencias
    warnings.filterwarnings('ignore')
    
    # Configurar logging
    logging.basicConfig(level=logging.ERROR)
    LOGGER.setLevel(logging.ERROR)
    urllibLogger.setLevel(logging.ERROR)
    
    # Suprimir logs del navegador
    os.environ['WDM_LOG_LEVEL'] = '0'
    logging.getLogger('WDM').setLevel(logging.NOTSET)
    
    # Suprimir mensajes de selenium
    os.environ['WDM_PRINT_FIRST_LINE'] = 'False'
    
    # Suprimir warnings de requests
    urllib3.disable_warnings()



class WaveBypass:
    def __init__(self):
        self.setup_driver()
        self.session_id = None
        
    def setup_driver(self):
         # Suprimir mensajes
        suppress_all_logs()
    
        chrome_options = Options()
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')
        chrome_options.add_argument('--disable-blink-features=AutomationControlled')
        chrome_options.add_argument('--disable-extensions')
        chrome_options.add_argument('--disable-gpu')
        chrome_options.add_argument('--headless')  # Esta opci�n hace que el navegador sea invisible
        chrome_options.add_experimental_option('excludeSwitches', ['enable-automation'])
        chrome_options.add_experimental_option('useAutomationExtension', False)
        chrome_options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36 OPR/114.0.0.0')
        
        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.execute_cdp_cmd('Network.setUserAgentOverride', {
            "userAgent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36 OPR/114.0.0.0'
        })
        self.driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
        self.driver.implicitly_wait(10)
    
    def get_session(self):
        try:
            print("Iniciando obtenci�n de sesi�n...")
            self.driver.get('https://key.getwave.gg/freemium-tasks')
            
            # Esperar a que la p�gina cargue completamente
            WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.TAG_NAME, "body"))
            )
            
            # Espera adicional para asegurar que las cookies se establezcan
            time.sleep(5)
            
            # Obtener todas las cookies
            cookies = self.driver.get_cookies()
            print(f"Cookies encontradas: {len(cookies)}")
            
            for cookie in cookies:
                print(f"Analizando cookie: {cookie['name']}")
                if cookie['name'] == 'wave-freemium-session':
                    self.session_id = cookie['value']
                    print(f"Session ID encontrado: {self.session_id}")
                    
                    # Agregar la cookie manualmente al driver
                    self.driver.add_cookie({
                        'name': 'wave-freemium-session',
                        'value': self.session_id,
                        'domain': '.getwave.gg'
                    })
                    
                    return self.session_id
            
            print("No se encontr� la cookie wave-freemium-session \n Trata cambiando de servidor VPN")
            return None
        except Exception as e:
            print(f"Error detallado obteniendo sesi�n: {str(e)}")
            return None

    def get_task(self):
        try:
            headers = {
                'host': 'api.getwave.gg',
                'sec-ch-ua': '"Chromium";v="128", "Not;A=Brand";v="24", "Opera GX";v="114"',
                'accept': 'application/json, text/plain, */*',
                'sec-ch-ua-mobile': '?0',
                'wave-freemium-session': self.session_id,
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36 OPR/114.0.0.0',
                'sec-ch-ua-platform': '"Windows"',
                'origin': 'https://key.getwave.gg',
                'sec-fetch-site': 'same-site',
                'sec-fetch-mode': 'cors',
                'sec-fetch-dest': 'empty',
                'referer': 'https://key.getwave.gg/',
                'accept-language': 'es-419,es;q=0.9',
                'priority': 'u=1, i'
            }

            response = requests.post('https://api.getwave.gg/v1/task/initiate', headers=headers)
            data = response.json()
            return data.get('link')

        except Exception as e:
            print(f"Error obteniendo task: {e}")
            return None

    def bypass_link(self, link):
        try:
            params = {'link': link}
            headers = {
                'accept': 'application/json, text/plain, */*',
                'accept-language': 'es-419,es;q=0.9',
                'origin': 'https://bypassunlock.com',
                'referer': 'https://bypassunlock.com/',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36 OPR/114.0.0.0',
                'sec-ch-ua': '"Chromium";v="128", "Not;A=Brand";v="24", "Opera GX";v="114"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'cross-site'
            }

            response = requests.get(
                f'https://bypassunlockapi-eqyp.onrender.com/bypass',
                params=params,
                headers=headers
            )
            
            data = response.json()
            return data.get('bypassed')

        except Exception as e:
            print(f"Error en bypass: {e}")
            return None

    def validate_task(self, bypassed_link):
        try:
            # Extraer el CB del link bypasseado
            parsed_url = urlparse(bypassed_link)
            query_params = parse_qs(parsed_url.query)
            cb = query_params.get('cb', [None])[0]

            headers = {
                'host': 'api.getwave.gg',
                'sec-ch-ua': '"Chromium";v="128", "Not;A=Brand";v="24", "Opera GX";v="114"',
                'accept': 'application/json, text/plain, */*',
                'sec-ch-ua-platform': '"Windows"',
                'sec-ch-ua-mobile': '?0',
                'wave-freemium-session': self.session_id,
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36 OPR/114.0.0.0',
                'content-type': 'application/json',
                'origin': 'https://key.getwave.gg',
                'sec-fetch-site': 'same-site',
                'sec-fetch-mode': 'cors',
                'sec-fetch-dest': 'empty',
                'referer': 'https://key.getwave.gg/',
                'accept-language': 'es-419,es;q=0.9',
                'priority': 'u=1, i'
            }

            response = requests.post(
                'https://api.getwave.gg/v1/task/validate',
                headers=headers,
                json={'cb': cb}
            )

            return response.json()

        except Exception as e:
            print(f"Error en validaci�n: {e}")
            return None

    def make_request(self, url, method='GET', headers=None, json=None):
        """Funci�n auxiliar para hacer requests con manejo de SSL"""
        try:
            if method == 'GET':
                response = requests.get(url, headers=headers, verify=False)
            else:
                response = requests.post(url, headers=headers, json=json, verify=False)
            return response.json()
        except Exception as e:
            print(f"Error en request a {url}: {e}")
            return None
    
    def check_task_status(self):
        try:
            headers = {
                'host': 'api.getwave.gg',
                'sec-ch-ua-platform': '"Windows"',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36',
                'accept': 'application/json, text/plain, */*',
                'sec-ch-ua': '"Chromium";v="130", "Google Chrome";v="130", "Not?A_Brand";v="99"',
                'sec-ch-ua-mobile': '?0',
                'wave-freemium-session': self.session_id,
                'origin': 'https://key.getwave.gg',
                'referer': 'https://key.getwave.gg/',
                'accept-language': 'es-ES,es;q=0.9'
            }
    
            data = self.make_request('https://api.getwave.gg/v1/task/all', headers=headers)
            if not data:
                return {'status': 'error'}
                
            if 'key' in data:
                return {'status': 'completed', 'key': data['key']}
            elif 'currentTask' in data:
                return {'status': 'in_progress', 'step': data['currentTask']}
            else:
                return {'status': 'error'}
    
        except Exception as e:
            print(f"Error verificando estado: {e}")
            return {'status': 'error'}
    
    def run(self):
        try:
            if not self.get_session():
                raise Exception("No se pudo obtener sesi�n")
            
            # Verificar estado inicial
            status = self.check_task_status()
            if status['status'] == 'completed':
                print(f"�Clave encontrada sin necesidad de pasos!: {status['key']}")
                
                return
    
            max_retries = 3  # N�mero m�ximo de intentos por paso
            current_step = status['step'] if status['status'] == 'in_progress' else 1
            
            while current_step <= 3:  # M�ximo 3 pasos
                print(f"\nProcesando Step {current_step}")
                
                for attempt in range(max_retries):
                    print(f"Intento {attempt + 1} del paso {current_step}")
                    
                    task_link = self.get_task()
                    if not task_link:
                        print("No se pudo obtener el link de la tarea")
                        if attempt < max_retries - 1:
                            time.sleep(5)
                            continue
                        else:
                            raise Exception(f"Fallaron todos los intentos del paso {current_step}")
                    
                    print(f"Link obtenido: {task_link}")
                    
                    bypassed = self.bypass_link(task_link)
                    if not bypassed or "?d" in bypassed:  # Validar link bypasseado
                        print("Link bypasseado inv�lido")
                        if attempt < max_retries - 1:
                            time.sleep(5)
                            continue
                        else:
                            raise Exception(f"Bypass fall� en todos los intentos del paso {current_step}")
                    
                    print(f"Link bypasseado: {bypassed}")
                    
                    try:
                        self.driver.get(bypassed)
                        time.sleep(2)
                        
                        # Validar el paso actual
                        validation = self.validate_task(bypassed)
                        if not validation:
                            print("Error en validaci�n")
                            continue
                            
                        print(f"Validaci�n paso {current_step}: {validation}")
                        
                        # Verificar estado despu�s de validaci�n
                        status = self.check_task_status()
                        if status['status'] == 'completed':
                            print(f"�Clave obtenida exitosamente!: {status['key']}")
                            #Almacenar la clave en un archivo o base de datos
                            with open('keys.txt', 'a') as f:
                                f.write(f"{server_vpn} - {status['key']}\n")
                            # Hacer un beep para notificar que se obtuvo la clave
                            winsound.Beep(1000, 300)  
                            return
                        elif status['status'] == 'in_progress':
                            current_step = status['step']
                            break  # Salir del bucle de intentos si el paso fue exitoso
                        
                    except Exception as e:
                        print(f"Error en el proceso: {e}")
                        if attempt < max_retries - 1:
                            time.sleep(5)
                            continue
                        else:
                            raise
                
                time.sleep(3)  # Espera entre pasos
                
            print("Se completaron todos los pasos sin obtener la clave")
    
        except Exception as e:
            print(f"Error fatal en el proceso: {e}")
        finally:
            self.driver.quit()

def run_instance(instance_id):
    try:
        print(f"\nIniciando instancia {instance_id}")
        bypass = WaveBypass()
        bypass.run()
    except Exception as e:
        print(f"Error en instancia {instance_id}: {e}")

def run_multiple_instances(num_instances=2):
    threads = []
    for i in range(num_instances):
        thread = threading.Thread(target=run_instance, args=(i+1,))
        threads.append(thread)
        thread.start()
    
    # Esperar a que todas las instancias terminen
    for thread in threads:
        thread.join()

if __name__ == "__main__":
    run_multiple_instances(2)