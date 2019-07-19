import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

def print_debug(*str):
    print(*str, file=sys.stderr)

# game loop
while True:
    my_score = int(input())
    enemy_score_1 = int(input())
    enemy_score_2 = int(input())
    my_rage = int(input())
    enemy_rage_1 = int(input())
    enemy_rage_2 = int(input())
    unit_count = int(input())
    
    player_info = {}
        
    water = []
    tankers = []
    
    other_veh = []
    
    all_info = {}
    
    for i in range(unit_count):
        unit_id, unit_type, player, mass, radius, x, y, vx, vy, extra, extra_2 = input().split()
        unit_id = int(unit_id)
        unit_type = int(unit_type)
        player = int(player)
        mass = float(mass)
        radius = int(radius)
        x = int(x)
        y = int(y)
        vx = int(vx)
        vy = int(vy)
        extra = int(extra)
        extra_2 = int(extra_2)
        
        # print_debug(unit_id, unit_type, player, mass, radius, x, y, vx, vy, extra, extra_2)
        
        if (player == 0) & (unit_type == 0): # My reaper
            player_info['x']=x
            player_info['y']=y
            
            print_debug(unit_id, unit_type, player, mass, radius, x, y, vx, vy, extra, extra_2)
        
        # Wreck
        elif (player == -1) & (unit_type == 4):
            water.append({'unit_id':unit_id, 'x':x, 'y':y})
            
        # Tanker
        elif (player == -1) & (unit_type == 3):
            tankers.append({'unit_id':unit_id, 'x':x, 'y':y})
        
        elif player > 0:
            other_veh.append({'unit_id':unit_id, 'x':x, 'y':y})
            
        all_info[unit_id] = {'x':x, 'y':y}

    print_debug(water)
    print_debug(tankers)
    
    # Find nearest/ Where do I want to move
    def nearest(player_info, other):
        x, y = player_info['x'], player_info['y']
        
        lst = {}
        for other_i in other:
            id_i = other_i['unit_id']
            x_i, y_i = other_i['x'], other_i['y']
            
            d = ((x_i - x)**2 + (y_i - y)**2)**.5
               
            lst[id_i] = d
            
        if len(lst) > 0:
            min_id = min(lst, key=lst.get)
            return min_id, lst[min_id]
        else:   # No water yet
        
            print_debug(lst)
            return 1, 0    # Follow Destroyer
        
    min_id, d = nearest(player_info, water)
    X_reaper, Y_reaper = all_info[min_id]['x'], all_info[min_id]['y']
    
    # Tanker nearest to my reaper, such that I have to move less
    min_id, d = nearest(player_info, tankers)
    X_destr, Y_destr = all_info[min_id]['x'], all_info[min_id]['y']
    
    min_id, d = nearest(player_info, other_veh)
    X_doof, Y_doof = all_info[min_id]['x'], all_info[min_id]['y']
        

    
    # # # ## ########

    THROTTLE = 300
    
    if d < 600:
        THROTTLE = int(d/2.)
    
    # Reaper (for water)
    if 0:   # TAR
        pass
    elif 0:
        print("WAIT")
    else:
        print(X_reaper, Y_reaper, THROTTLE)     
           
    # Destrotyer (destroys tankers) 
    # TODO Decide thresh
    if (my_rage >= 60) & (nearest(all_info[1], other_veh)[1] < 2000):
        min_id, _= nearest(all_info[1], other_veh)
        X, Y = all_info[min_id]['x'], all_info[min_id]['y']
        print('SKILL', X, Y)
        # 1/0
    elif 0:
        print("WAIT")
    else:   
        print(X_destr, Y_destr, 300) 
    
    # DOOF
    if 0:   # Oil
        print('SKILL')
    elif 0:
        pass
    else:   
        print(X_doof, Y_doof, 300)
        
