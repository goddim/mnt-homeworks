FROM centos:7
RUN yum install -y openssh-server && \
    ssh-keygen -A && \
    echo 'root:password' | chpasswd
EXPOSE 22
CMD ["/usr/sbin/sshd", "-D"]
