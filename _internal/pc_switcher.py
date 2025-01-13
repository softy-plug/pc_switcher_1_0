import os
import subprocess

def check_battery():
    # Проверка наличия аккумулятора
    try:
        battery_info = subprocess.check_output("wmic path win32_battery get status", shell=True)
        if "Status" in str(battery_info):
            return True
    except Exception as e:
        print(f"Ошибка при проверке аккумулятора: {e}")
    return False

def power_off():
    # Полное отключение питания
    os.system("shutdown /s /t 0")

def power_on():
    # Повторное включение питания (требует BIOS/UEFI настройки)
    print("Для повторного включения питания необходимо вручную включить ноутбук.")

def main():
    if check_battery():
        print("Аккумулятор обнаружен.")
        action = input("Введите 'off' для отключения питания или 'on' для включения: ").strip().lower()
        if action == 'off':
            power_off()
        elif action == 'on':
            power_on()
        else:
            print("Неверная команда.")
    else:
        print("Аккумулятор не обнаружен.")

if __name__ == "__main__":
    main()

# softy_plug