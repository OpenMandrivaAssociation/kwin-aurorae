%define plasmaver %(echo %{version} |cut -d. -f1-3)
%define stable %([ "$(echo %{version} |cut -d. -f2)" -ge 80 -o "$(echo %{version} |cut -d. -f3)" -ge 80 ] && echo -n un; echo -n stable)

Name:		kwin-aurorae
Version:	6.7.5
Release:	1
Summary:	Themeable window decoration for KWin
Group:		Graphical desktop/KDE
License:	GPLv2+
URL:		https://invent.kde.org/plasma/aurorae
Source0:	http://download.kde.org/%{stable}/plasma/%{plasmaver}/aurorae-%{version}.tar.xz

BuildSystem:	cmake
BuildOption:	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON

BuildRequires:	cmake(ECM)
BuildRequires:	cmake(KDecoration3)
BuildRequires:	cmake(KF6ColorScheme)
BuildRequires:	cmake(KF6Config)
BuildRequires:	cmake(KF6CoreAddons)
BuildRequires:	cmake(KF6I18n)
BuildRequires:	cmake(KF6KCMUtils)
BuildRequires:	cmake(KF6NewStuff)
BuildRequires:	cmake(KF6Package)
BuildRequires:	cmake(KF6Svg)
BuildRequires:	cmake(Qt6Core)
BuildRequires:	cmake(Qt6DBus)
BuildRequires:	cmake(Qt6Quick)
BuildRequires:	cmake(Qt6UiTools)
BuildRequires:	cmake(Qt6Widgets)
BuildRequires:	cmake(Qt6UiPlugin)

%description
Themeable window decoration engine for KWin.

%package devel
Summary:	Development files for %{name}
Group:		Development/KDE and Qt
Requires:	%{name} = %{EVRD}

%description devel
Headers and CMake files for %{name}.

%prep
%autosetup -p1 -n aurorae-%{version}

%files
%license LICENSES/*.txt
%doc README
%{_libdir}/qt6/*
%{_libdir}/libexec/*
%{_datadir}/knsrcfiles/aurorae.knsrc
%{_datadir}/kwin/*
%{_datadir}/locale/*

%files devel
%{_libdir}/cmake/*
