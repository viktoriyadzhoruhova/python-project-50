import argparse

def main():
    parser = argparse.ArgumentParser(
        description="Compares two configuration files and shows a difference."
    )
    parser.add_argument('first_file', help='First configuration file')
    parser.add_argument('second_file', help='Second configuration file')
    args = parser.parse_args()
    # На данном этапе не делаем ничего с файлами, просто выводим сообщение
    print("gendiff is working")

if __name__ == '__main__':
    main()
