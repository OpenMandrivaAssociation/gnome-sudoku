%define url_ver	%(echo %{version}|cut -d. -f1,2)

Name:		gnome-sudoku
Version:	3.16.0
Release:	3
Summary:	GNOME Sudoku game
License:	GPLv2+ and CC-BY-SA
Group:		Games/Puzzles
URL:		https://wiki.gnome.org/Apps/Sudoku
Source0:	https://download.gnome.org/sources/%{name}/%{url_ver}/%{name}-%{version}.tar.xz
BuildRequires:	pkgconfig(pygobject-3.0) >= 2.28.3
BuildRequires:	intltool
BuildRequires:	itstool
BuildRequires:	libxml2-utils
BuildRequires:	python3
BuildRequires:	pkgconfig(gtk+-3.0)
BuildRequires:	pkgconfig(glib-2.0) >= 2.40.0
BuildRequires:	pkgconfig(gio-2.0) >= 2.40.0
BuildRequires:	pkgconfig(qqwing) >= 1.1.3
BuildRequires:	pkgconfig(gee-0.8)
BuildRequires:	pkgconfig(json-glib-1.0)
# For help
Requires:	yelp

Obsoletes:	gnome-sudoku < 3.8.1

%description
GNOME version of the popular Sudoku Japanese logic game.

%prep
%setup -q

%build
export CFLAGS='-Wno-error'
%configure --enable-compile-warnings=no
%make

%install
%makeinstall_std

%find_lang %{name} --with-gnome

%files -f %{name}.lang
%doc COPYING
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/glib-2.0/schemas/org.gnome.sudoku.gschema.xml
%{_datadir}/%{name}
%{_iconsdir}/*/*/apps/%{name}.*
%{_iconsdir}/*/*/apps/%{name}-symbolic.*
%{_mandir}/man6/%{name}.6*
%{_datadir}/appdata/%{name}.appdata.xml
