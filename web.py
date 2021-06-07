from flask import Flask, render_template, request
app = Flask(__name__)
    
def board_design():
    height = 8
    width = 8    
    return [height, width]

def check_position(initial_pos=None, final_pos=None):
    height, width = board_design()
    change_row = False if initial_pos[0] == final_pos[0] else True
    change_column = False if initial_pos[1] == final_pos[1] else True
    if ((change_row == False and change_column == False) or (change_row != change_column)) and ((final_pos[0]>=1 and width>=final_pos[0]) and (final_pos[1]>=1 and height>=final_pos[1])):
        return True
    else:
        return False

@app.route('/', methods=["POST"])
def change_position():
    initial_pos = [int(request.form['initial_x']),int(request.form['initial_y'])]
    final_pos = [int(request.form['final_x']),int(request.form['final_y'])]
    if check_position(initial_pos=initial_pos,final_pos=final_pos):
        print(check_position(initial_pos=initial_pos,final_pos=final_pos))
        return board_position(position_tower=final_pos)
    else:
        return board_position("Moviment il·legal",initial_pos)

@app.route('/', methods=["GET"])
def board_position(notification=None, position_tower=None):
    height, width = board_design()
    if height<=1 or width<=1:
        return render_template('bad_board.html')
    position_tower = [1,height] if not position_tower else position_tower
    return render_template('board.html', height=height, width=width, position_tower=position_tower,notification=notification)

app.run( debug=True )