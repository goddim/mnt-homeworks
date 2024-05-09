# Домашнее задание к занятию 10 «Jenkins»

## Подготовка к выполнению

1. Создать два VM: для jenkins-master и jenkins-agent.
![image](https://github.com/goddim/HW_netology_main/assets/132663924/ffd08813-cf7a-4b01-ac06-f623b11d2946)

2. Установить Jenkins при помощи playbook.
3. Запустить и проверить работоспособность.
![image](https://github.com/goddim/HW_netology_main/assets/132663924/00cb59da-df02-4565-8be9-b1ad54951efb)

4. Сделать первоначальную настройку.
![image](https://github.com/goddim/HW_netology_main/assets/132663924/5ba29889-0f2e-4e5b-ac3a-acdc12851660)

## Основная часть

1. Сделать Freestyle Job, который будет запускать `molecule test` из любого вашего репозитория с ролью.
![image](https://github.com/goddim/HW_netology_main/assets/132663924/50c81e3f-d228-42ee-ad5d-d0aaa05aa21b)
![image](https://github.com/goddim/HW_netology_main/assets/132663924/3cc86a5f-8472-4435-8e64-0e9a05b02b2c)



2. Сделать Declarative Pipeline Job, который будет запускать `molecule test` из любого вашего репозитория с ролью.
3. Перенести Declarative Pipeline в репозиторий в файл `Jenkinsfile`.
4. Создать Multibranch Pipeline на запуск `Jenkinsfile` из репозитория.
5. Создать Scripted Pipeline, наполнить его скриптом из [pipeline](./pipeline).
6. Внести необходимые изменения, чтобы Pipeline запускал `ansible-playbook` без флагов `--check --diff`, если не установлен параметр при запуске джобы (prod_run = True). По умолчанию параметр имеет значение False и запускает прогон с флагами `--check --diff`.
7. Проверить работоспособность, исправить ошибки, исправленный Pipeline вложить в репозиторий в файл `ScriptedJenkinsfile`.
8. Отправить ссылку на репозиторий с ролью и Declarative Pipeline и Scripted Pipeline.
9. Сопроводите процесс настройки скриншотами для каждого пункта задания!!

## Необязательная часть

1. Создать скрипт на groovy, который будет собирать все Job, завершившиеся хотя бы раз неуспешно. Добавить скрипт в репозиторий с решением и названием `AllJobFailure.groovy`.
2. Создать Scripted Pipeline так, чтобы он мог сначала запустить через Yandex Cloud CLI необходимое количество инстансов, прописать их в инвентори плейбука и после этого запускать плейбук. Мы должны при нажатии кнопки получить готовую к использованию систему.

---

### Как оформить решение задания

Выполненное домашнее задание пришлите в виде ссылки на .md-файл в вашем репозитории.

---
