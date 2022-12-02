def get_data():
    with open("../inputs/2.in", "r") as fp:
        updated_mapping = {'X':'R','Y':'P','Z':'S','A':'R','B':'P','C':'S'}
        return [[updated_mapping[val] for val in line.strip("\n").split(" ")] for line in fp]

def game_winner(opponent,user):
    return 3 if opponent == user else {'SR':6,'RP':6,'PS':6}.get(opponent+user,0)

def get_updated_shape(opponent,user):
    possible_user_updates = {'RR':'S','PR':'R','SR':'P','RP':'R','PP':'P',
                             'SP':'S','RS':'P','PS':'S','SS':'R'}
    return (opponent, possible_user_updates[opponent+user])

def get_final_score(data,modify_user_val=False):
    total_game_score = 0
    for (opponent,user) in data:
        if modify_user_val:
            opponent,user = get_updated_shape(opponent,user)
        user_val = {'R':1,'P':2,'S':3}[user]       
        game_result = game_winner(opponent,user)
        total_game_score += (user_val + game_result)
    return total_game_score

def main():
    rps_data = get_data()
    print(get_final_score(rps_data))
    print(get_final_score(rps_data,modify_user_val=True))

main()