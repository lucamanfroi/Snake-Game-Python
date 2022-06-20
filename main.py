import pygame, sys, time, random

velocidade = 15

# Tamanho das janelas
tamanho_janela_x = 1380
tamanho_janela_y = 840

checar_erro = pygame.init()

if checar_erro[1] > 0:
    print("Erro " + checar_erro[1])
else:
    print("Jogo iniciado com sucesso!")

# Janela de inicializacao do jogo
pygame.display.set_caption("SNAKE!")
janela_jogo = pygame.display.set_mode((tamanho_janela_x, tamanho_janela_y))

# Cores
preto = pygame.Color(0, 0, 0)
branco = pygame.Color(255, 255, 255)
vermelho = pygame.Color(255, 0, 0)
verde = pygame.Color(0, 255, 0)
azul = pygame.Color(0, 0, 255)

controle_fps = pygame.time.Clock()

# Tamanho de uma unidade da cobra
tamanho_quadrado = 30


def iniciar_vars():
    global posicao_cabeca, posicao_comida, corpo_cobra, spawn_comida, placar, direcao
    direcao = "DIREITA"
    posicao_cabeca = [120, 60]
    corpo_cobra = [[120, 60]]
    posicao_comida = [random.randrange(1, (tamanho_janela_x // tamanho_quadrado)) * tamanho_quadrado,
                      random.randrange(1, (tamanho_janela_y // tamanho_quadrado)) * tamanho_quadrado]
    spawn_comida = True
    placar = 0


iniciar_vars()


def mostrar_placar(escolha, cor, fonte, tamanho):
    fonte_placar = pygame.font.SysFont(fonte, tamanho)
    superficie_placar = fonte_placar.render("Placar: " + str(placar), True, cor)
    rect_placar = superficie_placar.get_rect()
    if escolha == 1:
        rect_placar.midtop = (tamanho_janela_x / 10, 15)
    else:
        rect_placar.midtop =d (tamanho_janela_x / 2, tamanho_janela_y / 1.25)

    janela_jogo.blit(superficie_placar, rect_placar)


# Loop do jogo
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if (event.key == pygame.K_UP or event.key == ord("w")
                    and direcao != "BAIXO"):
                direcao = "CIMA"
            elif (event.key == pygame.K_DOWN or event.key == ord("s")
                  and direcao != "CIMA"):
                direcao = "BAIXO"
            elif (event.key == pygame.K_RIGHT or event.key == ord("d")
                  and direcao != "ESQUERDA"):
                direcao = "DIREITA"
            elif (event.key == pygame.K_LEFT or event.key == ord("a")
                  and direcao != "DIREITA"):
                direcao = "ESQUERDA"

    if direcao == "CIMA":
        posicao_cabeca[1] -= tamanho_quadrado
    elif direcao == "BAIXO":
        posicao_cabeca[1] += tamanho_quadrado
    elif direcao == "ESQUERDA":
        posicao_cabeca[0] -= tamanho_quadrado
    else:
        posicao_cabeca[0] += tamanho_quadrado

    if posicao_cabeca[0] < 0:
        posicao_cabeca[0] = tamanho_janela_x - tamanho_quadrado
    elif posicao_cabeca[0] > tamanho_janela_x - tamanho_quadrado:
        posicao_cabeca[0] = 0
    elif posicao_cabeca[1] < 0:
        posicao_cabeca[1] = tamanho_janela_y - tamanho_quadrado
    elif posicao_cabeca[1] > tamanho_janela_y - tamanho_quadrado:
        posicao_cabeca[1] = 0

    # Comendo fruta
    corpo_cobra.insert(0, list(posicao_cabeca))
    if posicao_cabeca[0] == posicao_comida[0] and posicao_cabeca[1] == posicao_comida[1]:
        placar += 1
        spawn_comida = False
    else:
        corpo_cobra.pop()

    # Spawn comida
    if not spawn_comida:
        posicao_comida = [random.randrange(1, (tamanho_janela_x // tamanho_quadrado)) * tamanho_quadrado,
                          random.randrange(1, (tamanho_janela_y // tamanho_quadrado)) * tamanho_quadrado]
        spawn_comida = True


    # Graficos
    janela_jogo.fill(preto)
    for pos in corpo_cobra:
        pygame.draw.rect(janela_jogo, verde, pygame.Rect(
            pos[0] + 2, pos[1] + 2,
            tamanho_quadrado - 2, tamanho_quadrado -2))

    pygame.draw.rect(janela_jogo, vermelho, pygame.Rect(posicao_comida[0],
                     posicao_comida[1], tamanho_quadrado, tamanho_quadrado))

    # Condicao de game over
    for block in corpo_cobra[1:]:
        if posicao_cabeca[0] == block[0] and posicao_cabeca[1] == block[1]:
            iniciar_vars()

    mostrar_placar(1, branco, 'consolas', 20)
    pygame.display.update()
    controle_fps.tick(velocidade)