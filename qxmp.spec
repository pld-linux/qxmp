Summary:	Qxmp - light media player (based on MPlayer) for Linux workstations
Summary(pl.UTF-8):	Qxmp - lekki odtwarzacz mediów (oparty na MPlayerze) dla Linuksa
Name:		qxmp
Version:	1.0
Release:	0.1
License:	GPL v2
Group:		X11/Applications/Multimedia
Source0:	http://www.xm1math.net/qxmp/%{name}-%{version}.tar.bz2
# Source0-md5:	9eb52b5b6c1dda6ff96790acb9915da8
URL:		http://www.xm1math.net/qxmp/
BuildRequires:	QtGui-devel >= 4.1.1
BuildRequires:	QtXml-devel
BuildRequires:	qt4-build >= 4.3.3-3
BuildRequires:	qt4-qmake >= 4.3.3-3
Requires:	mplayer
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Qxmp is a light media player (based on MPlayer) for Linux and Unix
workstations. With Qxmp you can easily play a wide variety of video
and audio files and streams using a simple and clean interface. Qxmp
is not a complex media manager - it provides a simple and compact
frontend to MPlayer, allowing you to just enjoy your media.

%description -l pl.UTF-8
Qxmp to lekki odtwarzacz mediów (oparty na MPlayerze) dla Linuksa i
Uniksa. Przy pomocy Qxmp można łatwo odtwarzać wiele różnych plików z
filmami i dźwiękiem oraz strumienie przy użyciu prostego i
przejrzystego interfejsu. Qxmp nie jest skomplikowanym zarządcą mediów
- udostępnia prosty i zwarty frontend do MPlayera, pozwalający po
prostu cieszyć się multimediami.

%prep
%setup -q

%build
qmake-qt4 \
	PREFIX=%{_prefix}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_desktopdir},%{_pixmapsdir}}

%{__make} install \
	INSTALL_ROOT=$RPM_BUILD_ROOT

mv -f $RPM_BUILD_ROOT%{_datadir}/%{name}/Qxmp.desktop \
	$RPM_BUILD_ROOT%{_desktopdir}
mv -f $RPM_BUILD_ROOT%{_datadir}/%{name}/Qxmp.{png,svg} \
	$RPM_BUILD_ROOT%{_pixmapsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc utilities/AUTHORS
%attr(755,root,root) %{_bindir}/qxmp
%{_desktopdir}/*.desktop
%{_pixmapsdir}/*
