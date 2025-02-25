import os
import translator_constants as constants
import translator_functions as functions


def main() -> None:
    os.system(command="cls")
    choice: int = int(input("Enter 1 for Online Translation, 2 for Offline Translation: "))

    source_pathfile: str = "./files/sample.txt"
    target_pathfile: str = "./files/translated.txt"

    file_content: str = functions.read_text_file(pathfile=source_pathfile)
    file_content = functions.normalize_text(text=file_content)
    paragraphs: list[str] = functions.get_paragraphs(text=file_content)
    try:
        with open(file=target_pathfile, mode="wt", encoding="utf-8") as file:
            for paragraph in paragraphs:
                if choice == 1:
                    translated: str = functions.groq_translate(
                        text=paragraph,
                        model_name=constants.GROQ_MODEL_NAME,
                        temperature=constants.TEMPERATURE,
                    )
                else:
                    translated: str = functions.local_translate(
                        text=paragraph,
                        model_name=constants.LOCAL_MODEL_NAME,
                        temperature=constants.TEMPERATURE,
                    )
                file.write(translated)
                file.write("\n\n")

        print("Translation Completed...")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
