import random

period1 = ['HYDROGEN', 'HELIUM']
period2 = ['LITHIUM', 'BERYLLIUM', 'BORON', 'CARBON', 'NITROGEN', 'OXYGEN', 'FLUORINE', 'NEON']
period3 = ['SODIUM', 'MAGNESIUM', 'ALUMINIUM', 'SILICON', 'PHOSPHORUS', 'SULFUR', 'CHLORINE', 'ARGON']
period4 = ['POTASSIUM', 'CALCIUM', 'SCANDIUM', 'TITANIUM', 'VANADIUM', 'CHROMIUM', 'MANGANESE', 'IRON', 'COBALT',
           'NICKEL', 'COPPER', 'ZINC', 'GALLIUM', 'GERMANIUM', 'ARSENIC', 'SELENIUM', 'BROMINE', 'KRYPTON']
period5 = ['RUBIDIUM', 'STRONTIUM', 'YTTRIUM', 'ZIRCONIUM', 'NIOBIUM', 'MOLYBDENUM', 'TECHNETIUM', 'RUTHENIUM',
           'RHODIUM', 'PALLADIUM', 'SILVER', 'CADMIUM', 'INDIUM', 'TIN', 'ANTIMONY', 'TELLURIUM', 'IODINE', 'XENON']
period6 = ['CAESIUM', 'BARIUM', 'LUTETIUM', 'HAFNIUM', 'TANTALUM', 'TUNGSTEN', 'RHENIUM', 'OSMIUM', 'IRIDIUM',
           'PLATINUM', 'GOLD', 'MERCURY', 'THALLIUM', 'LEAD', 'BISMUTH', 'POLONIUM', 'ASTATINE', 'RADON']
period6_f = ['LANTHANUM', 'CERIUM', 'PRASEODYMIUM', 'NEODYMIUM', 'PROMETHIUM', 'SAMARIUM', 'EUROPIUM', 'GADOLINIUM',
             'TERBIUM', 'DYSPROSIUM', 'HOLMIUM', 'ERBIUM', 'THULIUM', 'YTTERBIUM']
period7 = ['FRANCIUM', 'RADIUM', 'LAWRENCIUM', 'RUTHERFORDIUM', 'DUBNIUM', 'SEABORGIUM', 'BOHRIUM', 'HASSIUM',
           'MEITNERIUM', 'DARMSTADTIUM', 'ROENTGENIUM', 'COPERNICIUM', 'NIHONIUM', 'FLEROVIUM', 'MOSCOVIUM',
           'LIVERMORIUM', 'TENNESSINE', 'OGANESSON']
period7_f = ['ACTINIUM', 'THORIUM', 'PROTACTINIUM', 'URANIUM', 'NEPTUNIUM', 'PLUTONIUM', 'AMERICIUM', 'CURIUM',
             'BERKELIUM', 'CALIFORNIUM', 'EINSTEINIUM', 'FERMIUM', 'MENDELEVIUM', 'NOBELIUM']

element = period1 + period2 + period3 + period4 + period5 + period6 + period6_f + period7 + period7_f
element_group = [period1, period2, period3, period4, period5, period6, period6_f, period7, period7_f]

group_hint = ['Chu kì 1', 'Chu kì 2', 'Chu kì 3', 'Chu kì 4', 'Chu kì 5', 'Chu kì 6', 'Nguyên tố f chu kì 6',
              'Chu kì 7', 'Nguyên tố f chu kì 7']

hangman = ['💀', '😧', '😐', '🙂', '😀', '😄', '😆']

print('Ánh đang cần tìm nguyên tố hoá học phù hợp để làm lab.\nHãy giúp ánh tìm, tìm sai 6 lần là cook 💀💀💀')


def hint_giving():
    hint = ''
    for char_hint in element_group:
        char_hint = word
        hint_position = element_group.index(char_hint)
        hint = group_hint[hint_position]
    print(f'Bạn còn một lần sai.\nGợi ý: Nguyên tố của bạn thuộc {hint}\n')


restart = True
while restart:
    word = random.choice(element)
    lives = 6

    display = []
    for _ in range(len(word)):
        display += '_'

    end = False

    while not end:
        letter = input('\nĐoán chữ đi: ').upper()

        if letter in display:
            print(f'Chữ {letter} đoán rồi mà? Ánh cook 1 mạng!')
            lives -= 1

        for position in range(len(word)):
            char = word[position]
            if char == letter:
                print('Ăn may hay đấy ')
                display[position] = char

        if letter not in word:

            lives -= 1
            print(f'Hehe, chữ {letter} không có nha, Ánh sắp cook rồi... :<')
            if lives == 0:
                end = True
                print(f'\nThua rồi, há há\nÁnh đã lấy lộn chất và cook\nChất cần tìm là {word}')
            elif lives == 1:
                hint_giving()
        print(f"{' '.join(display)}")

        if "_" not in display:
            end = True
            print('Cảm ơn bạn vì đã giúp Ánh không nấu trong lab ♥️')

        print(hangman[lives])
    again = input('Bạn có muốn chơi lại? (Y/N)\n').lower()
    if again == 'n':
        restart = False
        print('Tạm biệt! Khi nào rảnh ghé chơi!')
