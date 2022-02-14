﻿# Вы можете расположить сценарий своей игры в этом файле.

# Определение персонажей игры.
define pr = Character('', color="#fdfdfd", image='')
define radio = Character('', color="#000000", image='radio', window_ysize= 0.44, what_xpos=0.3, what_ypos=0.55, who_ypos=50)
define br = Character('', color="#000000", image='br', window_ysize= 0.44, what_xpos=0.3, what_ypos=0.55, who_ypos=50)
define si = Character('', color="#000000", image='si', window_ysize= 0.44, what_xpos=0.3, what_ypos=0.55, who_ypos=50)
define th = Character(' ',what_color="#ffffff", what_radioefix="~", what_suffix="~", image='si', window_ysize= 0.44, what_xpos=0.3, what_ypos=0.55, who_ypos=50)
define robo = Character('', color="#000000", image='robo', window_ysize= 0.44, what_xpos=0.3, what_ypos=0.55, who_ypos=50)
define tv1 = Character('', color="#000000", image='')
define tv2 = Character('', color="#000000", image='')
define fl1 = Character('', color="#000000", image='')
define fl2 = Character('', color="#000000", image='')
define fl3 = Character('', color="#000000", image='')
$ centered = Character(None, xalign=0.5, yalign=0.5)
# Вместо использования оператора image можете просто
# складывать все ваши файлы изображений в папку images.
# Например, сцену bg room можно вызвать файлом "bg room.png",
# а eileen happy — "eileen happy.webp", и тогда они появятся в игре.

image street_animated:
    "street1.png"
    pause 0.2
    "street2.png"
    pause 0.2
    "street3.png"
    pause 0.2
    "street4.png"
    pause 0.2
    "street5.png"
    pause 0.2
    "street6.png"
    pause 0.2
    "street7.png"
    pause 0.2
    "street8.png"
    pause 0.2
    "street9.png"
    pause 0.2
    "street10.png"
    pause 0.2
    "street11.png"
    pause 0.2
    repeat


image robot_animated:
    "robot_walks1.png"
    pause 1.0
    "robot_walks2.png"
    pause 1.0
    "robot_walks3.png"
    pause 1.0
    "robot_walks4.png"
    pause 1.0
    "robot_walks5.png"
    pause 1.0
    "robot_walks6.png"
    pause 1.0
    repeat

# Игра начинается здесь:
label start:

    stop music

    stop audio

    stop sound

    scene black

    centered "Кажется, оно наконец-то работает."

    centered "Несколько лет спустя."

    play music [ "audio/Drowsy.wav", "audio/Street.wav", "audio/Leaf.wav"] fadeout 5.0 fadein 5.0 volume 0.6

    show street_animated with dissolve:
        yalign .275 subpixel True
        xalign .5 subpixel True

    pr "Сколько я себя помню, ответственность за заботу о младшем брате живет со мной бок о бок."
    pr "Отличаясь от рутины других детей, наша состояла в бесконечном чередовании работы и перемещений, приправленных периодическими радостями, способными показаться кому-то незначительными."
    pr "Возвращаясь домой, мы ежедневно проходили мимо закусочной, прислушиваясь к стоящему на ее прилавке радио, в надежде выцепить что-то интересное для обсуждения перед сном."
    pr "Однажды мы стали свидетелями диалога, не оставившего нас равнодушными."

    pr "Нашей студии удалось пообщаться с научным руководителем инновационного проекта по разработке многофункциональной разведывательно-проектировочной машины."
    pr "Успешный ввод в эксплуатацию которой изменит представление о разработке и строительстве инфраструктуры промышленных масштабов."
    pr "Здравствуйте. Расскажите, пожалуйста, поподробнее о вашем проекте."
    pr "Здравствуйте, мы разрабатываем автономного робота для помощи в изучении местности и дальнейшем строительстве в труднодоступных местах."
    pr "Можете рассказать, что в вашем роботе уникально?."
    pr "В роботе установлена новейшая нейронная сеть. Будучи результатом многолетнего труда лучших умов современности..."
    pr "...она способна к быстрому самообучению и практически идеальному воспроизведению человеческого мышления."
    pr "Сочетание умений с информационным фондом, которым оснащена эта машина, открывает перед нами возможности..."
    pr "...О масштабах которых нам остаётся только с энтузиазмом догадываться"
    pr "Звучит многообещающе. Когда мы сможем увидеть машину в действии?"
    pr "Это пока неизвестно, разработка находится на стадии тестирования. Мы периодически устраиваем испытания в условиях, приближенных к реальным."
    pr "Как только мы будем готовы поделиться результатами нашей работы, об этом станет официально известно."
    pr "Ясно. Большое спасибо, что согласились побеседовать с нами."
    pr "Далее в эфире..."

    br "Прикольный робот."
    si "Ага, даже не верится в существование подобного."
    br "Хотела бы взглянуть на него?"
    si "Да, интересно ведь."
    br "Скорее бы домой."
    si "Скоро будем, потерпи еще немного."

    hide street_animated with dissolve

    centered "Уже через некоторое время мы оказались дома. Небольшое укромное пространство, облагороженное детскими руками, обладало незаменимым уютом, скрашивающим конец очередного трудового дня. Мне было невероятно приятно, когда он называл это место домом." with dissolve
    centered "Утро" with dissolve
    centered "Проснувшись, мы с удивлением обнаружили, что привычный нам уличный вид был обогащен появившейся механической махиной, шумно перебирающей свои массивные ноги. Как сразу стало для нас очевидно, этим гостем стал тот самый робот, о существовании которого мы узнали буквально вчера." with dissolve

    show robot_animated with dissolve:
        yalign .275 subpixel True
        xalign .5 subpixel True

    br "Смотри!"
    si "Да… Я вижу"

    pr "Не успела я опомнится, как малой рванул навстречу механическому шкафу. Уже скоро мы оказались внутри большого ожившего холодильника." with dissolve
    pr "Одухотворенные происходящим, мы отправились в неизвестный путь, не побоявшись возможных последствий."

    si "Ты с ума сошел? Ты хоть на секунду задумался об \nопасности происходящего?"
    br "..."
    si "Ладно уже, будь, что будет. Сойдем с него при \nпервой же возможности."
    br "Договорились. Только давай осмотримся."
    si "Давай. Только будет аккуратен."
    br "Да-да, я понял."

    pr "Всяческое техническое наполнение этой машины, видневшееся изнутри, поражало воображение." with dissolve
    pr "Освоившись, как уже думали, за некоторое время в пути, мы с удивлением обнаружили для себя существование спальных мест, оборудования, о назначении которого нам не было известно и, конечно, еды."
    pr "Присутствующие здесь условия поездки окончательно сформировали у меня ассоциацию об этом месте как о какой-то смеси часовой башни и дома на колёсах."
    pr "Теперь, нам осталось лишь ждать, с интересом гадая о пользе тех или иных находок."

    pr "Успев обжиться в необычайно интересном для нас месте, мы успели забыть о столь ожидаемой возможности сойти и отправится в направлении нашего дома."
    pr "Поездка затянулась на более длительное время, чем можно было предположить. По ощущениям, наше незапланированное путешествие насчитывало уже почти сутки."
    pr "Начав волноваться об отдаленности от дома, мы заметили, что наш дом на ножках начал замедлять свой тяжелый ход."
    pr "Воспользовавшись шансом, мы спустились и принялись изучать местность, чем, похоже, занялось и доставившее нас сюда чудо техники, о чём свидетельствовала смена цвета горящего ока с желтого на красный."
    pr "Отойдя недалеко от «транспорта» и побродив в тщетных попытках нахождения обратного пути, мы поняли, что лучшим решением будет сдача в «металлический плен» нашего инновационного друга."

    pr "Вернувшись, нами с успокоением был обнаружен все тот же металлический шкаф, ставший для нас теперь олицетворением безопасности и, как тогда думали, билетом домой."
    pr "С опаской подобравшись ближе, мы решились подойти к нему спереди, чтоб дать о себе знать."
    pr "Горящий красным глаз вновь сменил цвет на уже привычный желтый, блик от которого, подобно зрачку, обратил «взгляд» робота на нас."

    robo "..."
    si "..."
    br "..."

    si "Здравствуйте, мы тут, как бы сказать… \nпотерялись. Не могли бы вы нам помочь?"
    pr "Внезапное появление непредусмотренных программой препятствий заставило механического гиганта «задуматься»."
    pr "Внезапно раздавшийся синтезированный голос, заставил нас усомниться в реальности происходящего."

    robo "Располагайтесь в зоне для персонала, по \nзавершении моей программы и возвращении \nв пункт отправления, вам будут даны \nдальнейшие инструкции."
    si "Хорошо, спасибо"

    pr "Приняв предложение нашего нового механического друга, мы вновь расположились в уже знакомом нам месте, оказавшимся зоной для транспортировки и отдыха персонала."
    pr "Немного волнуясь о своей дальнейшей судьбе, мы решили скрасить долгую поездку разговорами, напоминающими нам о доме."
    pr "Готовившись ко сну, мы случайным образом обнаружили, что можем взаимодействовать с роботом изнутри, однако продолжительные беседы со столь необычным собеседником."
    pr "На удивление, не принесли нам много сведений, показавшихся бы ребенку интересными."
    pr "Как выяснилось, машина совсем ничего не помнила о своей «жизни», а память начинает свой отсчет с момента выхода на задание."
    pr "Следующий день не заставил себя долго ждать. Как и последующие, он был наполнен живописными видами и изучением убранства нашего временного дома."
    pr "Единственное, чем отличился этот день – оползни, заставившие нас «потанцевать» в попытках за что-то ухватиться и удержать равновесие."
    pr "Мы, лишь свалившись на что-то твердое, обнаружили существование, должно быть, важного компьютера."
    pr "Об этом сигнализировали надписи «Разблокировка модуля памяти» и «Модуль синтеза речи». Как мы тогда подумали, это не возымело никаких последствий."
    hide robot_animated with dissolve
    centered "По словам нашего лязгающего друга, во время последнего вхождения в режим анализа, он видел изображения и слышал звуки, несоответствующие происходящему."
    centered "Из его рассказа можно было сделать вывод, что это было что-то вроде обычного человеческого сна. Но это же машина."
    centered "Неужели возможности искусственного интеллекта настолько широки и не изучены, что нам остается только пожимать плечами в догадках о природе подобных явлений."
    centered "Содержание этого «сна» было примерно следующим:"
    centered "Кажется, оно наконец-то работает."
    centered "Серьёзно, заработало?!"
    centered "Мы уже несколько лет пытались заставить это заработать."
    centered "Неужели, на моём веку случится такой прорыв."
    centered "Люди в халатах долго обсуждали, то, что создали спустя годы бессонных ночей и выгораний. Они, сломленные бесконечно неудачными попытками, создали нечто грандиозное, что изменит не только их жизнь, но и жизнь всего мира. Ученый, который заставил работать это, зажёг сигарету и снова произнёс:"
    centered "Кажется, оно наконец-то работает."

    show robot_animated with dissolve:
        yalign .275 subpixel True
        xalign .5 subpixel True

    pr "Последствия непреднамеренного вторжения в «мозг» нашего друга заставили программу запустить диагностику, с целью выявления и устранения неполадок."
    pr "Пробыв в роботе примерно неделю, обстановка начала понемногу меняться, причиной чему стал периодически возникающий у робота интерес к нам."
    pr "Он начал с нами разговаривать, пока ехал до необходимого места, тем самым разряжая обстановку и поднимая нам настроение."
    pr "Нам оставалось только догадываться, чем объяснить возникшую человечность, до этого не присущую машине."

    pr "Позже мы с братом заметили еще большие странности в поведении нашего «дома»."
    pr "Будучи идеально выдержанной и не колеблющейся, синтезированная речь приобрела характерную человеку интонацию."
    pr "Насторожив нас, подобный факт заставил провести еще одну диагностику и дальнейшую беседу, из которой нам стало известно об еще одном «сне», содержание которого наш друг не собирался нам раскрывать."
    pr "Он лишь упомянул, что на этот раз перед ним предстали двое совсем маленьких детей, чем-то похожих на нас."
    pr "Будто волнуясь, машина поставила нас перед фактом о том, что она вспомнила свое прошлое."
    pr "Не обычное прошлое, присущее машине, а прошлое, навсегда изменившее наше настоящее и будущее."
    pr "Как оказалось, перед нами предстало не чудо искусственного интеллекта, а человек, чье сознание было заперто в холодном металлическом теле."
    pr "Не способные поверить в данный факт, мы вынуждены были столкнуться с еще большим откровением."
    pr "По признанию нашего друга стало известно, что мы были знакомы при его жизни."

    stop music
    play music "audio/Return.wav" loop volume 0.6 fadein 10.0 fadeout 10.0

    pr "Неожиданно для нас он напел колыбельную, так хорошо знакомую нам. "
    pr "Возникшая ситуация не вызвала бы такую совокупность эмоций, если бы не тот факт, что эту колыбельную сочинил и напевал для нас наш ныне покойный отец… "


    pr "Совместное осознание столь непростой и душераздирающей ситуации стало не единственным выпавшим на тот день испытанием."
    pr "Он просил нас выполнить простую комбинацию действий, способную прекратить работу его «мозга», дарую ему освобождение и последний день его бесконечного заточения в этой метафизической тюрьме."
    hide robot_animated with dissolve
    centered "Это был его последний день..."
    return
