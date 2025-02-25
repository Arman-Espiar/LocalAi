import os
import translator_constants as constants
import translator_functions as functions


def main() -> None:
    os.system(command="cls")

    source_pathfile: str = "./files/sample.txt"
    target_pathfile: str = "./files/translated.txt"

    file_content: str = functions.read_text_file(pathfile=source_pathfile)
    file_content = functions.normalize_text(text=file_content)
    paragraphs: list[str] = functions.get_paragraphs(text=file_content)

    with open(file=target_pathfile, mode="wt", encoding="utf-8") as file:
        for paragraph in paragraphs:
            translated: str = functions.translate(
                text=paragraph,
                model_name=constants.MODEL_NAME,
                temperature=constants.TEMPERATURE,
            )
            file.write(translated)
            file.write("\n\n")

    print("Translation Completed...")


if __name__ == "__main__":
    main()
