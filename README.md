# Условие
Deep Learning School  graduftion project:  Реализация модели детекции в веб-приложении
TODO: add ipynb file to rep
## Описание
Выбор фреймворка/библиотеки для решения задачи детекции:
* Был выбран набор инструментов [mmdetection](https://github.com/open-mmlab/mmdetection/). В нем выбор пал на модель mask_rcnn_r50_caffe_fpn_mstrain-poly_3x_coco, которая обучена на датасете [COCO](https://cocodataset.org/)

## Структура проекта

Проект реализованан в трех частях:

1. WEB Клиентская часть: Js скрипт, который выполняется в WEB браузере index.html
2. Серверная часть, обработки HTTP запросов. Скрипт web.py.
3. Скрипт детекции объектов: mmdetectionl.py

## Используемые технологии
Front-end:
- Bootstrap

Back-end:
- pyramid
- python-daemon
- json

## Инструкция по запуску
1. mmdetection устанавливается по [инструкции](https://github.com/open-mmlab/mmdetection/)
2. Bootstrap устанавливается по [инструкции](https://getbootstrap.com/docs/4.3/getting-started/introduction/) 
3. Добавления модели в корень репозитория: mim download mmdet --config mask_rcnn_r50_caffe_fpn_mstrain-poly_3x_coco --dest .
4. Из корня запускаем сервер (по умолчанию запускается на порте 8000) для отдачи статики python: -m http.server
5. В файле server.py изменить пути по питона (python_path) и скрипта для детекции (script_path).
6. Запуск основного сервера:  sudo python3 back-end/server.py

# Источники
* [mmdetection](https://github.com/open-mmlab/mmdetection/)
* [COCO](https://cocodataset.org/)
* [Архитектура, куски кода](https://habr.com/ru/post/536742/)
* [Mask R-CNN](https://habr.com/ru/post/421299/)
* [Bootstrap](https://getbootstrap.com/docs/4.3/getting-started/introduction/)
