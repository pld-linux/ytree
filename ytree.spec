Summary:	A filemanager similar to XTree
Name:		ytree
Version:	1.99pl2
Release:	1
License:	GPL v2+
Group:		Applications/Console
Source0:	http://www.han.de/~werner/%{name}-%{version}.tar.gz
# Source0-md5:	fdebe0c35ea79b5896815326bffbec37
URL:		http://www.han.de/~werner/ytree.html
BuildRequires:	ncurses-devel >= 5.4
BuildRequires:	readline-devel >= 4.3
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A console based file manager in the tradition of Xtree.

%prep
%setup -q

%build
%{__make} \
	CFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -D -p ytree.1 $RPM_BUILD_ROOT%{_mandir}/man1/ytree.1
install -D -p ytree $RPM_BUILD_ROOT%{_bindir}/ytree

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES COPYING README THANKS ytree.conf
%{_mandir}/man1/ytree.1*
%attr(755,root,root) %{_bindir}/ytree
