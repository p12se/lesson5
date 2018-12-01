#README file for Lesson 5 of 'Thumbtack DevOps traineeship'

install: rpm-build, git

download zookeeper-3.4.13 here: http://apache-mirror.rbc.ru/pub/apache/zookeeper/zookeeper-3.4.13/zookeeper-3.4.13.tar.gz

#create required catalogs for rpm-build:
mkdir -p ./{BUILD,RPMS,SPECS,SRPMS,SOURCES}

#prepare build
copy .spec to ./SPECS
copy zookeeper archive to ./SOURCES

#check .spec file
copy 'templates' folder to /opt/zookeeper/templates in a package folders layout

#run build command
rpmbuild --define "_topdir ." -bb ./SPECS/zookeeper.spec