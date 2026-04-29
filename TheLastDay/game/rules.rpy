screen bezik_rules():
    modal True
    zorder 200
    add Solid("#00000080")
    
    frame:
        background Transform("images/rules_paper.png", size=(900, 950))
        xalign 0.5
        yalign 0.5
        xsize 900
        ysize 950
        
        vbox:
            spacing 10
            xalign 0.5
            yalign 0.5
            xsize 800
            
            text "Наш безик. Заметка на память.":
                size 30
                color "#2c1e0e"
                font "fonts/GreatVibes.ttf"
                xalign 0.5
            
            text "Папа говорит, что в безик играли ещё при прабабушке. Карты старые, потрёпанные, но мы их бережём.":
                size 20
                color "#2c1e0e"
                xalign 0.5
            
            text "Что нам нужно:":
                size 24
                color "#2c1e0e"
                font "fonts/GreatVibes.ttf"
                xalign 0.5
            
            text "Колода из 32 карт — от семёрок до тузов. В каждом новом раунде папа тасует заново, чтобы никто не жаловался на удачу.":
                size 20
                color "#2c1e0e"
                xalign 0.5
            
            text "Старшинство (кто кого бьёт):":
                size 24
                color "#2c1e0e"
                font "fonts/GreatVibes.ttf"
                xalign 0.5
            
            text "Туз — 11 очков\nДесятка — 10 очков\nКороль — 4 очка\nДама — 3 очка\nВалет — 2 очка\nСемёрка, восьмёрка, девятка — 0 очков, но в них своя хитрость…":
                size 20
                color "#2c1e0e"
                xalign 0.5
            
            text "Как играем:":
                size 24
                color "#2c1e0e"
                font "fonts/GreatVibes.ttf"
                xalign 0.5
            
            text "Ходим по очереди. Заходить в ту же масть, что и соперник, совсем не обязательно — папа говорит, это не козыри. Взятку забирает тот, у кого карта старше. А если кто-то сходил козырем — он и забирает.\n\nЗа каждую взятку — 10 очков. Мы с мамой часто считаем вслух, чтобы не запутаться.":
                size 20
                color "#2c1e0e"
                xalign 0.5
            
            text "Особые комбинации (объявляй, когда твой ход):":
                size 24
                color "#2c1e0e"
                font "fonts/GreatVibes.ttf"
                xalign 0.5
            
            text "• Безик (дама пик + валет треф) — 40 очков\n• Марьяж (король + дама одной масти) — 20 очков\n• Каре (4 одинаковые карты) — 100 очков\n• Сотня (десятка всех четырёх мастей) — 100 очков":
                size 20
                color "#2c1e0e"
                xalign 0.5
            
            text "Сколько играем:":
                size 24
                color "#2c1e0e"
                font "fonts/GreatVibes.ttf"
                xalign 0.5
            
            text "Три раунда. Потом считаем сумму очков. Кто больше — тот и молодец. Иногда мама уступает папе, а иногда папа — маме. Но мы знаем, что главное — не выигрыш, а время, проведённое вместе.\n\nДопишу потом. Пора ужинать.\n\nА.Р.":
                size 20
                color "#2c1e0e"
                xalign 0.5
        
        imagebutton:
            idle Transform("images/inventory/wax_seal.png", size=(100,100))
            hover Transform("images/inventory/wax_seal_dark.png", size=(100,100))
            action Hide("bezik_rules")
            xalign 0.95
            yalign 0.95