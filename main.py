#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Главный файл утилиты блокировки рекламы
Поддерживает Python 3.11
"""

import sys
import os
import time

# Добавляем текущую папку в путь для импорта
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from blocklists import get_blocklist, get_whitelist
from hosts_manager import HostsManager
from dns_server import run_learning_mode
import utils

def main():
    """Главная функция"""
    
    # Показываем баннер
    utils.print_banner()
    
    # Проверяем права администратора
    if not utils.is_admin():
        print("⚠️  Программа требует прав администратора!")
        print("🔄 Перезапуск с правами администратора...")
        utils.run_as_admin()
        return
    
    # Создаем менеджер hosts
    manager = HostsManager()
    
    while True:
        print(utils.print_menu())
        choice = input().strip()
        
        if choice == '1':
            print("\n🚀 Заблокировать рекламу на ВСЕХ платформах...")
            domains = get_blocklist('all')
            if manager.add_block_rules(domains):
                print(f"✅ Успешно заблокировано {len(domains)} доменов")
            else:
                print("❌ Ошибка при блокировке")
                
        elif choice == '2':
            print("\n🚀 Заблокировать рекламу на RuTube...")
            domains = get_blocklist('rutube')
            if manager.add_block_rules(domains):
                print(f"✅ Успешно заблокировано {len(domains)} доменов")
            else:
                print("❌ Ошибка при блокировке")
                
        elif choice == '3':
            print("\n🚀 Заблокировать рекламу на YouTube...")
            domains = get_blocklist('youtube')
            if manager.add_block_rules(domains):
                print(f"✅ Успешно заблокировано {len(domains)} доменов")
            else:
                print("❌ Ошибка при блокировке")
                
        elif choice == '4':
            print("\n🚀 Заблокировать рекламу на Дзен...")
            domains = get_blocklist('dzen')
            if manager.add_block_rules(domains):
                print(f"✅ Успешно заблокировано {len(domains)} доменов")
            else:
                print("❌ Ошибка при блокировке")
                
        elif choice == '5':
            print("\n🚀 Заблокировать рекламу на VK Video...")
            domains = get_blocklist('vkvideo')
            if manager.add_block_rules(domains):
                print(f"✅ Успешно заблокировано {len(domains)} доменов")
            else:
                print("❌ Ошибка при блокировке")
                
        elif choice == '6':
            print("\n🛑 Отключение блокировки...")
            if manager.remove_block_rules():
                print("✅ Блокировка отключена")
            else:
                print("❌ Ошибка при отключении")
                
        elif choice == '7':
            print("\n📚 Режим обучения...")
            run_learning_mode()
            
        elif choice == '8':
            print("\n📊 Статистика:")
            count = manager.get_current_block_count()
            print(f"   Заблокировано доменов: {count}")
            if utils.check_internet():
                print("   Интернет: ✅ Подключен")
            else:
                print("   Интернет: ❌ Нет подключения")
                
        elif choice == '9':
            print("\n🔧 Оптимизация Windows для блокировки...")
            print("   Эта опция отключает DNS-клиент для работы с большими списками")
            confirm = input("   Продолжить? (y/n): ")
            if confirm.lower() == 'y':
                # Здесь код оптимизации из предыдущего сообщения
                print("   Функция в разработке")
            else:
                print("   Отменено")
                
        elif choice == '0':
            print("\n👋 До свидания!")
            sys.exit(0)
            
        else:
            print("\n❌ Неверный выбор. Попробуйте снова.")
        
        print("\n" + "-"*50)
        input("Нажмите Enter для продолжения...")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n👋 Программа завершена пользователем")
        sys.exit(0)
    except Exception as e:
        print(f"\n❌ Критическая ошибка: {e}")
        sys.exit(1)
