init python:
    import math
    
    class Item:
        """Класс предмета инвентаря"""
        def __init__(self, id, name, icon, description, historical_note, secret_dialog=False, dialog_ref=None):
            self.id = id
            self.name = name
            self.icon = icon
            self.description = description
            self.historical_note = historical_note
            self.secret_dialog = secret_dialog  # открывает ли секретный диалог
            self.dialog_ref = dialog_ref  # ссылка на секретный диалог
            self.found = False
    
    class Inventory:
        """Класс инвентаря"""
        def __init__(self):
            self.items = []
            self.max_items = 7
            self.create_items()
            self.secret_dialog_triggered_3 = False
            self.secret_dialog_triggered_5 = False
            self.secret_dialog_triggered_7 = False
        
        def create_items(self):
            """Создание всех предметов"""
            self.items = [
                Item(1, "Икона Спаса Нерукотворного", "🕊️", 
                     "Небольшая икона, которую Анастасия взяла из Царского Села",
                     "Императорская семья всегда возила с собой походные иконы. Эту нашли в комнате девушек после расстрела. По свидетельствам охранников, княжны постоянно молились перед иконами.",
                     True, "secret_dialog_icon"),
                
                Item(2, "Евангелие Татьяны", "📖",
                     "Евангелие с закладкой и пометками Великой княжны",
                     "Татьяна часто читала вслух духовную литературу матери. В её дневнике есть запись: 'Читала Евангелие маме. Она сказала, что эти строки о нас'. Евангелие хранилось в её комнате.",
                     True, "secret_dialog_gospel"),
                
                Item(3, "Нательный крест Николая II", "✝️",
                     "Простой железный крест, который император носил под рубахой",
                     "После отречения Николай носил простую крестьянскую одежду и такой же простой крест. 'Я стал таким же, как мой народ', говорил он дочерям.",
                     True, "secret_dialog_cross"),
                
                Item(4, "Молитвослов Александры", "📓",
                     "Молитвослов с записями на английском и русском",
                     "Императрица записывала молитвы о смирении перед волей Божьей. Последняя запись: 'Научи нас, Господи, принимать всё с благодарностью'.",
                     True, "secret_dialog_prayer"),
                
                Item(5, "Библия с пометками", "📕",
                     "Библия Николая, где он отмечал важные места",
                     "Император подчеркивал строки о страданиях и терпении. Книга Иова была вся испещрена пометками. Особенно стих: 'Господь дал, Господь и взял'.",
                     True, "secret_dialog_bible"),
                
                Item(6, "Образок на мощах", "🕯️",
                     "Небольшой образок, который девочки носили с собой",
                     "В письмах Татьяна упоминала: 'Мы носим образки на теле, чтобы никто не отнял последнюю защиту'. Охранники так и не нашли их при обысках.",
                     True, "secret_dialog_image"),
                
                Item(7, "Крестик Алексея", "🔱",
                     "Маленький крестик цесаревича, подаренный бабушкой",
                     "Крестик Алексея нашли позже при эксгумации останков. На нём была гравировка: 'Спаси и сохрани'. Бабушка, вдовствующая императрица Мария Фёдоровна, подарила его внуку при рождении.",
                     True, "secret_dialog_alexey")
            ]
        
        def add_item(self, item_id):
            """Добавление предмета по ID"""
            for item in self.items:
                if item.id == item_id and not item.found:
                    item.found = True
                    
                    # Визуальное уведомление
                    renpy.show_screen("item_found_notification", item=item)
                    renpy.pause(2.0)
                    renpy.hide_screen("item_found_notification")
                    
                    # Проверка на секретные диалоги
                    self.check_secret_dialog_triggers()
                    
                    return True
            return False
        
        def check_secret_dialog_triggers(self):
            """Проверка условий для секретных диалогов"""
            count = self.count_found()
            
            # Триггер для 3 предметов - вечернее чтение Евангелия
            if count >= 3 and not self.secret_dialog_triggered_3:
                self.secret_dialog_triggered_3 = True
                renpy.call_in_new_context("evening_reading")
            
            # Триггер для 5 предметов - церковное песнопение
            if count >= 5 and not self.secret_dialog_triggered_5:
                self.secret_dialog_triggered_5 = True
                renpy.call_in_new_context("church_singing")
            
            # Триггер для 7 предметов - финальное откровение
            if count >= 7 and not self.secret_dialog_triggered_7:
                self.secret_dialog_triggered_7 = True
                renpy.call_in_new_context("final_revelation")
        
        def count_found(self):
            """Количество найденных предметов"""
            return sum(1 for item in self.items if item.found)
        
        def has_item(self, item_id):
            """Проверка наличия конкретного предмета"""
            for item in self.items:
                if item.id == item_id and item.found:
                    return True
            return False
        
        def get_item_by_id(self, item_id):
            """Получение предмета по ID"""
            for item in self.items:
                if item.id == item_id:
                    return item
            return None
        
        def get_found_items(self):
            """Список найденных предметов"""
            return [item for item in self.items if item.found]
    
    # Создаем глобальный инвентарь
    inventory = Inventory()


# ============================================
# ЭКРАНЫ ИНВЕНТАРЯ
# ============================================

screen item_found_notification(item):
    """Всплывающее уведомление о найденном предмете"""
    zorder 200
    frame:
        background Solid("#4a6b8a")
        xsize 400
        ysize 120
        xalign 0.5
        yalign 0.1
        
        vbox:
            spacing 10
            xalign 0.5
            yalign 0.5
            
            text "НОВЫЙ ПРЕДМЕТ НАЙДЕН!" size 20 bold True color "#ffd700" xalign 0.5
            hbox:
                spacing 20
                xalign 0.5
                text item.icon size 40
                text item.name size 18 color "#ffffff" yalign 0.5


screen advanced_inventory():
    """Главный экран инвентаря с сеткой"""
    modal True
    zorder 100
    
    frame:
        background Solid("#2b2b2b")
        xsize 900
        ysize 650
        xalign 0.5
        yalign 0.5
        
        vbox:
            spacing 20
            xfill True
            
            # Заголовок
            frame:
                background Solid("#4a3a2a")
                xfill True
                ysize 70
                
                hbox:
                    xfill True
                    spacing 20
                    
                    text "📦 БИБЛЕЙСКИЕ АТРИБУТЫ" size 30 color "#ffd700" xalign 0.3
                    
                    # Счетчик
                    frame:
                        background Solid("#2a2a2a")
                        xsize 100
                        ysize 50
                        yalign 0.5
                        
                        text f"{inventory.count_found()}/{inventory.max_items}" size 24 color "#ffffff" xalign 0.5 yalign 0.5
            
            # Информационная строка
            frame:
                background Solid("#3a3a3a")
                xfill True
                ysize 40
                
                text "Находите библейские атрибуты, чтобы открыть секретные сцены и диалоги" size 14 color "#cccccc" xalign 0.5 yalign 0.5
            
            # Сетка предметов
            frame:
                background Solid("#2a2a2a")
                xfill True
                ysize 400
                
                viewport:
                    scrollbars "vertical"
                    mousewheel True
                    
                    vbox:
                        spacing 20
                        
                        # Строки по 3 предмета
                        python:
                            items_per_row = 3
                            rows = math.ceil(len(inventory.items) / items_per_row)
                        
                        for row in range(rows):
                            hbox:
                                spacing 20
                                xalign 0.5
                                
                                for col in range(items_per_row):
                                    python:
                                        index = row * items_per_row + col
                                        if index < len(inventory.items):
                                            item = inventory.items[index]
                                        else:
                                            item = None
                                    
                                    if item:
                                        # Карточка предмета
                                        frame:
                                            background Solid("#3a3a3a" if item.found else "#1a1a1a")
                                            xsize 250
                                            ysize 220
                                            
                                            vbox:
                                                spacing 10
                                                xalign 0.5
                                                yalign 0.5
                                                
                                                # Иконка - ИСПРАВЛЕНО: убран условный оператор из текста
                                                $ icon_color = "#ffd700" if item.found else "#666666"
                                                text item.icon size 60 color icon_color xalign 0.5
                                                
                                                # Название
                                                $ name_color = "#ffffff" if item.found else "#666666"
                                                text item.name size 16 bold True color name_color xalign 0.5
                                                
                                                # Статус
                                                if item.found:
                                                    text "✓ НАЙДЕНО" size 12 color "#00ff00" xalign 0.5
                                                    
                                                    # Кнопка информации
                                                    textbutton "ПОДРОБНЕЕ":
                                                        style "inventory_button"
                                                        xalign 0.5
                                                        action Show("item_info_screen", item=item)
                                                else:
                                                    text "❌ НЕ НАЙДЕНО" size 12 color "#ff0000" xalign 0.5
                                                    text "???" size 20 color "#444444" xalign 0.5
                                    else:
                                        # Пустая ячейка
                                        frame:
                                            background Solid("#1a1a1a")
                                            xsize 250
                                            ysize 220
            
            # Нижняя панель
            hbox:
                spacing 20
                xalign 0.5
                
                textbutton "ЗАКРЫТЬ" action Hide("advanced_inventory") style "inventory_button"
                
                if inventory.count_found() == inventory.max_items:
                    textbutton "ФИНАЛЬНАЯ СЦЕНА" action [Hide("advanced_inventory"), Jump("final_revelation")] style "inventory_button"


screen item_info_screen(item):
    """Экран подробной информации о предмете"""
    modal True
    zorder 200
    
    frame:
        background Solid("#3a4a5a")
        xsize 500
        ysize 400
        xalign 0.5
        yalign 0.5
        
        vbox:
            spacing 20
            xfill True
            yfill True
            
            # Заголовок с иконкой
            hbox:
                spacing 20
                xalign 0.5
                
                text item.icon size 60
                text item.name size 24 bold True color "#ffd700" yalign 0.5
            
            # Разделитель
            frame:
                background Solid("#5a6b7a")
                xfill True
                ysize 2
            
            # Описание
            frame:
                background Solid("#2a3a4a")
                xfill True
                ysize 80
                
                text item.description size 16 color "#ffffff" xalign 0.5 yalign 0.5
            
            # Историческая справка
            vbox:
                spacing 5
                
                text "ИСТОРИЧЕСКАЯ СПРАВКА:" size 14 bold True color "#ffd700"
                
                frame:
                    background Solid("#2a3a4a")
                    xfill True
                    
                    text item.historical_note size 14 color "#cccccd" xalign 0.5
            
            # ID предмета
            text f"ID: {item.id}" size 12 color "#aaaaaa" xalign 0.5
            
            # Кнопка закрытия
            textbutton "ЗАКРЫТЬ" action Hide("item_info_screen") style "inventory_button" xalign 0.5


screen quick_inventory():
    """Быстрая панель инвентаря на экране"""
    zorder 50
    frame:
        background Solid("#2b2b2b")
        xpos 20
        ypos 20
        xsize 350
        ysize 60
        
        hbox:
            spacing 15
            xfill True
            yfill True
            
            # Иконка инвентаря
            text "📦" size 30 yalign 0.5
            
            # Быстрый показ найденных предметов
            hbox:
                spacing 5
                yalign 0.5
                
                for i in range(1, 8):
                    if inventory.has_item(i):
                        text "✓" color "#00ff00" size 20
                    else:
                        text "○" color "#666666" size 20
            
            # Счетчик
            text f"{inventory.count_found()}/7" size 18 color "#ffd700" yalign 0.5
            
            # Кнопка открытия инвентаря
            textbutton "ПОДРОБНЕЕ" action Show("advanced_inventory") style "quick_inventory_button" xalign 1.0


# Стили для кнопок
style inventory_button:
    size 18
    color "#ffffff"
    hover_color "#ffd700"
    background Solid("#5a5a5a")
    hover_background Solid("#6a6a6a")
    xpadding 20
    ypadding 10

style quick_inventory_button:
    size 14
    color "#ffffff"
    hover_color "#ffd700"
    background Solid("#4a4a4a")
    hover_background Solid("#5a5a5a")
    xpadding 10
    ypadding 5


# Активируем быстрый инвентарь на всех экранах
init python:
    config.overlay_screens.append("quick_inventory")


# ============================================
# СЕКРЕТНЫЕ ДИАЛОГИ (триггеры)
# ============================================

label evening_reading:
    """Сцена вечернего чтения (3 предмета)"""
    scene black with fade
    # Здесь будет ваша сцена
    "Вечернее чтение Евангелия (доступно при 3+ предметах)"
    return


label church_singing:
    """Сцена церковного песнопения (5 предметов)"""
    scene black with fade
    # Здесь будет ваша сцена
    "Церковное песнопение (доступно при 5+ предметах)"
    return


label final_revelation:
    """Финальная сцена-откровение (7 предметов)"""
    scene black with fade
    # Здесь будет ваша сцена
    "Финальное откровение (доступно при всех 7 предметах)"
    return

