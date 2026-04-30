# Вы можете расположить сценарий своей игры в этом файле.

# Определение персонажей игры.
define a = Character("Анастасия", who_color="#d05b20", what_color="#2c1e0e")
define ia = Character("Внутренний голос Анастасии", who_color="#57250c", what_color="#2c1e0e")
define o = Character("Ольга", who_color="#521aa7", what_color="#2c1e0e")
define t = Character("Татьяна", who_color="#4682B4", what_color="#2c1e0e")
define m = Character("Мария", who_color="#5256B9", what_color="#2c1e0e")
define n = Character("Николай", who_color="#185F3E", what_color="#2c1e0e")
define al = Character("Александра", who_color="#800020", what_color="#2c1e0e")
define ax = Character("Алексей", who_color="#2E8B57", what_color="#2c1e0e")
define g = Character("Охранник", who_color="#6E2500", what_color="#2c1e0e")
define b = Character("Доктор Боткин", who_color="#460707", what_color="#2c1e0e")
define h = Character("Харитонов", who_color="#9E664A", what_color="#2c1e0e")
define d = Character("Демидова", who_color="#F74242", what_color="#2c1e0e")

# Где-то после определений персонажей, но до label start
screen dog():
    timer 5.0 repeat True action Play("sound", "dog.mp3")

default card_game_active = False
default sekretny_dialog = False
default heard_soldiers = False
default all_items_collected = False
default poslednyaya_molitva = ""

# В самом начале игры
label start:
    # Сохраняем оригинальный overlay
    $ original_overlay = config.overlay_screens.copy()
    $ original_quick_menu = quick_menu
    $ game_finished = True
    $ game_over = True
    $ waiting_for_player = False
    $ card_game_active = False
    $ renpy.hide_screen("card_game_ui")
    
    # ПОЛНОЕ отключение всего интерфейса
    $ config.overlay_screens = []
    $ _preferences.afm_enable = False
    $ quick_menu = False
    
    # Скрываем все окна и кнопки
    window hide
    
    scene black with fade
    
    $ intro_texts = [
        "16 июля 1918 года.",
        "Екатеринбург, Дом Ипатьева.",
        "Семья Романовых находится в заточении уже 78 дней."
    ]
    
    $ i = 0
    while i < len(intro_texts):
        $ text_line = intro_texts[i]
        
        # Используем centered для полного отключения интерфейса
        centered "{color=#ffffff}[text_line]{/color}"
        
        $ i += 1
    
    # Восстанавливаем интерфейс
    $ quick_menu = original_quick_menu
    
    jump morning


# Игра начинается здесь:
label morning:

    # Включаем интерфейс только сейчас
    $ config.overlay_screens = original_overlay
    window show
    show screen quick_inventory

    
    python:
        if persistent.inventory_data:
            inventory = persistent.inventory_data
        else:
            inventory = Inventory()

    scene bg girl room with fade
    play music "audio/garden.mp3" loop volume 0.2 fadein 2.0


    "Комната девушек. Тусклый солнечный свет сочиться сквозь забеленные окна."
    "На походных кроватях спят княжны Романовы. Самая старшая - Ольга расположилась в дальнем углу комнаты, на кровати рядом с ней - Татьяна, у двери - Мария и, наконец, у окна лежит уже проснувшаяся Анастасия."

    ia "Сегодня мне снился Тобольск."

    ia "Вот наш дом, а чуть подле - заснеженный Иртыш."

    ia "Папа во дворе колит дрова, а мы с Алёшкой лепим снежную бабу..."

    ia "Сёстры опять помогают матушке на кухне."
    
    ia "Скоро Рождество… Так странно… Почему мне сниться зима? Ведь сейчас июль..."

    window hide
    menu:
        "Осмотреться в комнате":
            jump examine_room_morning

        "Разбудить Олю":
            jump wake_olga



label examine_room_morning:
    scene bg girl room with dissolve
    window show
    "Анастасия оглядывает комнату. Всё как обычно, но сегодня почему-то хочется рассмотреть каждую мелочь."

    window hide
    show bg girl room:
        linear 0.8 zoom 1.3
        # Двигаемся в пределах видимой области (anchor 0.5)
        linear 1.5 xanchor 0.5 xpos 0.4  # смещаем центр внимания левее
        pause 0.2
        linear 1.5 xanchor 0.5 xpos 0.6  # смещаем центр внимания правее
        pause 0.2
        linear 1.0 xanchor 0.5 xpos 0.5 zoom 1.0  # возврат
        
    $ renpy.pause(0.8 + 1.5 + 0.2 + 1.5 + 0.2 + 1.0, hard=True)

    menu:
        "Осмотреть тумбочку":
            $ inventory.add_item(1)
            play sound "audio/notify.mp3"
            "На тумбочке лежит небольшая икона Спаса Нерукотворного. Анастасия креститься, нашёптывая короткую молитву себе под нос, и берёт найденный предмет в руки."
            ia "Эту икону мама дала мне перед отъездом из Царского Села. Как же давно это было… Кажется, с того момента прошла целая вечность."
            ia "Негоже иконе на тумбочке лежать. Спрячу ка я её куда понадёжнее..."
            "Анастасия тихонько подходит к своей кроватке, чтобы не разбудить сестёр и прячет икону под подушку."

        "Посмотреть в окно":
            scene bg wind with dissolve
            play sound "audio/window.mp3"
            window show
            "Сквозь забеленные стёкла почти ничего не видно. Анастасия с трудом разглядывает в этой белизне размытые силуэты деревьев и небольшой кусочек неба."
            ia "А ведь раньше, в Царском Селе, я могла часами разглядывать живописные пейзажи. Я помню наш Александровский дворец, аккуратный и светлый, наши пруды с лебедями, парк невообразимых размеров... Жаль, что не могу насладиться этой красотой хоть ещё разок..."
            "Она тянется рукой к холодному стеклу... касается... но резко одёргивает её, оглядываясь на дверь - не вошёл ли часовой."
            window hide
        
        "Посмотреть на спящих сестер":
            "Анастасия обводит взглядом спящих сестер."
            "Ольга спит беспокойно — нахмурила брови, сжала губы. Даже во сне не может расслабиться, всегда переживает за всех."
            ia "Оля как вторая мама. Только мама устала, а Оля держится. Ради нас."
            "Татьяна поджала ноги к груди, свернулась калачиком. Даже во сне изящная, аккуратная."
            ia "Таня всегда говорила, что так теплее. Наверное, ей холодно. Нам всем холодно последнее время."
            "Мария улыбается во сне, чему-то своему, девичьему."
            ia "Машенька даже здесь находит повод для улыбки. Говорит, что Бог не оставляет, солнышко светит и птички поют. Хорошо, что она у нас есть."
            "Анастасия задерживает взгляд на каждой сестре и чувствует, как к горлу подступает комок."
            ia "Лишь бы мы были вместе. Что бы ни случилось — лишь бы вместе."
        
        "Вернуться к сестрам":
            jump wake_sisters
        "Вернуться к своей кровати":
            jump go_to_the_bed
    
    jump go_to_the_bed

label go_to_the_bed:

    scene bg girl room with dissolve

    window show

    "Анастасия возвращается к кровати, как вдруг её окликает нежный и ласковый голос одной из сестёр."
    "???" "Настенька, ты уже встала?"
    "Анастасия оглядывается." "Этот голос принадлежит Оле - её старшей сестре."
    "Ольга мягко улыбается и подходит к Анастасии."

    jump olga_question

label wake_olga:

    scene bg girl room with dissolve

    window show

    "Анастасия резко поднимается с кровати."
    "Внутренний голос Анастасии" "Батюшки! Который час?! Через это забеленное окно и намёка на солнышко нет. 
    Нужно скорее разбудить Ольгу, а то опять будет скандал из-за долгих сборов в ванную..."
    "Анастасия настороженно крадётся к Ольге. Та спит беспокойно - видно, что во сне её снова что-то тревожит."
    "Анастасия не хочет будить сестру: та и так плохо спит последнее время. Но страх берёт своё. 
    Она собирается с мыслями и уже тянет свою крохотную руку, чтобы коснуться плеча Ольги... 
    как та неожиданно приподнимается с кровати."
    "От такого внезапного пробуждения сестры Настя отстраняется от кровати. 
    Она выглядит слегка растерянной. Но мягкий и ласковый голос Ольги возвращает её к действительности."
    
    show olga sleepy:
        zoom 1.5
        pos (220, 150)
    show anastasia shy:
        zoom 1.2
        pos (960, 200)
    
    o "Настенька, тебя что-то беспокоит? На тебе лица нет."

    show olga shy:
        zoom 1.5
        pos (220, 150)
    show anastasia shy:
        zoom 1.2
        pos (960, 200)

    "Анастасия ещё несколько мгновений смотрит на сестру. По лицу той видно, что спалось ей плохо, хотя она старается не подавать виду."

    show olga shy:
        zoom 1.5
        pos (220, 150)
    show anastasia sleepy:
        zoom 1.2
        pos (960, 200)

    a "Оля... а.. который час? Я забеспокоилась что мы могли вздремнуть дольше положенного. Вот и вскочила так..."
    
    show olga shy:
        zoom 1.5
        pos (220, 150)
    show anastasia shy:
        zoom 1.2
        pos (960, 200)

    "Оля слегка улыбается. Прислушивается. В коридоре ходят то ли слуги, то ли охрана. Шаги медленные, размеренные."

    "Внутренний голос Анастасии" "Улыбка Оли успокаивает. В ней есть что-то умиротворяющее… не знаю что…"
    
    show olga sleepy:
        zoom 1.5
        pos (220, 150)
    show anastasia shy:
        zoom 1.2
        pos (960, 200)

    o "Сестрёнка, сейчас примерно половина восьмого. Не стоит беспокоиться. Я бы обязательно вас разбудила. Но ты умница. Лучше лишний раз проверить, чем потом жалеть."

    show olga shy:
        zoom 1.5
        pos (220, 150)
    show anastasia shy:
        zoom 1.2
        pos (960, 200)

    "Неожиданно для себя Анастасия чувствует облегчение. На её лице уже сверкает яркая улыбка, а в глазах заметен свойственный её глазам блеск."

    window hide
    hide olga shy
    hide anastasia shy
    with fade
    pause

    show olga shy:
        zoom 1.5
        pos (220, 150)
    show anastasia shy:
        zoom 1.2
        pos (960, 200)

    "Оля окончательно просыпается и встаёт с кровати. Она оглядывает Татьяну и Марию, которые всё ещё сладко спят. Старшая сестра пока не решается их будить."

    "Внутренний голос Ольги" "Пусть ещё поспят. Некуда нам торопиться..."
    "Взгляд Ольги снова падает на Анастасию. Та стоит в стороне - робкая, отстранённая, будто всё ещё пытается проснуться."

    jump olga_question

label olga_question:

    show olga sleepy:
        zoom 1.5
        pos (220, 150)
    show anastasia shy:
        zoom 1.2
        pos (960, 200)

    o "Как тебе спалось, Настенька?"

    window hide

    hide olga shy
    hide anastasia shy
    with fade

    default nastya_dream_answer = None
    window hide
    menu:
        "«Мне снился сон...»":
            window show

            $ nastya_dream_answer = "tobolsk"

            show olga shy:
                zoom 1.5
                pos (220, 150)
            show anastasia shy:
                zoom 1.2
                pos (960, 200)
            with fade

            "Анастасия немного мешкается. Она не хочет беспокоить сестру своим странным сном. Но всё же, немного подумав, решается сказать."

            show anastasia sleepy:
                zoom 1.2
                pos (960, 200)

            a "Если честно... мне снился заснеженный Тобольск..."

            show anastasia shy:
                zoom 1.2
                pos (960, 200)

            "Ольга удивлённо поднимает брови, но не перебивает."

            show anastasia sleepy:
                zoom 1.2
                pos (960, 200)

            a "Мы готовились к Рождеству. На кухне вкусно пахло едой... На улице зима. И вроде должно быть холодно... а мне тепло..."

            show anastasia shy:
                zoom 1.2
                pos (960, 200)

            "Анастасия опускает взгляд..."
            "Ольга аккуратно касается её плеча и произносит:"

            show olga sleepy:
                zoom 1.5
                pos (220, 150)

            o "Хорошее воспоминание, Настенька, хорошее... Мне тоже часто снится наша жизнь до..."

            show olga shy:
                zoom 1.5
                pos (220, 150)

            "Ольга подбирает нужное слово, чтобы не нагнать на сестру тоску."

            show olga sleepy:
                zoom 1.5
                pos (220, 150)

            o "...до всего этого..."
            o "Главное - не вешать носу. Пока мы вместе, нам никакие невзгоды не страшны."

            show olga shy:
                zoom 1.5
                pos (220, 150)

            "Анастасия смотрит на сестру. Лицо той слегка грустное, но в глазах виднеется огонёк надежды на 
            светлое будущее."
            "Анастасия невольно улыбается и тихо произносит:"

            show anastasia sleepy:
                zoom 1.2
                pos (960, 200)

            a "Спасибо... Оля..."

            show anastasia shy:
                zoom 1.2
                pos (960, 200)

        "«Охрана всю ночь не давала спать»":

            $ nastya_dream_answer = "bad_sleep"

            show olga shy:
                zoom 1.5
                pos (220, 150)
            show anastasia sleepy:
                zoom 1.2
                pos (960, 200)
            with fade

            a "Плохо, сестра... Охрана всю ночь пьянствовала... Не давала спать."

            show anastasia shy:
                zoom 1.2
                pos (960, 200)

            "Ольга понимающе кивает."

            show olga sleepy:
                zoom 1.5
                pos (220, 150)

            o "Слышала этих чертей. Небось, опять праздновали что-то..."

            show olga shy:
                zoom 1.5
                pos (220, 150)

            "На лице Насти пробежал лёгкий испуг..."
            ia "Что если они праздновали..."
            "Анастасия резко замотала головой."
            ia "Настя! Что за глупости! Возьми себя в руки. Этого просто не может быть!"

            if inventory.has_item(1):
                "Несмотря на попытки успокоить себя, рука Анастасии невольно касается подушки, под которой спрятана икона."
                "Ольга замечает это."

                show olga sleepy:
                    zoom 1.5
                    pos (220, 150)

                o "Что случилось, сестрёнка?"

                show olga shy:
                    zoom 1.5
                    pos (220, 150)
                show anastasia sleepy:
                    zoom 1.2
                    pos (960, 200)

                a "Злая мысль пробежала в голове... Вот утром икону нашла... Ту, что мама дала. Лежала на тумбочке. Я и подумала - она поможет справиться с этой мыслью..."

                show anastasia shy:
                    zoom 1.2
                    pos (960, 200)

                "Ольга нежно касается Настиных волос и слегка гладит её по голове."

                show olga sleepy:
                    zoom 1.5
                    pos (220, 150)

                o "Правильно, Настенька, правильно... Храни её. Это теперь наше единственное богатство."

                show olga shy:
                    zoom 1.5
                    pos (220, 150)
            else:
                show olga sleepy:
                    zoom 1.5
                    pos (220, 150)

                o "Что случилось, сестрёнка?"

                show olga shy:
                    zoom 1.5
                    pos (220, 150)
                show anastasia sleepy:
                    zoom 1.2
                    pos (960, 200)

                a "Нет, нет... всё хорошо... Просто мысль..."

                show olga sleepy:
                    zoom 1.5
                    pos (220, 150)
                show anastasia shy:
                    zoom 1.2
                    pos (960, 200)

                o "Мысли - они те ещё черти. Засядут в голове - потом и вовек не выковыряешь."
        
        "«Хорошо»":
            window show

            $ nastya_dream_answer = "good_sleep"

            show olga shy:
                zoom 1.5
                pos (220, 150)
            show anastasia sleepy:
                zoom 1.2
                pos (960, 200)

            a "Сегодня я спала крепко. Даже сон снился... хороший."

            show anastasia shy:
                zoom 1.2
                pos (960, 200)

            "Ольга улыбается. Видно, что она искренне рада за сестру."

            show olga sleepy:
                zoom 1.5
                pos (220, 150)

            o "Какое счастье, Настенька! Хорошо, что хоть сегодня удалось выспаться. 
            А то вчера ты беспокойно спала..."

            show olga shy:
                zoom 1.5
                pos (220, 150)
            show anastasia sleepy:
                zoom 1.2
                pos (960, 200)

            a "То кошмар был, Оля... страшный-престрашный..."

            show olga sleepy:
                zoom 1.5
                pos (220, 150)
            show anastasia shy:
                zoom 1.2
                pos (960, 200)

            o "Ну ничего! Теперь всё позади. Мы вместе, а значит, нас ждёт счастье!"

            show olga shy:
                zoom 1.5
                pos (220, 150)

    hide olga shy
    hide anastasia shy
    with fade

    
    "С другого конца комнаты донёсся лёгкий шорох. Сёстры обернулись."

    show tania shy:
        zoom 1.3
        pos (600, 130)

    "Перед ними уже стояла слегка сонная, но как всегда изящная и элегантная Татьяна."
    "Её причёска ничуть не растрепалась, пижама не помялась, а кожа в утреннем свете выглядела превосходно."

    show tania sleepy:
        zoom 1.3
        pos (600, 130)

    t "Доброе утро, сёстры."

    show tania shy:
        zoom 1.3
        pos (600, 130)

    "Эту фразу Татьяна произнесла сдержанно и изящно. Как только Таня и могла."

    show tania sleepy:
        zoom 1.3
        pos (600, 130)

    t "О чём шепчетесь?"

    hide tania sleepy

    show olga shy:
        zoom 1.5
        pos (220, 150)
    show anastasia shy:
        zoom 1.2
        pos (960, 200)

    "Оля и Настя переглянулись."

    if nastya_dream_answer == "tobolsk":

        show olga sleepy:
            zoom 1.5
            pos (220, 150)

        o "Да вот Настенька рассказывала, что сегодня ей снился Тобольск."

        show olga shy:
            zoom 1.5
            pos (220, 150)

        "Настя подхватывает:"

        show anastasia sleepy:
            zoom 1.2
            pos (960, 200)

        a "И не абы какой, а зимний! Представляешь, Таня, какая странность..."

        show anastasia shy:
            zoom 1.2
            pos (960, 200)

        hide olga shy
        hide anastasia shy

        show tania shy:
            zoom 1.3
            pos (600, 130)

        "Таня обводит глазами девочек и всё в том же сдержанном тоне продолжает:"

        show tania sleepy:
            zoom 1.3
            pos (930, 130)

        show anastasia shy 2:
            zoom 1.2
            pos (300, 200)
        with fade

        t "И правда странно... Главное, чтобы сон приятный и хороший был."

        show tania shy:
            zoom 1.3
            pos (930, 130)

        show anastasia sleepy 2:
            zoom 1.2
            pos (300, 200)

        a "А помнишь, Таня, как мы в Тобольске снеговика лепили? Прямо у крыльца..."

        show tania sleepy:
            zoom 1.3
            pos (930, 130)

        show anastasia shy 2:
            zoom 1.2
            pos (300, 200)

        t "Помню. Ты тогда в сугроб упала и хохотала так, что мама из окна выглянула."

        hide tania sleepy
        hide anastasia shy 2
        with fade

        "Сёстры улыбаются."
    
    elif nastya_dream_answer == "good_sleep":

        show olga sleepy:
            zoom 1.5
            pos (220, 150)

        show anastasia shy:
            zoom 1.2
            pos (960, 200)

        o "Настенька рассказывала о своём хорошем сне."

        show olga shy:
            zoom 1.5
            pos (220, 150)

        "Настя кивнула."

        hide olga shy
        hide anastasia shy
        show tania shy:
            zoom 1.3
            pos (600, 130)

        "Таня слегка улыбается и отвечает:"

        show tania sleepy:
            zoom 1.3
            pos (600, 130)

        t "Хорошие сны - большая редкость здесь... Храни о нём память."

        hide tania sleepy
        show olga shy:
            zoom 1.5
            pos (220, 150)

        show anastasia shy:
            zoom 1.2
            pos (960, 200)

        "Внутренний голос Анастасии" "Хорошие сны - редкость. Но может быть... может быть, это знак?"

        "Настя и Оля тоже слегка улыбнулись."

        hide anastasia shy
        hide olga shy
        with fade

    elif nastya_dream_answer == "bad_sleep":

        show olga shy:
            zoom 1.5
            pos (220, 150)

        show anastasia shy:
            zoom 1.2
            pos (960, 200)

        "Настя грустно смотрит в пол. Оля тоже поникает. Таня в недоумении смотрит на них."
        "Немного помолчав, Оля говорит:"

        show olga sleepy:
            zoom 1.5
            pos (220, 150)

        o "О снах говорили... сегодня... не самых приятных."

        hide olga sleepy
        hide anastasia shy
        with fade

        "Таня подходит и обнимает сестёр."

        show anastasia shy 2:
            zoom 1.2
            pos (500, 200)

        show olga shy:
            zoom 1.5
            pos (-100, 150)

        show tania sleepy:
            zoom 1.3
            pos (1200, 130)
        with fade

        t "Ничего, девочки, всё образуется... Нужно лишь немного потерпеть..."

        hide olga shy
        hide anastasia shy
        hide tania sleepy
        with fade

        "Внутренний голос Ольги" "Немного... Сколько этих «немного» мы уже прожили?"

    window hide
    pause

    show olga shy:
        zoom 1.5
        pos (220, 150)

    show anastasia sleepy:
        zoom 1.2
        pos (960, 200)
    with fade

    a "Который час?"

    show olga sleepy:
        zoom 1.5
        pos (220, 150)

    show anastasia shy:
        zoom 1.2
        pos (960, 200)

    o "Думаю, уже почти восемь... Что-то мы заболтались, девочки..."

    hide olga sleepy
    hide anastasia shy

    show olga shy:
        zoom 1.5
        pos (500, 150)
    with fade

    "Ольга оглядывает комнату, и её взгляд задерживается на всё ещё спящей Марии."

    show olga sleepy:
        zoom 1.5
        pos (500, 150)

    o "А наша Мари как всегда. Спит, как убитая. Пора её разбудить."

    show olga shy:
        zoom 1.5
        pos (500, 150)

    "Оля неспеша подходит к сестре и аккуратно касается её плеча."
    "Мари даже не пошевелилась. Спит, будто бы ничего и не произошло."
    "Оля трясёт её за плечо, после чего та наконец просыпается."

    show olga sleepy:
        zoom 1.5
        pos (500, 150)

    o "Доброе утро, засоня. Пора вставать."

    hide olga sleepy

    show maria shy:
        zoom 1.3
        pos (550, 200)

    "Мари нехотя поднимается с кровати и сладко зевает."

    show maria sleepy:
        zoom 1.3
        pos (550, 200)

    m "Доброе утро!"

    show maria shy:
        zoom 1.3
        pos (550, 200)

    "Радостно, чуть ли не крича, произносит Мария."

    show maria sleepy:
        zoom 1.3
        pos (550, 200)

    m "Я так хорошо спала! А какие сады мне снились! Вы бы видели!"

    show maria shy:
        zoom 1.3
        pos (550, 200)

    "Мари начинает размахивать руками и носиться по комнате, показывая всё, что только запомнила из своего сна."

    hide maria sleepy
    with fade

    show tania shy 2:
        zoom 1.3
        pos (900, 130)

    show anastasia shy 2:
        zoom 1.2
        pos (500, 200)

    show olga shy:
        zoom 1.5
        pos (-100, 150)

    "Анастасия громко хохочет, а Оля и Таня тихо умиляются этому в стороне."

    hide olga shy
    hide anastasia shy
    hide tania sleepy
    with fade

    show anastasia shy 2:
        zoom 1.2
        pos (600, 200)


    ia "Мари такая веселушка! И сны у неё забавные. И сама она по-доброму смешная..."

    "Анастасия смотрит на сестёр и чувствует тепло в груди."
    
    if inventory.count_found() >= 1:
        ia "Ну, теперь икона со мной. Сёстры рядом. Мама с папой за стеной. Оля права - пока мы вместе, нам ничего не страшно."
    else:
        ia "Мы выдержим это нелёгкое испытание. Таня права - осталось немного потерпеть. Ведь мы вместе. Мы - семья. А семье невзгоды не страшны."
    stop music fadeout 2.0
    
    # Переход к следующей сцене
    scene black with fade
    "Через некоторое время в дверь постучат - охрана зовёт умываться."
    
    jump scene_washing

label scene_washing:
    scene bg way with dissolve
    play sound "audio/going_hall.mp3"
    "Узкий коридор дома Ипатьева. Сестры идут к уборной в сопровождении красноармейца."
    show guard talk:
        zoom 1.4
        pos (550, 80)
    with fade

    g "Шевелитесь, барышни. Нечего тут прохлаждаться."

    hide guard talk

    if inventory.has_item(1):
        show anastasia shy 2:
            zoom 1.2
            pos (600, 200)

        ia "Грубит, как всегда. Но сегодня я почему-то не злюсь."

        hide anastasia shy 2
        with fade


    "Мария наклоняется к сестрам и говорит едва слышно."

    show guard talk:
        zoom 1.4
        pos (1600, 80)

    show maria sleepy:
        zoom 1.3
        pos (550, 200)

    m "Этот вчера у Тани спросил, не скучно ли нам без балов."

    hide maria sleepy

    show tania shy 2:
        zoom 1.3
        pos (550, 130)

    "Татьяна бледнеет, но отвечает шепотом."

    show tania sleepy 2:
        zoom 1.3
        pos (550, 130)

    t "Я сделала вид, что не слышу. Мама велела не отвечать на грубости."

    hide tania sleepy

    show olga sleepy:
        zoom 1.5
        pos (500, 150)

    o "Главное, чтобы Алексея не тревожили. У него ночью нога болела. Я слышала, он стонал."

    hide olga sleepy
    hide guard

    "Анастасия вспоминает, что вчера видела что-то странное."

    show guard:
        zoom 1.4
        pos (1600, 80)

    show anastasia sleepy 2:
        zoom 1.2
        pos (600, 200)

    a "Я слышала, Леню Седнева куда-то увели вчера."

    hide anastasia sleepy 2

    show maria sleepy:
        zoom 1.3
        pos (550, 200)

    m "Этот поваренок... Жаль, ведь они с Лешенькой дружили."

    hide maria sleepy

    show tania sleepy 2:
        zoom 1.3
        pos (550, 130)

    t "Да. Мама тоже тревожится, увидим ли мы вновь этого мальчика."

    hide tania shy 2
    hide guard

    if inventory.count_found() >= 1:
        window hide
        menu:
            "Поделиться находкой с сестрами":

                show guard:
                    zoom 1.4
                    pos (1600, 80)

                show anastasia sleepy 2:
                    zoom 1.2
                    pos (600, 200)

                a "Девочки... Я сегодня иконку нашла. На тумбочке лежала. Та, спасовая."

                hide anastasia sleepy 2

                show olga sleepy:
                    zoom 1.5
                    pos (500, 150)

                o "Тише, Настя! Охранник услышит."
                o "Спрячь получше. Это теперь наша святыня."

                hide olga sleepy

                show tania sleepy 2:
                    zoom 1.3
                    pos (550, 130)

                t "Мама говорила, что иконы нас хранят. Может, это знак?"

                hide tania sleepy 2

                show maria sleepy:
                    zoom 1.3
                    pos (550, 200)

                m "Конечно, знак! Бог с нами, девочки. Он не оставит."

                hide maria sleepy
                hide guard

            "Промолчать о находке":

                show anastasia shy 2:
                    zoom 1.2
                    pos (600, 200)

                ia "Слишком опасно — охрана может услышать. Расскажу вечером, когда останемся одни."
                hide anastasia shy 2


    # Подходим к уборной
    scene bg bath with dissolve

    show guard talk:
        zoom 1.4
        pos (550, 80)

    g "Заходите по одной. Остальные ждите здесь."

    hide guard talk

    play sound "audio/door_close.mp3"

    "Первой заходит Ольга. Сестры ждут в коридоре под присмотром охраны."


    window hide
    menu:
        "Переглянуться с Марией":

            show anastasia shy:
                zoom 1.2
                pos (960, 200)

            show maria shy:
                zoom 1.3
                pos (300, 200)

            "Анастасия ловит взгляд Марии. Та улыбается — той самой своей светлой улыбкой, которая всегда согревает."

            show anastasia shy:
                zoom 1.2
                pos (960, 200)

            show maria sleepy:
                zoom 1.3
                pos (300, 200)

            m "Помнишь, как в Царском мы бегали к пруду купаться? А мама потом ругалась, что мы мокрые?"

            show anastasia sleepy:
                zoom 1.2
                pos (960, 200)

            show maria shy:
                zoom 1.3
                pos (300, 200)

            a "Помню. Ты тогда в платье в воду прыгнула, потому что жарко было."

            show anastasia shy:
                zoom 1.2
                pos (960, 200)

            show maria sleepy:
                zoom 1.3
                pos (300, 200)

            m "А Татьяна нас прикрывала, говорила, что мы просто облились."

            show anastasia shy:
                zoom 1.2
                pos (960, 200)

            show maria shy:
                zoom 1.3
                pos (300, 200)

            "Сестры тихо смеются, но тут же замолкают — охранник оборачивается."
            ia "Хорошо, что есть Мария. Она умеет напомнить, что мы просто девочки, а не узницы."

            hide anastasia shy
            hide maria shy

        "Посмотреть на охранника":

            show anastasia shy 2:
                zoom 1.2
                pos (200, 200)

            show guard:
                zoom 1.4
                pos (1100, 80)

            "Анастасия внимательно смотрит на красноармейца. Ей кажется, что сегодня он ведет себя иначе — более нервно, часто оглядывается, теребит винтовку."
            ia "Он будто ждет чего-то. Или боится. Интересно, о чем они думают, эти солдаты? Снятся ли им те, кого они стерегут?"

            hide guard

            show guard 2:
                zoom 1.4
                pos (1100, 80)

            "Охранник ловит взгляд Анастасии"

            show guard talk 2:
                zoom 1.4
                pos (1100, 80)

            g "Чего уставилась? Отвернись."

            show guard 2:
                zoom 1.4
                pos (1100, 80)

            show anastasia shy:
                zoom 1.2
                pos (200, 200)

            "Анастасия отводит глаза, но чувство тревоги не проходит."

            show guard:
                zoom 1.4
                pos (1100, 80)

            if inventory.has_item(1):
                "Анастасия машинально сжимает в кармане икону."
                ia "Господи, сохрани нас. Что бы ни случилось — сохрани."

            hide guard
            hide anastasia shy

    show olga sleepy:
        zoom 1.5
        pos (500, 150)
    with fade

    o "Я закончила. Таня, иди ты."

    hide olga sleepy

    play sound "audio/door_close.mp3"

    "Татьяна заходит в уборную. Ожидание продолжается."

    window hide
    menu:
        "Спросить Ольгу о самочувствии Алексея":

            show anastasia sleepy:
                zoom 1.2
                pos (960, 200)

            show olga shy:
                zoom 1.5
                pos (220, 150)

            a "Оля, ты говорила, у Алексея нога болела. Он сильно мучился?"

            show anastasia shy:
                zoom 1.2
                pos (960, 200)

            show olga sleepy:
                zoom 1.5
                pos (220, 150)

            o "Я слышала, как он плакал ночью. Тихо так, в подушку. Чтобы мама не слышала."

            show anastasia sleepy:
                zoom 1.2
                pos (960, 200)

            show olga shy:
                zoom 1.5
                pos (220, 150)

            a "Бедный Лешка. Он же совсем мальчик еще, а терпит как взрослый."

            show anastasia shy:
                zoom 1.2
                pos (960, 200)

            show olga sleepy:
                zoom 1.5
                pos (220, 150)

            o "Папа говорит, казаки так терпят. А Леша хочет быть казаком."

            show olga shy:
                zoom 1.5
                pos (220, 150)

            "Ольга грустно улыбается."

            hide olga shy
            hide anastasia shy

        "Спросить Ольгу, что думает о словах охранника про балы":

            show anastasia sleepy:
                zoom 1.2
                pos (960, 200)

            show olga shy:
                zoom 1.5
                pos (220, 150)

            a "Оля, а тот охранник... про балы спросил. Это же издевательство, да?"

            show anastasia shy:
                zoom 1.2
                pos (960, 200)

            show olga sleepy:
                zoom 1.5
                pos (220, 150)

            o "Конечно. Но мы не должны показывать, что нам больно. Мама права — молчание лучшее оружие."
            o "Пусть думают, что мы не понимаем, не чувствуем. Мы-то знаем правду."
            hide olga sleepy
            hide anastasia shy

        "Просто стоять молча":

            show anastasia shy 2:
                zoom 1.2
                pos (600, 200)

            "Анастасия молчит, думая о своем. Сестры рядом, но каждая погружена в свои мысли."
            ia "Сколько еще это будет продолжаться? Месяц? Год? Всегда?"

            hide anastasia shy 2

    show tania shy:
        zoom 1.3
        pos (550, 130)
    with fade

    "Мария заходит в уборную. Татьяна присоединяется к сестрам."
    play sound "audio/door_close.mp3"

    hide tania shy

    show anastasia shy 2:
        zoom 1.2
        pos (500, 200)

    show olga shy:
        zoom 1.5
        pos (-100, 150)

    show tania sleepy:
        zoom 1.3
        pos (1200, 130)
    with fade

    t "Вода ледяная. Но я быстро."

    show olga sleepy:
        zoom 1.5
        pos (-100, 150)

    show tania shy:
        zoom 1.3
        pos (1200, 130)

    o "Таня, ты бледная. Не заболела?"

    show olga shy:
        zoom 1.5
        pos (-100, 150)

    show tania sleepy:
        zoom 1.3
        pos (1200, 130)

    t "Нет. Просто не выспалась. Думала о Лене Седневе всю ночь."

    show anastasia sleepy 2:
        zoom 1.2
        pos (500, 200)

    show tania shy:
        zoom 1.3
        pos (1200, 130)

    a "Таня, не переживай. Может, его правда к дяде отпустили?"

    show anastasia shy 2:
        zoom 1.2
        pos (500, 200)

    show tania sleepy:
        zoom 1.3
        pos (1200, 130)

    t "А если нет, Настя? Если с ним что-то случилось? Он же совсем ребенок."

    show olga sleepy:
        zoom 1.5
        pos (-100, 150)

    show tania shy:
        zoom 1.3
        pos (1200, 130)

    o "Татьяна, не накручивай себя. Мама сказала — будем надеяться на лучшее."

    show olga shy:
        zoom 1.5
        pos (-100, 150)

    show tania sleepy:
        zoom 1.3
        pos (1200, 130)

    t "Легко сказать... Я помню его глаза, когда его уводили. Он будто знал что-то."

    show tania shy:
        zoom 1.3
        pos (1200, 130)

    hide olga shy
    hide tania shy
    hide anastasia shy 2
    with fade

    show maria sleepy:
        zoom 1.3
        pos (550, 200)

    play sound "audio/door_close.mp3"

    m "Фух, вода холоднющая! Я аж подпрыгнула."

    hide maria sleepy

    show guard talk:
        zoom 1.4
        pos (550, 80)

    g "Все вышли? Тогда назад. Живо."

    hide guard talk

    "Сестры возвращаются по коридору."

    play sound "audio/going_hall.mp3"


    # Переход к завтраку
    scene black with fade

    jump breakfast


label breakfast:
    scene bg dinner with fade
    play music "audio/dinner.mp3" loop volume 0.15 fadein 1.0

    "Семья собирается в столовой. Алексей сидит бледный, нога опухла."

    show nick:
        zoom 1.1
        pos (200, 80)

    show alex:
        zoom 1.1
        pos (900, 180)

    show sasha:
        zoom 1.3
        pos (1200, 100)
    with fade

    show nick talk:
        zoom 1.1
        pos (200, 80)

    stop music fadeout 2.0

    n "Как нога, мой мальчик?"

    show nick:
        zoom 1.1
        pos (200, 80)

    show alex talk:
        zoom 1.1
        pos (900, 180)

    ax "Терпимо, Папа. Только если резко повернуться - больно."

    show alex:
        zoom 1.1
        pos (900, 180)

    show sasha talk:
        zoom 1.3
        pos (1200, 100)

    al "Я просила доктора Боткина посмотреть. Он придет после завтрака."

    show sasha:
        zoom 1.3
        pos (1200, 100)

    hide sasha
    hide alex
    hide nick

    play sound "audio/door_close.mp3"

    show botkin talk:
        zoom 1.1
        pos (600, 100)
    with fade

    b "Уже пришел, Ваше Величество."

    show botkin:
        zoom 1.1
        pos (600, 100)

    "Доктор Боткин подходит к Алексею."

    show botkin talk:
        zoom 1.1
        pos (400, 100)

    show alex:
        zoom 1.1
        pos (900, 180)

    b "Позволите?"

    show botkin:
        zoom 1.1
        pos (400, 100)

    show alex talk:
        zoom 1.1
        pos (900, 180)

    ax "Да, доктор."

    hide alex
    hide botkin

    # Вызов мини-игры
    call minigame_help_doctor from _call_minigame_help_doctor

    # После мини-игры

    jump activities


label minigame_help_doctor:

    scene bg game with fade

    "Анастасия помогает доктору Боткину перевязать ногу Алексея."

    b "Княжна, сегодня я хочу научить вас правильной медицинской процедуре."
    b "Запоминайте внимательно. Я скажу только один раз."

    b "Первое: осмотреть ногу и спросить пациента о самочувствии."
    b "Второе: подготовить воду и проверить её температуру — не горячая ли, не холодная ли."
    b "Третье: смочить ткань в подготовленной воде."
    b "Четвёртое: приложить влажный компресс к опухоли."
    b "Пятое: подождать 30 секунд, чтобы компресс подействовал."
    b "Шестое: нанести мазь поверх компресса."
    b "Седьмое: забинтовать ногу — не туго, но и не слабо."
    b "Восьмое: подложить подушку под ногу для оттока крови."
    b "Девятое: укрыть ногу одеялом — пациенту должно быть тепло."
    b "И десятое: сказать Алексею ободряющие слова. Это не менее важно, чем лекарства."

    b "Всё запомнили? Тогда приступайте. Я буду наблюдать."


    $ correct_sequence = [
        "осмотр",
        "вода",
        "ткань",
        "компресс",
        "пауза",
        "мазь",
        "бинты",
        "подушка",
        "одеяло",
        "слова"
    ]

    $ step_names = {
        "осмотр": "осмотреть ногу и спросить о боли",
        "вода": "подготовить воду и проверить температуру",
        "ткань": "смочить ткань",
        "компресс": "приложить компресс",
        "пауза": "подождать 30 секунд",
        "мазь": "нанести мазь",
        "бинты": "забинтовать ногу",
        "подушка": "подложить подушку",
        "одеяло": "укрыть одеялом",
        "слова": "сказать ободряющие слова"
    }

    $ player_sequence = []
    $ mistakes = 0
    $ max_mistakes = 3
    $ hint_used = False


    while len(player_sequence) < len(correct_sequence) and mistakes < max_mistakes:

        $ next_step = correct_sequence[len(player_sequence)]
        $ step_num = len(player_sequence) + 1

        if step_num <= 4:
            $ menu_items = [
                ("Осмотреть ногу", "осмотр"),
                ("Подготовить воду", "вода"),
                ("Смочить ткань", "ткань"),
                ("Приложить компресс", "компресс"),
                ("Нанести мазь", "мазь_ошибка"),
                ("Забинтовать", "бинты_ошибка"),
                ("Подложить подушку", "подушка_ошибка")
            ]
            if not hint_used:
                $ menu_items.append(("Попросить подсказку", "подсказка"))

            $ renpy.random.shuffle(menu_items)

            $ choice = renpy.display_menu(
                [(item[0], item[1]) for item in menu_items],
                screen="choice",
                title="Этап подготовки (шаг [step_num]/10):"
            )

            if choice == "осмотр" and next_step == "осмотр" and "осмотр" not in player_sequence:
                $ player_sequence.append("осмотр")
                "Анастасия осматривает ногу Алексея."
                ax "Щиколотка болит, но терпимо."
                "Боткин одобрительно кивает."

            elif choice == "вода" and next_step == "вода" and "вода" not in player_sequence:
                $ player_sequence.append("вода")
                "Анастасия приносит воду и пробует пальцем."
                a "Тёплая, в самый раз."
                b "Хорошо."

            elif choice == "ткань" and next_step == "ткань" and "ткань" not in player_sequence:
                $ player_sequence.append("ткань")
                "Анастасия смачивает чистую ткань в подготовленной воде."

            elif choice == "компресс" and next_step == "компресс" and "компресс" not in player_sequence:
                $ player_sequence.append("компресс")
                "Анастасия аккуратно прикладывает влажную ткань к опухоли."
                ax "Прохладно... но приятно."

            elif choice == "подсказка":
                $ hint_used = True
                "Анастасия" "Доктор, я забыла... Что сейчас?"
                b "Сейчас этап подготовки. Нужно [step_names[next_step]]."

            else:
                $ mistakes += 1
                if choice == "мазь_ошибка":
                    b "Рано! Сначала подготовка. Нужно осмотреть ногу и подготовить компресс."
                elif choice == "бинты_ошибка":
                    b "Рано! Компресс ещё не подействовал. Сначала нужно всё подготовить."
                elif choice == "подушка_ошибка":
                    b "Подушка в самом конце, после всех процедур."
                else:
                    b "Не сейчас. Нужно следовать порядку."

        elif step_num <= 7:
            $ menu_items = [
                ("Подождать", "пауза"),
                ("Нанести мазь", "мазь"),
                ("Забинтовать", "бинты"),
                ("Подложить подушку", "подушка_ошибка"),
                ("Укрыть одеялом", "одеяло_ошибка"),
                ("Сказать слова", "слова_ошибка")
            ]
            if not hint_used:
                $ menu_items.append(("Попросить подсказку", "подсказка"))

            $ renpy.random.shuffle(menu_items)

            $ choice = renpy.display_menu(
                [(item[0], item[1]) for item in menu_items],
                screen="choice",
                title="Этап лечения (шаг [step_num]/10):"
            )

            if choice == "пауза" and next_step == "пауза" and "пауза" not in player_sequence:
                $ player_sequence.append("пауза")
                "Анастасия ждёт, считая про себя."
                $ renpy.pause(2.0)
                b "Терпение — важная часть лечения."

            elif choice == "мазь" and next_step == "мазь" and "мазь" not in player_sequence:
                $ player_sequence.append("мазь")
                "Анастасия берёт мазь и аккуратно наносит поверх компресса."

            elif choice == "бинты" and next_step == "бинты" and "бинты" not in player_sequence:
                $ player_sequence.append("бинты")
                "Анастасия осторожно бинтует ногу — не туго, но и не слабо."
                ax "Нормально, не давит."

            elif choice == "подсказка":
                $ hint_used = True
                "Анастасия" "Доктор, я забыла... Что сейчас?"
                b "Сейчас этап лечения. Нужно [step_names[next_step]]."

            else:
                $ mistakes += 1
                if choice == "подушка_ошибка":
                    b "Подушка позже, сначала зафиксируй повязку."
                elif choice == "одеяло_ошибка":
                    b "Рано укрывать. Сначала нужно закончить лечение."
                elif choice == "слова_ошибка":
                    b "Добрые слова — в самом конце, когда всё уже сделано."
                else:
                    b "Не сейчас. Нужно следовать порядку."

        else:
            $ menu_items = [
                ("Подложить подушку", "подушка"),
                ("Укрыть одеялом", "одеяло"),
                ("Сказать слова", "слова"),
                ("Осмотреть ногу", "осмотр_ошибка"),
                ("Подготовить воду", "вода_ошибка"),
                ("Нанести мазь", "мазь_ошибка")
            ]
            if not hint_used:
                $ menu_items.append(("Попросить подсказку", "подсказка"))

            $ renpy.random.shuffle(menu_items)

            $ choice = renpy.display_menu(
                [(item[0], item[1]) for item in menu_items],
                screen="choice",
                title="Этап завершения (шаг [step_num]/10):"
            )

            if choice == "подушка" and next_step == "подушка" and "подушка" not in player_sequence:
                $ player_sequence.append("подушка")
                "Анастасия подкладывает подушку под ногу Алексея."

            elif choice == "одеяло" and next_step == "одеяло" and "одеяло" not in player_sequence:
                $ player_sequence.append("одеяло")
                "Анастасия укрывает ногу Алексея одеялом."
                ax "Тепло... Спасибо, Настя."

            elif choice == "слова" and next_step == "слова" and "слова" not in player_sequence:
                $ player_sequence.append("слова")
                menu:
                    "Что сказать Алексею?"

                    "«Ты смелый, Лёшенька. Скоро поправишься.»":
                        a "Ты смелый, Лёшенька. Скоро поправишься."
                        ax "Правда?"
                        a "Правда. Мы же Романовы."
                        ax "Спасибо, Настя."

                    "«Казаки так не плачут, а ты молодец.»":
                        a "Казаки так не плачут, а ты молодец."
                        ax "Я стараюсь."

                    "«Хочешь, потом почитаю тебе?»":
                        a "Хочешь, потом почитаю тебе?"
                        ax "Про казаков?"
                        a "Про казаков."
                        ax "Хорошо..."

                "Алексей слабо улыбается."

            elif choice == "подсказка":
                $ hint_used = True
                a "Доктор, я забыла... Что сейчас?"
                b "Мы уже почти закончили. Осталось [step_names[next_step]]."

            else:
                $ mistakes += 1
                if choice == "осмотр_ошибка":
                    b "Осмотр был в самом начале. Сейчас уже завершение."
                elif choice == "вода_ошибка":
                    b "Вода уже не нужна. Мы на финальном этапе."
                elif choice == "мазь_ошибка":
                    b "Мазь уже нанесена. Сейчас только завершающие шаги."
                else:
                    b "Не сейчас. Нужно следовать порядку."


    if mistakes >= max_mistakes:
        b "Княжна, медицина требует точности. Давайте я закончу сам."
        "Боткин быстро и профессионально завершает процедуру."
        "Анастасия расстроена, но Алексей сжимает её руку."
        ax "Ничего, Настя. Ты старалась."

    else:
        b "Превосходно, княжна!"
        b "Из вас выйдет замечательная сестра милосердия."

        if mistakes == 0:
            b "И ни одной ошибки! Ваши родители могут гордиться."

        if hint_used:
            b "Вы не побоялись спросить — это тоже признак настоящего врача."
        else:
            b "Вы всё запомнили с первого раза. Редкий дар."

        ax "Настя... Спасибо. Правда легче стало."
        "Анастасия гладит брата по голове."
        a "Отдыхай, Лёшенька."

    jump activities


# СЦЕНА: УТРЕННИЕ ЗАНЯТИЯ
label activities:
    scene bg live morn with fade

    "После завтрака семья собирается в гостиной. Александра Фёдоровна чувствует себя лучше и сидит с детьми."

    show sasha:
        zoom 1.3
        pos (900, 100)

    show tania:
        zoom 1.2
        pos (200, 150)
    with fade

    "Татьяна, как всегда, помогает матери. В руках у неё небольшая книга в тёмном переплёте."

    show sasha talk:
        zoom 1.3
        pos (900, 100)

    al "Таня, почитай нам сегодня. У меня так болит голова, что трудно самой держать книгу."

    show sasha:
        zoom 1.3
        pos (900, 100)

    show tania talk:
        zoom 1.2
        pos (200, 150)

    t "Конечно, мама. Что бы вы хотели?"

    show sasha talk:
        zoom 1.3
        pos (900, 100)

    show tania:
        zoom 1.2
        pos (200, 150)

    al "То место, где о милосердии. Мы вчера остановились."

    show sasha:
        zoom 1.3
        pos (900, 100)

    show tania:
        zoom 1.2
        pos (200, 150)

    "Татьяна открывает книгу на закладке - выцветшей розовой ленточке."


    play sound "audio/book_turn.mp3"

    hide tania
    hide sasha
    with fade

    show anastasia:
        zoom 1.1
        pos (600, 250)

    menu:
        "Рассмотреть закладку":

            show tania:
                zoom 1.2
                pos (300, 150)

            show anastasia:
                zoom 1.1
                pos (900, 250)
            with fade

            "Анастасия замечает, что закладка необычная — на конце пришит маленький крестик из бисера."

            show tania:
                zoom 1.2
                pos (300, 150)

            show anastasia talk:
                zoom 1.1
                pos (900, 250)

            a "Таня, какая красивая закладка! Ты сама сделала?"

            show tania talk:
                zoom 1.2
                pos (300, 150)

            show anastasia:
                zoom 1.1
                pos (900, 250)

            t "Да, ещё в Царском Селе. Мама помогла."

            show tania:
                zoom 1.2
                pos (300, 150)

            show anastasia talk:
                zoom 1.1
                pos (900, 250)

            a "Можно посмотреть поближе?"

            show tania talk:
                zoom 1.2
                pos (300, 150)

            show anastasia:
                zoom 1.1
                pos (900, 250)

            t "Конечно, Настя."

            show tania:
                zoom 1.2
                pos (300, 150)

            show anastasia:
                zoom 1.1
                pos (900, 250)

            "Анастасия берёт закладку в руки. Шёлк выцвел, но работа видна - аккуратная, терпеливая."
            ia "Таня всегда была самой терпеливой из нас. Даже в мелочах."
            $ inventory.add_item(2)
            play sound "audio/notify.mp3"
            "Анастасия возвращает закладку на место, но запоминает её."

            hide anastasia talk
            hide tania
            with fade

        "Промолчать":

            show tania:
                zoom 1.2
                pos (300, 150)

            show anastasia:
                zoom 1.1
                pos (900, 250)
            with fade

            "Анастасия не хочет отвлекать сестру. Она просто слушает, как Татьяна читает Евангелие."
            "Голос сестры звучит мягко и спокойно. На душе становится чуть легче."
            ia "Хорошо, что есть Таня. Она всегда знает, что сказать."

            hide anastasia talk
            hide tania
            with fade

    if inventory.has_item(2):

        show anastasia:
            zoom 1.1
            pos (600, 250)

        ia "Таня так трепетно относится к этой книге. Интересно, что она там отмечала?"

        hide anastasia

    show tania talk:
        zoom 1.2
        pos (600, 150)

    t "Здесь... 'Будьте милосердны, как и Отец ваш милосерд. Не судите, и не будете судимы; не осуждайте, и не будете осуждены; прощайте, и прощены будете.'"

    hide tania talk
    with fade

    "Тишина в комнате. Даже Алексей, который обычно ёрзает, затихает на своей кровати."

    show nick:
        zoom 1.1
        pos (300, 80)

    show sasha talk:
        zoom 1.3
        pos (900, 100)

    al "Слышите, дети? 'Прощайте, и прощены будете'. Мы должны помнить об этом каждый день."

    show nick talk:
        zoom 1.1
        pos (300, 80)

    show sasha:
        zoom 1.3
        pos (900, 100)

    n "Даже когда нам трудно прощать?"

    show nick:
        zoom 1.1
        pos (300, 80)

    "Николай Александрович подходит к жене и садится рядом."

    show nick:
        zoom 1.1
        pos (300, 80)

    show sasha talk:
        zoom 1.3
        pos (900, 100)

    al "Особенно когда трудно, Ники. Тогда это hardest... как это по-русски... самое важное."

    show nick talk:
        zoom 1.1
        pos (300, 80)

    show sasha:
        zoom 1.3
        pos (900, 100)

    n "Ты всегда была мудрее меня в этих вопросах, Сана."

    show nick:
        zoom 1.1
        pos (300, 80)

    show sasha talk:
        zoom 1.3
        pos (900, 100)

    al "Я просто научилась видеть Бога во всём, что происходит. Даже здесь, в этом доме."

    hide sasha
    hide nick
    with fade

    show tania:
        zoom 1.2
        pos (600, 150)

    "Татьяна продолжает читать, её голос звучит мягко и успокаивающе."

    show tania talk:
        zoom 1.2
        pos (600, 150)

    t "'Давайте, и дастся вам: мерою доброю, утрясенною, нагнетенною и переполненною отсыплют вам в лоно ваше...'"

    hide tania talk
    with fade

    show anastasia:
        zoom 1.1
        pos (900, 250)

    show maria:
        zoom 1.2
        pos (300, 240)

    "Анастасия, сидящая рядом, шепчет Марии."

    show anastasia talk:
        zoom 1.1
        pos (900, 250)

    a "Я ничего не понимаю, но так красиво звучит..."

    show anastasia:
        zoom 1.1
        pos (900, 250)

    show maria talk:
        zoom 1.2
        pos (300, 240)

    m "Тише, Настя. Это же Евангелие."

    hide anastasia
    hide maria
    with fade

    show sasha:
        zoom 1.3
        pos (600, 100)

    "Александра Фёдоровна ласково смотрит на дочерей."

    show sasha talk:
        zoom 1.3
        pos (600, 100)

    al "Татьяна, остановись здесь. Дай детям подумать."

    hide sasha

    show tania talk:
        zoom 1.2
        pos (600, 150)

    t "Мама, а Вы правда верите, что нас отсюда выпустят?"

    hide tania

    "Вопрос повисает в воздухе. Все замирают."

    show nick:
        zoom 1.1
        pos (200, 80)

    show alex:
        zoom 1.1
        pos (900, 180)

    show sasha talk:
        zoom 1.3
        pos (1200, 100)

    al "Я верю, что всё, что происходит — Промысл Божий. Мы должны быть благодарны за каждый день вместе."

    show nick talk:
        zoom 1.1
        pos (200, 80)

    show sasha:
        zoom 1.3
        pos (1200, 100)

    n "Сана права. Мы живы, мы все здесь, мы вместе. Это уже много."

    show nick:
        zoom 1.1
        pos (200, 80)

    show alex talk:
        zoom 1.1
        pos (900, 180)

    ax "Но папа, я хочу домой... В Царское..."

    show alex:
        zoom 1.1
        pos (900, 180)

    "Голос Алексея дрожит. Александра подходит к сыну, гладит по голове."

    show sasha talk:
        zoom 1.3
        pos (1200, 100)

    al "Лешенька, наш дом там, где мы все. И там, где Бог. А Бог везде с нами."

    show sasha:
        zoom 1.3
        pos (1200, 100)

    "Алексей утыкается в плечо матери, и та тихо шепчет ему что-то на ухо."

    hide sasha
    hide alex
    hide nick
    with fade

    if inventory.has_item(2):
        call secret_dialog_morning from _call_secret_dialog_morning

    show sasha:
        zoom 1.3
        pos (900, 100)

    show tania:
        zoom 1.2
        pos (200, 150)


    "Татьяна закрывает книгу, но не убирает её — держит в руках, поглаживая обложку."

    show tania talk:
        zoom 1.2
        pos (200, 150)

    t "Мама, можно я сегодня сама выберу место для вечернего чтения?"

    show sasha talk:
        zoom 1.3
        pos (900, 100)

    show tania:
        zoom 1.2
        pos (200, 150)

    al "Конечно, моя хорошая. Ты уже достаточно взрослая, чтобы выбирать."

    show sasha:
        zoom 1.3
        pos (900, 100)

    "Татьяна улыбается, но в её глазах стоит грусть."

    hide sasha
    hide tania

    show olga talk:
        zoom 1.2
        pos (550, 170)
    with fade

    o "А можно мы с Настей пойдём на кухню? Харитонов обещал показать, как хлеб печь."

    hide olga talk

    show sasha talk:
        zoom 1.3
        pos (600, 100)

    al "Идите, девочки. Только не мешайте Ивану Михайловичу."

    hide sasha talk

    show anastasia talk:
        zoom 1.1
        pos (900, 250)

    show maria:
        zoom 1.2
        pos (300, 240)

    a "Ура! Мария, пойдёшь с нами?"

    show anastasia:
        zoom 1.1
        pos (900, 250)

    show maria talk:
        zoom 1.2
        pos (300, 240)

    m "Конечно! Я тоже хочу научиться."

    hide anastasia talk
    hide maria talk

    "Сёстры убегают, оставляя Татьяну с родителями."

    show nick talk:
        zoom 1.1
        pos (300, 80)

    show sasha:
        zoom 1.3
        pos (900, 100)
    with fade

    n "Таня, ты сегодня какая-то задумчивая. Всё хорошо?"

    hide nick talk
    hide sasha

    show tania talk 2:
        zoom 1.2
        pos (600, 150)

    t "Папа... Я просто думаю о том, что мама сказала. О благодарности."

    t "Я благодарна. Правда. За каждый день, за вас, за сестёр, за Алексея..."

    t "Но иногда мне так страшно, что я не могу дышать. Особенно ночью."

    hide tania talk 2

    show nick:
        zoom 1.1
        pos (300, 80)

    show sasha:
        zoom 1.3
        pos (900, 100)

    "Николай и Александра переглядываются."

    show sasha talk:
        zoom 1.3
        pos (900, 100)

    al "Иди к нам, доченька."

    hide sasha talk
    hide nick
    with fade

    show nick:
        zoom 1.1
        pos (200, 80)

    show tania 2:
        zoom 1.2
        pos (800, 150)

    show sasha:
        zoom 1.3
        pos (1200, 100)

    "Татьяна подходит, и родители обнимают её вдвоём."

    show nick talk:
        zoom 1.1
        pos (200, 80)

    n "Знаешь, Таня, даже императоры боятся. Даже мы. Это нормально."

    n "Но мы должны быть сильными. Не для себя — для Алексея, для младших. Ты понимаешь?"

    show nick:
        zoom 1.1
        pos (200, 80)

    show tania talk 2:
        zoom 1.2
        pos (800, 150)

    t "Понимаю, папа. Я стараюсь."

    show tania 2:
        zoom 1.2
        pos (800, 150)

    show sasha talk:
        zoom 1.3
        pos (1200, 100)

    al "Мы знаем. И мы гордимся тобой."

    show sasha:
        zoom 1.3
        pos (1200, 100)

    "Татьяна вытирает глаза и пытается улыбнуться."

    show tania talk 2:
        zoom 1.2
        pos (800, 150)

    t "Я пойду, проверю, как там девочки. А то Настя опять муку везде рассыплет."

    hide tania 2 talk
    hide sasha
    hide nick
    with fade

    show nick:
        zoom 1.1
        pos (300, 80)

    show sasha:
        zoom 1.3
        pos (900, 100)

    play sound "audio/door_close.mp3"

    "Родители смеются, и Татьяна выходит."

    "Александра смотрит вслед дочери, и её лицо омрачается."

    show sasha talk:
        zoom 1.3
        pos (900, 100)

    al "Ники... Они такие молодые. Им бы жить, танцевать, влюбляться..."

    show nick talk:
        zoom 1.1
        pos (300, 80)

    show sasha:
        zoom 1.3
        pos (900, 100)

    n "Я знаю, Сана. Знаю."

    show nick:
        zoom 1.1
        pos (300, 80)

    show sasha talk:
        zoom 1.3
        pos (900, 100)

    al "За что они страдают? Чем они заслужили?"

    show nick talk:
        zoom 1.1
        pos (300, 80)

    show sasha:
        zoom 1.3
        pos (900, 100)

    n "Не мы выбираем свой крест. Мы можем только нести его с достоинством."

    show nick:
        zoom 1.1
        pos (300, 80)

    show sasha talk:
        zoom 1.3
        pos (900, 100)

    al "Наши дети несут его лучше нас."

    show nick:
        zoom 1.1
        pos (300, 80)

    show sasha:
        zoom 1.3
        pos (900, 100)

    "Николай обнимает жену. Несколько минут они стоят молча, глядя в забеленное окно."

    hide sasha
    hide nick

    scene black with fade
    "Через час в доме запахнет свежим хлебом. На кухне будет слышен смех сестёр и ворчание повара Харитонова, который делает вид, что сердится, но на самом деле рад."

    jump baking_scene


label secret_dialog_morning:

    play sound "audio/book_turn.mp3"

    show sasha:
        zoom 1.3
        pos (900, 100)

    show tania:
        zoom 1.2
        pos (200, 150)

    "Татьяна перелистывает страницы и на мгновение замирает."

    show sasha:
        zoom 1.3
        pos (900, 100)

    show tania talk:
        zoom 1.2
        pos (200, 150)

    t "Мама... Здесь, где я отметила. Можно прочитать?"

    show sasha talk:
        zoom 1.3
        pos (900, 100)

    show tania:
        zoom 1.2
        pos (200, 150)

    al "Прочитай, Таня."

    show sasha:
        zoom 1.3
        pos (900, 100)

    show tania talk:
        zoom 1.2
        pos (200, 150)

    t "'Блаженны изгнанные за правду, ибо их есть Царство Небесное. Блаженны вы, когда будут поносить вас и гнать и всячески неправедно злословить за Меня.'"

    show sasha:
        zoom 1.3
        pos (900, 100)

    show tania:
        zoom 1.2
        pos (200, 150)

    "Тишина. Даже Анастасия, обычно непоседливая, застывает."

    show sasha:
        zoom 1.3
        pos (900, 100)

    show tania talk:
        zoom 1.2
        pos (200, 150)

    t "Мама... Это же про нас, да? 'Изгнанные за правду'..."

    show sasha talk:
        zoom 1.3
        pos (900, 100)

    show tania:
        zoom 1.2
        pos (200, 150)

    al "Подойди ко мне, девочка моя."

    show sasha:
        zoom 1.3
        pos (900, 100)

    show tania:
        zoom 1.2
        pos (200, 150)

    "Татьяна подходит, и Александра Фёдоровна обнимает её, прижимая к себе."

    show sasha talk:
        zoom 1.3
        pos (900, 100)

    show tania:
        zoom 1.2
        pos (200, 150)

    al "Про нас, моя родная. Про нас."

    al "Знаешь, Таня, я много думала об этих словах. 'Блаженны' — значит счастливы. Счастливы изгнанные."

    show sasha:
        zoom 1.3
        pos (900, 100)

    show tania talk:
        zoom 1.2
        pos (200, 150)

    t "Как мы можем быть счастливы здесь, мама?"

    show sasha talk:
        zoom 1.3
        pos (900, 100)

    show tania:
        zoom 1.2
        pos (200, 150)

    al "Потому что нас изгнали за то, что мы не предали. Не предали веру, не предали друг друга, не предали Россию."

    al "Нас лишили дворцов, но не лишили любви. Нас лишили власти, но не лишили достоинства."

    show sasha:
        zoom 1.3
        pos (900, 100)

    show tania talk:
        zoom 1.2
        pos (200, 150)

    t "А Бог... Он видит?"

    show sasha talk:
        zoom 1.3
        pos (900, 100)

    show tania:
        zoom 1.2
        pos (200, 150)

    al "Он видит всё, Таня. И он с нами. Особенно сейчас."

    show sasha:
        zoom 1.3
        pos (900, 100)

    show tania:
        zoom 1.2
        pos (200, 150)

    "Александра целует дочь в лоб."

    show sasha talk:
        zoom 1.3
        pos (900, 100)

    show tania:
        zoom 1.2
        pos (200, 150)

    al "Сохрани эту веру. Она нужнее, чем хлеб. Нужнее, чем вода."

    show sasha:
        zoom 1.3
        pos (900, 100)

    show tania talk:
        zoom 1.2
        pos (200, 150)

    t "Я постараюсь, мама."

    show sasha talk:
        zoom 1.3
        pos (900, 100)

    show tania:
        zoom 1.2
        pos (200, 150)

    al "Я знаю. Ты моя сильная девочка."

    show sasha:
        zoom 1.3
        pos (900, 100)

    show tania:
        zoom 1.2
        pos (200, 150)

    "Они сидят обнявшись, пока остальные тихо занимаются своими делами."

    hide tania
    hide sasha


# ПЕРЕМЕННЫЕ ДЛЯ МИНИ-ИГРЫ
default bread_type = "karavay"
default bake_time = 60
default baking_success = False
default bread_quality = "mediocre"
default correct_order = []
default current_step = 0
default wrong_step = ""
default random_event = None
default extra_time = 0


# СЦЕНА: ВЫПЕЧКА ХЛЕБА (полная)
label baking_scene:
    scene bg kitchen with fade
    show har:
        zoom 1.1
        pos (650, 150)

    "Харитонов хлопочет у печи."

    play sound "audio/door_close.mp3"

    transform anastasia_custom:
        zoom 1.1
        ypos 250
        on show:
            xpos 1500
            easein 0.5 xpos 1200

    transform maria_custom:
        zoom 1.2
        ypos 250
        on show:
            xpos -200
            easein 0.5 xpos 0

    show anastasia at anastasia_custom
    show maria talk at maria_custom


    m "Харитонов, позвольте! Мы сами хотим к обеду хлеб испечь."

    show maria:
        zoom 1.2
        pos (0, 250)

    show anastasia talk:
        zoom 1.1
        pos (1200, 250)

    a "Сами-сами! Мы умеем. Немножко."

    show anastasia:
        zoom 1.1
        pos (1200, 250)

    show har talk:
        zoom 1.1
        pos (650, 150)

    h "Ишь чего удумали, барышни. Не гоже княжеским дочкам в муке руки по локоть обваливать. Скажут потом - Харитонов не доглядел."

    hide har talk
    hide anastasia talk
    hide maria
    with fade

    show tania talk:
        zoom 1.2
        pos (600, 150)

    t "Харитонов, ну право слово. Позвольте девчонкам. Одну-единственную буханку. А вы сами пока хоть полчаса отдохнёте."

    hide tania talk
    with fade

    show har talk:
        zoom 1.1
        pos (650, 150)

    show maria:
        zoom 1.2
        pos (0, 250)

    show anastasia:
        zoom 1.1
        pos (1200, 250)

    h "Татьяна Николаевна! Да с ними хлопот — в два раза больше. Не видать мне с ними никакого отдыху. Они ж не стряпать — они воевать пришли."

    show har:
        zoom 1.1
        pos (650, 150)

    show maria talk:
        zoom 1.2
        pos (0, 250)

    m "Дя-а-а-денька..."

    show maria:
        zoom 1.2
        pos (0, 250)

    show anastasia talk:
        zoom 1.1
        pos (1200, 250)

    a "Ну пожа-а-а-алуйста..."

    show anastasia:
        zoom 1.1
        pos (1200, 250)

    show har talk:
        zoom 1.1
        pos (650, 150)

    h "Ла-а-адно. Уговорили, сорванцы. Вон подите в кладовой фартуки возьмите. Да такие, чтоб не жалко. И руки потом мыть — до локтей."

    hide maria
    hide anastasia
    hide har talk
    with fade

    "Девочки с визгом убегают."

    scene bg kitchen with fade

    show tania 2:
        zoom 1.2
        pos (1200, 150)

    "Татьяна ждёт у двери."

    show anastasia 2:
        zoom 1.1
        pos (600, 250)

    show maria:
        zoom 1.2
        pos (100, 250)
    with fade

    play sound "audio/door_close.mp3"
    "Анастасия и Мария возвращаются, перепоясанные в огромные фартуки."

    show tania talk 2:
        zoom 1.2
        pos (1200, 150)

    t "Давайте, я помогу."

    show tania 2:
        zoom 1.2
        pos (1200, 150)

    "Татьяна молча завязывает каждой хвост, поправляет воротник Марии, целует ту в макушку и уходит."

    hide tania 2
    with fade

    show har talk 2:
        zoom 1.1
        pos (1200, 150)

    h "Ну, боярышни-поварихи, что печь будем? По-французски — багет, чтоб хрустел, али по-нашему — каравай, чтоб душу грел?"

    hide har talk 2
    hide anastasia 2
    hide maria

    menu:
        "Багет":
            $ bread_type = "baguette"

            show har talk:
                zoom 1.1
                pos (650, 150)

            h "Ох и выдумщицы! Царскую кровь в вас, барышни, даже самой суровой мукой не перебить. Франция, стало быть, в атаку. Ну, смотрите."
        "Каравай":
            $ bread_type = "karavay"

            show har talk:
                zoom 1.1
                pos (650, 150)

            h "То-то же. Мягкий русский каравай любого француза с его багетом уделает. Записывайте рецепт на носы."

    h "Значит так. Стол мукой присыпаем. Горстку муки - горкой. В горке - ямочку."
    h "В ямочку - яйца. Потом - соль. Потом - водичкой разбавляем. Неспешно."

    hide har talk

    call baking_minigame

    if baking_success:
        h "Молодцы! Все ингредиенты в нужном порядке, и даже с помехами справились."
    else:
        if wrong_step == "таймаут":
            h "Эх, не уложились вы во время... Но ничего, я помогу."
        else:
            h "Ошиблись, барышни. Давайте я поправлю."

    h "А теперь: это всё руками перемешиваем! До комочка, до тягучего, чтоб от пальцев не отлипал. На железку - и в печь."

    menu:
        "Сколько печь хлеб?"
        "30 минут":
            $ bake_time = 30
        "1 час":
            $ bake_time = 60
        "1.5 часа":
            $ bake_time = 90

    if bread_type == "karavay":
        scene bg oven_karavay with fade
    else:
        scene bg oven_baguette with fade

    if baking_success:
        if bake_time == 60:
            $ bread_quality = "perfect"
            h "Красота-а-а! Ну, девчонки, ну молодцы! Обрадовали дядьку. Маменька с папенькой поди, небось горды за вас. Такой хлеб и к царскому столу — не стыдно."
        elif bake_time == 30:
            $ bread_quality = "raw"
            h "Эх... недопёкся мякиш. Сыроват. Но мы не гордые. Скажем - «ржаному хлебу учёного не надо»."
        else:
            $ bread_quality = "burnt"
            h "Э-э-эх... Ох, подгорел наш хлеб-то. Ну, что уж есть - того не воротишь. Сударыне подадим, какой вышел. Помощью слёзы лить — себя не уважать. Он и пригорелый собой хорош. А с сегодняшним супом — самое то."
    else:
        if bake_time == 60:
            $ bread_quality = "mediocre"
            h "Ну, вышло не ахти, но съедобно. В следующий раз получится лучше."
        elif bake_time == 30:
            $ bread_quality = "raw"
            h "Недопёклось ещё. Ничего, в другой раз."
        else:
            $ bread_quality = "burnt"
            h "Подгорело. Но мы не горюем."

    "Харитонов гладит Марию по голове заскорузлой ладонью, Настю толкает плечом. Девочки смеются."

    if bread_quality == "perfect":
        if not inventory.has_item(6):
            $ inventory.add_item(6)
            play sound "audio/notify.mp3"
            "Вы нашли маленький образок, спрятанный за иконой на кухне."

    jump lunch_scene



label baking_minigame:
    scene bg kitchen table with fade

    $ ingredients_list = ["Мука", "Яйца", "Соль", "Вода"]
    $ renpy.random.shuffle(ingredients_list)
    $ correct_order = ingredients_list
    $ current_step = 0
    $ baking_success = False
    $ wrong_step = ""
    $ extra_time = 0

    $ random_event = renpy.random.choice(["none", "flour_spill", "egg_fall", "salt_spill", "water_splash"])
    
    if random_event != "none":
        h "Смотрите, девочки, осторожнее. У меня сегодня рука не твёрдая - может, чего упадёт."
    
    if random_event == "flour_spill":
        call event_flour_spill
    elif random_event == "egg_fall":
        call event_egg_fall
    elif random_event == "salt_spill":
        call event_salt_spill
    elif random_event == "water_splash":
        call event_water_splash

    call screen baking_ingredients_fast
    
    if current_step >= len(correct_order):
        $ baking_success = True
    else:
        $ baking_success = False

    return


screen baking_ingredients_fast():
    modal True
    zorder 100
    
    default remaining = max(5, 10 + extra_time)  
    

    timer 1.0 repeat True action If(remaining > 0, SetScreenVariable("remaining", remaining - 1), [Function(baking_timeout_fast), Return()])
    
    imagebutton:
        idle Transform("images/flour.png", size=(500, 500))
        hover Transform("images/flour.png", size=(510, 510))
        action Function(baking_step_fast, "Мука")
        xpos 100
        ypos 200
    
    imagebutton:
        idle Transform("images/eggs.png", size=(200, 200))
        hover Transform("images/eggs.png", size=(210, 210))
        action Function(baking_step_fast, "Яйца")
        xpos 700
        ypos 300
    
    imagebutton:
        idle Transform("images/salt.png", size=(200, 200))
        hover Transform("images/salt.png", size=(210, 210))
        action Function(baking_step_fast, "Соль")
        xpos 1000
        ypos 200
    
    imagebutton:
        idle Transform("images/water.png", size=(450, 450))
        hover Transform("images/water.png", size=(460, 460))
        action Function(baking_step_fast, "Вода")
        xpos 1200
        ypos 500
    
    $ order_text = " > ".join(correct_order)
    text "Правильный порядок: [order_text]" size 40 color "#ffffff" xalign 0.5 ypos 50
    text "Осталось: [remaining] сек" size 40 color "#ffffff" xalign 0.5 ypos 100


init python:
    def baking_step_fast(ingredient):
        global current_step, correct_order, wrong_step
        if current_step < len(correct_order):
            if ingredient == correct_order[current_step]:
                current_step += 1
                renpy.notify(f"✓ {ingredient} добавлен(а)! Осталось: {len(correct_order) - current_step}")
                if current_step >= len(correct_order):
                    renpy.hide_screen("baking_ingredients_fast")
                    renpy.jump("baking_minigame_success")
            else:
                wrong_step = f"неправильный_{ingredient}"
                renpy.notify(f"✗ Ошибка! {ingredient} — не тот ингредиент. Нужен: {correct_order[current_step]}")
                renpy.hide_screen("baking_ingredients_fast")
                renpy.jump("baking_minigame_fail")
        else:
            renpy.hide_screen("baking_ingredients_fast")
            renpy.jump("baking_minigame_success")
    
    def baking_timeout_fast():
        global wrong_step
        wrong_step = "таймаут"
        renpy.hide_screen("baking_ingredients_fast")
        renpy.jump("baking_minigame_fail")



label baking_minigame_success:
    $ baking_success = True
    return

label baking_minigame_fail:
    $ baking_success = False
    return



label event_flour_spill:
    "Внезапно мешок с мукой опрокидывается, и мука рассыпается по столу!"
    menu:
        "Быстро собрать муку":
            $ extra_time = 2
            "Вы быстро сгребаете муку обратно."
            "+2 секунды к таймеру"
        "Продолжить, не обращая внимания":
            $ extra_time = -2
            h "Эх, нерадивые! Теперь тесто хуже будет."
            "-2 секунды"
    return

label event_egg_fall:
    "Яйцо выскальзывает из рук и падает на пол!"
    menu:
        "Взять новое яйцо":
            $ extra_time = 1
            "Вы хватаете другое яйцо. Харитонов одобрительно кивает." 
            "+1 секунда"
        "Попытаться поднять разбитое":
            $ extra_time = -3
            "Пока вы возитесь с осколками, время уходит."
            "-3 секунды"
    return

label event_salt_spill:
    "Солонка опрокидывается, и соль рассыпается!"
    menu:
        "Аккуратно собрать соль":
            $ extra_time = 0
            "Вы спасаете большую часть соли." 
            h "Ловко!"
        "Не обращать внимания":
            $ extra_time = -2
            h "Соли-то не хватит! Эх..."
            "-2 секунды"
    return

label event_water_splash:
    "Кувшин с водой качнулся, и вода плеснула на стол!"
    menu:
        "Быстро вытереть тряпкой":
            $ extra_time = 1
            "Вы вытираете стол"
            h "Молодцы!"
            "+1 секунда"
        "Растеряться":
            $ extra_time = -2
            "Вы теряете несколько секунд, не зная, что делать."
            "-2 секунды"
    return


label lunch_scene:
    scene bg dinner with fade

    play music "audio/dinner.mp3" loop volume 0.15 fadein 1.0

    show alex talk 2:
        zoom 1.1
        pos (300, 180)

    show sasha:
        zoom 1.3
        pos (900, 100)

    ax "Маменька, ну сколько можно? Сил уже нет! Кушать хочу."

    show alex 2:
        zoom 1.1
        pos (300, 180)

    show sasha talk:
        zoom 1.3
        pos (900, 100)

    al "Лёшенька, потерпи чуток. Настенька и Машенька старались - для всех нас. Хлеб сами пекли. Разве можно не дождаться?"

    hide alex 2
    hide sasha talk
    with fade

    stop music fadeout 2.0

    show anastasia talk 2:
        zoom 1.1
        pos (800, 250)

    show maria:
        zoom 1.2
        pos (200, 250)

    a "Внимание! Представляем вам чудо-хлеб от Анастасии и Марии!"

    show anastasia 2:
        zoom 1.1
        pos (800, 250)

    show maria talk:
        zoom 1.2
        pos (200, 250)

    m "С пылу, с жару."

    show anastasia 2:
        zoom 1.1
        pos (800, 250)

    show maria:
        zoom 1.2
        pos (200, 250)

    "Девочки смеются, садятся на места."

    hide maria
    hide anastasia 2
    with fade

    show olga talk:
        zoom 1.2
        pos (550, 170)

    o "Какие девчонки молодцы! Такой хлеб сами испекли."

    hide olga talk

    if bread_quality == "perfect":
        if bread_type == "karavay":
            show bread_perfect_round at truecenter with dissolve
        else:
            show bread_perfect_oval at truecenter with dissolve
        $ renpy.pause(2.0)
        hide bread_perfect_round
        hide bread_perfect_oval

        show nick:
            zoom 1.1
            pos (200, 80)

        show alex talk:
            zoom 1.1
            pos (800, 180)

        show sasha:
            zoom 1.3
            pos (1200, 100)

        ax "Маменька, папенька! Гляньте, какой румяный! А запах..! Можно мне первый ломтик?"

        show alex:
            zoom 1.1
            pos (800, 180)

        show sasha talk:
            zoom 1.3
            pos (1200, 100)

        al "И впрямь! Ну молодцы, ну поварята!"

        hide nick
        hide alex
        hide sasha talk

        show olga:
            zoom 1.2
            pos (900, 170)

        show tania talk:
            zoom 1.2
            pos (300, 150)

        t "Какая элегантная, изысканная булка."

        show olga talk:
            zoom 1.2
            pos (900, 170)

        show tania:
            zoom 1.2
            pos (300, 150)

        o "Молодцы, девочки."

        hide olga talk
        hide tania

        show nick talk:
            zoom 1.1
            pos (200, 80)

        show alex:
            zoom 1.1
            pos (800, 180)

        show sasha:
            zoom 1.3
            pos (1200, 100)

        n "Храбрые, сильные духом — да ещё и творческие. Горжусь вами, дети."

        hide alex
        hide nick talk
        hide sasha
        with fade

    elif bread_quality == "raw":
        if bread_type == "karavay":
            show bread_raw_round at truecenter with dissolve
        else:
            show bread_raw_oval at truecenter with dissolve
        $ renpy.pause(2.0)
        hide bread_raw_round
        hide bread_raw_oval

        show nick:
            zoom 1.1
            pos (200, 80)

        show alex talk:
            zoom 1.1
            pos (800, 180)

        show sasha:
            zoom 1.3
            pos (1200, 100)
        with fade

        ax "А внутри… сыровато как-то…"

        show nick talk:
            zoom 1.1
            pos (200, 80)

        show alex:
            zoom 1.1
            pos (800, 180)

        n "Это не сырость, Лёша. Это… нежность. По-деревенски. Такой хлеб дольше жуют — дольше сыт будешь."

        hide alex
        hide nick talk
        hide sasha

        show anastasia 2:
            zoom 1.1
            pos (800, 250)

        show maria talk:
            zoom 1.2
            pos (200, 250)

        m "Мы боялись пересушить…"

        hide maria talk
        hide anastasia 2

        show nick:
            zoom 1.1
            pos (200, 80)

        show alex:
            zoom 1.1
            pos (800, 180)

        show sasha talk:
            zoom 1.3
            pos (1200, 100)

        al "Ничего, Машенька. На войне как на войне. В следующий раз получится."

        hide nick
        hide alex
        hide sasha talk
        with fade

    elif bread_quality == "burnt":
        if bread_type == "karavay":
            show bread_burnt_round at truecenter with dissolve
        else:
            show bread_burnt_oval at truecenter with dissolve
        $ renpy.pause(2.0)
        hide bread_burnt_round
        hide bread_burnt_oval

        show nick:
            zoom 1.1
            pos (200, 80)

        show alex talk:
            zoom 1.1
            pos (800, 180)

        show sasha:
            zoom 1.3
            pos (1200, 100)
        with fade

        ax "Маменька, а почему хлеб… горелый?"

        show nick talk:
            zoom 1.1
            pos (200, 80)

        show alex:
            zoom 1.1
            pos (800, 180)

        show sasha:
            zoom 1.3
            pos (1200, 100)

        n "Ну, Алексей, не кричи так. Девочки старались. Да и не горелый он — так, пропёкся слегка больше обычного."
        
        hide alex
        hide nick talk
        hide sasha

        show anastasia 2:
            zoom 1.1
            pos (800, 250)

        show maria:
            zoom 1.2
            pos (200, 250)

        "Настя и Мария виновато опускают головы."

        hide maria
        hide anastasia 2

        show nick:
            zoom 1.1
            pos (200, 80)

        show alex:
            zoom 1.1
            pos (800, 180)

        show sasha talk:
            zoom 1.3
            pos (1200, 100)

        al "Девочки, не вешать нос! Москва тоже не сразу строилась. Главное — от души."

        hide alex
        hide nick talk
        hide sasha
        with fade

    else:  
        if bread_type == "karavay":
            show bread_perfect_round at truecenter with dissolve
        else:
            show bread_perfect_oval at truecenter with dissolve
        $ renpy.pause(2.0)
        hide bread_perfect_round
        hide bread_perfect_oval

        show nick:
            zoom 1.1
            pos (200, 80)

        show alex talk:
            zoom 1.1
            pos (800, 180)

        show sasha:
            zoom 1.3
            pos (1200, 100)
        with fade

        ax "Хлеб… какой-то странный…"

        show nick talk:
            zoom 1.1
            pos (200, 80)

        show alex:
            zoom 1.1
            pos (800, 180)

        n "Ничего, Лёша. В следующий раз получится лучше."

        hide alex
        hide nick talk
        hide sasha

        show anastasia 2:
            zoom 1.1
            pos (800, 250)

        show maria talk:
            zoom 1.2
            pos (200, 250)

        m "Мы старались…"

        hide maria talk
        hide anastasia 2

        show nick:
            zoom 1.1
            pos (200, 80)

        show alex:
            zoom 1.1
            pos (800, 180)

        show sasha talk:
            zoom 1.3
            pos (1200, 100)

        al "И мы это ценим, девочки."

        hide nick
        hide alex
        hide sasha talk
        with fade

    show har:
        zoom 1.1
        pos (650, 150)

    "Харитонов тем временем разлил суп."

    show har talk:
        zoom 1.1
        pos (650, 150)

    h "Суп куриный… к царскому столу подан."

    hide har talk

    show nick talk:
        zoom 1.1
        pos (600, 80)

    n "Господи, благослови…"

    hide nick talk
    with fade

    "Все крестятся. Харитонов кланяется, уходит."

    scene bg dinner with dissolve

    "Семья приступает к трапезе."

    play sound "audio/cought.mp3"

    show sasha talk:
        zoom 1.3
        pos (600, 100)
    with fade

    "Александра Фёдоровна начинает сильно кашлять - глухо, надрывно, давясь воздухом."

    hide sasha talk
    with fade

    show sasha:
        zoom 1.3
        pos (900, 100)

    show dem talk:
        zoom 1.3
        pos (200, 100)

    d "Ваше Величество… Позвать Боткина?"

    show sasha talk:
        zoom 1.3
        pos (900, 100)

    show dem:
        zoom 1.3
        pos (200, 100)

    al "Не надо… Анна… Подайка лучше водички… тёплой… Да попроси у Харитонова ромашку — в чай заварю."

    hide dem
    hide sasha talk
    with fade

    play sound "audio/door_close.mp3"

    "Демидова убегает."


    show alex scary:
        zoom 1.1
        pos (700, 180)

    ax "..."

    hide alex scary

    show nick:
        zoom 1.1
        pos (300, 80)

    show sasha:
        zoom 1.3
        pos (900, 100)

    "Николай кладёт руку на плечо Александры."

    show sasha talk:
        zoom 1.3
        pos (900, 100)

    al "Всё хорошо."

    show sasha:
        zoom 1.3
        pos (900, 100)

    "Александра отводит его ладонь - нежно, но твёрдо."

    hide sasha
    hide alex
    hide nick

    show olga 2:
        zoom 1.2
        pos (1000, 170)

    show tania:
        zoom 1.2
        pos (300, 150)

    "Татьяна и Ольга переглядываются. Татьяна хочет встать, но Ольга незаметно качает головой - не надо суеты."

    hide tania
    hide olga
    with fade

    "Кашель стихает. Тишина. Только ложки звенят."

    show nick talk:
        zoom 1.1
        pos (300, 80)

    show olga 2:
        zoom 1.2
        pos (900, 170)

    n "Солнце сегодня… редкое. Воздух какой."

    show nick:
        zoom 1.1
        pos (300, 80)

    show olga talk 2:
        zoom 1.2
        pos (900, 170)

    o "Хорошо бы пройтись, папенька."

    hide olga talk 2
    hide nick

    show anastasia talk:
        zoom 1.1
        pos (300, 250)

    show alex:
        zoom 1.1
        pos (900, 180)

    a "О да! Я так устала сидеть. Хоть в саду…"

    show anastasia:
        zoom 1.1
        pos (300, 250)

    show alex talk:
        zoom 1.1
        pos (900, 180)

    ax "И я! И я с вами!"

    hide alex talk
    hide anastasia

    show nick:
        zoom 1.1
        pos (600, 80)

    n "..." 
    "Николай переводит взгляд на Александру. Та слабо кивает."

    hide nick

    show sasha talk:
        zoom 1.3
        pos (600, 100)

    al "Идите, дети. Только недолго."

    hide sasha talk
    with fade

    "Семья неспешно поднимается."

    show dem:
        zoom 1.3
        pos (550, 100)

    play sound "audio/door_close.mp3"

    "Демидова возвращается с чашкой ромашкового настоя."

    hide dem

    show sasha talk:
        zoom 1.3
        pos (600, 100)

    al "Погодите минуту… Дай отдышаться."

    show sasha:
        zoom 1.3
        pos (600, 100)

    "Она делает глоток. Глаза закрывает на секунду."

    hide sasha

    show nick talk:
        zoom 1.1
        pos (600, 80)

    n "Мы не спешим, Швыбзик. Светит солнце - и слава Богу."

    hide nick talk

    jump walk_scene

label walk_scene:
    scene bg garden with fade
    play music "audio/garden.mp3" loop volume 0.25 fadein 2.0

    "Солнце пробивается сквозь дощатый забор. Слышны шаги часового за стеной."

    show nick:
        zoom 1.1
        pos (600, 80)
    with fade

    "Николай идёт вперёд, заложив руки за спину."

    hide nick
    with fade

    show tania:
        zoom 1.2
        pos (800, 150)

    show alex 2:
        zoom 1.1
        pos (500, 180)

    "Татьяна ведёт Алексея за руку - он прихрамывает, но отказывается от коляски."

    hide alex 2
    hide tania
    with fade

    show anastasia 2:
        zoom 1.1
        pos (900, 250)

    show maria:
        zoom 1.2
        pos (300, 250)

    "Мария и Анастасия замыкают шествие, перешёптываясь."

    hide maria
    hide anastasia 2
    with fade

    show tania:
        zoom 1.2
        pos (400, 150)

    show alex talk 2:
        zoom 1.1
        pos (100, 180)

    show nick 2:
        zoom 1.1
        pos (1100, 80)

    ax "Папенька, а почему в этом саду нет ни одного дерева, на которое можно залезть?"

    show alex 2:
        zoom 1.1
        pos (100, 180)

    show nick talk 2:
        zoom 1.1
        pos (1100, 80)

    n "Потому что этот сад, Лёша, посадили не для радости. А для того, чтобы мы видели небо."

    show nick 2:
        zoom 1.1
        pos (1100, 80)

    "Татьяна сжимает руку брата."

    hide tania
    hide alex 2
    hide nick 2
    with fade

    show anastasia 2:
        zoom 1.1
        pos (1100, 250)

    show maria:
        zoom 1.2
        pos (300, 250)

    "Анастасия подходит к забору, проводит пальцами по доскам."

    show anastasia talk 2:
        zoom 1.1
        pos (1100, 250)

    a "Интересно, что там? За этим забором?"

    show anastasia 2:
        zoom 1.1
        pos (1100, 250)

    show maria talk:
        zoom 1.2
        pos (300, 250)

    m "Улица. Наверное, обычная. Пыльная. С собаками."

    hide maria talk
    hide anastasia 2

    menu:
        "Что скажет Татьяна?"
        "Не надо смотреть в щели, Настя. Там солдаты. Увидят — подумают что-то не то.":

            show tania talk:
                zoom 1.2
                pos (600, 150)
            with fade

            t "Не надо смотреть в щели, Настя. Там солдаты. Увидят — подумают что-то не то."

            hide tania talk
            with fade

            show anastasia:
                zoom 1.1
                pos (900, 250)

            show maria:
                zoom 1.2
                pos (300, 250)

            "Анастасия отходит от забора, виновато опустив голову."

            hide maria
            hide anastasia
            with fade

        "Давай я подсажу тебя. Посмотришь одну секунду.":

            show tania talk:
                zoom 1.2
                pos (600, 150)
            with fade

            t "Давай я подсажу тебя. Посмотришь одну секунду."

            hide tania
            with fade

            show tania:
                zoom 1.2
                pos (1000, 190)

            show anastasia 2:
                zoom 1.1
                pos (1300, 100)

            show maria:
                zoom 1.2
                pos (300, 250)

            "Татьяна подсаживает сестру. Анастасия заглядывает в щель."
            scene bg hole with fade
            play sound "audio/knock_angry.mp3"
            "Голос из-за забора:" "Отойти от ограждения!"
            scene bg garden with fade

            show tania:
                zoom 1.2
                pos (600, 190)

            show anastasia:
                zoom 1.1
                pos (1100, 250)

            show maria:
                zoom 1.2
                pos (300, 250)

            "Девочки отпрыгивают. Николай качает головой, но не ругает."

            hide maria
            hide tania
            hide anastasia
            with fade
            
        "За забором такая же Россия, как и везде. Только мы от неё отрезаны.":

            show tania talk:
                zoom 1.2
                pos (600, 150)
            with fade

            t "За забором такая же Россия, как и везде. Только мы от неё отрезаны."

            hide tania
            with fade

            show anastasia 2:
                zoom 1.1
                pos (1100, 250)

            show maria 2:
                zoom 1.2
                pos (300, 250)

            "Тишина повисает над садом. Мария отворачивается от забора, пряча глаза."

            hide maria 2
            hide anastasia 2
            with fade

    "Они доходят до грядки с увядшей зеленью. Алексей садится на скамейку. Татьяна поправляет ему воротник."

    "Николай достаёт папиросу, но не закуривает, мнёт в пальцах."

    show nick talk:
        zoom 1.1
        pos (300, 80)

    show anastasia:
        zoom 1.1
        pos (900, 250)

    n "Знаете, дети… Я много читал в этих стенах. Историю. Особенно про старых царей. Знаете, что их всех объединяло?"

    show nick:
        zoom 1.1
        pos (300, 80)

    show anastasia talk:
        zoom 1.1
        pos (900, 250)

    a "Короны?"

    show nick talk:
        zoom 1.1
        pos (300, 80)

    show anastasia:
        zoom 1.1
        pos (900, 250)

    n "Нет. Последние дни. У всех у них были последние дни. И почти никто об этом не знал."

    hide nick talk
    hide anastasia
    with fade

    show tania 2:
        zoom 1.2
        pos (900, 150)

    show maria 2:
        zoom 1.2
        pos (300, 250)
    with fade

    "Пауза. Мария кусает губу. Татьяна смотрит на отца с удивлением - он никогда не говорил так прямо."

    hide maria 2
    hide tania 2

    show nick:
        zoom 1.1
        pos (300, 80)

    show anastasia talk:
        zoom 1.1
        pos (900, 250)

    a "Папенька… А мы знаем?"

    show nick:
        zoom 1.1
        pos (300, 80)

    show anastasia:
        zoom 1.1
        pos (900, 250)

    "Николай молчит. Кладёт папиросу обратно в портсигар."

    show nick talk:
        zoom 1.1
        pos (300, 80)

    show anastasia:
        zoom 1.1
        pos (900, 250)

    n "Мы знаем только то, что Бог даёт знать. А остальное - ветер."

    hide nick talk
    hide anastasia

    if bread_type == "karavay" and baking_success:
        $ heard_soldiers = True
        scene bg hole with fade
        "Анастасия отходит к дальней стене сада, где доски чуть отошли. В щель виден край улицы. Там стоят двое солдат — молодой и пожилой. Они не видят Настю. Она замирает, подслушивает."

        "Молодой солдат" "Слышь, Петрович… А правда, что их… ну… того? Скоро?"

        "Старый солдат" "Цыц, дурак. Не твоего ума дело. Сказано — охранять. Значит, охраняем."

        "Молодой солдат" "Да я так… Жалко ведь. Девчонки вон совсем ещё. И мальчик хромой."

        "Старый солдат" "Жалеть - не наша работа. Наша работа - приказ выполнять. А сердце… сердце засунь подальше. Оно тебе здесь боком вылезет."

        scene bg garden with fade

        show anastasia:
            zoom 1.1
            pos (900, 250)

        show tania 2:
            zoom 1.2
            pos (300, 150)

        "Анастасия отходит от щели. Лицо у неё белое. Она возвращается к Татьяне и хватает её за рукав."

        hide tania 2

        show tania:
            zoom 1.2
            pos (300, 150)

        show anastasia talk:
            zoom 1.1
            pos (900, 250)

        a "Таня… Я слышала… Они говорят… Про «того». Что скоро."

        show anastasia:
            zoom 1.1
            pos (900, 250)

        "Татьяна замирает. Секунда - и она берёт себя в руки."

        menu:
            "Что сделает Татьяна?"
            "Молчи. Никому ни слова. Особенно Мари и Лёше. Я сама скажу отцу.":

                show tania talk:
                    zoom 1.2
                    pos (300, 150)

                t "Молчи. Никому ни слова. Особенно Мари и Лёше. Я сама скажу отцу."

                show tania:
                    zoom 1.2
                    pos (300, 150)

                "Татьяна обнимает сестру. Её голос твёрд, но руки дрожат."

                hide tania
                hide anastasia
                with fade

            "Скажем всем. Пусть знают. Хватит притворяться.":

                show tania talk:
                    zoom 1.2
                    pos (300, 150)

                t "Скажем всем. Пусть знают. Хватит притворяться."

                show tania:
                    zoom 1.2
                    pos (300, 150)

                "Татьяна сжимает кулаки. В её глазах — отчаяние и решимость."

                hide tania
                hide anastasia
                with fade

            "Это просто солдатские разговоры. Они сами ничего не знают. Забудь, Настя.":

                show tania talk:
                    zoom 1.2
                    pos (300, 150)

                t "Это просто солдатские разговоры. Они сами ничего не знают. Забудь, Настя."

                show tania:
                    zoom 1.2
                    pos (300, 150)

                "Татьяна гладит сестру по голове, но сама бледнеет."

                hide tania
                hide anastasia
                with fade

    "Николай замечает, что девочки шепчутся. Подходит."

    show tania:
        zoom 1.2
        pos (800, 150)

    show anastasia:
        zoom 1.1
        pos (1300, 250)

    show nick talk:
        zoom 1.1
        pos (200, 80)
    with fade

    n "Что случилось?"

    hide tania
    hide anastasia

    show nick:
        zoom 1.1
        pos (200, 80)

    show tania talk 2:
        zoom 1.2
        pos (800, 150)

    show anastasia:
        zoom 1.1
        pos (1300, 250)

    t "Ничего, папенька. Настя просто испугалась… ящерицы."

    show tania 2:
        zoom 1.2
        pos (800, 150)

    "Николай смотрит пристально, верит не до конца, но кивает."

    show nick talk:
        zoom 1.1
        pos (200, 80)

    n "В этом саду много чего есть. Кроме надежды."

    show nick:
        zoom 1.1
        pos (200, 80)

    hide nick
    hide anastasia
    hide tania 2
    with fade

    "Он садится рядом с Алексеем. Гладит сына по голове."


if not inventory.has_item(3):
    menu:
        "Подойти к отцу и спросить о его кресте" if heard_soldiers:

            show anastasia talk:
                zoom 1.1
                pos (900, 250)

            show nick:
                zoom 1.1
                pos (300, 80)
            with fade

            a "Папенька... Можно вас спросить?"

            show anastasia:
                zoom 1.1
                pos (900, 250)

            show nick talk:
                zoom 1.1
                pos (300, 80)

            n "Конечно, Настенька."

            show anastasia talk:
                zoom 1.1
                pos (900, 250)

            show nick:
                zoom 1.1
                pos (300, 80)

            a "Ваш крест... Вы всегда его носите?"

            show anastasia:
                zoom 1.1
                pos (900, 250)

            "Николай достаёт крест из-за ворота гимнастёрки."

            show anastasia:
                zoom 1.1
                pos (900, 250)

            show nick talk:
                zoom 1.1
                pos (300, 80)

            n "Этот крест мне подарила мама, когда я был маленьким. Я ношу его всю жизнь."

            show anastasia talk:
                zoom 1.1
                pos (900, 250)

            show nick:
                zoom 1.1
                pos (300, 80)

            a "Можно подержать?"

            show anastasia:
                zoom 1.1
                pos (900, 250)

            show nick talk:
                zoom 1.1
                pos (300, 80)

            n "Держи, дочка."

            show anastasia:
                zoom 1.1
                pos (900, 250)

            show nick:
                zoom 1.1
                pos (300, 80)

            "Анастасия берёт тяжёлый серебряный крест. Он хранит тепло отца."
            $ inventory.add_item(3)
            play sound "audio/notify.mp3"

            hide anastasia
            hide nick
            with fade
            
        "Спросить, что папа чувствует, когда молится":

            show anastasia talk:
                zoom 1.1
                pos (900, 250)

            show nick:
                zoom 1.1
                pos (300, 80)
            with fade

            a "Папенька... А когда вы молитесь, вам становится легче?"

            show anastasia:
                zoom 1.1
                pos (900, 250)

            show nick talk:
                zoom 1.1
                pos (300, 80)

            n "Знаешь, Настя, молитва - это как разговор с самым близким другом. Иногда слов не нужно. Просто быть."

            show anastasia talk:
                zoom 1.1
                pos (900, 250)

            show nick:
                zoom 1.1
                pos (300, 80)

            a "Я тоже хочу так научиться."

            show anastasia:
                zoom 1.1
                pos (900, 250)

            show nick talk:
                zoom 1.1
                pos (300, 80)

            n "Ты уже умеешь. Просто закрой глаза и слушай своё сердце."

            show nick:
                zoom 1.1
                pos (300, 80)

            "Анастасия закрывает глаза на секунду. Ей кажется, что она чувствует что-то тёплое внутри."

            show anastasia talk:
                zoom 1.1
                pos (900, 250)

            show nick:
                zoom 1.1
                pos (300, 80)

            a "Кажется, получается..."

            show anastasia:
                zoom 1.1
                pos (900, 250)

            show nick talk:
                zoom 1.1
                pos (300, 80)

            n "Видишь? Бог всегда с тобой, даже если ты не носишь крест на шее."

            hide anastasia
            hide nick
            with fade
            
        "Промолчать и просто идти рядом с отцом":

            show anastasia 2:
                zoom 1.1
                pos (900, 250)

            show nick:
                zoom 1.1
                pos (400, 80)
            with fade

            "Анастасия молча идёт рядом с отцом. Ей не нужны слова. Просто быть рядом - уже достаточно."
            "Николай кладёт руку ей на плечо. Они идут молча, и это молчание говорит больше любых слов."

            hide anastasia 2
            hide nick
            with fade

    show nick:
        zoom 1.1
        pos (300, 80)

    show alex talk:
        zoom 1.1
        pos (900, 180)

    ax "Папенька, а когда мы уедем отсюда?"

    show alex:
        zoom 1.1
        pos (900, 180)

    "Николай молчит. Долго. Потом очень тихо:"

    show nick talk:
        zoom 1.1
        pos (300, 80)

    n "Скоро, Лёша. Скоро."
    play music "audio/guard.mp3" fadein 2.0 volume 0.3

    hide alex
    hide nick talk
    with fade

    "Все замолкают. Слышно только шаги часового. Где-то за забором лает собака."

    "Мария срывает увядший одуванчик и дует на него. Семечки не летят."

    menu:
        "Татьяна предлагает:"
        "Вернёмся в дом. Маменька, наверное, заждалась. И ромашковый чай уже остыл.":

            show tania talk 2:
                zoom 1.2
                pos (600, 150)

            t "Вернёмся в дом. Маменька, наверное, заждалась. И ромашковый чай уже остыл."

            hide tania talk 2
            
            "Николай кивает."

        "Посидим ещё немного. Здесь хотя бы воздух. В доме… душно.":

            show tania talk 2:
                zoom 1.2
                pos (600, 150)

            t "Посидим ещё немного. Здесь хотя бы воздух. В доме… душно."

            hide tania talk 2

            "Николай садится обратно на скамейку. Никто не двигается с места."

            "Проходит несколько минут..."

        "Давайте споём. Тихо. Ту песню, что пели в Тобольске. Маменька услышит в окно.":

            show tania talk 2:
                zoom 1.2
                pos (600, 150)

            t "Давайте споём. Тихо. Ту песню, что пели в Тобольске. Маменька услышит в окно."

            hide tania talk 2

            play music "audio/romans.mp3" fadein 2.0 volume 0.3
            "Семья начинает тихо петь."
            "Голоса звучат тихо, но ровно."
            play sound "audio/knock_angry.mp3"
            stop music fadeout 0.5
            "Из-за забора раздаётся крик:"
            "Голос" "Прекратить!"
            "Песня обрывается. Тишина."

    "Николай поднимается. Подаёт руку Алексею. Татьяна берёт Марию за локоть. Анастасия идёт последней, оглядываясь на щель в заборе."
    stop music fadeout 2.0

    jump free_time

label free_time:
    scene bg living with fade

    "Ранний вечер. Гостиная."

    show tania:
        zoom 1.2
        pos (200, 150)
    
    show olga 2:
        zoom 1.2
        pos (1000, 170)
    with fade

    "Татьяна сидит в кресле, вышивает рубашку Алексею. Ольга рядом - узор на канве."

    hide olga 2
    hide tania
    with fade

    show anastasia:
        zoom 1.1
        pos (900, 250)

    show maria:
        zoom 1.2
        pos (300, 250)

    "Мария и Анастасия расположились на полу, перебирают нитки и листают старый альбом с фотографиями."

    hide anastasia
    hide maria
    with fade
    
    if not inventory.has_item(4):
            "В углу комнаты Анастасия замечает старую коробку, которую привезли ещё из Тобольска. Она так и стоит неразобранная."
            
            menu:
                "Предложить сестрам разобрать коробку":

                    show anastasia talk:
                        zoom 1.1
                        pos (900, 250)

                    show maria:
                        zoom 1.2
                        pos (300, 250)
                    with fade

                    a "Мария, может, посмотрим, что там? Всё равно делать нечего."

                    show anastasia:
                        zoom 1.1
                        pos (900, 250)

                    show maria talk 2:
                        zoom 1.2
                        pos (300, 250)

                    m "Правда! Я совсем забыла про неё."

                    scene bg boxes with fade
                    
                    "Сестры пододвигают коробку к себе и начинают аккуратно перебирать её содержимое."
                    m "Смотрите, мамины платки! Помните этот, с вышивкой? Она его в Царском любила."
                    a "А это папины запонки... Я думала, они потерялись в Тобольске."
                    
                    "Анастасия запускает руку на дно коробки и нащупывает небольшую книгу в кожаном переплёте."
                    a "Cмотри!"
                    
                    "Она достаёт молитвослов. Обложка потёрта, уголки сбиты, но застёжка всё ещё держит."
                    m "Это же мамин молитвослов! Тот самый, который она всегда держала под подушкой."
                    m "А я думала, его конфисковали при обыске..."
                    
                    play sound "audio/book_turn.mp3"

                    "Анастасия осторожно открывает книгу. Страницы пожелтели, но на полях - знакомый тонкий почерк матери."
                    
                    m "Надо вернуть маме. Она без него, наверное, очень скучает."
                    a "Я отнесу."
                    
                    "Анастасия прячет молитвослов за пазуху и чувствует, как тепло разливается по груди."
                    $ inventory.add_item(4)
                    play sound "audio/notify.mp3"
                    scene bg living with fade
                    
                "Просто посмотреть, что сверху":
                    scene bg boxes with fade
                    "Анастасия подходит к коробке и заглядывает в неё, не трогая глубоко."
                    "Сверху лежат старые газеты и несколько платков. Она не решается копаться глубже."
                    a "Наверное, потом разберём. Не сейчас."
                    ia "Слишком много воспоминаний. Они ещё не выветрились."
                    scene bg living with fade
                    "Она возвращается к альбому с фотографиями."
                    
                "Не трогать коробку":
                    scene bg boxes with fade
                    "Анастасия смотрит на коробку, но решает не трогать её. Пусть стоит, как стоит."
                    scene bg living with fade
                    ia "Может, в другой раз. Когда будет легче."
                    "Она отворачивается и снова берёт в руки альбом."

    "Анастасия находит старую фотографию, где Таня демонстрирует свою первую вышивку."

    show maria 2:
        zoom 1.2
        pos (700, 250)

    show anastasia talk:
        zoom 1.1
        pos (1100, 250)

    show tania:
        zoom 1.2
        pos (100, 150)

    a "Таня, гляди! Ты тут совсем девчушка, как мы с Мари. А в руках у тебя какая красота!"

    show anastasia:
        zoom 1.1
        pos (1100, 250)

    "Таня поднимает голову, с теплотой смотрит на фотографию и снова возвращается к своей новой работе."

    show maria talk 2:
        zoom 1.2
        pos (700, 250)

    m "Тань, а что ты сейчас вышиваешь?"

    show maria 2:
        zoom 1.2
        pos (700, 250)

    show tania talk:
        zoom 1.2
        pos (100, 150)

    t "Я вышиваю рубашку Алексею. На локтях она уже протёрлась..."

    show tania:
        zoom 1.2
        pos (100, 150)

    show anastasia talk:
        zoom 1.1
        pos (1100, 250)

    a "Оля, а ты?"

    hide anastasia talk
    hide tania
    hide maria 2

    show olga talk:
        zoom 1.2
        pos (550, 170)

    o "А я подарок Мари. Скоро же её именины… надо подготовиться."

    show olga:
        zoom 1.2
        pos (550, 170)

    "Пауза. На секунду Ольга замирает."

    show olga talk:
        zoom 1.2
        pos (550, 170)

    o "Хотя не знаю, будут ли праздновать."

    hide olga talk

    show nick talk 2:
        zoom 1.1
        pos (650, 80)

    n "Будем праздновать, дети. Всегда будем. Что бы ни случилось."

    hide nick talk 2
    with fade

    "Ольга опускает глаза. Татьяна кусает губу, но продолжает шить."

    play sound "audio/book_turn.mp3"

    "Анастасия переворачивает страницу альбома. В кромнате беспокойная тишина."

    show anastasia talk:
        zoom 1.1
        pos (900, 250)

    show maria:
        zoom 1.2
        pos (300, 250)
    with fade

    a "Вот здесь мы в Ливадии. Помните? Папенька в белом, маменька в шляпе… и море."

    show anastasia:
        zoom 1.1
        pos (900, 250)

    show maria talk:
        zoom 1.2
        pos (300, 250)

    m "Море… Я уже забыла, как оно пахнет."

    show anastasia talk:
        zoom 1.1
        pos (900, 250)

    show maria:
        zoom 1.2
        pos (300, 250)

    a "А в Тобольске пахло снегом. А здесь… здесь ничем не пахнет. Воздух как вата."

    hide maria
    hide anastasia talk
    with fade

    show nick 2:
        zoom 1.1
        pos (650, 80)

    "Николай откладывает книгу. его взгляд падает на..."

    menu optional_name:
        "Небольшой журнальный столик":
            scene bg read with fade
            "На столике лежит Библия."

            play sound "audio/book_turn.mp3"

            "Николай берёт её в руки, открывает на случайной странице."
        
            if not inventory.has_item(5):
                n "Настя, подойди. Я хочу тебе кое-что показать."
                a "Что, папа?"
                "Николай перелистывает страницы."
                n "Смотри. Я делаю пометки в тех местах, которые помогают мне не терять надежду."
                "Анастасия видит аккуратные карандашные крестики и короткие слова на полях."
                
                menu:
                    "Внимательно рассмотреть пометки":
                        a "Можно посмотреть поближе?"
                        n "Конечно, дочка."
                        "Анастасия проводит пальцем по строчке, где написано: 'Не бойся, ибо Я с тобою'."
                        a "Папа... Это помогает?"
                        n "Очень. Когда я читаю эти слова, я вспоминаю, что мы не одни."
                        a "Я запомню это место."
                        "Анастасия закрывает Библию, но чувство тепла остаётся."
                        $ inventory.add_item(5)
                        play sound "audio/notify.mp3"
                        
                    "Спросить, какое место папа любит больше всего":
                        a "Папа, а какое место вы любите больше всего?"
                        n "Вот это: 'Приидите ко Мне все труждающиеся и обремененные, и Я успокою вас'."
                        n "Оно напоминает: мы не одни в своих страданиях. Есть Тот, кто видит нас."
                        a "Я запомню эти слова."
                        n "Запомни, дочка. Они могут пригодиться."
                        
                    "Просто послушать":
                        a "Я просто постою рядом, если можно."
                        n "Конечно, Настя. Иногда молчание лучше слов."
                        "Они стоят рядом, глядя в одну книгу. Тихо. Спокойно."

            
        "На вышивку Ольги":
            scene bg cross with fade
            "Николай обращает внимание на работу Оли. Старшая дочь старательно вышивает что-то. Он шёпотом обращается к ней, чтобы Мари не слышала"
            n "Доченька, а что за подарок ты готовишь Машеньке?"
            o "Папенька, я вышиваю солнце, пляж, море... Всё то, что так любит наша Мари"
            "Николай довольно улыбается и похлопывает дочь по плечу."
        "На окно":
            scene bg window_dinner with fade
            n "Темнеет... хотя может ещё светло... не поймёшь"
            "Николай печально садиться на кресло, погружённый в свои мысли."
    scene bg living with fade

    play sound "audio/door_close.mp3"

    show dem 2:
        zoom 1.3
        pos (550, 100)

    "В комнату заходит Демидова."

    show dem talk 2:
        zoom 1.3
        pos (550, 100)

    d "Ваше Величество, Харитонов просит вас к столу. Ужин уже готов. Алексей с Александрой Фёровной уже в зале."

    hide dem talk 2

    show nick talk 2:
        zoom 1.1
        pos (650, 80)

    n "Пойдёмте, дети, завтра довышиваете."

    scene black with fade
    centered "Ужин проходил на удивление спокойно."

    jump cards

label cards:
    scene bg live even with fade
    "После ужина. Все вновь в гостиной. Николай достаёт колоду карт - потрёпанную, в пятнах. Садится напротив Александры."
    show nikolai at left
    show aleksandra at right
    show children_back at center

    n "Что ж, день был долгим. Может, сыграем партию в безик?"

    al "С удовольствием, Ники. Дети, кто хочет посмотреть?"

    o "Я посмотрю."
    t "И я."
    ax "А можно мне с вами?"
    
    n "В следующий раз, Алёша. А пока смотри и запоминай."

    menu:
        "Играть за Александру":
            $ player_is_nikolai = False
            al "Держись, Ники! Я в этой игре — лучшая!"
            
            call card_game_start from _call_card_game_start
        
        "Играть за Николая":
            $ player_is_nikolai = True
            n "Ха! Сегодня я поддаваться не буду!"
            
            call card_game_start from _call_card_game_start_1
    
    jump after_card_game
    


# ПЕРЕМЕННЫЕ ДЛЯ КАРТОЧНОЙ ИГРЫ
default player_hand = []
default opponent_hand = []
default player_score = 0
default opponent_score = 0
default current_trick = []
default declared_combos_player = []
default declared_combos_opponent = []
default game_round = 1
default game_over = False
default game_finished = False
default selected_card = None
default waiting_for_player = True
default game_log = []
default last_trick_info = ""
default player_is_nikolai = True



init python:
    def add_to_log(message):
        global game_log
        game_log.append(message)
        if len(game_log) > 10:
            game_log.pop(0)
        renpy.restart_interaction()
    
    def select_card(card_index):
        global selected_card
        if waiting_for_player:
            selected_card = card_index
            renpy.restart_interaction()




label card_game_rules:
    scene black with fade
    play music "audio/cards.mp3" loop volume 0.2
    show text "Игра в безик" at truecenter with dissolve
    $ renpy.pause(2.0)
    hide text
    
    show text "Колода: 32 карты (от 7 до туза)" at truecenter with dissolve
    $ renpy.pause(1.5)
    hide text
    
    show text "Цель: набрать больше очков, чем соперник" at truecenter with dissolve
    $ renpy.pause(1.5)
    hide text
    
    show text "Очки дают:" at truecenter with dissolve
    $ renpy.pause(1.0)
    hide text
    
    show text "Безик (дама пик + валет треф) — 40 очков" at truecenter with dissolve
    $ renpy.pause(1.5)
    hide text
    
    show text "Марьяж (король и дама одной масти) — 20 очков" at truecenter with dissolve
    $ renpy.pause(1.5)
    hide text
    
    show text "Каре (4 одинаковые карты) — 100 очков" at truecenter with dissolve
    $ renpy.pause(1.5)
    hide text
    
    show text "Сотня (10 всех мастей) — 100 очков" at truecenter with dissolve
    $ renpy.pause(1.5)
    hide text
    
    show text "Взятки — по 10 очков за каждую" at truecenter with dissolve
    $ renpy.pause(1.5)
    hide text
    
    show text "Играем 3 раунда. Поехали!" at truecenter with dissolve

    stop music
    $ renpy.pause(2.0)
    hide text
    
    scene black with fade
    return



label card_game_start:
    $ card_game_active = True

    $ inventory_was_shown = renpy.get_screen("quick_inventory") is not None
    if inventory_was_shown:
        hide screen quick_inventory
    
    # Отключаем интерфейс
    $ original_overlay_game = config.overlay_screens.copy()
    $ original_quick_menu_game = quick_menu
    $ config.overlay_screens = []
    $ _preferences.afm_enable = False
    $ quick_menu = False
    window hide

    # Сброс переменных раунда
    $ game_finished = False
    $ game_over = False
    $ game_round = 1
    
    call card_game_rules
    
    python:
        # Инициализация первого раунда без отдельной функции
        suits = ["пики", "трефы", "бубны", "черви"]
        ranks = ["7", "8", "9", "10", "валет", "дама", "король", "туз"]
        rank_values = {
            "7": 0, "8": 0, "9": 0, "10": 10,
            "валет": 2, "дама": 3, "король": 4, "туз": 11
        }
        deck = []
        for suit in suits:
            for rank in ranks:
                deck.append({"rank": rank, "suit": suit, "value": rank_values[rank]})

        renpy.random.shuffle(deck)
        
        player_hand = deck[:8]
        opponent_hand = deck[8:16] 
        current_trick = []
        declared_combos_player = []
        declared_combos_opponent = []
        waiting_for_player = True
        last_trick_info = ""
        selected_card = None
        game_finished = False
        
        if player_is_nikolai:
            add_to_log("=== НАЧАЛО ИГРЫ ===")
            add_to_log(f"Николай против Александры. Раунд {game_round}")
        else:
            add_to_log("=== НАЧАЛО ИГРЫ ===")
            add_to_log(f"Александра против Николая. Раунд {game_round}")
    
    scene bg table with fade
    call screen card_game_ui

    # Восстановление интерфейса после игры
    $ config.overlay_screens = original_overlay_game
    $ quick_menu = original_quick_menu_game
    window show
    
    if inventory_was_shown:
        show screen quick_inventory
    
    # Определение победителя
    if player_score > opponent_score:
        jump card_game_player_wins
    elif player_score < opponent_score:
        jump card_game_opponent_wins
    else:
        jump card_game_tie


screen card_game_ui():
    modal True
    zorder 100
    
    if game_finished:
        timer 0.01 action Return()
    
    # Рука игрока
    hbox:
        xalign 0.5
        yalign 0.9
        spacing 10
        for i, card in enumerate(player_hand):
            $ card_name = f"{card['rank']}_{card['suit']}"
            imagebutton:
                idle Transform(f"images/cards/{card_name}.png", size=(200, 300))
                hover Transform(f"images/cards/{card_name}.png", size=(220, 320))
                action Function(select_card, i)
                if selected_card == i and waiting_for_player:
                    background Solid("#ffd70080")
    
    # Рука противника (рубашкой)
    hbox:
        xalign 0.5
        yalign 0.1
        spacing 10
        for i in range(len(opponent_hand)):
            add "images/cards/back.png":
                size (120, 160)
    
    # Текущая взятка
    hbox:
        xalign 0.5
        yalign 0.5
        spacing 20
        for card in current_trick:
            $ card_name = f"{card['rank']}_{card['suit']}"
            add Transform(f"images/cards/{card_name}.png", size=(200, 300))
    
    textbutton "Объявить комбинацию":
        xalign 0.2
        yalign 0.6
        background "#8B4513"
        hover_background "#CD853F"
        text_color "#FFFFFF"
        action Function(check_combinations)

    imagebutton:
        idle Transform("images/inventory/rules.png", size=(100,100))
        hover Transform("images/inventory/rules_dark.png", size=(110,110))
        xalign 0.05
        yalign 0.6
        action Show("bezik_rules")
    
    if selected_card is not None and waiting_for_player:
        textbutton "Сделать ход":
            xalign 0.8
            yalign 0.6
            background "#8B4513"
            hover_background "#CD853F"
            text_color "#FFFFFF"
            action Function(make_player_move)
    
    if player_is_nikolai:
        frame:
            xalign 0.5
            yalign 0.05
            background Solid("#00000080")
            text "Николай: [player_score]  |  Александра: [opponent_score]" size 30 color "#ffffff"
    else:
        frame:
            xalign 0.5
            yalign 0.05
            background Solid("#00000080")
            text "Александра: [player_score]  |  Николай: [opponent_score]" size 30 color "#ffffff"
    
    if waiting_for_player:
        if player_is_nikolai:
            frame:
                xalign 0.5
                yalign 0.95
                background Solid("#00000080")
                text "Ход Николая" size 30 color "#ffd700"
        else:
            frame:
                xalign 0.5
                yalign 0.95
                background Solid("#00000080")
                text "Ход Александры" size 30 color "#ffd700"
    else:
        if player_is_nikolai:
            frame:
                xalign 0.5
                yalign 0.95
                background Solid("#00000080")
                text "Ход Александры..." size 30 color "#ffd700"
        else:
            frame:
                xalign 0.5
                yalign 0.95
                background Solid("#00000080")
                text "Ход Николая..." size 30 color "#ffd700"
    
    if last_trick_info:
        frame:
            xalign 0.5
            yalign 0.45
            background Solid("#000000aa")
            text last_trick_info size 28 color "#ffd700"


init python:
    def make_player_move():
        global selected_card, player_hand, current_trick, waiting_for_player
        global last_trick_info, game_finished
        
        if selected_card is not None and waiting_for_player:
            card = player_hand.pop(selected_card)
            current_trick.append(card)
            selected_card = None
            waiting_for_player = False
            
            if player_is_nikolai:
                add_to_log(f"Николай выложил {card['rank']} {card['suit']}")
            else:
                add_to_log(f"Александра выложила {card['rank']} {card['suit']}")
            
            renpy.restart_interaction()
            opponent_move_logic()
            renpy.restart_interaction()
    
    def opponent_move_logic():
        global opponent_hand, current_trick, player_score, opponent_score, waiting_for_player
        global last_trick_info, game_finished, game_round
        
        if not waiting_for_player and not game_finished:
            if opponent_hand:
                # Противник ходит первой картой (можно улучшить логику)
                best_card = opponent_hand[0]
                opponent_hand.remove(best_card)
                current_trick.append(best_card)
                
                if player_is_nikolai:
                    add_to_log(f"Александра выложила {best_card['rank']} {best_card['suit']}")
                else:
                    add_to_log(f"Николай выложил {best_card['rank']} {best_card['suit']}")
                
                if len(current_trick) == 2:
                    player_card = current_trick[0]
                    opponent_card = current_trick[1]
                    
                    if player_card["value"] > opponent_card["value"]:
                        player_score += 10
                        if player_is_nikolai:
                            last_trick_info = f"Николай взял взятку! (+10)  {player_card['rank']} {player_card['suit']} > {opponent_card['rank']} {opponent_card['suit']}"
                            add_to_log(f"Николай выиграл взятку! +10 очков")
                        else:
                            last_trick_info = f"Александра взяла взятку! (+10)  {player_card['rank']} {player_card['suit']} > {opponent_card['rank']} {opponent_card['suit']}"
                            add_to_log(f"Александра выиграла взятку! +10 очков")
                    elif opponent_card["value"] > player_card["value"]:
                        opponent_score += 10
                        if player_is_nikolai:
                            last_trick_info = f"Александра взяла взятку! (+10)  {opponent_card['rank']} {opponent_card['suit']} > {player_card['rank']} {player_card['suit']}"
                            add_to_log(f"Александра выиграла взятку! +10 очков")
                        else:
                            last_trick_info = f"Николай взял взятку! (+10)  {opponent_card['rank']} {opponent_card['suit']} > {player_card['rank']} {player_card['suit']}"
                            add_to_log(f"Николай выиграл взятку! +10 очков")
                    else:
                        last_trick_info = f"Ничья! {player_card['rank']} {player_card['suit']} = {opponent_card['rank']} {opponent_card['suit']}"
                        add_to_log(f"Ничья в взятке! Очки никому")
                    
                    current_trick = []
                
                # Проверка окончания раунда (если руки пусты)
                if not player_hand and not opponent_hand:
                    end_round()
                
                waiting_for_player = True
            else:
                waiting_for_player = True
    
    def check_combinations():
        global player_score, declared_combos_player, last_trick_info
        
        # Безик
        has_queen_spades = any(c["rank"] == "дама" and c["suit"] == "пики" for c in player_hand)
        has_jack_clubs = any(c["rank"] == "валет" and c["suit"] == "трефы" for c in player_hand)
        if has_queen_spades and has_jack_clubs and "bezik" not in declared_combos_player:
            player_score += 40
            declared_combos_player.append("bezik")
            add_to_log("БЕЗИК! +40 очков")
            last_trick_info = "БЕЗИК! +40 очков"
        
        # Марьяжи
        for suit in ["пики", "трефы", "бубны", "черви"]:
            has_king = any(c["rank"] == "король" and c["suit"] == suit for c in player_hand)
            has_queen = any(c["rank"] == "дама" and c["suit"] == suit for c in player_hand)
            combo_name = f"marriage_{suit}"
            if has_king and has_queen and combo_name not in declared_combos_player:
                player_score += 20
                declared_combos_player.append(combo_name)
                add_to_log(f"Марьяж {suit}! +20 очков")
                last_trick_info = f"Марьяж {suit}! +20 очков"
        
        # Каре
        ranks_count = {}
        for card in player_hand:
            ranks_count[card["rank"]] = ranks_count.get(card["rank"], 0) + 1
        for rank, count in ranks_count.items():
            if count >= 4 and f"four_{rank}" not in declared_combos_player:
                player_score += 100
                declared_combos_player.append(f"four_{rank}")
                add_to_log(f"Каре из {rank}! +100 очков")
                last_trick_info = f"Каре из {rank}! +100 очков"
        
        # Сотня
        has_ten_spades = any(c["rank"] == "10" and c["suit"] == "пики" for c in player_hand)
        has_ten_clubs = any(c["rank"] == "10" and c["suit"] == "трефы" for c in player_hand)
        has_ten_diamonds = any(c["rank"] == "10" and c["suit"] == "бубны" for c in player_hand)
        has_ten_hearts = any(c["rank"] == "10" and c["suit"] == "черви" for c in player_hand)
        if has_ten_spades and has_ten_clubs and has_ten_diamonds and has_ten_hearts and "hundred" not in declared_combos_player:
            player_score += 100
            declared_combos_player.append("hundred")
            add_to_log("Сотня! +100 очков")
            last_trick_info = "Сотня! +100 очков"
        
        renpy.restart_interaction()
    
    def end_round():
        global game_round, player_score, opponent_score, game_finished, game_over
        global player_hand, opponent_hand, declared_combos_player, declared_combos_opponent
        global last_trick_info, waiting_for_player, selected_card, current_trick
        
        if game_round < 3:
            game_round += 1
            add_to_log(f"Раунд {game_round}")
            last_trick_info = f"Раунд {game_round}"  # опционально
            
            suits = ["пики", "трефы", "бубны", "черви"]
            ranks = ["7", "8", "9", "10", "валет", "дама", "король", "туз"]
            rank_values = {
                "7": 0, "8": 0, "9": 0, "10": 10,
                "валет": 2, "дама": 3, "король": 4, "туз": 11
            }
            deck = []
            for suit in suits:
                for rank in ranks:
                    deck.append({"rank": rank, "suit": suit, "value": rank_values[rank]})
            
            renpy.random.shuffle(deck)
            
            player_hand = deck[:8]
            opponent_hand = deck[8:16]
            current_trick = []
            declared_combos_player = []
            declared_combos_opponent = []
            waiting_for_player = True
            selected_card = None
        else:
            game_over = True
            game_finished = True
            add_to_log(f"Игра окончена")
            add_to_log(f"Итог: {player_score} : {opponent_score}")
        
        renpy.restart_interaction()


label card_game_player_wins:
    scene bg live even with fade
    
    if player_is_nikolai:
        show nikolai at left
        show aleksandra at right
    else:
        show aleksandra at left
        show nikolai at right
    
    show children_back at center
    
    if player_is_nikolai:
        n "Кажется, я выиграл!"
        al "Поздравляю, Ники. Сегодня ты был сильнее."
        a "Ура! Папа победил!"
        ax "А в следующий раз я тоже сыграю!"
    else:
        al "Кажется, сегодня удача на моей стороне."
        n "В следующий раз я возьму реванш."
        t "Мама, вы так ловко играете!"
        ax "А в следующий раз я тоже сыграю!"
        al "Это всё практика, Таня."

    $ card_game_active = False
    jump after_card_game


label card_game_opponent_wins:
    scene bg dinner with fade
    
    if player_is_nikolai:
        show nikolai at left
        show aleksandra at right
    else:
        show aleksandra at left
        show nikolai at right
    
    show children_back at center
    
    if player_is_nikolai:
        al "Кажется, сегодня удача на моей стороне."
        n "В следующий раз я возьму реванш."
        t "Мама, вы так ловко играете!"
        al "Это всё практика, Таня."
    else:
        n "Кажется, я выиграл!"
        al "Поздравляю, Ники. Сегодня ты был сильнее."
        a "Ура! Папа победил!"
        ax "А в следующий раз я тоже сыграю!"
        n "Обязательно, Алёша. А теперь пора отдыхать."

    $ card_game_active = False
    jump after_card_game


label card_game_tie:
    scene bg live even with fade
    
    if player_is_nikolai:
        show nikolai at left
        show aleksandra at right
    else:
        show aleksandra at left
        show nikolai at right
    
    show children_back at center
    
    n "Ничья! В следующий раз обязательно выиграю."
    al "Согласна. А теперь пора спать."

    $ card_game_active = False
    jump after_card_game



label after_card_game:
    $ game_finished = False
    $ game_over = False
    $ game_round = 1
    $ player_score = 0
    $ opponent_score = 0
    
    "Николай смотрит на часы. Время уже почти десять."
    
    n "Пожалуй, на сегодня хватит. Продолжим завтра. А то поздно. Детям спать пора. Да и нам не помешало бы отдохнуть."
    
    "Александра Фёдоровна одобрительно кивает."
    
    ax "Ещё! Давайте ещё сыграем! Я не хочу спать. Маменька, я не устал. Честно-причестно!"
    
    "Александра Фёдоровна нежно улыбается сыну и гладит его по голове."
    
    al "Утро вечеру мудренее, Лёша. Завтра нас ждёт не менее насыщенный день..."
    
    "На лице матери читается тоска. Она оглядывает девочек, немного задерживая взгляд на Ольге, которая, похоже, уловила её состояние."
    
    "По лицу Оли заметно, что она хочет что-то сказать."
    
    if inventory.count_found() >= 6:
        "Оля шепчет это едва слышно, под нос. Но Николай улавливает её слова."
        "Она тихо произносит:"
        o "Если завтра вообще настанет..."
        
        "Николай поднимается со стула, подходит к Оле и приобнимает её за плечи — ласково, с осторожностью."
        
        n "Давайте помолимся, дети. За нашу семью, за наше счастье и благополучие... как молятся за наши души простые работяги за пределами нашей клетки."
        
        "Александра Фёдоровна подхватывает речь мужа."
        
        al "Помните, дети: чтобы ни случилось — Бог един. Он сострадает нам, плачет с нами и радуется за нас. Хоть наши судьбы и в Его руках, пока мы вместе — нам не страшны преграды!"
        
        "Все улыбаются. На душе у каждого что-то своё, но абсолютно каждый знает: он не один, пока рядом семья."
    else:
        "Оля сглатывает слова. Мысли роятся в голове: «Всякие глупости лезут. Нужно быть сильной, нужно держаться. Подавать младшим пример»."
        
        "Николай встаёт, крестит детей."
        "Александра целует каждого в макушку, нашёптывая строки из Библии."
        
        "Все расходятся."
    
    jump before_sleep


# СЦЕНА: ПОДГОТОВКА КО СНУ
 
label before_sleep:
    
    scene bg night_room
    with fade
    play music "audio/night.mp3" loop volume 0.2 fadein 2.0
 
    "22:00. Комната Александры Фёдоровны (она же спальня девочек)."
    "Александра сидит на краю кровати. Девочки стоят перед ней — Ольга, Татьяна, Мария, Анастасия."
    "Все в ночных сорочках, с распущенными волосами."
 
    "Александра крестит каждую. Целует в лоб."
 
    al "Храни тебя Господь, Ольга..."
    al "Храни тебя Господь, Татьяна..."
    al "Храни тебя Господь, Мария..."
    al "Храни тебя Господь, Анастасия..."
 
    "Голос её срывается на последнем имени. Она замолкает, сглатывает."
 
    a "Мама, а вы с папой ещё долго?"
 
    "Анастасия обнимает мать."
 
    al "Нет, мы тоже скоро. Идите. Спите."
 
    "Девочки уходят. В дверях Анастасия оборачивается."
 
    a "Маменька... я люблю вас."
 
    al "И я тебя, Настя. Иди."
 
    scene bg parents
    with dissolve
 
    "Николай входит. Подходит к жене."
    "Она стоит у окна, смотрит на забелённое известкой стекло."
 
    n "Сана... ты как?"
 
    al "Я молюсь, Ники. Всё время молюсь."
 
    n "Я знаю. Я тоже."
 
    "Он встаёт рядом. Оба смотрят на белое окно. За ним — темнота. Ни звёзд. Ни огней."
 
    n "Знаешь... я не жалею ни о чём."
 
    al "Даже о том, что отрёкся?"
 
    n "Особенно о том. Может быть, именно это и нужно было сделать. Чтобы мы оказались здесь. Вместе."
 
    "Она кладёт голову ему на плечо. Он обнимает её."
 
    "Тишина. Слышно, как за стеной ходит часовой."
    play music "audio/steps_guard.mp3" loop volume 0.2 fadein 2.0
    

 
    menu:
        "Кто произносит последнюю молитву перед сном?"
 
        "Николай":
            n "Господи, прими нас. Мы готовы."
            $ poslednyaya_molitva = "nikolay"
 
        "Александра":
            al "Пресвятая Богородица, спаси нас. Спаси детей моих."
            $ poslednyaya_molitva = "aleksandra"
 
        "Оба молча крестятся":
            "Николай и Александра молча крестятся на образ в углу."
            $ poslednyaya_molitva = "molchanie"
 
    "Лампа гаснет. Темнота."
    stop music fadeout 2.0
 
    jump noch_aleksey
 
    # СЦЕНА 4.1: ПРОБУЖДЕНИЕ
 
label noch_aleksey:
    scene bg parents
    with fade
    play music "audio/night.mp3" loop volume 0.2 fadein 2.0
 
    "01:30. Слабая луна пробивается сквозь забелённое окно."
    "Алексей спит беспокойно - нога ноет, подушка сбилась."
 
    play sound "audio/car_3.mp3"
    "Внезапно - гул. Нарастающий. Грузовик. Под самыми окнами."
 
    "Алексей резко садится. Сердце колотится."
 
    ax "Что это? Почему машина ночью?"
 
    "Никто не отвечает. За стеной — шаги. Не привычные, тяжёлые. Много пар."
 
    menu:
        "Что делает Алексей?"
 
        "Позвать маму":
            ax "Маменька..."
            $ aleksey_plachet = True
            "Страшно. Очень страшно. Хочется к маме..."
 
        "Сжать кулаки и молчать":
            "Алексей закусывает губу и садится ровно."
            $ aleksey_plachet = False
            "Но я же мужчина. Мне уже 13. Папа сказал, казаком буду."
 
    play sound "audio/knock_door.mp3"
    "Стук в дверь. Короткий, сухой."
 
    b "Ваше Императорское Высочество... простите, что бужу. Вас просят спуститься. В городе неспокойно."
 
    "Алексей смотрит на дверь. Нога болит. Он не зовёт на помощь. Он держится стойко."
 
    jump sbory
            
 
    # СЦЕНА: СБОРЫ
 
label sbory:
 
    scene bg night_room
    with fade
 
    "Комната девочек. Ольга зажигает лампу. Руки дрожат, но лицо спокойно."
 
    o "Мама, что происходит?"
 
    al "Не знаю, девочка. Одевайтесь теплее. Там подвал, наверное, холодно."
 
    "Татьяна хватает с кровати подушку — маленькую, в наволочке с вышитыми васильками."
 
    t "Я взяла подушку для Алексея. Ему жёстко сидеть."
 
    "Мария снимает с угла икону Спаса Нерукотворного. Заворачивает в платок."
 
    m "А я — икону. Маменька благословила."
 
    "Анастасия мечется по комнате, заглядывает под кровать, за шкаф."
 
    a "Я Джоя не нашла... Он где-то в доме бегает. Я не могу его бросить!"
 
    al "Оставь, Настя. Потом найдётся. Он умный. Он выживет."
 
    "Анастасия замирает. Смотрит на мать. Кивает. Берёт только платок."

 
    scene bg night
    with dissolve
 
    "Коридор."

    
if not inventory.has_item(7):
    "Анастасия замечает, что Алексей трогает шею."
    ax "Настя... Мой крестик. Я снял его на ночь и забыл надеть."
    a "Где он?"
    ax "На тумбочке... Но сейчас нельзя туда возвращаться!"
    
    menu:
        "Вернуться за крестиком":
            a "Я мигом!"
            "Анастасия выскальзывает из комнаты. Сердце колотится. Шаги охраны где-то рядом."
            "Она вбегает в комнату Алексея, хватает маленький серебряный крестик на тонком шнурке."
            ia "Это крестик, который бабушка подарила. Лёша никогда с ним не расставался."
            "Она выбегает обратно, пряча крестик в кулаке."
            "Охрана" "Куда пошла?! Быстро к остальным!"
            "Анастасия возвращается к семье, пряча руки за спиной."
            a "Лёша, держи."
            "Она надевает крестик на брата. Он улыбается."
            ax "Спасибо, Настя. Теперь я спокоен."
            $ inventory.add_item(7)
            play sound "audio/notify.mp3"

            $ all_items_collected = inventory.count_found() >= 7
            if all_items_collected:
                ia "У каждого из нас теперь есть что-то святое... Мы взяли с собой самое дорогое. Что бы ни случилось — мы не одни."
            
        "Отдать свой крестик":
            a "Лёша... Возьми мой."
            "Анастасия снимает с шеи свой крестик и надевает на брата."
            a "Он тебе нужнее. Иди."
            "Алексей сжимает в руке крестик сестры. На его глаза наворачиваются слёзы."
            ax "Спасибо, Настя. Я сохраню его."
            a "Я знаю. Ты сильный, Лёшенька."
            "Анастасия гладит брата по голове. Крестик ушёл, но на душе тепло."
            
        "Сказать, что крестик останется здесь, но вера всегда с ним":
            a "Лёша... Нельзя возвращаться. Охрана везде."
            ax "Но... бабушкин крестик..."
            a "Он останется здесь. Но ты носишь его в сердце. Помнишь, что бабушка говорила?"
            ax "Что Бог всегда со мной, даже если нет креста на шее."
            a "Правильно. Бог видит тебя. И бабушка видит. А крестик... Он будет ждать нас. Если мы вернёмся."
            ax "А если не вернёмся?"
            "Анастасия берёт брата за руку."
            a "Тогда он останется здесь, как напоминание. Что мы были. Что мы верили. Что мы - семья."
            "Алексей кивает. Слёзы текут по щекам, но он не плачет вслух."
            a "Идём. Мы вместе."
    
    n "Лёша, я понесу тебя. Обними за шею."
 
    "Николай поднимает сына на руки. Алексей худой, лёгкий. Слишком лёгкий."
 
    ax "Папа... я не боюсь."
 
    n "Я знаю, сынок. Я знаю."

    stop music fadeout 2.0
 
    if all_items_collected:
        scene bg stairs
        with dissolve

        "Николай останавливается на мгновение и обводит взглядом детей."
        "Все - Ольга, Татьяна, Мария, Анастасия, Алексей на руках - смотрят на него."

        n "Дети... Я хочу, чтобы вы знали. Что бы ни случилось - я горжусь вами. Всеми."

        "Александра подходит, встаёт рядом. Кладёт руку на плечо мужа."

        al "Мы вместе. Всегда вместе. Навсегда."

        "Тишина. Никто не плачет. Анастасия улыбается - нервно, но искренне."
        
        n "Ну же, выше нос дети! Давайте помолимся за наше благополучие..."
        # КРУТАЯ МОЛИТВА
        $ sekretny_dialog = True
    else:
        "Николай молчит. Только крестит детей в воздухе."
        "Александра шепчет «Идите за мной». И всё."
        $ sekretny_dialog = False
 
    scene black with fade
    "Семья наконец спустилась. В коридоре уже виднеются Юровский и четверо солдат с винтовками."
    
    g "Следуйте за мной. Без паники."
    
    play sound "audio/steps.mp3"
    "Все идут по коридору. Алексей на руках у отца. Мария прижимает икону к груди."

 
    jump podval
    
 
    # СЦЕНА: СПУСК
 
label podval:
 
    scene bg basement with fade
 
    "Полуподвал. Сыро. Пахнет известью и землёй."
    "Одна электрическая лампочка под потолком. Стены — крашеный тёмный бетон."
    "Решётка на единственном окне."
 
    "Семья заходит. 40 минут ожидания. Никто не садится на пол - только стоят, сбившись в кучу."
 
    "Александра оглядывается. В комнате - ни стула, ни скамьи."
    "Сдержано и гордо она обращается к Юровскому."
 
    al "Здесь нет стульев. Мой сын болен, ему нельзя стоять."
 
    "Юровский молчит несколько секунд. Кивает одному из охранников."
 
    g "Принесут."
 
    "Охранник выходит. Возвращается через минуту с двумя венскими стульями. Ставит посреди комнаты."
    play sound "audio/furniture.mp3"

    al "Садись, Лёшенька. Рядом со мной."
 
    "Александра садится на один стул. Алексей - на второй, справа от неё."
    "Николай встаёт за спиной жены. Девочки - рядом, вплотную."
 
    "Тишина. Тяжёлая, мокрая."
 
    a "Мария, у тебя икона с собой?"
 
    m "Да."
 
    "Мария разворачивает платок, показывает икону."
 
    a "Подержи, я тоже перекрещусь."
 
    "Мария держит икону перед сёстрами. Ольга, Татьяна, Мария, Анастасия по очереди касаются губами образа."
    "Алексей смотрит, но не двигается — нога болит."
 
    "Тем временем охрана суетиться. Кто-то постояно выходит, кто-то заходит, но рядом с семьёй всегда кто-то есть. Одних не оставляют."
 
    jump poslednie_slova
 
    # СЦЕНА: ПОСЛЕДНИЕ СЛОВА
 
label poslednie_slova:
    play sound "audio/steps.mp3"
    "Шаги за дверью. Много шагов."
 
    "Юровский входит первым. За ним — 8 человек: трое латышей, двое русских, остальные из ЧОП."
    "У всех маузеры. Один держит винтовку."
 
    "Юровский разворачивает лист бумаги. Голос — громкий, казённый."
 
    g "Внимание! Ввиду того, что ваши родственники продолжают наступление на Советскую Россию, Уральский исполком постановил расстрелять вас."
 
    "Николай слышит. Не сразу понимает. Поворачивается к семье — не к Юровскому."
 
    n "Что? Что?"
 
    "Юровский поднимает маузер."
 
    g "Вот что!"

    play sound "audio/shoot.mp3"
 
    "Первый выстрел — в упор, в Николая. Тело оседает."
 
    scene bg basement_kill with dissolve
    
    play music "audio/shooting.mp3" loop volume 0.4 fadein 2.0

    "Секунда — и звук взрывается. Выстрелы. Крики. Пыль."
 
    "Икона падает на пол. Подушка Алексея летит в угол."
    "Палачи стреляют беспорядочно. Те, кто подаёт признаки жизни, добиваются штыками."
 
    jump videnie_ohrannika
 
    # ВИДЕНИЕ ОХРАННИКА
 
label videnie_ohrannika:

    "Один из охранников — молодой, лет двадцати, с трясущейся винтовкой."
    "Сквозь дым и хаос он видит лица."
 
    g "Они не кричат. Они молятся. Даже дети."
 
    "Он видит Анастасию — она упала на колени, прижав руки к груди. Губы шевелятся."
 
    menu:
        "Что делает охранник?"
 
        "Отвернуться и зажать уши":
            "Охранник отворачивается, зажимает уши."
            g "Я не могу. Я не хотел. Простите, Господи..."
 
        "Смотреть до конца":
            "Охранник сжимает зубы. Смотрит. Запоминает каждое лицо."
            g "Я запомню всё. Каждое лицо. Чтобы потом... чтобы когда-нибудь рассказать."
 
        "Выстрелить в потолок":
            "Охранник поднимает маузер вверх."
            g "Я не буду в них стрелять. Пусть убьют меня."

            play sound "audio/shoot.mp3"
            "Выстрел гремит в тесном подвале. Кто-то кричит «Ты с ума сошёл!»"
 
    "Перед лицом мужчины образ невинной Анастасии. Она молится... но не за себя.. за них.. за тех, кто причиняет ей и её семье боль"
    a "Господи, прости им. Они не знают, что делают."
    
    stop music fadeout 2.0

    "Последние выстрелы. Тишина."

 
    jump posle
 
    # СЦЕНА: ПОСЛЕ
 
label posle:
 
    scene bg bad
    with fade
 
    play music "audio/night.mp3" loop volume 0.5 fadein 2.0
    
    play sound "audio/body.mp3" volume 0.2
    "Тела грузят в грузовик. Брезент. Ночь. Фары тусклые."
    
    show screen dog

    g "Собака воет. Та, рыжая, что всегда с мальчиком была. Зачем мы их... Зачем?"
 
    "Джой сидит у крыльца. Поднимает морду к небу. Воет. Долго."
 
    "Охранник не прогоняет."

    play sound "audio/car_2.mp3"
    
    "Мотор грузовика заводится. Рёв заглушает вой."
    "Грузовик уезжает в тёмную июльскую ночь..."
    hide screen dog
    stop music fadeout 2.0
    stop sound
 
    jump epilog
 
    # ЧАСТЬ: ЭПИЛОГ

label epilog: 
    $ original_overlay = config.overlay_screens.copy()
    hide screen quick_inventory
    $ config.overlay_screens = []
    $ _preferences.afm_enable = False
    $ quick_menu = False

    window hide
    
    scene black
    with fade
    play music "audio/end.mp3" loop fadein 2.0

 
    show text "16–17 июля 1918 года" with dissolve
    pause 2.0
    hide text with dissolve

    window show
 
    scene bg girl room
    with dissolve
    "Пустая комната девушек. Она навечно лишилась счастливого смеха."
 
    scene bg kitchen
    with dissolve
    "Кухня. Запачканный стол. Запах хлеба давно выветрился."
 
    scene bg garden
    with dissolve
    "Сад. Забор до неба. Ветер шевелит увядшую траву."
  
    scene bg bad
    with dissolve
    "Дом Ипатьева. Ночь. И мертвые тела в грузовике."

    $ config.overlay_screens = []
    $ _preferences.afm_enable = False
    $ quick_menu = False

    window hide
 
    scene black
    with fade
 
    show text "В ночь с 16 на 17 июля 1918 года\nв Екатеринбурге были расстреляны:" with dissolve
    pause 3.0
    hide text with dissolve
 
    show text "Император Николай Александрович — 50 лет" with dissolve
    pause 2.0
    hide text with dissolve
 
    show text "Императрица Александра Фёдоровна — 46 лет" with dissolve
    pause 2.0
    hide text with dissolve
 
    show text "Великая княжна Ольга Николаевна — 22 года" with dissolve
    pause 2.0
    hide text with dissolve
 
    show text "Великая княжна Татьяна Николаевна — 21 год" with dissolve
    pause 2.0
    hide text with dissolve
 
    show text "Великая княжна Мария Николаевна — 19 лет" with dissolve
    pause 2.0
    hide text with dissolve
 
    show text "Великая княжна Анастасия Николаевна — 17 лет" with dissolve
    pause 2.0
    hide text with dissolve
 
    show text "Цесаревич Алексей Николаевич — 13 лет" with dissolve
    pause 3.0
    hide text with dissolve
 
    show text "С ними погибли верные слуги:" with dissolve
    pause 2.0
    hide text with dissolve
 
    show text "Доктор Евгений Боткин" with dissolve
    pause 1.5
    hide text with dissolve
 
    show text "Камердинер Алексей Трупп" with dissolve
    pause 1.5
    hide text with dissolve
 
    show text "Повар Иван Харитонов" with dissolve
    pause 1.5
    hide text with dissolve
 
    show text "Горничная Анна Демидова" with dissolve
    pause 3.0
    hide text with dissolve
 
    if sekretny_dialog:
        show text "«Приидите ко Мне все труждающиеся\nи обремененные, и Я успокою вас»" with dissolve
        pause 4.0
        hide text with dissolve
 
    scene black
    with fade
 
    show text "В 1981 году Русская Православная Церковь за границей\nпричислила их к лику святых." with dissolve
    pause 3.0
    hide text with dissolve
 
    show text "В 2000 году Русская Православная Церковь\nканонизировала их как страстотерпцев." with dissolve
    pause 3.0
    hide text with dissolve
 
    show text "Их память — 17 июля." with dissolve
    pause 4.0
    hide text with dissolve
 
    scene black
    with fade
 
    show text "КОНЕЦ" with dissolve
    pause 3.0
    hide text with dissolve
    stop music fadeout 2.0
    $ config.overlay_screens = original_overlay

    $ renpy.full_restart()