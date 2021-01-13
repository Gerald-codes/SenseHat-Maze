
def menu_option():
    print('MAIN NENU')
    print('=========')
    option_list=('Read and load maze from file','View maze','Play maze game',\
                'Configue current maze','Export maze to file','Create new maze'\
                ,'Play maze using SenseHAT','View Leaderboard')
    for i in range(len(option_list)):
        print('[{}] {}'.format(i+1,option_list[i]))
    print()
    print('[0] Exit Maze')
#Current Maze function
def current_maze(maze):
    for i in range(len(maze)):
        print(maze[i])

#Option 1
def read_load_maze_file():
    try:
            
        print('Option [1] Read and load maze from file\n')
        filename=input('Enter the name of the data file: ')
        file=open(filename,'r')
        maze=[]
        line_list=[]
        for line in file:
            line=line.strip('\n')
            line_list=list(line)
            maze.append(line_list)
        print('Number of lines read:{} \n '.format(len(maze)))
        return maze
    except Exception as e:
        print('Name of file not found.')


#Option 2
def view_maze(maze):
    print('Option [2]: View Maze \n')
    print('===============================')
    for i in range(len(maze)):
        print(maze[i])
        

#Option 3
def play_maze(maze):
    print('Option [3] Play maze game')
    print('=================================')
    for q in range(len(maze)):
            for w in range(len(maze[q])):
                if maze[q][w]=='B':
                    b_row=q
                    b_col=w

    import copy
    play_maze=copy.deepcopy(maze)
    moves=0
    while True:
        for i in range(len(play_maze)):
            print(play_maze[i])
        for i in range(len(play_maze)):
            for j in range(len(play_maze[i])):
                if play_maze[i][j]=='A':
                    row = i
                    col = j
        print('\nLocation of You(A) = (Row {}, Column {})'.format(row,col))
        print('Location of End (B) = (Row {}, Column {})'.format(b_row,b_col))
        movement=input("\nPress 'W' for UP, 'A' for LEFT, 'S' for DOWN, 'D' for RIGHT, 'M' for MAIN NENU': ")
        movement = movement.upper()
        if movement=='W':
            if play_maze[row-1][col]=='X':
                print('\nInvalid Movement,try again!')
            else:
                play_maze[row][col]='O'
                play_maze[row-1][col]='A'
        elif movement=='S':
            if play_maze[row+1][col]=='X':
                print('\nInvalid Movement,try again!')
            else:
                play_maze[row][col]='O'
                play_maze[row+1][col]='A'
        elif movement=='A':
            if play_maze[row][col-1]=='X':
                print('\nInvalid Movement,try again!')
            else:
                play_maze[row][col]='O'
                play_maze[row][col-1]='A'
        elif movement=='D':
            if play_maze[row][col+1]=='X':
                print('\nInvalid Movement,try again!')
            else:
                play_maze[row][col]='O'
                play_maze[row][col+1]='A'
        elif movement=='M':
            return
        else:   
            print('Invalid Movement, try again!')
        if play_maze[b_row][b_col]=='A':
            play_maze[row][col]='O'
            play_maze[b_row][b_col]='A'
            for i in range(len(play_maze)):
                print(play_maze[i])
            name=input('Enter you name: ')
            print('CONGRATULATION {},YOU WON!!!'.format(name.upper()))
            #print('Number of moves: {}'.format(moves))
            score=(31-moves)*10
            print('Score:{}'.format(score))
            leaderboard_file=open('leaderboard.csv','a')
            leaderboard_file.write('\n')
            leaderboard_file.write(name+str(',')+str(score))
        
            leaderboard_file.close()
            break
        else:
            moves+=1
            print('Number of moves: {}'.format(moves))
            continue

#Option 4
def config_current_maze(maze):
    print('\nOption [4] Configure current maze')
    print('\n========================================')
    current_maze(maze)
    
    print('\nCONFIGURATION MENU')
    print('==================')
    config_list=['Create wall','Create passageway','Create start point',\
                 'Create end point']
    for j in range(len(config_list)):
        print('[{}] {}'.format(j+1,config_list[j]))
    print('\n[0] Exit to Main Menu')

    option=input('\n\nEnter your options: ')
    if option=='0':
        return
    else:
        print('========================================')
        current_maze(maze)
        try:
            coordinate=input('\nEnter the coordinate of the item you wish to change E.g. Row,Column'\
                             '\nOR\n==============================='
                             "\n'B' to return to Configure Menu."\
                             "\n'M' to return to Main Menu: ")
            coordinate=coordinate.upper()
            if coordinate=='B':
                config_current_maze(maze)
            elif coordinate=='M':
                return
            coordinate_list=[]
            coordinate_list=list(coordinate.split(','))
            coordinate_list[-1]=int(coordinate_list[-1])
            if option=='1':
                maze[int(coordinate_list[0])][int(coordinate_list[-1])]='X'
                config_current_maze(maze)
            elif option=='2':
                maze[int(coordinate_list[0])][int(coordinate_list[-1])]='O'
                config_current_maze(maze)
            elif option=='3':
                for i in range(8):
                    for j in range(8):
                        if maze[i][j]=='A':
                            maze[i][j]='O'
                maze[int(coordinate_list[0])][int(coordinate_list[-1])]='A'
                config_current_maze(maze)
            elif option=='4':
                for i in range(8):
                    for j in range(8):
                        if maze[i][j]=='B':
                            maze[i][j]='O'
                maze[int(coordinate_list[0])][int(coordinate_list[-1])]='B'
                config_current_maze(maze)
            else:
                print('Invalid Option,try again!')
                config_current_maze(maze)

            
        except Exception as e:
            print('Try again with integers')
    
#Option 5
def export_maze_to_file(maze):
    print('Option[5] Export maze to file')
    filename=input('\nEnter filename to save to (end with .csv or .txt): ')
    if (filename[-4:-1]+filename[-1])=='.txt' or '.csv':
        file=open(filename,'w')
        for i in range(len(maze)):
            file.write(str(''.join(maze[i])))
            file.write('\n')
        file.close()
        return filename
    else:
        print('Invalid file name')
    
#Option 6
def create_Nmaze(maze):
    print('Option [6] Create new maze!')
    confirmation=input('\nThis will empty the current maze. Are you sure?(Y or N): ')
    confirmation=confirmation.upper()
    if confirmation=='Y':
        dimension=input('\nEnter the dimension of the maze (row,column): ')
        dimension_list=[]
        dimension_list=dimension.split(',')
        row=[]
        for i in range(int(dimension_list[0])):
            row.append('X')
        new_maze=[]
        for k in range(int(dimension_list[-1])):
            new_maze.append(row)
        print('A new maze of {} by {} has been created.'.format(dimension_list[0],dimension_list[-1]))
        print('Please run configure maze to start configuring new maze.')
        maze=new_maze
        return maze
    elif confirmation=='N':
        return maze

    else:
        print('Invalid optionl,Try again!')
#Option 7
def play_maze_w_sensehat(maze):
    try:
        from sense_hat import SenseHat
        sense = SenseHat()
        sense.clear()
        x=[211,211,211]
        o=[0,0,0]
        a=[255,0,0]
        b=[0,128,0]
        import time
        starttime=time.clock()
        game=True
        while game:
          maze_list=[]
          for i in range(len(maze)):
            for j in range(len(maze[i])):
              if maze[i][j]=='X':
                maze[i][j]=x
              elif maze[i][j]=='O':
                maze[i][j]=o
              elif maze[i][j]=='A':
                maze[i][j]=a
              elif maze[i][j]=='B':
                maze[i][j]=b
              maze_list.append(maze[i][j])
          maze1=maze_list
          sense.set_pixels(maze1)

          for event in sense.stick.get_events():
            for i in range(len(maze)):
              for j in range(len(maze[i])):
                if maze[i][j]==a:
                  row=i
                  col=j
            for q in range(len(maze)):
              for w in range(len(maze[q])):
                if maze[q][w]==b:
                  b_row=q
                  b_col=w
        
            if event.action=='pressed':
              if event.direction=='up':
                if maze[row-1][col]==x:
                  maze[row][col]=a
                else:
                  maze[row-1][col]=a
                  maze[row][col]=o
              elif event.direction =='down':
                if maze[row+1][col]==x:
                  maze[row][col]=a
                else:
                  maze[row+1][col]=a
                  maze[row][col]=o
              elif event.direction =='right':
                if maze[row][col+1]==x:
                  maze[row][col]=a
                else:
                  maze[row][col+1]=a
                  maze[row][col]=o  
              elif event.direction =='left':
                if maze[row][col-1]==x:
                  maze[row][col]=a
                else:
                  maze[row][col-1]=a
                  maze[row][col]=o
              if maze[b_row][b_col]==a:
                stoptime=time.clock()
                time_taken=stoptime-starttime
                sense.show_message('You Won in {:.2}S!'.format(time_taken),text_colour=[250,0,0],scroll_speed=.05,\
                           back_colour=[0,0,0])
            
                game=False
    except Exception as e:
        print('This function is not available without SenseHat')
#Option 8
def leaderboard():
    print('Option [8] View Leaderboard')
    print('\n\n{:<30}{}'.format('Name','Score'))
    print('===================================')
    file=open('leaderboard.csv','r')
    temp_file=[]
    k=0
    l=0
    for line in file:
        line_list=[]
        line = line.strip('\n')
        line_list = line.split(',')
        temp_file.append(line_list)
    leaderboard=[]
    score_list=[]
    for i in range(len(temp_file)):
        score_list.append(int(temp_file[i][1]))
        score_list.sort(reverse=True)
    while l<len(score_list):
        if score_list[l]==score_list[-1]:
            break
        else:
            while k<len(score_list):
                if l+k+1>=len(score_list):
                    break
                    
                else:
                    if score_list[l]==score_list[l+k+1]:
                        score_list.remove(score_list[l])
                        break
                        

                    k+=1
                l+=1
    for k in range(len(score_list)):
        for j in range(len(temp_file)):
            if int(temp_file[j][1])==int(score_list[k]):
                leaderboard.append(temp_file[j])
    if len(leaderboard)>10:
        for i in range(0,10):
            for k in range(len(leaderboard)):
                print('{:<30}{}'.format(leaderboard[i][0],leaderboard[i][-1]))
    else:
        for line in leaderboard:
            print('{:<30}{}'.format(line[0],line[-1]))
    file.close()

while True:
    menu_option()
    print()
    option=input('Enter your option: ')
    if option=='1':
        maze=read_load_maze_file()
    elif option=='2':
        view_maze(maze)
    elif option=='3':
        play_maze(maze)
    elif option=='4':
        config_current_maze(maze)
    elif option=='5':
        export_maze_to_file(maze)
    elif option=='6':
        maze=create_Nmaze(maze)
    elif option=='7':
        play_maze_w_sensehat(maze)
    elif option=='8':
        leaderboard()
    elif option=='0':
        break
    else:
        print('Invalid option,try again')
