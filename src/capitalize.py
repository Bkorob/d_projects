def main():
    def capitalize(text):
        if text == '':
            return ''
        first, *other = text
        return f'{first.upper()}{"".join(other)}'
    return capitalize

if __name__ == '__main__':
    main()
