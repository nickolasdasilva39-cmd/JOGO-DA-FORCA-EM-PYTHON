import random

def desenha_forca(erros):
    estagios = [
        """
           --------
           |      |
           |      
           |    
           |      
           |     
          ---
        """,
        """
           --------
           |      |
           |      O
           |    
           |      
           |     
          ---
        """,
        """
           --------
           |      |
           |      O
           |      |
           |      
           |     
          ---
        """,
        """
           --------
           |      |
           |      O
           |     /|
           |      
           |     
          ---
        """,
        """
           --------
           |      |
           |      O
           |     /|\\
           |      
           |     
          ---
        """,
        """
           --------
           |      |
           |      O
           |     /|\\
           |     / 
           |     
          ---
        """,
        """
           --------
           |      |
           |      O
           |     /|\\
           |     / \\
           |     
          ---
        """
    ]
    return estagios[erros]

def jogar_forca():
    palavras = ['ALGORITMO', 'PYTHON', 'PROGRAMACAO', 'DESENVOLVEDOR', 'COMPUTADOR', 'INTERNET', 'TECLADO']
    palavra_secreta = random.choice(palavras)
    letras_descobertas = ['_' for _ in palavra_secreta]
    letras_tentadas = []
    erros = 0
    max_erros = 6

    print("--- Bem-vindo ao Jogo da Forca ---")
    
    while erros < max_erros and '_' in letras_descobertas:
        print(desenha_forca(erros))
        print("Palavra:", " ".join(letras_descobertas))
        print("Letras já tentadas:", ", ".join(letras_tentadas) if letras_tentadas else "Nenhuma")
        
        chute = input("\nDigite uma letra: ").strip().upper()
        
        # Validação da entrada do usuário
        if not chute.isalpha() or len(chute) != 1:
            print("\n⚠️  Por favor, digite apenas UMA letra válida.")
            continue
            
        if chute in letras_tentadas:
            print("\n⚠️  Você já tentou essa letra. Escolha outra.")
            continue
            
        letras_tentadas.append(chute)
        letras_tentadas.sort()
        
        # Verifica se o chute está na palavra
        if chute in palavra_secreta:
            print(f"\n✅ Boa! A letra '{chute}' está na palavra.")
            for i, letra in enumerate(palavra_secreta):
                if letra == chute:
                    letras_descobertas[i] = chute
        else:
            erros += 1
            print(f"\n❌ Que pena! A letra '{chute}' não está na palavra.")
            
    # Condições de fim de jogo
    if '_' not in letras_descobertas:
        print(f"\n🎉 Parabéns, você ganhou! A palavra era: {palavra_secreta}")
    else:
        print(desenha_forca(erros))
        print(f"\n💀 Game Over! Você foi enforcado. A palavra correta era: {palavra_secreta}")

if __name__ == "__main__":
    jogar_forca()
