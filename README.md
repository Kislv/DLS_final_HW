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

Bootstrap устанавливается по [инструкции](https://getbootstrap.com/docs/4.3/getting-started/introduction/)

Back-end:
- pyramid
- python-daemon
- json

mmdetection устанавливается по [инструкции](https://github.com/open-mmlab/mmdetection/)

## Подробная информация о модели

[Mask R-CNN](https://habr.com/ru/post/421299/)

# Источники
* [mmdetection](https://github.com/open-mmlab/mmdetection/)
* [COCO](https://cocodataset.org/)
* [Архитектура](https://habr.com/ru/post/536742/)
* [Mask R-CNN](https://habr.com/ru/post/421299/)
* [Bootstrap](https://getbootstrap.com/docs/4.3/getting-started/introduction/)