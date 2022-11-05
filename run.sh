#!/bin/sh
export FLASK_APP=webapp && export FLASK_ENV=development && flask run

''' Сокращение строки запуска для зупуска сервера. Выполняем в консоле команду 'hmod +x run.sh' - которая делает 
файл исполняемым. Далее для запуска сервера пишем './run.sh' '''