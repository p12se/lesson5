#README file for Lesson 8 of 'Thumbtack DevOps traineeship' - Homework

install packages on build node: rpm-build, git
note: make sure zookeeper package installed on the host with kafka

download kafka-2.11-1.0.0 here: http://apache-mirror.rbc.ru/pub/apache/kafka/1.0.0/kafka_2.11-1.0.0.tgz

#create required catalogs for rpm-build:
mkdir -p ./{BUILD,RPMS,SPECS,SRPMS,SOURCES}

#prepare build
copy .spec to ./SPECS
unpack kafka archive and copy folder "kafka_2.11-1.0.0" to ./SOURCES

#check .spec file
add required commands and check for other bugs

#run build command
rpmbuild --define "_topdir <absolute path to your build catalog>" -bb ./SPECS/kafka.spec



#Structure of kafka-2.11-1.0.0 package
dedicated user:group for kafka service: kafka:kafka
/opt/kafka_2.11-1.0.0
/opt/kafka_2.11-1.0.0/config/management.properties
/opt/kafka_2.11-1.0.0/~log (softlink to /var/log/kafka)
/var/log/kafka
/etc/sysconfig/kafka
/etc/systemd/system/kafka.service
