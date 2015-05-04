%define url_ver	%(echo %{version}|cut -d. -f1,2)

Name:		gnome-sudoku
Version:	3.16.0
Release:	1
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
%configure
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
%{_mandir}/man6/%{name}.6*
%{_datadir}/appdata/%{name}.appdata.xml


%changelog
* Tue Feb 17 2015 wally <wally> 3.14.2-2.mga5
+ Revision: 815331
- require yelp for showing help

* Tue Nov 11 2014 ovitters <ovitters> 3.14.2-1.mga5
+ Revision: 796294
- new version 3.14.2

* Wed Oct 15 2014 ovitters <ovitters> 3.14.1-1.mga5
+ Revision: 757161
- new version 3.14.1

  + umeabot <umeabot>
    - Second Mageia 5 Mass Rebuild

* Sun Sep 28 2014 tv <tv> 3.14.0-2.mga5
+ Revision: 731147
- rebuild so that it picks typelib() requires

* Mon Sep 22 2014 ovitters <ovitters> 3.14.0-1.mga5
+ Revision: 719242
- new version 3.14.0

* Tue Sep 16 2014 umeabot <umeabot> 3.13.92-2.mga5
+ Revision: 679773
- Mageia 5 Mass Rebuild

* Tue Sep 16 2014 ovitters <ovitters> 3.13.92-1.mga5
+ Revision: 676959
- new version 3.13.92

* Wed Aug 27 2014 pterjan <pterjan> 3.13.90-1.mga5
+ Revision: 668531
- Update BuildRequires based on configure

  + ovitters <ovitters>
    - new version 3.13.90

* Mon Jul 21 2014 ovitters <ovitters> 3.13.4-1.mga5
+ Revision: 655245
- new version 3.13.4

* Tue Jun 24 2014 ovitters <ovitters> 3.13.3-1.mga5
+ Revision: 639429
- update filelist, no longer noarch
- new version 3.13.3

* Mon Jun 23 2014 ovitters <ovitters> 3.12.2-4.mga5
+ Revision: 638846
- update url

* Sat May 31 2014 pterjan <pterjan> 3.12.2-3.mga5
+ Revision: 629675
- Rebuild for new Python

* Sat May 31 2014 pterjan <pterjan> 3.12.2-2.mga5
+ Revision: 629533
- Rebuild for new Python

* Mon May 12 2014 ovitters <ovitters> 3.12.2-1.mga5
+ Revision: 622086
- new version 3.12.2

* Mon Apr 14 2014 ovitters <ovitters> 3.12.1-1.mga5
+ Revision: 614074
- new version 3.12.1

* Mon Mar 24 2014 ovitters <ovitters> 3.12.0-1.mga5
+ Revision: 607934
- new version 3.12.0

* Sun Mar 16 2014 ovitters <ovitters> 3.11.92-1.mga5
+ Revision: 604238
- new version 3.11.92

* Mon Feb 17 2014 ovitters <ovitters> 3.11.90-1.mga5
+ Revision: 593374
- new version 3.11.90

* Fri Feb 07 2014 dams <dams> 3.11.3-1.mga5
+ Revision: 585468
- new version 3.11.3

* Mon Nov 11 2013 ovitters <ovitters> 3.10.2-1.mga4
+ Revision: 550504
- new version 3.10.2

* Sat Nov 02 2013 fwang <fwang> 3.10.1-3.mga4
+ Revision: 548896
- add requires on python-gi

* Tue Oct 22 2013 umeabot <umeabot> 3.10.1-2.mga4
+ Revision: 541396
- Mageia 4 Mass Rebuild

* Sat Oct 12 2013 ovitters <ovitters> 3.10.1-1.mga4
+ Revision: 495862
- new version 3.10.1

* Mon Sep 23 2013 ovitters <ovitters> 3.10.0-1.mga4
+ Revision: 484280
- new version 3.10.0

* Mon Sep 16 2013 ovitters <ovitters> 3.9.92-1.mga4
+ Revision: 480450
- new version 3.9.92

* Wed Aug 21 2013 fwang <fwang> 3.9.90-1.mga4
+ Revision: 468743
- new version 3.9.90

* Sun Jun 09 2013 fwang <fwang> 3.8.1-4.mga4
+ Revision: 440975
- cleanup  spec

* Sun Jun 09 2013 dams <dams> 3.8.1-3.mga4
+ Revision: 440862
- fix requires

* Sun Jun 09 2013 dams <dams> 3.8.1-2.mga4
+ Revision: 440840
- Better 'Obsoletes'

* Sun Jun 09 2013 dams <dams> 3.8.1-1.mga4
+ Revision: 440835
- imported package gnome-sudoku

