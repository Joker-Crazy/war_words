# war_words

Для збору даних потрібно зробити декілька кроків:
1. Відповідно до інструкцій встановити програму Docker:
    https://docs.docker.com/engine/install/
2. Запустити команду:
    ~$ `docker build -t war_words .`
3. Запустити команду яка безпосередньо запустить збір даних:
    ~$ `docker run -v $PWD/results:/results -v $PWD/src:/project/src war_words`
