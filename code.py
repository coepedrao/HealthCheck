import psutil
import platform
import GPUtil
import shutil
import os

def get_cpu_temp():
    if platform.system() == "Windows":
        return "Não disponível no Windows sem software adicional"
    elif platform.system() == "Linux":
        try:
            with open("/sys/class/thermal/thermal_zone0/temp", "r") as f:
                temp = int(f.read()) / 1000
            return temp
        except:
            return "Não foi possível obter a temperatura da CPU"
    else:
        return "Sistema operacional não suportado"

def get_gpu_info():
    gpus = GPUtil.getGPUs()
    if not gpus:
        return "Nenhuma GPU detectada"
    gpu_data = {}
    for gpu in gpus:
        gpu_data[gpu.name] = {
            "Uso": gpu.load * 100,
            "Temperatura": gpu.temperature,
            "Memória utilizada": gpu.memoryUsed,
            "Memória total": gpu.memoryTotal
        }
    return gpu_data

def check_system():
    cpu_usage = psutil.cpu_percent(interval=1)
    cpu_temp = get_cpu_temp()
    ram = psutil.virtual_memory()
    gpu_info = get_gpu_info()

    print(f"Uso da CPU: {cpu_usage}%")
    print(f"Temperatura da CPU: {cpu_temp}")
    print(f"Uso de RAM: {ram.percent}% ({ram.used / (1024**3):.2f}GB/{ram.total / (1024**3):.2f}GB)")
    print(f"Informações da GPU: {gpu_info}")
    
    if cpu_usage > 85:
        print("⚠️ Alto uso da CPU! Considere fechar alguns programas.")
    if isinstance(cpu_temp, (int, float)) and cpu_temp > 80:
        print("⚠️ A temperatura da CPU está muito alta! Verifique o resfriamento.")
    if ram.percent > 90:
        print("⚠️ Alto uso de RAM! Considere liberar memória.")
    if isinstance(gpu_info, dict):
        for nome, info in gpu_info.items():
            if info["Uso"] > 90:
                print(f"⚠️ A GPU {nome} está com alto uso! Considere reduzir a carga gráfica.")
            if info["Temperatura"] > 85:
                print(f"⚠️ A temperatura da GPU {nome} está muito alta! Verifique o resfriamento.")

if __name__ == "__main__":
    check_system()
