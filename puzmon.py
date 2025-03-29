#インポート
import random
import math
#グローバル変数の宣言
ELEMENT_SYMBOLS = {
        '火':'$',
        '水':'~',
        '風':'@',
        '土':'#',
        '命':'&',
        '無':' ',
        }
ELEMENT_COLORS ={
        '火':1,
        '水':6,
        '風':2,
        '土':3,
        '命':5,
        '無':7,
        }
#関数宣言
def main():
    friends =[
            {'name':'青龍',
             'hp':150,
             'max_hp':150,
             'element':'風',
             'ap':15,
             'dp':10,
             },
            {'name':'朱龍',
             'hp':150,
             'max_hp':150,
             'element':'火',
             'ap':25,
             'dp':10,
             },
            {'name':'白虎',
             'hp':150,
             'max_hp':150,
             'element':'土',
             'ap':20,
             'dp':5,
             },
            {'name':'玄武',
             'hp':150,
             'max_hp':150,
             'element':'水',
             'ap':20,
             'dp':15,
             },
            ]
    monster_list = [
            {
            'name':'スライム',
            'hp':100,
            'max_hp':100,
            'element':'水',
            'ap':10,
            'dp':1
            },
            {
            'name':'ゴブリン',
            'hp':200,
            'max_hp':200,
            'element':'土',
            'ap':20,
            'dp':5
            },
            {
            'name':'オオコウモリ',
            'hp':300,
            'max_hp':300,
            'element':'風',
            'ap':30,
            'dp':10
            },
            {
            'name':'ウェアウルフ',
            'hp':400,
            'max_hp':400,
            'element':'風',
            'ap':40,
            'dp':15
            },
            {
            'name':'ドラゴン',
            'hp':600,
            'max_hp':600,
            'element':'火',
            'ap':50,
            'dp':20
            },
    ]
    while(True):
        player_name = input('プレーヤー名を入力して下さい>>')
        if len(player_name) > 0:
            break
        else:
            print('エラー プレイヤー名を入力してください')
    print('*** Puzzle & Monsters ***')
    party = organize_party(player_name,friends)
    show_party(party)
    kills = go_dungeon(party ,monster_list)
    if kills == len(monster_list):
        print('*** GAME CLEARED! ***')
        print(f'倒したモンスター数={kills}')
    else:
        print('*** GAME OVER! ***')
        print(f'倒したモンスター数={kills}')

def organize_party(player_name,friends):
    max_hp = 0
    dp = 0
    for friend in friends:
        max_hp += friend['max_hp']
        dp += friend['dp']
    hp = max_hp
    dp = dp // len(friends)
    party = {
            'name':player_name,
            'friends':friends,
            'hp':hp,
            'max_hp':max_hp ,
            'dp':dp,
            }
    return party

def show_party(party):
    print('<パーティ編成>------------------')
    for friend in party['friends']:
        name = friend['name']
        hp = friend['hp']
        ap = friend['ap']
        dp = friend['dp']
        symbol = None
        color = None
        if friend['element'] == '風':
            symbol = ELEMENT_SYMBOLS['風']
            color = ELEMENT_COLORS['風']
        elif friend['element'] == '火':
            symbol = ELEMENT_SYMBOLS['火']
            color = ELEMENT_COLORS['火']
        elif friend['element'] == '土':
            symbol = ELEMENT_SYMBOLS['土']
            color = ELEMENT_COLORS['土']
        else:
            symbol = ELEMENT_SYMBOLS['水']
            color = ELEMENT_COLORS['水']
        print(f'\033[4{color}m{symbol}{name}{symbol}\033[0m HP= {hp} 攻撃= {ap} 防御= {dp}')
    print('-------------------------------')
    print()

def go_dungeon(party,monster_list):
    kills = 0

    print(f'{party['name']}のパーティ(HP={party['hp']})はダンジョンに到着した')
    for monster in monster_list:
        kills += do_battle(party,monster)
        hp = party['hp']
        #hp=0
        if hp > 0:
            print(f'{party['name']}はさらに奥に進んだ')
            print('==================================')
        else:
            print(f'{party['name']}はダンジョンから逃げ出した')
            return kills

    print(f'{party['name']}はダンジョンを制覇した')
    return kills

def do_battle(party,monster):
    gems = fill_gems()
    print_monster_name(monster)
    print('が現れた!')
    while(True):
        if party['hp'] > 0:
            on_player_turn(party,monster,gems)
            if monster['hp'] <= 0:
                break
        if monster['hp'] > 0:
            on_enemy_turn(party,monster)
            if party['hp'] <= 0:
                print ('パーティのHPは0になった')
                return 0
    print_monster_name(monster)
    print('を倒した!')
    return 1

def print_monster_name(monster):
    symbol = ELEMENT_SYMBOLS[monster['element']]
    color = ELEMENT_COLORS[monster['element']]

    monster_name = monster['name']
    print(f'\033[4{color}m{symbol}{monster_name}{symbol}\033[0m',end='')

def on_player_turn(party,monster,gems):
    print(f'\n【{party['name']}のターン】(HP={party['hp']})')
    show_battle_field(party,monster,gems)
    com = input('コマンド?>')
    dmg = do_attack(party,monster,com)
    print(f'{dmg}のダメージを与えた')
    monster['hp'] -= dmg

def on_enemy_turn(party,monster):
    print(f'\n【 ', end ='')
    print_monster_name(monster)
    print(f'のターン】(HP={monster['hp']})')
    dmg =do_enemy_attack(party,monster)
    print(f'{dmg}のダメージを受けた')
    party['hp'] -= dmg

def do_attack(party,monster,com):
    dmg = math.floor(abs((hash(com) % 50)* random.uniform(0.9,1.1)))
    return dmg

def do_enemy_attack(party,monster):
    dmg = math.floor((monster['ap'] - party['dp']) * random.uniform(0.9,1.1))
    return dmg
    
def show_battle_field(party,monster,gems):
    print('バトルフィールド')
    print_monster_name(monster)
    print(f'HP = {monster['hp']} / {monster['max_hp']}' )
    print()
    for friend in party['friends']:
        print_monster_name(friend)
        print(' ',end='')
    print(f'HP = {party['hp']} / {party['max_hp']}')
    print('---------------------------')
    print('A B C D E F G H I J K L M N')
    print_gems(gems)
    print('---------------------------')

def fill_gems():
    temp = [random.randint(0,3) for _ in range(14)]
    gems = []
    for i in temp:
        if i == 0:
            gems.append('火')
        elif i == 1:
            gems.append('水')
        elif i == 2:
            gems.append('風')
        else:
            gems.append('土')
    return gems
def print_gems(gems):
    for gem in gems:
        symbol = ELEMENT_SYMBOLS[gem]
        color = ELEMENT_COLORS[gem]
        print(f'\033[4{color}m{symbol}\033[0m ' ,end='')
    print()


#main関数の呼び出し
main()
