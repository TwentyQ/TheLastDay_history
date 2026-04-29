init python:
    import math

    class Item:
        def __init__(self, id, name, icon_file, hover_icon_file, description, historical_note, secret_dialog=False, dialog_ref=None):
            self.id = id
            self.name = name
            self.icon_file = icon_file          # обычная иконка
            self.hover_icon_file = hover_icon_file  # иконка при наведении
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
                Item(1, "Икона Спаса Нерукотворного",
                     "images/inventory/icon.png",
                     "images/inventory/icon_dark.png",
                     "Мамина любимая икона. Она сказала: «Смотри на Него, когда страшно». Я смотрю. Её не отобрали, спрятали под подушкой.",
                     "Икона Спаса Нерукотворного была частью походного иконостаса семьи. Её брали даже в ссылку."),

                Item(2, "Евангелие Татьяны",
                     "images/inventory/bibl.png",
                     "images/inventory/bibl_dark.png",
                     "Таня читает каждый вечер. Она отметила страницу: «Блаженны изгнанные правды ради». Я спросила, почему. Она не ответила, только улыбнулась.",
                     "Великая княжна Татьяна часто читала вслух духовную литературу. В ссылке она помогала матери молиться."),

                Item(3, "Нательный крест Николая",
                     "images/inventory/cross_n.png",
                     "images/inventory/cross_n_dark.png",
                     "Папин крест. Я спросила: «Ты его ради нас носишь?» Он обнял меня: «Ради всех. И ради вас, мои девочки»",
                     "Простой железный крест стал символом пути, пройденного последним русским императором. После его мученической кончины этот образ глубоко укоренился в народной памяти, став олицетворением смирения и искупительной жертвы"),

                Item(4, "Молитвослов Александры",
                     "images/inventory/prayer.png",
                     "images/inventory/prayer_dark.png",
                     "Мама записала на полях: «Дарите любовь, даже когда больно». У неё дрожат руки, но она пишет. Я не понимала раньше… Теперь понимаю.",
                     "Императрица Александра Федоровна в заключении вела духовный дневник, позже изданный как книга «Сад сердца». Её записи полны размышлений о смирении, силе веры и любви. Она писала: «Чем меньше надежды, тем сильнее вера..."),

                Item(5, "Библия с пометками",
                     "images/inventory/notes.png",
                     "images/inventory/notes_dark.png",
                     "Папа подчеркнул: «Приидите ко Мне все труждающиеся…». Я спросила, труждающиеся - это мы? Он не ответил. Только перекрестил меня.",
                     "Николай II был глубоко верующим человеком и часто делал пометы в своём экземпляре Библии. Он воспринимал свою судьбу и страдания своей семьи как волю Божию, находя утешение в чтении Священного Писания."),

                Item(6, "Образок на мощах",
                     "images/inventory/icons.png",
                     "images/inventory/icons_dark.png",
                     "Тайный образок. Мария носила его на груди. Она сказала: «Это от бабушки, от святой». Я боюсь даже трогать. Но сегодня взяла - пусть хранит.",
                     "В домах Романовых хранилось множество святынь. В частности, известен «Крест-Мощевик», принадлежавший семье императора. После гибели семьи он был спасён и ныне является чтимой реликвией"),

                Item(7, "Крестик Алексея",
                     "images/inventory/cross_a.png",
                     "images/inventory/cross_a_dark.png",
                     "Крестик Алёши. Говорят, его подарила бабушка, императрица Мария Фёдоровна. Он никогда с ним не расставался. Я верю, что её молитвы доходят до нас даже сейчас",
                     "Связь бабушки и внука была очень тёплой. Сохранились письма царевича, в которых он обращается «Милая Бабушка!», делится новостями об учёбе и подписывается «любящий тебя Алексей».")
            ]

        def add_item(self, item_id):
            for item in self.items:
                if item.id == item_id and not item.found:
                    item.found = True
                    renpy.notify(f"{item.name} - мы должны это запомнить")
                    return True
            return False

        def has_item(self, item_id):
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
    zorder 300
    imagebutton:
        idle Transform("images/inventory/book.png", size=(150,150))
        hover Transform("images/inventory/book_dark.png", size=(150,150))
        xpos 1720
        ypos 20
        action Show("diary_inventory")


# =====================================================
# ГЛАВНЫЙ ЭКРАН ИНВЕНТАРЯ (ДНЕВНИК)
# =====================================================
screen diary_inventory():
    modal True
    zorder 100
    add Solid("#00000080")
    add "images/inventory/open.png" xalign 0.5 yalign 0.5

    text "Артефакты [inventory.count_found()]/[inventory.max_items]" size 60 color "#2c1e0e" font "fonts/GreatVibes.ttf":
        xpos 520
        ypos 180

    # ЛЕВАЯ СТРАНИЦА (предметы 1-4)
    fixed:
        xpos 520
        ypos 260
        xsize 420
        ysize 600
        vbox:
            spacing 35
            text "Святыни":
                size 40
                color "#2c1e0e"
                font "fonts/GreatVibes.ttf"
            for i in range(0,4):
                if i < len(inventory.items):
                    $ item = inventory.items[i]
                    hbox:
                        spacing 20
                        if item.found:
                            imagebutton:
                                idle Transform(item.icon_file, size=(100,100))
                                hover Transform(item.hover_icon_file, size=(100,100))
                                action Show("item_info_screen", item=item)
                        else:
                            text "?" size 80 color "#8B7355"
                        text item.name:
                            size 30
                            color ("#2c1e0e" if item.found else "#8B7355")
                            font "fonts/GreatVibes.ttf"
                            yalign 0.5

    # ПРАВАЯ СТРАНИЦА (предметы 5-7)
    fixed:
        xpos 1000
        ypos 260
        xsize 410
        ysize 600
        vbox:
            spacing 35
            text "Записи":
                size 40
                color "#2c1e0e"
                font "fonts/GreatVibes.ttf"
            for i in range(4,7):
                if i < len(inventory.items):
                    $ item = inventory.items[i]
                    hbox:
                        spacing 20
                        if item.found:
                            imagebutton:
                                idle Transform(item.icon_file, size=(100,100))
                                hover Transform(item.hover_icon_file, size=(100,100))
                                action Show("item_info_screen", item=item)
                        else:
                            text "?" size 80 color "#8B7355"
                        text item.name:
                            size 30
                            color ("#2c1e0e" if item.found else "#8B7355")
                            font "fonts/GreatVibes.ttf"
                            yalign 0.5
            frame:
                background "#8B7355"
                xsize 360
                ysize 1
            if inventory.count_found() == 0:
                text "Пока ничего не найдено..." size 25 color "#8B7355"
            elif inventory.count_found() < 3:
                text "Найдено несколько святынь..." size 25 color "#2c1e0e"
            elif inventory.count_found() < 5:
                text "Господь с нами..." size 25 color "#2c1e0e"
            elif inventory.count_found() < 7:
                text "Почти всё собрано..." size 25 color "#2c1e0e"
            else:
                text "Да будет воля Твоя..." size 25 color "#2c1e0e"

    imagebutton:
        idle "images/inventory/bookmark.png"   # без Transform, используем оригинальный размер
        hover "images/inventory/bookmark_dark.png"
        focus_mask True
        xpos 940
        ypos -50
        action Hide("diary_inventory")

# =====================================================
# ЭКРАН ОПИСАНИЯ ПРЕДМЕТА
# =====================================================
screen item_info_screen(item):
    modal True
    zorder 200
    add Solid("#00000080")

    frame:
        background Transform("images/inventory/letter.png", size=(800,650))
        xalign 0.5
        yalign 0.5
        xsize 800
        ysize 650

        frame:
            background None
            xfill True
            yfill True
            xmargin 100
            ymargin 100

            # Убираем yalign 0.5, добавляем yoffset и верхний отступ
            vbox:
                spacing 25
                xalign 0.5
                yoffset -30   # поднимаем весь блок вверх
                # Альтернатива: добавить пустой текст сверху как распорку
                # или использовать ypos 0

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

                frame:
                    background "#8B7355"
                    xsize 550
                    ysize 2
                    xalign 0.5

                text item.description:
                    size 30
                    color "#2c1e0e"
                    font "fonts/GreatVibes.ttf"
                    xalign 0.5
                    text_align 0.5
                    layout "subtitle"

                text item.historical_note:
                    size 20
                    color "#2c1e0e"
                    font "fonts/RussoOne.ttf"
                    xalign 0.5
                    text_align 0.5
                    layout "subtitle"

        # Кнопка-печать
        imagebutton:
            idle Transform("images/inventory/wax_seal.png", size=(200,200))
            hover Transform("images/inventory/wax_seal_dark.png", size=(200,200))
            action Hide("item_info_screen")
            align (1, 0.95)

# Подключаем быстрый инвентарь как оверлей
init python:
    config.overlay_screens.append("quick_inventory")