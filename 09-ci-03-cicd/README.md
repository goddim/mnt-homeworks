# Домашнее задание к занятию 9 «Процессы CI/CD»

## Подготовка к выполнению

1. Создайте два VM в Yandex Cloud с параметрами: 2CPU 4RAM Centos7 (остальное по минимальным требованиям).
2. Пропишите в [inventory](./infrastructure/inventory/cicd/hosts.yml) [playbook](./infrastructure/site.yml) созданные хосты.
3. Добавьте в [files](./infrastructure/files/) файл со своим публичным ключом (id_rsa.pub). Если ключ называется иначе — найдите таску в плейбуке, которая использует id_rsa.pub имя, и исправьте на своё.
![image](https://github.com/goddim/HW_netology_main/assets/132663924/226541f8-6c92-40d0-90fd-27cd7c048d47)

4. Запустите playbook, ожидайте успешного завершения.
![image](https://github.com/goddim/HW_netology_main/assets/132663924/9e070fd8-8ed7-4efa-a679-57d0ce33a381)

5. Проверьте готовность SonarQube через [браузер](http://localhost:9000).
6. Зайдите под admin\admin, поменяйте пароль на свой.
![image](https://github.com/goddim/HW_netology_main/assets/132663924/915af488-5e1c-4de7-bb2e-798d33c32dcb)

7.  Проверьте готовность Nexus через [бразуер](http://localhost:8081).
8. Подключитесь под admin\admin123, поменяйте пароль, сохраните анонимный доступ.
![image](https://github.com/goddim/HW_netology_main/assets/132663924/dc25d973-7c9b-4277-acac-decfd705cacc)


## Знакомоство с SonarQube

### Основная часть

1. Создайте новый проект, название произвольное.
2. Скачайте пакет sonar-scanner, который вам предлагает скачать SonarQube.
3. Сделайте так, чтобы binary был доступен через вызов в shell (или поменяйте переменную PATH, или любой другой, удобный вам способ).
4. Проверьте `sonar-scanner --version`.
![image](https://github.com/goddim/HW_netology_main/assets/132663924/12aef6b0-edd7-436a-9050-7befe956625d)

5. Запустите анализатор против кода из директории [example](./example) с дополнительным ключом `-Dsonar.coverage.exclusions=fail.py`.
![image](https://github.com/goddim/HW_netology_main/assets/132663924/b45daffa-1a7a-4d68-a518-3a4a30c4f6ae)

6. Посмотрите результат в интерфейсе.
![image](https://github.com/goddim/HW_netology_main/assets/132663924/5e40bb56-a317-4018-9010-c1fc2cd8b683)

7. Исправьте ошибки, которые он выявил, включая warnings.
![image](https://github.com/goddim/HW_netology_main/assets/132663924/33ac94b0-d171-465d-95ef-9029ad468640)
![image](https://github.com/goddim/HW_netology_main/assets/132663924/abcf3d55-cea1-4c4d-86a2-626cf21a7562)

8. Запустите анализатор повторно — проверьте, что QG пройдены успешно.

9. Сделайте скриншот успешного прохождения анализа, приложите к решению ДЗ.

![image](https://github.com/goddim/HW_netology_main/assets/132663924/9ccf61ea-3b2f-44ee-80f4-fdace474fc40)

## Знакомство с Nexus

### Основная часть

1. В репозиторий `maven-public` загрузите артефакт с GAV-параметрами:

 *    groupId: netology;
 *    artifactId: java;
 *    version: 8_282;
 *    classifier: distrib;
 *    type: tar.gz.
   
2. В него же загрузите такой же артефакт, но с version: 8_102.
3. Проверьте, что все файлы загрузились успешно.
4. В ответе пришлите файл `maven-metadata.xml` для этого артефекта.
![image](https://github.com/goddim/HW_netology_main/assets/132663924/6c5e12a7-dffe-4943-82a7-a825c1033bc9)

### Знакомство с Maven

### Подготовка к выполнению

1. Скачайте дистрибутив с [maven](https://maven.apache.org/download.cgi).
2. Разархивируйте, сделайте так, чтобы binary был доступен через вызов в shell (или поменяйте переменную PATH, или любой другой, удобный вам способ).
3. Удалите из `apache-maven-<version>/conf/settings.xml` упоминание о правиле, отвергающем HTTP- соединение — раздел mirrors —> id: my-repository-http-unblocker.
4. Проверьте `mvn --version`.
![image](https://github.com/goddim/HW_netology_main/assets/132663924/fb68d7c5-9da8-4324-a9f8-f24ef576350e)

5. Заберите директорию [mvn](./mvn) с pom.

### Основная часть

1. Поменяйте в `pom.xml` блок с зависимостями под ваш артефакт из первого пункта задания для Nexus (java с версией 8_282).
![image](https://github.com/goddim/HW_netology_main/assets/132663924/0f97da6b-2648-4683-9a79-cedc5dfe327a)

2. Запустите команду `mvn package` в директории с `pom.xml`, ожидайте успешного окончания.
![image](https://github.com/goddim/HW_netology_main/assets/132663924/0ec22490-6792-4893-8439-d0f57ab08867)

3. Проверьте директорию `~/.m2/repository/`, найдите ваш артефакт.
![image](https://github.com/goddim/HW_netology_main/assets/132663924/cc2720ce-78ae-4149-983d-3c466b71909e)

4. В ответе пришлите исправленный файл `pom.xml`.

---

### Как оформить решение задания

Выполненное домашнее задание пришлите в виде ссылки на .md-файл в вашем репозитории.

---
