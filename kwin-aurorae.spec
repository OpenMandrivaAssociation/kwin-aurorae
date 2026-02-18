# set to nil when packaging a release, 
# or the long commit tag for the specific git branch
%define commit_tag %{nil}

# when using a commit_tag (i.e. not nil) add a commit date
# decoration ~0.yyyyMMdd to Version number
%define commit_date %{nil}

%define qt_ver 6


Name:           kwin-aurorae
Version:        6.6.0
Release:        1
Summary:        Themeable window decoration for kwin
Group:          Settings
License:        GPLv2, MIT
URL:            https://invent.kde.org/plasma/aurorae/-/archive

# change the source URL depending on if the package is a release version or a git version
%if "%{commit_tag}" != "%{nil}"
Source0:        %url/v%version/aurorae-v%version.tar.gz
%else
Source0:        %url/v%version/aurorae-v%version.tar.gz
%endif

BuildSystem:    cmake
BuildOption:    -DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON

BuildRequires:  cmake(kwin)
BuildRequires:  cmake(KDecoration3)
BuildRequires:  cmake(KF6ColorScheme)
BuildRequires:  cmake(KF6Config)
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6KCMUtils) 
BuildRequires:  cmake(KF6NewStuff)
BuildRequires:  cmake(KF6Package)
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6DBus)
BuildRequires:  cmake(Qt6Quick)
BuildRequires:  cmake(Qt6UiTools)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  cmake(Qt6UiPlugin)
BuildRequires:  cmake(VulkanLoader)

%description
%summary

%package devel
Summary:        %summary development package
Requires:       %name = %version

%description devel
%summary 

%files
%license LICENSES/*.txt
%doc README
%{_libdir}/qt%{qt_ver}/*
%{_libdir}/libexec/*
%{_datadir}/knsrcfiles/aurorae.knsrc
%{_datadir}/kwin/*
%{_datadir}/locale/*

%files devel
%{_libdir}/cmake/*

