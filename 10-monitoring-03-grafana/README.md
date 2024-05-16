
### Задание 1

1. Используя директорию [help](./help) внутри этого домашнего задания, запустите связку prometheus-grafana.
1. Зайдите в веб-интерфейс grafana, используя авторизационные данные, указанные в манифесте docker-compose.
1. Подключите поднятый вами prometheus, как источник данных.
1. Решение домашнего задания — скриншот веб-интерфейса grafana со списком подключенных Datasource.

   ## ОТВЕТ
   ![image](https://github.com/goddim/HW_netology_main/assets/132663924/012d0696-62ea-4aeb-9242-7503912f1f79)

## Задание 2

Изучите самостоятельно ресурсы:

1. [PromQL tutorial for beginners and humans](https://valyala.medium.com/promql-tutorial-for-beginners-9ab455142085).
1. [Understanding Machine CPU usage](https://www.robustperception.io/understanding-machine-cpu-usage).
1. [Introduction to PromQL, the Prometheus query language](https://grafana.com/blog/2020/02/04/introduction-to-promql-the-prometheus-query-language/).

Создайте Dashboard и в ней создайте Panels:

- утилизация CPU для nodeexporter (в процентах, 100-idle);
- CPULA 1/5/15;
- количество свободной оперативной памяти;
- количество места на файловой системе.

Для решения этого задания приведите promql-запросы для выдачи этих метрик, а также скриншот получившейся Dashboard.
### ОТВЕТ

 утилизация CPU для nodeexporter (в процентах, 100-idle);
![image](https://github.com/goddim/HW_netology_main/assets/132663924/fad383ab-c129-45c3-a33e-82662263374c)

- CPULA 1/5/15;
![image](https://github.com/goddim/HW_netology_main/assets/132663924/b136c27a-7f12-4f07-8cd7-2e0c29863147)

- количество свободной оперативной памяти;
![image](https://github.com/goddim/HW_netology_main/assets/132663924/64fd5b96-dc22-429a-88b0-8819dcd6390a)

- количество места на файловой системе
  ![image](https://github.com/goddim/HW_netology_main/assets/132663924/ff5dc40d-d03c-4cd3-a6e2-de192a3c06e8)

## Задание 3

1. Создайте для каждой Dashboard подходящее правило alert — можно обратиться к первой лекции в блоке «Мониторинг».
1. В качестве решения задания приведите скриншот вашей итоговой Dashboard.
![image](https://github.com/goddim/HW_netology_main/assets/132663924/4273ea0b-dac6-41dc-a746-93b31b7bea6e)

## Задание 4

1. Сохраните ваш Dashboard.Для этого перейдите в настройки Dashboard, выберите в боковом меню «JSON MODEL». Далее скопируйте отображаемое json-содержимое в отдельный файл и сохраните его.
1. В качестве решения задания приведите листинг этого файла.

---

### Как оформить решение задания

Выполненное домашнее задание пришлите в виде ссылки на .md-файл в вашем репозитории.

---
