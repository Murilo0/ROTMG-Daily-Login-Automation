import pyautogui
import cv2
import numpy as np
import time

def find_image_on_screen(image_path: str, confidence: float = 0.8) -> tuple | None:
    try:
        location = pyautogui.locateCenterOnScreen(image_path, confidence=confidence)
        if location is not None:
            print(f"Image '{image_path}' found at {location}.")
            return location
        else:
            print(f"Image '{image_path}' not found.")
            return None
    except Exception as e:
        print(f"Error trying locate the image: '{image_path}': {e}")
        return None

def click_image(image_path: str, confidence: float = 0.9, button: str = 'left'):
    coords = find_image_on_screen(image_path, confidence)
    if coords:
        pyautogui.click(coords, button=button)
        print(f"Clicked on '{image_path}' em {coords}.")
    else:
        print(f"Not enable to click '{image_path}' wasn't found.")

def wait_for_image(image_path: str, timeout: int = 10, confidence: float = 0.9) -> bool:
    """
    Espera até que uma imagem apareça na tela, por um tempo máximo especificado.

    Args:
        image_path (str): O caminho para o arquivo de imagem.
        timeout (int): Tempo máximo de espera em segundos.
        confidence (float): A precisão da correspondência.

    Returns:
        bool: True se a imagem apareceu, False caso contrário.
    """
    start_time = time.time()
    while time.time() - start_time < timeout:
        if find_image_on_screen(image_path, confidence) is not None:
            print(f"Image '{image_path}' found.")
            return True
        time.sleep(0.5) # Pausa para não sobrecarregar a CPU
    print(f"Timeout. Image '{image_path}' not found in {timeout} seconds.")
    return False


# --- Abordagem 2: Usando OpenCV (Mais Avançada) ---
# Esta abordagem é mais rápida e oferece mais controle, mas é mais complexa.

def find_image_with_opencv(template_path: str, threshold: float = 0.8) -> tuple | None:
    """
    Localiza uma imagem (template) na tela usando OpenCV.

    Args:
        template_path (str): Caminho para a imagem modelo a ser procurada.
        threshold (float): Limiar de correspondência (0.0 a 1.0).

    Returns:
        tuple: Coordenadas (x, y) do centro da imagem encontrada.
        None: Se a imagem não for encontrada.
    """
    # 1. Capturar a tela
    screenshot = pyautogui.screenshot()
    screen_img = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)
    
    # 2. Carregar a imagem modelo (template)
    template_img = cv2.imread(template_path, cv2.IMREAD_COLOR)
    if template_img is None:
        print(f"Erro: não foi possível carregar a imagem modelo de '{template_path}'")
        return None
    
    template_h, template_w, _ = template_img.shape

    # 3. Comparar a imagem modelo com a captura de tela
    result = cv2.matchTemplate(screen_img, template_img, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

    # 4. Verificar se a correspondência é boa o suficiente
    if max_val >= threshold:
        center_x = max_loc[0] + template_w // 2
        center_y = max_loc[1] + template_h // 2
        print(f"OpenCV encontrou '{template_path}' com precisão de {max_val:.2f} em ({center_x}, {center_y})")
        return (center_x, center_y)
    
    print(f"OpenCV não encontrou '{template_path}' com o limiar de {threshold}.")
    return None