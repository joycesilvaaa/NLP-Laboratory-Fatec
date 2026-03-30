from googletrans import Translator
import asyncio

class TranslatorGoogle:
    def __init__(self) -> None:
        self._translator = Translator()
        self._language_src = 'auto'
        self._language_dest = 'en'
        self._choose_language()

    async def execute(self) -> None:
        try:
            phrase = str(input("Digite uma frase: ")).strip()
            result = await self._translator.translate(phrase, src=self._language_src, dest=self._language_dest)
            print(f"Tradução: {result.text}")
        except Exception as e:
            print("Erro na tradução:", e)

    def _choose_language(self)-> None:
        print("----- Tradução de Frases -----")
        print("Escolha o idioma de destino:")
        print("1 - Português")
        print("2 - Inglês")
        print("3 - Sair")
        print("------------------------------")
        language = int(input("Digite a opção: "))
        match language:
            case 1:
                self._language_dest = 'pt'
            case 2:
                self._language_dest = 'en'
            case 3:
                exit()
            case _:
                print("Opção inválida.")
                exit()

if __name__ == "__main__":
    asyncio.run(TranslatorGoogle().execute())