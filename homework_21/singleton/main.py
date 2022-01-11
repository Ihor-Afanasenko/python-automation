from logger import Logger

if __name__ == '__main__':
    # E.g.
    first_logger = Logger()
    print(first_logger.log('First statement'))
    second_logger = Logger()
    print(second_logger.log('Second statement'))

    print(f'First instance -> {first_logger} \nSecond instance -> {second_logger}')
    print(id(first_logger) == id(second_logger))
