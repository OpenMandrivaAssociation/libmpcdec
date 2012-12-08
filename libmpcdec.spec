%define major 5
%define libname %mklibname mpcdec %{major}
%define develname %mklibname mpcdec -d

Summary:	Portable Musepack decoder library
Name:		libmpcdec
Version:	1.2.6
Release:	12
License:	BSD
Group:		System/Libraries
URL:		http://www.musepack.net/
Source:		http://files.musepack.net/source/%{name}-%{version}.tar.bz2

%description
Portable Musepack decoder library.

%package -n %{libname}
Summary:	Dynamic libraries from %{name}
Group:		System/Libraries

%description -n %{libname}
Dynamic libraries from %{name}.

%package -n %{develname}
Summary:	Header files and static libraries from %{name}
Group:		Development/C
Requires:	%{libname} >= %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n %{develname}
Libraries and includes files for developing programs based on %{name}.

%prep
%setup -q

%build
%configure2_5x --disable-static

%make

%install
%makeinstall_std

%files -n %{libname}
%{_libdir}/*.so.%{major}*

%files -n %{develname}
%doc AUTHORS README ChangeLog
%{_includedir}/*
%{_libdir}/*.so


%changelog
* Mon May 02 2011 Oden Eriksson <oeriksson@mandriva.com> 1.2.6-9mdv2011.0
+ Revision: 661499
- mass rebuild

* Sun Nov 28 2010 Oden Eriksson <oeriksson@mandriva.com> 1.2.6-8mdv2011.0
+ Revision: 602579
- rebuild

* Tue Mar 16 2010 Oden Eriksson <oeriksson@mandriva.com> 1.2.6-7mdv2010.1
+ Revision: 520887
- rebuilt for 2010.1

* Wed Sep 02 2009 Christophe Fergeau <cfergeau@mandriva.com> 1.2.6-6mdv2010.0
+ Revision: 425622
- rebuild

  + Anssi Hannula <anssi@mandriva.org>
    - add more old obsoletes on devel package

* Sat Jul 12 2008 Funda Wang <fwang@mandriva.org> 1.2.6-5mdv2009.0
+ Revision: 234140
- drop wrong provides (liblibfoo-devel)

* Tue Jun 17 2008 Thierry Vignaud <tv@mandriva.org> 1.2.6-4mdv2009.0
+ Revision: 222933
- rebuild

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Tue Mar 04 2008 Oden Eriksson <oeriksson@mandriva.com> 1.2.6-3mdv2008.1
+ Revision: 178967
- rebuild

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild
    - kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Wed Aug 29 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 1.2.6-1mdv2008.0
+ Revision: 74637
- spec file clean
- new devel library policy
- new version


* Fri Feb 23 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 1.2.5-1mdv2007.0
+ Revision: 124937
- make use of %%{major}
- make it work
- new version

* Thu Jan 18 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 1.2.4-1mdv2007.1
+ Revision: 110071
- new version

* Mon Dec 04 2006 Götz Waschk <waschk@mandriva.org> 1.2.3-1mdv2007.1
+ Revision: 90354
- Import libmpcdec

* Mon Dec 04 2006 Götz Waschk <waschk@mandriva.org> 1.2.3-1mdv2007.1
- New version 1.2.3

* Fri Dec 02 2005 Götz Waschk <waschk@mandriva.org> 1.2.2-1mdk
- New release 1.2.2

* Wed Oct 05 2005 Götz Waschk <waschk@mandriva.org> 1.2.1-1mdk
- New release 1.2.1

* Wed Aug 31 2005 Götz Waschk <waschk@mandriva.org> 1.2-2mdk
- mkrel

* Mon Aug 15 2005 Austin Acton <austin@mandriva.org> 1.2-1mdk
- initial package

