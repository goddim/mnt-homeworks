# Домашнее задание к занятию 2 «Работа с Playbook»

## Подготовка к выполнению

1. * Необязательно. Изучите, что такое [ClickHouse](https://www.youtube.com/watch?v=fjTNS2zkeBs) и [Vector](https://www.youtube.com/watch?v=CgEhyffisLY).
2. Создайте свой публичный репозиторий на GitHub с произвольным именем или используйте старый.
3. Скачайте [Playbook](./playbook/) из репозитория с домашним заданием и перенесите его в свой репозиторий.
4. Подготовьте хосты в соответствии с группами из предподготовленного playbook.

## Основная часть

1. Подготовьте свой inventory-файл `prod.yml`.
2. Допишите playbook: нужно сделать ещё один play, который устанавливает и настраивает [vector](https://vector.dev). Конфигурация vector должна деплоиться через template файл jinja2. От вас не требуется использовать все возможности шаблонизатора, просто вставьте стандартный конфиг в template файл. Информация по шаблонам по [ссылке](https://www.dmosk.ru/instruktions.php?object=ansible-nginx-install). не забудьте сделать handler на перезапуск vector в случае изменения конфигурации!
3. При создании tasks рекомендую использовать модули: `get_url`, `template`, `unarchive`, `file`.
4. Tasks должны: скачать дистрибутив нужной версии, выполнить распаковку в выбранную директорию, установить vector.
5. Запустите `ansible-lint site.yml` и исправьте ошибки, если они есть.
08-ansible-02-playbook/images/1.png
6. Попробуйте запустить playbook на этом окружении с флагом `--check`.
08-ansible-02-playbook/images/2.png
7. Запустите playbook на `prod.yml` окружении с флагом `--diff`. Убедитесь, что изменения на системе произведены.
08-ansible-02-playbook/images/3.png

8. Повторно запустите playbook с флагом `--diff` и убедитесь, что playbook идемпотентен.
08-ansible-02-playbook/images/4.png

9. Подготовьте README.md-файл по своему playbook. В нём должно быть описано: что делает playbook, какие у него есть параметры и теги. Пример качественной документации ansible playbook по [ссылке](https://github.com/opensearch-project/ansible-playbook). Так же приложите скриншоты выполнения заданий №5-8
10. Готовый playbook выложите в свой репозиторий, поставьте тег `08-ansible-02-playbook` на фиксирующий коммит, в ответ предоставьте ссылку на него.

### Описание Playbook

Playbook находится в файле [site.yml](./playbook/site.yml)

Inventory находится в файле [prod.yml](./playbook/inventory/prod.yml)

Переменные находятся в файле [vars.yml](./playbook/group_vars/clickhouse/vars.yml)

Playbook устанавливает сервисы clickhouse и vector.

Для установки сервиса clickhouse с сайта разработчика устанавливаются пакеты:
```
    clickhouse-common-static
    clickhouse-server
    clickhouse-client
```

После этого создаётся БД logs. Ввиду того, что доступ к СУБД появляется не сразу после запуска сервиса clickhouse-server, попытки создания БД выполняются в цикле, пока не увенчаются успехом.

В заключение в БД logs создаётся таблица logs, с полями, которые позволяют загружать записи из syslog-а:
```
CREATE TABLE IF NOT EXISTS logs.logs (
    apname String,
    facility String,
    hostname String,
    message String,
    msgid String,
    procid Int,
    severity String,
    timestamp String,
    version Int
) ENGINE = MergeTree ORDER BY timestamp;'
```

Для установки сервиса vector с сайта разработчика устанавливаются пакеты:

    vector

После из шаблона создаётся конфигурационный файл /etc/vector/vector.toml, который содержит набор команд для загрузки данных из syslog в БД clickhouse.

Playbook использует следующие переменные:

```
    clickhouse_version - требуемая версия clickhouse
    vector_version - требуемая версия vector
```
---
