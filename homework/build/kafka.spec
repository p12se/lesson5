%{!?_release: %define _release 1.0.0}
%{!?_version: %define _version 2.11}

%define __jar_repack %{nil}
%define debug_package %{nil}
%define name         kafka
%define _prefix      /opt
%define _conf_dir    %{_sysconfdir}/kafka
%define _log_dir     %{_var}/log/kafka
%define _data_dir    %{_sharedstatedir}/kafka

Name: kafka
Summary: Kafka is used for building real-time data pipelines and streaming apps
Version: %{_version}
Release: %{_release}
License: Apache License, Version 2.0
Group: Applications/Databases
URL: http://kafka.apache.org/
Prefix: %{_prefix}
Vendor: Apache Software Foundation
Packager: Traineeship Lineate
Provides: kafka
BuildArch: noarch
BuildRequires: systemd
Requires(pre): /usr/sbin/useradd, /usr/bin/getent
Requires(postun): /usr/sbin/userdel

%description
Apache Kafka is an open-source stream processing platform developed by the Apache Software Foundation written in Scala and Java. The project aims to provide a unified, high-throughput, low-latency platform for handling real-time data feeds.

%prep

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_prefix}/kafka_%{version}-%{release}

%clean
rm -rf $RPM_BUILD_ROOT

%pre
/usr/bin/getent group kafka >/dev/null || /usr/sbin/groupadd -r kafka
if ! /usr/bin/getent passwd kafka >/dev/null ; then
    /usr/sbin/useradd -r -g kafka -m -d /home/kafka -s /bin/bash -c "Kafka" kafka
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
%attr(-,kafka,kafka) %{_prefix}/kafka_%{version}-%{release}
