import pygame
import random
import os
import sqlite3
pygame.mixer.pre_init(44100, -16, 2, 2048)
pygame.init()
#pygame.mixer.init(44100, -16, 2, 2048)
WIDTH = 1280
HEIGHT = 720
conn = sqlite3.connect("PnT.db",timeout=10)
cursor = conn.cursor()
screen = pygame.display.set_mode((WIDTH,HEIGHT))
logo = pygame.image.load('logo.png')
pygame.display.set_caption('Python no Rizumu')
pygame.display.set_icon(logo)
login_screen = pygame.display.set_mode((640,480))
colors = {'black':(0,0,0),'white':(255,255,255),'red':(255, 0, 0)}
pygame.display.set_icon(logo)

def text_objects(text,font):
    textSurface = font.render(text,True,colors['black'])
    return textSurface, textSurface.get_rect()
    
def button(text,x,y,w,h,inactive_color,active_color,img,vert = False,action = None):
    mouse = pygame.mouse.get_pos()
    temp = img.get_rect()
    click = pygame.mouse.get_pressed()
    if x+temp[2] > mouse[0] > x and y+temp[3] > mouse[1] > y:
        btn = pygame.draw.rect(screen, active_color,(x,y,temp[2],temp[3]))
        if click[0] == 1 and action != None:
            action()
    else:
        btn = pygame.draw.rect(screen, inactive_color,(x,y,temp[2],temp[3]))
    largeText = pygame.font.Font('freesansbold.ttf',40)
    TextSurf, TextRect = text_objects(text,largeText)
    if vert == True:
        TextSurf = pygame.transform.rotate(TextSurf,90)
        TextSurf = pygame.transform.flip(TextSurf,True,True)
    TextRect.center = ((x+(temp[2]/2)),(y+(temp[3]/2)))
    screen.blit(img,(x,y))
    screen.blit(TextSurf, TextRect)
    return btn

def auth():#login='',password=''
    def auth_login(login='',password=''):
        sql = f"SELECT * FROM Users WHERE Login ='{login}'"
        cursor.execute(sql)
        t = cursor.fetchone()
        try:
            if t[0] == login and t[1] == password:
                level='User'
                print("Hello")
                main_menu(level)
                return level
        except:
            print("ERR0R")
    auth = True
    guest = pygame.image.load("./sprites/auth/GUEST.png").convert_alpha()
    register = pygame.image.load("./sprites/auth/REGISTER.png").convert_alpha()
    login = pygame.image.load("./sprites/auth/LOGIN.png").convert_alpha()
    auth_rects = {}
    auth_funcs = {register:register,login:auth_login,guest:main_menu}
    auth_sprites = {guest:(400,400),login:(250,400),register:(10,400)}
    background = pygame.Surface((640,480)).convert()
    background.fill((225,225,225))
    login_screen.blit(background,(0,0))
    text = pygame_textinput.TextInput()
    login = ''
    password =''
    while auth == True:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse = pygame.mouse.get_pos()
                for i in auth_rects.keys():
                    btn_rect = auth_rects[i]
                    if (btn_rect[1] >= mouse[0] >= btn_rect[0]
                    and btn_rect[3] >= mouse[1] >= btn_rect[2] ):
                        if auth_funcs[i] == auth_login:
                            auth_login(login,password)
                        else:
                            auth_funcs[i]()
        login_screen.blit(background,(0,0))
        if text.update(events):
            print(text.update(events))
            if login != '':
                password = text.get_text()
            else:
                login = text.get_text()
            text.clear_text()
            print('l:',login,'p:',password)
        login_screen.blit(text.get_surface(), (200,200))
        for i in auth_sprites.keys():
            temp = i.get_rect()
            rect = pygame.Rect(auth_sprites[i][0], auth_sprites[i][1], auth_sprites[i][0] + temp[2], auth_sprites[i][1] + temp[3])
            auth_rects[i] = rect
            screen.blit(i,auth_sprites[i])
        pygame.display.update()

def main_menu(level=''):
    pygame.display.set_mode((1280,720))
    menu = True
    background = pygame.image.load("./sprites/main_menu/Main_Menu_BG.png").convert_alpha()
    start = pygame.image.load("./sprites/main_menu/Main_Menu_Start.png").convert_alpha()
    multiplayer = pygame.image.load("./sprites/main_menu/MULTIPLAYER.png").convert_alpha()
    customize =pygame.image.load("./sprites/main_menu/CUSTOMIZE.png").convert_alpha()
    settings = pygame.image.load("./sprites/main_menu/Main_Menu_Settings.png").convert_alpha()
    exit = pygame.image.load("./sprites/main_menu/Main_Menu_Exit.png").convert_alpha()
    rank_bg = pygame.image.load("./sprites/main_menu/Main_Menu_Rank_BG.png").convert_alpha()
    settings_2 = pygame.image.load("./sprites/main_menu/settings.png").convert_alpha()
    sprites ={start:(13,387),multiplayer:(13,449),customize:(13,511),settings:(13,573),exit:(13,635),rank_bg:(1,1),settings_2:(750,0)}
    main_menu_rects = {}
    main_menu_funcs = {start:song_select,settings:settings,exit:pygame.quit}
    screen.blit(background,(0,0))
    for i in sprites.keys():
        temp = i.get_rect()
        rect = pygame.Rect(sprites[i][0], sprites[i][1], sprites[i][0] + temp[2], sprites[i][1] + temp[3])
        main_menu_rects[i] = rect
        screen.blit(i,sprites[i])
    while menu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse = pygame.mouse.get_pos()
                for i in main_menu_rects.keys():
                    btn_rect = main_menu_rects[i]
                    if (btn_rect[1] >= mouse[0] >= btn_rect[0]
                    and btn_rect[3] >= mouse[1] >= btn_rect[2] ):
                        main_menu_funcs[i]()
        pygame.display.flip()

def song_select():
    song_select_bin = True
    song_select_background = pygame.image.load("./sprites/song_select/song_select_bg.png").convert_alpha()
    sprites = [pygame.image.load("./sprites/song_select/song_bg_1.png").convert_alpha(),
               pygame.image.load("./sprites/song_select/song_bg_2.png").convert_alpha(),
               pygame.image.load("./sprites/song_select/song_bg_3.png").convert_alpha()]
    song_select_bottom = pygame.image.load("./sprites/song_select/song_select_bottom.png").convert_alpha()
    song_select_top = pygame.image.load("./sprites/song_select/song_select_top.png").convert_alpha()
    screen.blit(song_select_background,(0,0))
    screen.blit(song_select_bottom,(0,620))
    screen.blit(song_select_top,(0,0))
    songs_list=[]
    offset = 0
    with os.scandir('./Songs') as songs:
        for i in songs:
            songs_list.append(i.name)
    while song_select_bin:
        buttons=[]
        a = button(songs_list[-1+offset],412,111,200,100,colors['white'],colors['red'],sprites[0])
        buttons.append(a)
        b = button(songs_list[0+offset],412,311,200,100,colors['white'],colors['red'],sprites[1])
        buttons.append(b)
        c = button(songs_list[1+offset],412,511,200,100,colors['white'],colors['red'],sprites[2])
        buttons.append(c)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                try:
                    mouse = pygame.mouse.get_pos()
                    for i in range(len(songs_list)):
                        btn_rect = buttons[i].left,buttons[i].right,buttons[i].top,buttons[i].bottom
                        if (btn_rect[1] >= mouse[0] >= btn_rect[0]
                        and btn_rect[3] >= mouse[1] >= btn_rect[2]):
                            game(songs_list[offset])
                except:
                    pass
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    if offset+4 >=len(songs_list):
                        offset = 0-3
                    else:
                        offset+=1
                    print(offset)
                if event.key == pygame.K_DOWN:
                    if offset <= 0-len(songs_list)+1:
                        offset=0
                    else:
                        offset-=1
                    print(offset)
                if event.key == pygame.K_RETURN:
                    game(songs_list[offset])
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
            pygame.display.flip()
def game(song):
    print(song)
    screenrect=screen.get_rect()
    try:
        background = pygame.image.load(f"./Songs/{song}/bg.png").convert_alpha()
    except:
        background = pygame.Surface(screen.get_size()).convert()
        background.fill((255,140,0))
    screen.blit(background,(0,0))
    FPS = 60
    FPS_Show = False
    running = True
    clock = pygame.time.Clock()
    ballx,bally=0,206
    time = 0
    score = 0
    music = pygame.mixer.music.load(f'./Songs/{song}/music.mp3')
    with open(f'./Songs/{song}/muzukashi.pnt','r') as f:
        BPM = f.read(10)[6:9]
        note = f.read()[8:].split()
        all_pattern = []
        for i in note:
            f = i.index(',')
            all_pattern.append([int(i[:f]),int(i[f+1:])])
    dx,dy=int(1*(int(BPM)/20)),10
    pygame.mixer.music.set_volume(1)
    notes = [pygame.image.load("./sprites/game/don.png").convert_alpha(),
             pygame.image.load("./sprites/game/kat.png").convert_alpha(),
             pygame.image.load("./sprites/game/don_B.png").convert_alpha(),
             pygame.image.load("./sprites/game/kat_B.png").convert_alpha()]
    playfield = pygame.image.load("./sprites/game/playfield.png").convert_alpha()
    game_info = [pygame.image.load("./sprites/game/info_bg.png").convert_alpha()]
    taiko = [pygame.image.load("./sprites/game/taiko_empty.png").convert_alpha(),
             pygame.image.load("./sprites/game/taiko_rim_left.png").convert_alpha(),
             pygame.image.load("./sprites/game/taiko_center_left.png").convert_alpha(),
             pygame.image.load("./sprites/game/taiko_center_right.png").convert_alpha(),
             pygame.image.load("./sprites/game/taiko_rim_right.png").convert_alpha()]
    hit = pygame.image.load("./sprites/game/hit.png").convert_alpha()
    hit_rect = (300,21,400)
    playfield_w = playfield.get_width()
    screen.blit(playfield,(0,170))
    largeText = pygame.font.Font('freesansbold.ttf',25)
    song_name = text_objects(f"{song}",largeText)
    song_name_rect = (1000,61,song_name[1][2]+1000,song_name[1][3]+61)
    screen.blit(song_name[0],song_name_rect)
    moving = True
    pygame.mixer.music.play()
    note = [0,notes[random.randint(0,3)]]
    note_collide = False
    center = 350 #x
    to_center = 930
    pattern = []
    for i in all_pattern.copy():
        if i[0] <= 2000:
            all_pattern.remove(i)
            pattern.append(i)
    while running == True:
        fps = clock.tick(FPS)
        ms = 1000/60
        time += ms
        #print(time)

        if FPS_Show:
            pygame.display.set_caption(f"FPS: {round(clock.get_fps())}. Time: {round(time/1000)}")
        else:
            pygame.display.set_caption(f'{song}')
        if ballx > playfield_w and moving == True:
            moving = False
            note[1] = notes[random.randint(0,3)]
            if note[1] == notes[0] or note[1] == notes[1]:
                ballx,bally=0,206
            else:
                ballx,bally=0,191
            moving = True
        if moving:
            ballx+=dx
            screen.blit(playfield,(0,170))
            playfield.blit(hit,(300,21))
            playfield.blit(game_info[0],(-4,6))
            playfield.blit(taiko[0],(135,21))
            new_x = playfield_w - ballx
            note[0] = new_x
            screen.blit(note[1],(new_x,bally))
            if note[0] <= hit_rect[2] and note[0] >= hit_rect[0]:
                note_collide = True
            else:
                note_collide = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                volume = pygame.mixer.music.get_volume()
                if event.button == 3:
                    pygame.mixer.music.set_volume(volume-0.1)
                if event.button == 1:
                    pygame.mixer.music.set_volume(volume+0.1)
                print('Volume:',volume,'Button:',event.button)
            elif event.type == pygame.KEYDOWN:
                keys = pygame.key.get_pressed()
                if keys[pygame.K_UP]:
                    dx+=1
                    print('Speed:',dx)
                if keys[pygame.K_DOWN]:
                    dx-=1
                    print('Speed:',dx)
                if keys[pygame.K_r]:
                    moving = False
                    pygame.mixer.music.pause()
                if keys[pygame.K_SPACE]:
                    moving = True
                    pygame.mixer.music.unpause()
                if keys[pygame.K_F12]:
                    FPS_Show = True if FPS_Show == False else False
                if  keys[pygame.K_z] and keys[pygame.K_v]:
                    screen.blit(taiko[1],(135,191))
                    screen.blit(taiko[4],(185,191))
                    if note_collide and note[1] == notes[3]:
                        score+=1
                if keys[pygame.K_x] and keys[pygame.K_c]:
                    screen.blit(taiko[2],(145,201))
                    screen.blit(taiko[3],(185,201))
                    if note_collide and note[1] == notes[2]:
                        score+=1
                if keys[pygame.K_z]:
                    screen.blit(taiko[1],(135,191))
                    if note_collide and note[1] == notes[1]:
                        score+=1
                if keys[pygame.K_x]:
                    screen.blit(taiko[2],(145,201))
                    if note_collide and note[1] == notes[0]:
                        score+=1
                if keys[pygame.K_c]:
                    screen.blit(taiko[3],(185,201))
                    if note_collide and note[1] == notes[0]:
                        score+=1
                if keys[pygame.K_v]:
                    screen.blit(taiko[4],(185,191))
                    if note_collide and note[1] == notes[1]:
                        score+=1
                print(score)
        pygame.display.flip()
main_menu()
#auth()
