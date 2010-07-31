%define prj    Horde_Tree

%define xmldir  %{_var}/lib/pear
%define peardir %(pear config-get php_dir 2> /dev/null)

Name:          horde-tree
Version:       0.0.2
Release:       %mkrel 3
Summary:       Horde Tree API
License:       LGPL
Group:         Networking/Mail
Url:           http://pear.horde.org/index.php?package=%{prj}
Source0:       %{prj}-%{version}.tgz
BuildArch:     noarch
Requires(pre): php-pear
Requires:      php-pear
Requires:      horde-util
Requires:      php-gettext
BuildRequires: php-pear
BuildRequires: php-pear-channel-horde

%description
The Horde_Tree:: class provides a tree view of hierarchical information.
It allows for expanding/collapsing of branches and maintains their state.
It can work together with the Horde_Tree javascript class to achieve this
in DHTML on supported browsers.


%prep
%setup -q -n %{prj}-%{version}

%build
%__mv ../package.xml .

%install
pear install --packagingroot %{buildroot} --nodeps package.xml

%__rm -rf %{buildroot}/%{peardir}/.{filemap,lock,registry,channels,depdb,depdblock}

%__mkdir_p %{buildroot}%{xmldir}
%__cp package.xml %{buildroot}%{xmldir}/%{prj}.xml

%clean
%__rm -rf %{buildroot}

%post
pear install --nodeps --soft --force --register-only %{xmldir}/%{prj}.xml

%postun
if [ "$1" -eq "0" ]; then
  pear uninstall --nodeps --ignore-errors --register-only pear.horde.org/%{prj}
fi

%files
%defattr(-, root, root)
%{xmldir}/%{prj}.xml
%dir %{peardir}/Horde/Tree
%{peardir}/Horde/Tree.php
%{peardir}/Horde/Tree/html.php
%{peardir}/Horde/Tree/javascript.php
%{peardir}/Horde/Tree/select.php

