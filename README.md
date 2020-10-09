# war_words

Для збору даних потрібно зробити декілька кроків:
1. Відповідно до інструкцій встановити програму Docker:  
    https://docs.docker.com/engine/install/
2. Запустити команду:  
    ~$ `docker build -t war_words .`
3. Запустити команду яка безпосередньо запустить збір даних:  
    ~$ `docker run -v $PWD/results:/results -v $PWD/src:/project/src war_words`

Для того щоб працювати у Jupiter Notepad з ВебБраузера для своїх досліджень
 потрібно у терміналі запустити наступну команду:  
~$ `docker run -it -v $PWD:/project -p 8888:8888 war_words jupyter notebook --allow-root --ip=0.0.0.0 --port=8888`  
а далі перейти за посиланням, котре буде у вікні терміналу.

