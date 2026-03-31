init python:
    import math

    class Item:
        def __init__(self, id, name, icon_file, description, historical_note, secret_dialog=False, dialog_ref=None):
            self.id = id
            self.name = name
            self.icon_file = icon_file
            self.description = description
            self.historical_note = historical_note
            self.secret_dialog = secret_dialog
            self.dialog_ref = dialog_ref
            self.found = False


    class Inventory:
        def __init__(self):
            self.items = []
            self.max_items = 7
            self.create_items()

            self.secret_dialog_triggered_3 = False
            self.secret_dialog_triggered_5 = False
            self.secret_dialog_triggered_7 = False


        def create_items(self):
            self.items = [
                Item(1,"Икона Спаса Нерукотворного","images/inventory/icon.png",
                "Небольшая икона, которую Анастасия взяла из Царского Села",
                "Императорская семья всегда возила с собой походные иконы."),

                Item(2,"Евангелие Татьяны","images/inventory/bibl.png",
                "Евангелие с закладкой и пометками Великой княжны",
                "Татьяна часто читала духовную литературу матери."),

                Item(3,"Нательный крест Николая","images/inventory/cross_n.png",
                "Простой железный крест",
                "После отречения Николай носил простой крест."),

                Item(4,"Молитвослов Александры","images/inventory/prayer.png",
                "Молитвослов с записями",
                "Императрица записывала молитвы о смирении."),

                Item(5,"Библия с пометками","images/inventory/notes.png",
                "Библия Николая",
                "Император подчеркивал строки о терпении."),

                Item(6,"Образок на мощах","images/inventory/icons.png",
                "Небольшой образок",
                "Девочки носили его тайно."),

                Item(7,"Крестик Алексея","images/inventory/cross_a.png",
                "Крестик цесаревича",
                "Подарок Марии Фёдоровны.")
            ]


        def add_item(self, item_id):
            for item in self.items:
                if item.id == item_id and not item.found:
                    item.found = True
                    renpy.notify(f"[{item.name}] найден!")
                    return True
            return False
            
            
        def has_item(self, item_id):
            """Проверка наличия предмета по ID"""
            for item in self.items:
                if item.id == item_id and item.found:
                    return True
            return False


        def count_found(self):
            return sum(1 for item in self.items if item.found)


default inventory = Inventory()


# =====================================================
# БЫСТРАЯ ИКОНКА ИНВЕНТАРЯ
# =====================================================

screen quick_inventory():
    zorder 50
    imagebutton:
        idle Transform("images/inventory/book.png", size=(150,150))
        hover Transform("images/inventory/book.png", size=(150,150), matrixcolor=TintMatrix("#808080"))
        xpos 1720
        ypos 20
        action Show("diary_inventory")


# =====================================================
# ГЛАВНЫЙ ЭКРАН ИНВЕНТАРЯ (УВЕЛИЧЕННЫЕ ИКОНКИ)
# =====================================================

screen diary_inventory():
    modal True
    zorder 100
    add Solid("#00000080")
    add "images/inventory/open.png" xalign 0.5 yalign 0.5

    # ЗАГОЛОВОК
    text "Артефакты [inventory.count_found()]/[inventory.max_items]" size 60 color "#2c1e0e" font "fonts/GreatVibes.ttf":
        xpos 520
        ypos 180

    # ЛЕВАЯ СТРАНИЦА (ИКОНКИ 100x100 + БОЛЬШОЙ ОТСТУП)
    fixed:
        xpos 520
        ypos 260
        xsize 420
        ysize 600
        vbox:
            spacing 35  # УВЕЛИЧЕНО расстояние между строками
            text "Святыни":
                size 40
                color "#2c1e0e"
                font "fonts/GreatVibes.ttf"
            for i in range(0,4):
                if i < len(inventory.items):
                    $ item = inventory.items[i]
                    hbox:
                        spacing 20  # УВЕЛИЧЕНО расстояние между иконкой и текстом
                        if item.found:
                            imagebutton:
                                idle Transform(item.icon_file, size=(100,100))  # БЫЛО 60, СТАЛО 100
                                hover Transform(item.icon_file, size=(100,100), matrixcolor=TintMatrix("#808080"))
                                action Show("item_info_screen", item=item)
                        else:
                            text "?" size 80 color "#8B7355"  # БЫЛО 50, СТАЛО 80
                        text item.name:
                            size 30  # БЫЛО 20, СТАЛО 22
                            color ("#2c1e0e" if item.found else "#8B7355")
                            font "fonts/GreatVibes.ttf"
                            yalign 0.5  # Выравнивание по центру относительно иконки

    # ПРАВАЯ СТРАНИЦА (ИКОНКИ 100x100 + БОЛЬШОЙ ОТСТУП)
    fixed:
        xpos 1000
        ypos 260
        xsize 410
        ysize 600
        vbox:
            spacing 35  # УВЕЛИЧЕНО
            text "Записи":
                size 40
                color "#2c1e0e"
                font "fonts/GreatVibes.ttf"
            for i in range(4,7):
                if i < len(inventory.items):
                    $ item = inventory.items[i]
                    hbox:
                        spacing 20  # УВЕЛИЧЕНО
                        if item.found:
                            imagebutton:
                                idle Transform(item.icon_file, size=(100,100))  # БЫЛО 60, СТАЛО 100
                                hover Transform(item.icon_file, size=(100,100), matrixcolor=TintMatrix("#808080"))
                                action Show("item_info_screen", item=item)
                        else:
                            text "?" size 80 color "#8B7355"  # БЫЛО 50, СТАЛО 80
                        text item.name:
                            size 30  # БЫЛО 20, СТАЛО 22
                            color ("#2c1e0e" if item.found else "#8B7355")
                            font "fonts/GreatVibes.ttf"
                            yalign 0.5
            frame:
                background "#8B7355"
                xsize 360
                ysize 1
            if inventory.count_found()==0:
                text "Пока ничего не найдено..." size 25 color "#8B7355"
            elif inventory.count_found()<3:
                text "Найдено несколько святынь..." size 25 color "#2c1e0e"
            elif inventory.count_found()<5:
                text "Господь с нами..." size 25 color "#2c1e0e"
            elif inventory.count_found()<7:
                text "Почти всё собрано..." size 25 color "#2c1e0e"
            else:
                text "Да будет воля Твоя..." size 25 color "#2c1e0e"

    # ЗАКРЫТЬ (закладка)
    imagebutton:
        idle Transform("images/inventory/bookmark.png", size=(700,1100))
        hover Transform("images/inventory/bookmark.png", size=(700,1100), matrixcolor=TintMatrix("#808080"))
        xpos 1010
        ypos -30
        action Hide("diary_inventory")


# =====================================================
# ЭКРАН ОПИСАНИЯ ПРЕДМЕТА (тоже увеличим иконку)
# =====================================================

screen item_info_screen(item):
    """Экран информации о предмете"""
    modal True
    zorder 200
    add Solid("#00000080")
    
    # Контейнер для всего содержимого
    frame:
        background Transform("images/inventory/letter.png", size=(800,650))
        xalign 0.5
        yalign 0.5
        xsize 800
        ysize 650
        
        # Внутренний контейнер с отступами
        frame:
            background None
            xfill True
            yfill True
            xmargin 50
            ymargin 50
            
            vbox:
                spacing 25
                xalign 0.5
                yalign 0.5
                
                # Верхний блок с иконкой и названием
                hbox:
                    spacing 40
                    xalign 0.4
                    
                    add Transform(item.icon_file, size=(120,120)):
                        yoffset 20
                    text item.name:
                        size 40
                        color "#2c1e0e"
                        yalign 0.9
                        font "fonts/GreatVibes.ttf"
                
                # Линия-разделитель
                frame:
                    background "#8B7355"
                    xsize 550
                    ysize 2
                    xalign 0.5
                
                # Описание
                text item.description:
                    size 30
                    color "#2c1e0e"
                    font "fonts/GreatVibes.ttf"
                    xalign 0.5
                    text_align 0.5
                    layout "subtitle"
                
                # Историческая справка
                text item.historical_note:
                    size 30
                    color "#2c1e0e"
                    font "fonts/RussoOne.ttf"
                    xalign 0.5
                    text_align 0.5
                    layout "subtitle"
                
                # Кнопка закрытия
                imagebutton:
                    idle Transform("images/inventory/wax_seal.png", size=(200,200))
                    hover Transform("images/inventory/wax_seal.png", size=(200,200), matrixcolor=TintMatrix("#808080"))
                    action Hide("item_info_screen")
                    xpos -57  # отступ слева в пикселях
                    ypos 20
# =====================================================
# ПОДКЛЮЧЕНИЕ
# =====================================================

init python:
    config.overlay_screens.append("quick_inventory")