#インポート

#グローバル変数の宣言

#関数宣言
def main():
    player_name = input('プレーヤー名を入力して下さい>>')
    print('*** Puzzle & Monsters ***')
    kills = go_dungeon(player_name)
    print('*** GAME CLEARED ***')
    print(f'倒したモンスター数={kills}')

def go_dungeon(player_name):
    print(f'{player_name}はダンジョンに到着した')
    print(f'{player_name}はダンジョンに制覇した')
    return 5 
main()
