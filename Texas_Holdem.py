import random
import json
from collections import Counter



# 定義一副撲克牌
Poker = tuple(['♣A','♣2','♣3','♣4','♣5','♣6','♣7','♣8','♣9','♣T','♣J','♣Q','♣K','♦A','♦2','♦3','♦4','♦5','♦6','♦7','♦8','♦9','♦T','♦J','♦Q','♦K','♥A','♥2','♥3','♥4','♥5','♥6','♥7','♥8','♥9','♥T','♥J','♥Q','♥K','♠A','♠2','♠3','♠4','♠5','♠6','♠7','♠8','♠9','♠T','♠J','♠Q','♠K'])


# 牌型字典
Poker_StraightFlush_Convert = json.load(open("Dictionary/Poker_StraightFlush_Convert"))
StraightFlush_List = [word for word, _ in Poker_StraightFlush_Convert.items()]
Poker_FourOfKind_Convert = json.load(open("Dictionary/Poker_FourOfKind_Convert"))
FourOfKind_List = [word for word, _ in Poker_FourOfKind_Convert.items()]
Poker_Fullhouse_Convert = json.load(open("Dictionary/Poker_Fullhouse_Convert"))
Poker_Fullhouse_list = [word for word, _ in Poker_Fullhouse_Convert.items()]
Poker_Flush_Convert = json.load(open("Dictionary/Poker_Flush_Convert"))
Poker_Flush_list = [word for word, _ in Poker_Flush_Convert.items()]
Poker_Straight_Convert = json.load(open("Dictionary/Poker_Straight_Convert"))
Poker_Straight_list = [word for word, _ in Poker_Straight_Convert.items()]
Poker_Three_Convert = json.load(open("Dictionary/Poker_Three_Convert"))
Poker_Three_list = [word for word, _ in Poker_Three_Convert.items()]
Poker_TwoPair_Convert = json.load(open("Dictionary/Poker_TwoPair_Convert"))
Poker_TwoPair_list = [word for word, _ in Poker_TwoPair_Convert.items()]
Poker_Pair_Convert = json.load(open("Dictionary/Poker_Pair_Convert"))
Poker_Pair_list = [word for word, _ in Poker_Pair_Convert.items()]
Poker_Single_Convert = json.load(open("Dictionary/Poker_Single_Convert"))



# 整理手牌順序
def Sort_Poker(poker_list):
    poker_sort_temp, poker_sort_list = [], []
    poker_sort_temp += [Poker_Single_Convert[poker] for poker in poker_list]
    poker_sort_temp.sort()
    poker_sort_list += [Poker_Single_Convert[str(poker_num)] for poker_num in poker_sort_temp]
    return poker_sort_list

# 洗牌
def Shuffle(Deck = 1):
    return random.sample(Poker * Deck, k=52 * Deck)

# 發牌
def Deal(Card_list, Card_all, poker_num):
    for _ in range(poker_num):
        Card_list.append(Card_all.pop(0))
    return Card_list, Card_all

# 排列組合出所有手牌
def Showing_Card(C7ard_list, Get_num=5):
    C7ard_list = Sort_Poker(C7ard_list)

    C7ard_all = []
    for i in range(len(C7ard_list) + 1 - Get_num):
        for j in range(i + 1, len(C7ard_list)):
            for k in range(j + 1, len(C7ard_list)):
                for l in range(k + 1, len(C7ard_list)):
                    for m in range(l + 1, len(C7ard_list)):
                        C7ard_all.append(C7ard_list[i] + C7ard_list[j] + C7ard_list[k] + C7ard_list[l] + C7ard_list[m])

    return best_card(C7ard_list, C7ard_all)


# 找出最強的牌型
def best_card(Orginal_Card, Card_list):

    Card_type = [False, False, False, False, False, False, False, False, False]

    if len(set(Card_list) & set(StraightFlush_List)) > 0:                               # Poker_StraightFlush
        best_card = list(set(Card_list) & set(StraightFlush_List))
        if len(best_card) > 1:
            best_value = [Poker_StraightFlush_Convert[card] for card in best_card]
            best_index = best_value.index(max(best_value))
            Card_type[0] = True
            return best_card[best_index], Poker_StraightFlush_Convert[best_card[best_index]], 'StraightFlush', False, Card_type
        Card_type[0] = True
        return best_card[0], Poker_StraightFlush_Convert[best_card[0]], 'StraightFlush', False, Card_type

    elif len(set(Card_list) & set(FourOfKind_List)) > 0:                                # Poker_FourOfKind
        best_card = list(set(Card_list) & set(FourOfKind_List))
        if len(best_card) > 1:
            best_value = [Poker_FourOfKind_Convert[card] for card in best_card]
            best_index = best_value.index(max(best_value))
            Card_type[1] = True
            return best_card[best_index], Poker_FourOfKind_Convert[best_card[best_index]], 'FourOfKind', False, Card_type
        Card_type[1] = True
        return best_card[0], Poker_FourOfKind_Convert[best_card[0]], 'FourOfKind', False, Card_type

    elif len(set(Card_list) & set(Poker_Fullhouse_list)) > 0:                           # Poker_Fullhouse
        best_card = list(set(Card_list) & set(Poker_Fullhouse_list))
        if len(best_card) > 1:
            best_value = [Poker_Fullhouse_Convert[card] for card in best_card]
            best_index = best_value.index(max(best_value))
            Card_type[2] = True
            return best_card[best_index], Poker_Fullhouse_Convert[best_card[best_index]], 'Fullhouse', False, Card_type
        Card_type[2] = True
        return best_card[0], Poker_Fullhouse_Convert[best_card[0]], 'Fullhouse', False, Card_type

    elif len(set(Card_list) & set(Poker_Flush_list)) > 0:                               # Poker_Flush
        best_card = list(set(Card_list) & set(Poker_Flush_list))
        if len(best_card) > 1:
            best_value = [Poker_Flush_Convert[card] for card in best_card]
            best_index = best_value.index(max(best_value))
            Card_type[3] = True
            return best_card[best_index], Poker_Flush_Convert[best_card[best_index]], 'Flush', False, Card_type
        Card_type[3] = True
        return best_card[0], Poker_Flush_Convert[best_card[0]], 'Flush', False, Card_type

    elif len(set(Card_list) & set(Poker_Straight_list)) > 0:                               # Poker_Straight
        best_card = list(set(Card_list) & set(Poker_Straight_list))
        if len(best_card) > 1:
            best_value = [Poker_Straight_Convert[card] for card in best_card]
            best_index = best_value.index(max(best_value))
            Card_type[4] = True
            return best_card[best_index], Poker_Straight_Convert[best_card[best_index]], 'Straight', False, Card_type
        Card_type[4] = True
        return best_card[0], Poker_Straight_Convert[best_card[0]], 'Straight', False, Card_type


    Card_convert = [(Poker_Single_Convert[card] - 1) // 4 for card in Orginal_Card]
    poker_counter = Counter(Card_convert)

    SameCard_num = poker_counter.most_common(1)[0][1]
    most_card = poker_counter.most_common(1)[0][0]

    most_card_index = []
    for i, card in enumerate(Card_convert):
        if card == most_card:
            most_card_index.append(i)

    most_card_all = ''
    for j in most_card_index:
        most_card_all += Orginal_Card[j]

    if SameCard_num == 3:
        Card_type[5] = True
        return most_card_all, Poker_Three_Convert[most_card_all], 'ThreeOfKind', True, Card_type

    elif poker_counter.most_common(2)[0][1] == poker_counter.most_common(2)[1][1] and poker_counter.most_common(2)[0][1] == 2:
        if poker_counter.most_common(3)[2][1] == 2:
            TwoPair1_num = poker_counter.most_common(3)[1][0]
            TwoPair2_num = poker_counter.most_common(3)[2][0]
        else:
            TwoPair1_num = poker_counter.most_common(2)[0][0]
            TwoPair2_num = poker_counter.most_common(2)[1][0]

        TwoPair_card_index = []
        for i, card in enumerate(Card_convert):
            if card == TwoPair1_num or card == TwoPair2_num:
                TwoPair_card_index.append(i)

        TwoPair_card_all = ''
        for j in TwoPair_card_index:
            TwoPair_card_all += Orginal_Card[j]

        Card_type[6] = True
        return TwoPair_card_all, Poker_TwoPair_Convert[TwoPair_card_all], 'Two Pair', True, Card_type

    elif SameCard_num == 2:
        Card_type[7] = True
        return most_card_all, Poker_Pair_Convert[most_card_all], 'Pair', True, Card_type

    else:
        Card_type[8] = True
        return Orginal_Card[-1], Poker_Single_Convert[Orginal_Card[-1]], 'Zilch', True, Card_type



# 牌型平手的情況下比最大的牌
def Draw_Game(Player1_Card, Player2_Card, game_Win, game_Lose, game_Draw):
    Player1_Card = Sort_Poker(Player1_Card)
    Player2_Card = Sort_Poker(Player2_Card)

    for i in range(5):
        if Poker_Single_Convert[Player1_Card[-1-i]] > Poker_Single_Convert[Player2_Card[-1-i]]:
            print('Player Wins!')
            game_Win += 1
            return game_Win, game_Lose, game_Draw
        elif Poker_Single_Convert[Player1_Card[-1-i]] < Poker_Single_Convert[Player2_Card[-1-i]]:
            print('Player Lose...')
            game_Lose += 1
            return game_Win, game_Lose, game_Draw
        elif Poker_Single_Convert[Player1_Card[-1-i]] == Poker_Single_Convert[Player2_Card[-1-i]] and i == 4:
            print('Chop_Game')
            game_Draw += 1
            return game_Win, game_Lose, game_Draw


def main():
    Player_Card, Opponent_Card, Flop_Card = [], [], []
    Shuffle_Poker = Shuffle(Deck = 1)

    Player_Card, Shuffle_Poker = Deal(Player_Card, Shuffle_Poker, 2)
    Opponent_Card, Shuffle_Poker = Deal(Opponent_Card, Shuffle_Poker, 2)
    Flop_Card, Shuffle_Poker = Deal(Flop_Card, Shuffle_Poker, 5)

    print('Player Card:{}'.format(Player_Card))
    print('Opponent Card:{}'.format(Opponent_Card))
    print('Flop Card:{}'.format(Flop_Card))
    print('--------------------------------------------------------------------------------------------------------------------------')

    Player_showing = Showing_Card(Sort_Poker(Player_Card + Flop_Card))
    Opponent_showing =  Showing_Card(Sort_Poker(Opponent_Card + Flop_Card))

    print('Player showing: {}'.format(Player_showing[0]), Player_showing[2])
    print('Opponent showing: {}'.format(Opponent_showing[0]), Opponent_showing[2])

    print('--------------------------------------------------------------------------------------------------------------------------')
    if Player_showing[1] > Opponent_showing[1]:
        print('Player Win!')
    elif Player_showing[1] < Opponent_showing[1]:
        print('Player Lose...')
    elif Player_showing[1] == Opponent_showing[1] and Player_showing[3] and Opponent_showing[3]:
        print('OT')
        Draw_Game(Player_Card + Flop_Card, Opponent_Card + Flop_Card, 0, 0, 0)
    elif Player_showing[1] == Opponent_showing[1] and Player_showing[3] == False and Opponent_showing[3] == False:
        print('Draw')


def Backtesting_2Player(Player_Card, Opponent_Card, Flop_Card, Player_Win, Player_Lose, Player_Draw, Card_Type):

    Shuffle_Poker = Shuffle(Deck=1)

    for p_poke in Player_Card:Shuffle_Poker.remove(p_poke)
    for o_poke in Opponent_Card:Shuffle_Poker.remove(o_poke)
    for f_poke in Flop_Card:Shuffle_Poker.remove(f_poke)

    for _ in range(2-len(Player_Card)):
        Player_Card.append(Shuffle_Poker.pop(0))
    for _ in range(2-len(Opponent_Card)):
        Opponent_Card.append(Shuffle_Poker.pop(0))
    for _ in range(5-len(Flop_Card)):
        Flop_Card.append(Shuffle_Poker.pop(0))

    print('Player Card:{}'.format(Player_Card))
    print('Opponent Card:{}'.format(Opponent_Card))
    print('Flop Card:{}'.format(Flop_Card))

    Player_showing = Showing_Card(Sort_Poker(Player_Card + Flop_Card))
    Opponent_showing = Showing_Card(Sort_Poker(Opponent_Card + Flop_Card))

    print('Player showing: {}'.format(Player_showing[0]), Player_showing[2])
    print('Opponent showing: {}'.format(Opponent_showing[0]), Opponent_showing[2])
    print('')
    # print('--------------------------------------------------------------------------------------------------------------------------')


    if Player_showing[1] > Opponent_showing[1]:
        print('Player Win!')
        Player_Win += 1
    elif Player_showing[1] < Opponent_showing[1]:
        print('Player Lose...')
        Player_Lose += 1
    elif Player_showing[1] == Opponent_showing[1] and Player_showing[3] and Opponent_showing[3]:
        print('OT', end='')
        Player_Win, Player_Lose, Player_Draw = Draw_Game(Player_Card + Flop_Card, Opponent_Card + Flop_Card, Player_Win, Player_Lose, Player_Draw)

    elif Player_showing[1] == Opponent_showing[1] and Player_showing[3] == False and Opponent_showing[3] == False:
        Player_Draw += 1
        print('Draw')

    for type_i in range(len(Player_showing[4])):
        if Player_showing[4][type_i]:Card_Type[type_i] += 1

    return Player_Win, Player_Lose, Player_Draw, Card_Type


def Backtesting_main(Player_Card, Opponent_Card, Flop_Card, round_num = 100000):

    round_Win, round_Lose, round_Draw, Card_Type = 0, 0, 0, [0, 0, 0, 0, 0, 0, 0, 0, 0]             # 紀律勝負與牌型次數總和

    for _ in range(round_num):
        round_Win, round_Lose, round_Draw, Card_Type = Backtesting_2Player(Player_Card.copy(), Opponent_Card.copy(), Flop_Card.copy(), round_Win, round_Lose, round_Draw, Card_Type)
        print('==========================================================================================================================')
    print('Win odds:{}% |'.format(round(round_Win/round_num*100, 2)), 'Chop odds:{}% |'.format(round(round_Draw/round_num*100, 2)), 'Lose odds:{}%'.format(round(round_Lose/round_num*100, 2)))
    print('FlushStraight : {}% |'.format(round(Card_Type[0]/round_num*100, 2)), 'Four : {}% |'.format(round(Card_Type[1]/round_num*100, 2)),'Fullhouse : {}% |'.format(round(Card_Type[2]/round_num*100, 2)),'Flush : {}% |'.format(round(Card_Type[3]/round_num*100, 2)), 'Straight : {}% |'.format(round(Card_Type[4]/round_num*100, 2)), 'Three : {}% |'.format(round(Card_Type[5]/round_num*100, 2)), '2Pair : {}% | '.format(round(Card_Type[6]/round_num*100, 2)), 'Pair : {}% | '.format(round(Card_Type[7]/round_num*100, 2)), 'Single : {}%'.format(round(Card_Type[8]/round_num*100, 2)))



if __name__ == "__main__":
    player_card, Opponent_Card, Flop_Card = ['♥A', '♠A'], ['♥K', '♠K'], []                          # 定義自己手牌, 對手手牌, 公用牌
    Backtesting_main(Player_Card=player_card, Opponent_Card=[], Flop_Card=[], round_num=10000)       # 回測一萬組