%{!?_release: %define _release 0}
%{!?_version: %define _version 3.4.13}

%define __jar_repack %{nil}
%define debug_package %{nil}
%define name         zookeeper
%define _prefix      /opt
%define _conf_dir    %{_sysconfdir}/zookeeper
%define _log_dir     %{_var}/log/zookeeper
%define _data_dir    %{_sharedstatedir}/zookeeper

Name: zookeeper
Summary: ZooKeeper is a high-performance coordination service for distributed applications.
Version: %{_version}
Release: %{_release}
License: Apache License, Version 2.0
Group: Applications/Databases
URL: http://zookeper.apache.org/
Prefix: %{_prefix}
Vendor: Apache Software Foundation
Packager: Lineate DevOps team
Provides: zookeeper
BuildArch: noarch
BuildRequires: systemd
Requires(pre): /usr/sbin/useradd, /usr/bin/getent
Requires(postun): /usr/sbin/userdel

%description
ZooKeeper allows distributed processes to coordinate with each other through a shared hierarchal namespace which is organized similarly to a standard file system. The name space consists of data registers - called znodes, in ZooKeeper parlance - and these are similar to files and directories. Unlike a typical file system, which is designed for storage, ZooKeeper data is kept in-memory, which means ZooKeeper can acheive high throughput and low latency numbers. The ZooKeeper implementation puts a premium on high performance, highly available, strictly ordered access. The performance aspects of ZooKeeper means it can be used in large, distributed systems. The reliability aspects keep it from being a single point of failure. The strict ordering means that sophisticated synchronization primitives can be implemented at the client.

%prep

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_prefix}/zookeeper-%{version}
mkdir -p $RPM_BUILD_ROOT%{_prefix}/zookeeper-%{version}/templates
cp %{_sourcedir}/templates/* $RPM_BUILD_ROOT%{_prefix}/zookeeper-%{version}/templates/

%clean
rm -rf $RPM_BUILD_ROOT

%pre
/usr/bin/getent group zookeeper >/dev/null || /usr/sbin/groupadd -r zookeeper
if ! /usr/bin/getent passwd zookeeper >/dev/null ; then
    /usr/sbin/useradd -r -g zookeeper -m -d %{_prefix}/zookeeper -s /bin/bash -c "Zookeeper" zookeeper
fi

%post
systemctl enable %{name}
systemctl daemon-reload

%preun
systemctl stop %{name}
systemctl disable %{name}

%postun

%files
%defattr(-,root,root)
#%{_unitdir}/zookeeper.service
%attr(-,zookeeper,zookeeper) %{_prefix}/zookeeper-%{version}
