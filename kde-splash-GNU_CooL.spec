
%define		_splash		GNU_CooL

Summary:	KDE splash screen
Summary(pl):	Ekran startowy KDE
Name:		kde-splash-%{_splash}
Version:	1.0
Release:	1
License:	GPL
Group:		X11/Amusements
#Source0:	http://www.kde-look.org/content/download.php?content=12861
Source0:	http://www.kde-look.org/content/files/12861-GNU.tar.gz	
# Source0-md5:	e2f29a50ceae3fa4b2bd6b6b3c8dcea7
URL:		http://www.kde-look.org/content/show.php?content=12861
Provides:	kde-splash
Requires:	kdebase-desktop >= 9:3.2.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
"GNU CooL" KDE splash screen. Contains fancy picture of GNU ;-)

%description -l pl
Ekran startowy KDE "GNU CooL". Zawiera ¶mieszny obrazek GNU ;-)

%prep
%setup -q -n %{_splash}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/apps/ksplash/Themes/%{_splash}
install * $RPM_BUILD_ROOT%{_datadir}/apps/ksplash/Themes/%{_splash}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_datadir}/apps/ksplash/*
