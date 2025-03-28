#インポート

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
            {'名前':'青龍',
             'HP':150,
             '最大HP':150,
             '属性':'風',
             '攻撃力':15,
             '防御力':10,
             },
            {'名前':'朱龍',
             'HP':150,
             '最大HP':150,
             '属性':'火',
             '攻撃力':25,
             '防御力':10,
             },
            {'名前':'白虎',
             'HP':150,
             '最大HP':150,
             '属性':'土',
             '攻撃力':20,
             '防御力':5,
             },
            {'名前':'玄武',
             'HP':150,
             '最大HP':150,
             '属性':'水',
             '攻撃力':20,
             '防御力':15,
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
        max_hp += friend['最大HP']
        dp += friend['防御力']
    hp = max_hp
    dp = dp // len(friends)
    party = {
            'プレーヤー名':player_name,
            '味方モンスター':friends,
            'HP':hp,
            '最大HP':max_hp ,
            '防御力':dp,
            }
    return party

def show_party(party):
    print('<パーティ編成>------------------')
    for friend in party['味方モンスター']:
        name = friend['名前']
        hp = friend['HP']
        ap = friend['攻撃力']
        dp = friend['防御力']
        symbol = None
        color = None
        if friend['属性'] == '風':
            symbol = ELEMENT_SYMBOLS['風']
            color = ELEMENT_COLORS['風']
        elif friend['属性'] == '火':
            symbol = ELEMENT_SYMBOLS['火']
            color = ELEMENT_COLORS['火']
        elif friend['属性'] == '土':
            symbol = ELEMENT_SYMBOLS['土']
            color = ELEMENT_COLORS['土']
        else:
            symbol = ELEMENT_SYMBOLS['水']
            color = ELEMENT_COLORS['水']
        print(f'\033[3{color}m{symbol}{name}{symbol}\033[0m HP= {hp} 攻撃= {ap} 防御= {dp}')
    print('-------------------------------')
    print()

def go_dungeon(party,monster_list):
    kills = 0

    print(f'{party['プレーヤー名']}のパーティ(HP={party['HP']})はダンジョンに到着した')
    for monster in monster_list:
        kills += do_battle(monster)
        hp = party['HP']
        #hp=0
        if hp > 0:
            print(f'{party['プレーヤー名']}はさらに奥に進んだ')
            print('==================================')
        else:
            print(f'{party['プレーヤー名']}はダンジョンから逃げ出した')
            return kills

    print(f'{party['プレーヤー名']}はダンジョンを制覇した')
    return kills

def do_battle(monster):
    print_monster_name(monster)
    print('が現れた!')
    print_monster_name(monster)
    print('を倒した!')
    return 1

def print_monster_name(monster):
    symbol = ELEMENT_SYMBOLS[monster['element']]
    color = ELEMENT_COLORS[monster['element']]

    monster_name = monster['name']
    print(f'\033[3{color}m{symbol}{monster_name}{symbol}\033[0m',end='')

def on_player_turn(party,monster):
    print(f'【{party['プレーヤー名']}のターン】(HP={})')


def on_enemy_turn():


def do_battle():


def do_attack():

def do_enemy_attack():

main()
