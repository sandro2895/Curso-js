largura1 = float(input('Quantos metro(s) tem a largura da parede? : '))
altura1 = float(input('Quantos metro(s) tem a altura da parede? : '))
print('Sua parede tem a dimensão de {:.1f}x{:.1f} e a sua area é de {}m².'.format(largura1, altura1, largura1*altura1))
print('Para pintar a parede completa, você precisará de {}l de tinta.'.format((largura1*altura1)/2))
